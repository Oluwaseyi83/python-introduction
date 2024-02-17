import boto3

client = boto3.client ('ec2')

response = client.run_instances(
    ImageId = 'ami-0e731c8a588258d0d',
    InstanceType = 't2.micro',
    MaxCount = 1,
    MinCount = 1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'PYHON EC2'
                },
            ]
        },
    ],
)

print(response)


