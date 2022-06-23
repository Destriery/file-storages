import boto3
import pytest

from enum import Enum

from src.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME


class Constants(Enum):
    BUCKET_NAME = BUCKET_NAME
    OBJECT_NAME = 'test_folder/new_test_object.txt'
    CONTENT = b'new_test_object'


@pytest.fixture()
def constants():
    return Constants


@pytest.fixture()
def resource():
    return boto3.resource(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
