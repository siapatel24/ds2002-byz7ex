import boto3
import requests
import os

#Client for reusable connection
s3 = boto3.client('s3', region_name='us-east-1')

#Fetch and save a file from the internet
def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")

# Download file 
image_url = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnFwa3kzZnFubG9ucm1yYTQ3eDRrbGRheDR2d3I3OG1seGdsem1rYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4FQMuOKR6zQRO/giphy.gif"
local_file = "downloaded_image.gif"
download_file(image_url, local_file)

# Upload file to a bucket in S3
bucket = 'ds2002-byz7ex'

with open(local_file, 'rb') as f:
    resp = s3.put_object(
        Body = f,
        Bucket = bucket,
        Key = local_file
    )

expires_in = 600

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': local_file},
    ExpiresIn=expires_in
)

#Output the presigned URL
print(response)
