import boto3


def get_ami_id():
    ssm_client = boto3.client('ssm', region_name='ap-south-1')
    parameter = ssm_client.get_parameter(
        Name='/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64'
    )

    return parameter['Parameter']['Value']
