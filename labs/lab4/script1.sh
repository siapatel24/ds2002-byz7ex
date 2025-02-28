#!/bin/bash


#Assign positional arguements 
LOCAL_FILE="$1"
BUCKET="$2"
EXPIRATION="$3"

#Upload a file to a private bucket
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET/"

#Presign a URL to the file with a 7 day expiration
aws s3 presign --expires-in "$EXPIRATION" "s3://$BUCKET/$LOCAL_FILE"

