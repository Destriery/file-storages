import pytest

from src.storage_objects import S3StorageObject, S3Resource


@pytest.fixture()
def storage_object(resource: S3Resource, constants):
    path = f'{constants.BUCKET_NAME.value}/{constants.OBJECT_NAME.value}'

    return S3StorageObject(path, resource)


def test_write(storage_object: S3StorageObject, constants):
    storage_object.write(constants.CONTENT.value)


def test_read(storage_object: S3StorageObject, constants):
    assert storage_object.read() == constants.CONTENT.value


def test_delete(storage_object: S3StorageObject, constants):
    storage_object.delete()
