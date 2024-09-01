import json
import boto3
import urllib.parse

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Event triggered from S3 via EventBridge")
    print(event)
    
    # Check if the event has the necessary details
    if 'detail' in event and 'bucket' in event['detail'] and 'object' in event['detail']:
        source_bucket = event['detail']['bucket']['name']
        source_key = urllib.parse.unquote_plus(event['detail']['object']['key'])
        
        # Define the destination bucket and key with the revised prefix
        destination_bucket = 's3-eventbridge-sushan-revised-3'  # Change this to your destination bucket name
        destination_key = 'revised_' + source_key
        
        try:
            # Copy the object to the destination bucket
            s3.copy_object(
                Bucket=destination_bucket,
                CopySource={'Bucket': source_bucket, 'Key': source_key},
                Key=destination_key
            )
            print(f"Successfully copied {source_key} from {source_bucket} to {destination_key} in bucket {destination_bucket}")
        except Exception as e:
            print(f"Error copying object {source_key} to {destination_key}: {e}")
    else:
        print("Event does not contain necessary details to process S3 object.")

    return {
        'statusCode': 200,
        'body': json.dumps('File copied successfully to the new bucket with revised prefix!')
    }
