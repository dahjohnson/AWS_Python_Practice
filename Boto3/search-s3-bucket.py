import boto3


# Define resource type
aws_resource = boto3.resource('s3')

# List all AWS buckets
print(list(aws_resource.buckets.all()))

# List the number/length of buckets
print(len(list(((aws_resource.buckets.all())))))


# Print AWS buckets For Loop
for bucket in aws_resource.buckets.all():
    print(bucket.name)