import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
response = ec2.describe_instances()
# print(response)
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
        #  print(instance['InstanceId'])
         ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
         print(f"Terminated instance: {instance['InstanceId']}")