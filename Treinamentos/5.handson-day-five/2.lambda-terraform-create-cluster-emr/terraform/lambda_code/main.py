import boto3
from os.path import join

emr = boto3.client('emr')

def lambda_handler(event, context):
    cluster_id = create_cluster_emr()
    print(cluster_id)
    return "success"


def execute_job():
    version = 'latest'
    code_bucket = 's3://datarocket-code-spark'
    
    main_path = join(code_bucket, version, 'main.py')
    modules_path = join(code_bucket, version, 'modules.zip')

    job_parameters = {
        'job_name': 'job_processed_data',
        'input_path': 's3://datarocket-raw',
        'output_path': 's3://datarocket-processed',
        'spark_config': {
            '--executor-memory': '1G',
            '--driver-memory': '2G'
        }
    }

    step_args = [
        "/usr/bin/spark-submit",
        '--py-files', modules_path,
        main_path, str(job_parameters)
    ]

    step = {
        "Name": job_parameters['job_name'],
        'ActionOnFailure': 'CONTINUE',
        'HadoopJarStep': {
            'Jar': 's3://us-east-2.elasticmapreduce/libs/script-runner/script-runner.jar',
            'Args': step_args
        }
    }
    
    return step

def create_cluster_emr():
    step_execute_job = execute_job()

    cluster_id = emr.run_job_flow(
        Name='execute_pyspark_job',
        LogUri='s3://aws-logs-503147517431-us-east-2',
        ReleaseLabel='emr-5.32.0',
        Applications=[
            {
                'Name': 'Spark'
            },
        ],
        Instances={
            'InstanceGroups': [
                {
                    'Name': "Master nodes",
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'MASTER',
                    'InstanceType': 'm5.xlarge',
                    'InstanceCount': 1,
                },
                {
                    'Name': "Slave nodes",
                    'Market': 'ON_DEMAND',
                    'InstanceRole': 'CORE',
                    'InstanceType': 'm5.xlarge',
                    'InstanceCount': 1,
                }
            ],
            'Ec2KeyName': 'treinamento-ec2',
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
            'Ec2SubnetId': 'subnet-163a445a',
        },
        Steps=[
            step_execute_job
        ],
        VisibleToAllUsers=True,
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole',
        Tags=[
            {
                'Key': 'treinamento',
                'Value': 'inter-emr',
            },
        ],
    )

    return cluster_id['JobFlowId']
