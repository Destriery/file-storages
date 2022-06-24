import os


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

AWS_CAN_CONNECT = bool(AWS_ACCESS_KEY_ID and AWS_ACCESS_KEY_ID)