import boto3

def lambda_handler(event, context):
    
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    client = boto3.client('ec2')
    regions = [region['RegionName']
        for region in client.describe_regions()['Regions']]
        
    for region in regions:
        print('Instances in EC2 Region {0}:'.format(region))
        ec2 = boto3.resource('ec2', region_name = region)
        
        response = ec2.describe_snapshots(OwnerIds=[account_id])
        snapshots = response['Snapshots']
        
        snapshots.sort(key=lambda x: x['StartTime'])
        
        snapshots = snapshots[:-3]
        
        for snapshots in snapshots:
            id = snapshots['SnapshotId']
            try:
                print('Deleting snapshot:', id)
                ec2.delete_snapshot(SnapshotId=id)
            except Exception as e:
                if 'InvalidSnapshot.InUse' in e.message:
                    print('Snapshot {} in use, skipping.'.format(id))
                    continue