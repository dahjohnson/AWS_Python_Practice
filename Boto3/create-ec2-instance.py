import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_instances


ami_id = 'ami-0b5eea76982371e91'
ec2_name = 'EC2_A'

ec2_resource = boto3.resource('ec2')

# Define EC2 instance being created
response = ec2_resource.create_instances(
    ImageId = ami_id,
    InstanceType = 't2.micro',
    MaxCount = 1,
    MinCount = 1,
    TagSpecifications=[
        {
        'ResourceType': 'instance',
        'Tags': [
                {
                    'Key': 'Name',
                    'Value': ec2_name
                },
            ]
        },
    ],
)
 
# modify Max and Min Count to create multipe instances

print(response)