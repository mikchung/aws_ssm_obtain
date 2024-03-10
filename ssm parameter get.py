import boto3

# Configure SSM client
ssm = boto3.client('ssm',
                    aws_access_key_id='',
                    aws_secret_access_key='',
                    region_name='')

# Specify the parameter name
parameter_name = ''

# Retrieve the parameter value
try:
    response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
    parameter_value = response['Parameter']['Value']

    # Use the retrieved value
    print("Retrieved parameter value:", parameter_value)

except Exception as e:
    print("Error retrieving parameter:", e)