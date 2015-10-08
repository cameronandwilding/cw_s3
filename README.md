Cameron & Wilding - S3 tool
===========================


Requirements
------------

- python 2.x (>=2.6)
- pip
- boto3

Installation
------------

*Boto3*

- (recommended) create a virtial environment

```
pip install virtualenv
# goto to repo root
virtualenv venv
./venv/bin/pip install boto3
```

- or globally: ```pip install boto3```

*Credentials*

- ```mkdir ~/.aws```
- create a file in ```~/.aws/credentials``` with the content:

```
[default]
aws_access_key_id = ID
aws_secret_access_key = SECRET
```

- add the necessary AWS credentials
