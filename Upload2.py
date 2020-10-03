import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAWNUK7LR33PSOZCPU'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'testelambda1234567'

data = open('leao.jpg', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='uploads/leao.jpg', Body=data)

print ("Upload realizado com sucesso!")
