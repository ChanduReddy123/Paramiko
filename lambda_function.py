import boto3
import paramiko
def worker_handler(event, context):

    s3_client = boto3.client('s3')
    #Download private key file from secure S3 bucket
    s3_client.download_file('chandupemkeys','chandu-ohio.pem', '/tmp/chandu-ohio.pem')

    key = paramiko.RSAKey.from_private_key_file("/tmp/chandu-ohio.pem")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host=event['IP']
    username = event['username']
    print("Connecting to " + host)
    client.connect( hostname = host , username = username, pkey = key )
    print("Connected to " + host)

    commands = [
        "echo 'Hello chandu this is from lambda function' > /home/ubuntu/testing"
        ]
    for command in commands:
        print("Executing {}".format(command))
        stdin , stdout, stderr = client.exec_command(command)
        print(stdout.read())
        print(stderr.read())

    return
    {
        'message' : "Script execution completed. See Cloudwatch logs for complete output"
    }

