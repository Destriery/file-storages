import pytest

from src.storage_objects import OSStorageObject, StorageObject, S3StorageObject, BotoS3Resource

from .config import AWS_CAN_CONNECT


def test_write(test_storage_object_instance: StorageObject, constants):
    test_storage_object_instance.write(constants.CONTENT.value)


def test_read(test_storage_object_instance: StorageObject, constants):
    assert test_storage_object_instance.read() == constants.CONTENT.value


def test_delete(test_storage_object_instance: StorageObject, constants):
    test_storage_object_instance.delete()


# S3StorageObject
@pytest.fixture()
def s3_storage_object(resource: BotoS3Resource, constants):
    return S3StorageObject(constants.OBJECT_NAME.value, constants.BUCKET_NAME.value, resource)


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_s3_write(s3_storage_object: S3StorageObject, constants):
    s3_storage_object.write(constants.CONTENT.value)


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_s3_read(s3_storage_object: S3StorageObject, constants):
    assert s3_storage_object.read() == constants.CONTENT.value


@pytest.mark.skipif(not AWS_CAN_CONNECT, reason="Not enough parameters to connect to AWS")
def test_s3_delete(s3_storage_object: S3StorageObject):
    s3_storage_object.delete()


# OSStorageObject
@pytest.fixture()
def os_storage_object(constants):
    path = f'tests/.tmp/{constants.BUCKET_NAME.value}/{constants.OBJECT_NAME.value}'

    return OSStorageObject(path)


def test_os_write(os_storage_object: OSStorageObject, constants):
    os_storage_object.write(constants.CONTENT.value)


def test_os_read(os_storage_object: OSStorageObject, constants):
    assert os_storage_object.read() == constants.CONTENT.value


def test_os_delete(os_storage_object: OSStorageObject):
    os_storage_object.delete()
