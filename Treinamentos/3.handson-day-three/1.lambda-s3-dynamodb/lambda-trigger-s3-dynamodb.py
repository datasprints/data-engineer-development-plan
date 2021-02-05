import json
import urllib
import boto3
import random
import string
import urllib.parse
from decimal import Decimal

print("working in the role")


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'datarocket-raw'

    try:
        file_obj = event["Records"][0]
        filename = urllib.parse.unquote_plus(file_obj['s3']['object']['key'], encoding='utf-8')

        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=bucket_name, Key=filename)
        
        fileObj = s3.get_object(Bucket=bucket_name, Key=filename)
        file_content = fileObj["Body"].read().decode("utf-8")
        file_json = json.loads(file_content)

        dynamo_db = boto3.resource('dynamodb')
        dynamoTable = dynamo_db.Table('acoes')

        with dynamoTable.batch_writer() as batch:
            for record in file_json:
                batch.put_item(Item={
                    'id': ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
                    'codigo': record[0]['codigo'],
                    'horario': record[0]['horario'],
                    'valor': Decimal(record[0]['valor'])
                })

        return "Lambda Working"
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
            filename, bucket_name))
        raise e
