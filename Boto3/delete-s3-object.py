import boto3, os, glob

# Define S3 resource type
s3_resource = boto3.client('s3')

# Define bucket name
bucket_name = 'luit-black-team-192023'

# Delete single object in bucket
# s3_resource.delete_object(Bucket = bucket_name, 
#     Key = 'file-name-in-bucket.txt')
    
# Delete multiple objects
objects = s3_resource.list_objects(Bucket = bucket_name)['Contents']

for object in objects:
    s3_resource.delete_object(Bucket = bucket_name, 
        Key = object['Key'])