import boto3

vpc_resource = boto3.client('ec2')

response = vpc_resource.describe_vpcs()

# Print number of VPCs
print(f"Number of VPCs: {len(response['Vpcs'])}")

# List VPC IDs only
print("\nVPC IDs:")
for vpc in response['Vpcs']:
    print(vpc['VpcId'])

# Describe VPC by VPC ID - VpcIds argument must be list

vpc_id = ['vpc-0fd6f14d0b2bb6f80']

response2 = vpc_resource.describe_vpcs(VpcIds = vpc_id)

print("\nDescribe VPC ID: {0}".format(vpc_id))
print(response2)