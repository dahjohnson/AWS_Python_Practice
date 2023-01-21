import boto3

def lambda_handler(object, context):
    
    # Get list of regions
    client = boto3.client('ec2')
    regions = [region['RegionName']
        for region in client.describe_regions()['Regions']]
        
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)
        print('Region:', region)
        
        # List only unattached volumes
        volumes = ec2.volumes.filter(
            Filters = [{'Name': 'status', 'Values': ['Available']}])
            
        for volume in volumes:
            v = ec2.Volume(volume.id)
            print('Deleting EBS Volume: {}, Size: {} GiB'.format(v.id, v.size))
            v.delete()