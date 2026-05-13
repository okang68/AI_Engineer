import boto3
from dotenv import load_dotenv

load_dotenv()

print(boto3.client("s3").list_buckets()["Buckets"][:1])
