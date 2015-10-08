Cameron & Wilding - S3 tool
===========================


Requirements
------------

- python 2.x (>=2.6)
- pip
- boto3
- argparse

Installation
------------

*Virtual Python environment (recommended)*

```
pip install virtualenv
```

*Modules*

```
pip install boto3
pip install argparse
```

*Credentials*

- ```mkdir ~/.aws```
- create a file in ```~/.aws/credentials``` with the content:

```
[default]
aws_access_key_id = ID
aws_secret_access_key = SECRET
```

- add the necessary AWS credentials


Usage
-----

**Direct Python API**

*Upload file*

```PYTHON
import s3

package = s3.S3UploadPackage(
    file_path="/PATH/TO/FILE",
    project="my_project",
    upload_type=s3.S3UploadType.DB_DUMP,
    rotation_policy=s3.S3RotationPolicy.weekly()
)

s = s3.S3Handler(bucket_name=BUCKET_NAME)
s.upload(package)

```


**Runners**

*Ping (health check)*

Print out "Works!" if it's accessible:

```BASH
$> python s3_ping.py BUCKETNAME && echo "Works!"
```

*Upload file*

```BASH
$> python s3_upload.py -h

usage: s3_upload.py [-h] [--type TYPE] [--month] [--week] [--day] [--hour]
                    B F P

Upload file to S3 bucket.

positional arguments:
  B            bucket name
  F            file to upload
  P            project it belongs to

optional arguments:
  -h, --help   show this help message and exit
  --type TYPE  type of the upload, possible values: asset, database, files
  --month      add monthly rotation policy
  --week       add weekly rotation policy
  --day        add daily rotation policy
  --hour       add hourly rotation policy

$> python s3_upload.py my_bucket ~/Desktop/dump.sql.gz my_project --type database --day --month
```
