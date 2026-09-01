import os
import boto3
from fastapi import UploadFile

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "eu-north-1")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

async def upload_file_to_s3(file: UploadFile) -> str:
    try:
        s3_client.upload_fileobj(
            file.file,
            AWS_BUCKET_NAME,
            file.filename,
            ExtraArgs={"ContentType": file.content_type}
        )
        file_url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{file.filename}"
        return file_url
    except Exception as e:
        raise RuntimeError(f"Failed to upload file to S3: {str(e)}")