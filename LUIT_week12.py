# Empty List of AWS Services

awsServices = []

# Populate List of AWS Services

awsServices.append('EC2')
awsServices.append('Lamda')
awsServices.append('DynamoDB')
awsServices.append('API Gateway')
awsServices.insert(0, 'S3')

# Print Original list and length of list

print('ORIGINAL')
print('List of AWS Services:', awsServices)
print('# of Items in List:', len(awsServices))

# Remove two services from list

awsServices.remove('EC2')
del awsServices[3]

# Print New list and length of list

print('MODIFIED')
print('List of AWS Services:', awsServices)
print('# of Items in List:', len(awsServices))