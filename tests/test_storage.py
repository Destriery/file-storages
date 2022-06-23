import pytest

from src.storages import S3Storage


@pytest.fixture()
def storage(resource, constants):
    path = f'{constants.BUCKET_NAME.value}/{constants.OBJECT_NAME.value}'

    return S3Storage(path, resource)


def test_write(storage: S3Storage, constants):
    storage.write(constants.CONTENT.value)


def test_read(storage: S3Storage, constants):
    assert storage.read() == constants.CONTENT.value


def test_delete(storage: S3Storage, constants):
    storage.delete()
