import argparse
import s3

parser = argparse.ArgumentParser(description='Upload file to S3 bucket.')
parser.add_argument('bucket', metavar='B', type=str, help='bucket name')
parser.add_argument('file', metavar='F', type=str, help='file to upload')
parser.add_argument('project', metavar='P', type=str, help='project it belongs to')
parser.add_argument('--type', action='store', help='type of the upload, possible values: asset, database, files')
parser.add_argument('--month', action='store_true', help='add monthly rotation policy')
parser.add_argument('--week', action='store_true', help='add weekly rotation policy')
parser.add_argument('--day', action='store_true', help='add daily rotation policy')
parser.add_argument('--hour', action='store_true', help='add hourly rotation policy')

args = parser.parse_args()

rotation_policy = s3.S3RotationPolicy(
    month=args.month,
    weekday=args.week,
    day=args.day,
    hour=args.hour
)

package = s3.S3UploadPackage(
    file_path=args.file,
    project=args.project,
    upload_type=args.type,
    rotation_policy=rotation_policy
)

service = s3.S3Handler(bucket_name=args.bucket)
service.upload(package)
