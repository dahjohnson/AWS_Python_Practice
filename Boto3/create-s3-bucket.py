import boto3

# AWS Documentation https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket

# Define resource type
aws_resource = boto3.resource('s3')

# Define S3 bucket name
bucket = aws_resource.Bucket('luit-black-team-192023')

# Create Bucket
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)

# If creating bucket in us-east-1, leave out the CreateBucketConfiguration parameter

# Delete Bucket
# response = bucket.delete()

print(response)