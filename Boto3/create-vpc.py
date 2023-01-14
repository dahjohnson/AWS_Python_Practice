import boto3

# Define VPC resource
vpc_resource = boto3.client('ec2')

response = vpc_resource.create_vpc(CidrBlock='192.168.0.0/16')

print(response)