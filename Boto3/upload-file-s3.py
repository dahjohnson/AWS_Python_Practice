import boto3

# Define AWS/S3 Resource
s3_resource = boto3.client('s3')

# Define local file path
upload_file_path = '/home/ec2-user/environment/Python_Practice/Boto3/test.txt'

# Upload file to bucket
s3_resource.upload_file(
    Filename = upload_file_path,
    Bucket = 'luit-black-team-192023',
    Key = 'file-name-in-bucket.txt'
)