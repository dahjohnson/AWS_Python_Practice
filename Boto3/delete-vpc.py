import boto3

vpc_resource = boto3.client('ec2')

vpc_id = 'vpc-0a8d28a691a179604'

response = vpc_resource.delete_vpc(
    VpcId = vpc_id)
    
print(response)