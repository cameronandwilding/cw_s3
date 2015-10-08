import boto3
import botocore
from sys import argv

if len(argv) < 2:
    print("Missing argument. Usage: python s3_ping.py BUCKET_NAME")
    exit(1)

s3 = boto3.resource('s3')

bucket_name = argv[1]
bucket = s3.Bucket(bucket_name)
try:
    s3.meta.client.head_bucket(Bucket=bucket_name)
except botocore.exceptions.ClientError as e:
    print("Could not find bucket. Either S3 or bucket error")
    exit(2)
except Exception as e:
    print(e.message)
    exit(3)

exit(0)
