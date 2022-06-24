import pytest

from src.storage_objects import StorageObject, S3StorageObject, S3Resource

from .config import AWS_CAN_CONNECT


def test_write(test_storage_object_instance: StorageObject, constants):
    test_storage_object_instance.write(constants.CONTENT.value)


def test_read(test_storage_object_instance: StorageObject, constants):
    assert test_storage_object_instance.read() == constants.CONTENT.value


def test_delete(test_storage_object_instance: StorageObject, constants):
    test_storage_object_instance.delete()


# S3StorageObject
@pytest.fixture()
def s3_storage_object(resource: S3Resource, constants):
    path = f'{constants.BUCKET_NAME.value}/{constants.OBJECT_NAME.value}'

    return S3StorageObject(path, resource)


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_s3_write(s3_storage_object: S3StorageObject, constants):
    s3_storage_object.write(constants.CONTENT.value)


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_s3_read(s3_storage_object: S3StorageObject, constants):
    assert s3_storage_object.read() == constants.CONTENT.value


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_s3_delete(s3_storage_object: S3StorageObject):
    s3_storage_object.delete()
