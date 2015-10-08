import boto3
from datetime import datetime
from os import path


class S3UploadType:
    GENERIC_ASSET = "asset"
    DB_DUMP = "database"
    FILE_DUMP = "files"

    def __init__(self):
        raise Exception("Enum class should not be instantiated.")


class S3RotationPolicy:
    def __init__(self, month=False, weekday=False, day=False, hour=False, glue="_"):
        self.glue = glue
        self.month = month
        self.weekday = weekday
        self.day = day
        self.hour = hour

    @classmethod
    def weekly(self):
        return S3RotationPolicy(weekday=True)

    def path_marker(self):
        parts = []
        now = datetime.now()
        if self.month:
            parts.append(now.strftime('%b'))

        if self.weekday:
            parts.append(now.strftime('%a'))

        if self.day:
            parts.append(now.strftime('%d'))

        if self.hour:
            parts.append(now.strftime('%H'))

        return self.glue.join(parts).lower()


class S3Handler:
    # @TODO maybe to configuration
    def __init__(self, bucket_name="cwdumps"):
        """
        :type bucket_name: string
        """
        self.bucket_name = bucket_name
        self.s3 = boto3.resource('s3')

    def upload(self, upload_package):
        """
        :type upload_package: S3UploadPackage
        """
        self.s3.Object(self.bucket_name, upload_package.full_destination_path()).put(Body=open(upload_package.path, 'rb'))


class S3UploadPackage():
    def __init__(self, file_path, project, upload_type=S3UploadType.GENERIC_ASSET, rotation_policy=S3RotationPolicy.weekly()):
        self.project = project
        self.rotation_policy = rotation_policy
        self.upload_type = upload_type
        self.path = file_path

    def full_destination_path(self):
        file_name = path.basename(self.path)
        parts = [self.project, self.upload_type, self.rotation_policy.path_marker() + "__" + file_name]
        return "/".join(parts)
