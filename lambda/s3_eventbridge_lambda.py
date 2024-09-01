import boto3
import zipfile
import tarfile
import io
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print(f"Received event: {json.dumps(event)}")
    
    # Extract relevant information from EventBridge event
    detail = event.get('detail', {})
    source_bucket = detail.get('bucket', {}).get('name')
    object_key = detail.get('object', {}).get('key')
    
    if not source_bucket or not object_key:
        print("Error: Unable to extract bucket and key information from event")
        return
    
    print(f"Processing file: {object_key} from bucket: {source_bucket}")
    
    # Download the file from S3
    try:
        response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
        file_content = response['Body'].read()
    except Exception as e:
        print(f"Error downloading file: {str(e)}")
        return
    
    # Determine if it's a zip or tar file
    if object_key.endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(file_content)) as zip_ref:
            for file_name in zip_ref.namelist():
                file_data = zip_ref.read(file_name)
                s3_client.put_object(Bucket='s3-eventbridge-sushan-revised-3', Key=file_name, Body=file_data)
    elif object_key.endswith('.tar') or object_key.endswith('.tar.gz'):
        with tarfile.open(fileobj=io.BytesIO(file_content), mode='r:*') as tar_ref:
            for member in tar_ref.getmembers():
                if member.isfile():
                    file_data = tar_ref.extractfile(member).read()
                    s3_client.put_object(Bucket='s3-eventbridge-sushan-revised-3', Key=member.name, Body=file_data)
    else:
        print(f"Unsupported file type: {object_key}")
        return
    
    print(f"Unarchived {object_key} to s3-eventbridge-sushan-revised-3")