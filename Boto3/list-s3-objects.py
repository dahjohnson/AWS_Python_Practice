import boto3

s3_resource = boto3.client('s3')

# Define bucket name variable
bucket_name = 'luit-black-team-192023'

# Define bucket contents variable
objects = s3_resource.list_objects(Bucket = bucket_name)['Contents']

# List the number of objects in bucket
len(objects)

# Print object key names
for object in objects:
    print(object['Key'])