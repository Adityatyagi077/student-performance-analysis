import boto3
import pandas as pd
import os

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

bucket_name = "student-analysis-data-adityatyagi"
file_key = "Student_Marks.csv"

# download file
s3.download_file(bucket_name, file_key, "data.csv")

# read with pandas

df = pd.read_csv("data.csv")

print(df.head())
