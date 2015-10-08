import boto3

if __name__ == "__main__":
  s3 = boto3.resource('s3')

  # s3.Object('cwdumps', '').put(Body=open('', 'rb'))

  # print("Done")

  bucket = s3.Bucket('cwdumps')
  exists = True
  try:
    s3.meta.client.head_bucket(Bucket="cwdumps")
  except botocore.exceptions.ClientError as e:
    error_code = int(e.response["Error"]["Code"])
    if error_code == 404:
      exists = False

  print(exists)

  # for bucket in s3.buckets.all():
  #   print(bucket)
  #   for key in bucket.objects.all():
  #     print(key.key)
