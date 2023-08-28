import boto3

s3 = boto3.client("s3")
sns = boto3.client("sns")

def lw(event, context):
    for record in event['Records']:
        # Get the bucket name and object key from the event record
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Determine if the object is a file or a folder
        if object_key.endswith('/'):
            # Retrieve the list of files in the folder
            files_in_folder = get_files_in_folder(bucket_name, object_key)
            
            if files_in_folder:
                message = f"A folder '{object_key}' was uploaded. Files in the folder: {', '.join(files_in_folder)}"
            else:
                message = f"A folder '{object_key}' was uploaded. The folder is empty."
        else:
            message = f"A file '{object_key}' was uploaded."
            
        # Publish a message to SNS
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:693939771894:test-event01',
            Message=message,
            Subject='New Upload in S3'
        )

        print(message)

def get_files_in_folder(bucket, folder_key):
    files = []
    
    # List objects in the specified folder
    response = s3.list_objects_v2(Bucket=bucket, Prefix=folder_key, Delimiter='/')
    
    for obj in response.get('Contents', []):
        files.append(obj['Key'])
    
    return files
