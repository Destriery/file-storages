from typing import Any
import boto3
import pytest

from enum import Enum

from src.file_storages.storages._base.storage import Storage
from src.file_storages.storages._base.storage_object import StorageObject

from .config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME


class Constants(Enum):
    BUCKET_NAME = BUCKET_NAME or 'test_bucket'
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


@pytest.fixture()
def test_storage_object(constants):
    class TestStorageObject(StorageObject):
        def __init__(self, path: str, base_path: str, resource: Any = None) -> None:
            ...

        def read(self) -> bytes:
            return constants.CONTENT.value

        def write(self, content: bytes) -> None:
            pass

        def delete(self) -> None:
            pass

    return TestStorageObject


@pytest.fixture()
def test_storage_object_instance(test_storage_object, constants):
    path = f'{constants.BUCKET_NAME.value}/{constants.OBJECT_NAME.value}'

    return test_storage_object(path, None)


@pytest.fixture()
def test_storage(test_storage_object):
    class TestStorage(Storage):
        resource = None
        object_type = test_storage_object

        def __init__(self) -> None:
            ...

    return TestStorage


@pytest.fixture()
def test_storage_instance(test_storage, constants):
    return test_storage()


@pytest.fixture()
def test_storage_without_resource(test_storage_object):
    class TestStorage(Storage):
        object_type = test_storage_object

        def __init__(self) -> None:
            ...

    return TestStorage


@pytest.fixture()
def test_storage_without_resource_instance(test_storage_without_resource, constants):
    return test_storage_without_resource()
