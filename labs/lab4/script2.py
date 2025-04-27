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
image_url = "https://images.app.goo.gl/yS4EyKLwRDfh52VNA"
local_file = "downloaded_image.gif"
path = os.path.join(os.getcwd(), file) # Saves to current directory

download_file(image_url, local_file)

# Upload file to a bucket in S3
bucket = 'ds2002-byz7ex'
local_file = 'project/file'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file
)

#Presign the file with an expiration time
expires_in = 600

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

#Output the presigned URL
print(response)
