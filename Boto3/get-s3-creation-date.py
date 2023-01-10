import boto3

# Define AWS Resource
aws_resource = boto3.client('s3')


# print(aws_resource.list_buckets())

# Variables
bucket_name = aws_resource.list_buckets()['Buckets'][2]['Name']
create_date = aws_resource.list_buckets()['Buckets'][2]['CreationDate']

# print bucket name and creation date in a specific format
print(bucket_name + ': ' + create_date.strftime("%d%m%y_%H:%M:%s"))

# Print Bucket Name and Creation Date w/ For Loop
for bucket in aws_resource.list_buckets()['Buckets']:
    print(bucket['Name'])
    print(bucket['CreationDate'])
