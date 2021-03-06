import pytest
from botocore.exceptions import ClientError

from .config import AWS_CAN_CONNECT


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_get_nonexist_content(resource, constants):
    bucket = resource.Bucket(constants.BUCKET_NAME.value)
    file_object = bucket.Object(constants.OBJECT_NAME.value)

    with pytest.raises(ClientError) as error:
        file_object.get()['Body'].read()

    assert error.typename == 'NoSuchKey'


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_save_content(resource, constants):
    bucket = resource.Bucket(constants.BUCKET_NAME.value)
    file_object = bucket.Object(constants.OBJECT_NAME.value)

    response = file_object.put(Body=constants.CONTENT.value)

    assert response['ResponseMetadata']['HTTPStatusCode'] == 200


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_get_content(resource, constants):
    bucket = resource.Bucket(constants.BUCKET_NAME.value)
    file_object = bucket.Object(constants.OBJECT_NAME.value)

    content = file_object.get()['Body'].read()

    assert content == constants.CONTENT.value


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_delete_object(resource, constants):
    bucket = resource.Bucket(constants.BUCKET_NAME.value)
    file_object = bucket.Object(constants.OBJECT_NAME.value)

    response = file_object.delete()

    assert response['ResponseMetadata']['HTTPStatusCode'] == 204
