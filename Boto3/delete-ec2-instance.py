import boto3

ec2_client = boto3.client('ec2')

ec2_reservations_list = ec2_client.describe_instances()['Reservations']

id_list = []
for instances in ec2_reservations_list:
    instance=instances['Instances']
    for ids in instance:
        instance_id=ids['InstanceId']
        id_list.append(instance_id)
        
# print(id_list)

ec2_client.terminate_instances(InstanceIds = id_list)