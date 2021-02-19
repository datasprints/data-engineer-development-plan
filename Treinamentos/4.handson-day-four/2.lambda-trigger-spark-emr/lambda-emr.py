import boto3
from os.path import join


def lambda_handler(event, context):
    emr = boto3.client('emr')
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

    action = emr.add_job_flow_steps(JobFlowId='j-21MNKL3BUMHU0', Steps=[step])
    return action