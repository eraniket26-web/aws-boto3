import boto3
from ami_utils import get_ami_id

# step 1:- Get ec2 ami id to create aws instance use ssm service
# ssm_client = boto3.client('ssm',region_name='ap-south-1')
# parameter = ssm_client.get_parameter(
#     Name='/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64'
# )

# ami_id = parameter['Parameter']['Value']
# print(ami_id)

ami_id = get_ami_id()

ec2 = boto3.client('ec2', region_name='ap-south-1')
response = ec2.run_instances(
    ImageId=ami_id,    
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1)

print(response['Instances'][0]['InstanceId'])





