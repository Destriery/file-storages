import pytest

from src.file_storages.storages._base.storage import Storage
from src.file_storages.storages.s3 import S3Storage

from .config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def test_build_object_without_resource(test_storage_without_resource_instance: Storage, constants):

    with pytest.raises(AttributeError):
        test_storage_without_resource_instance.build_object(constants.OBJECT_NAME.value, constants.BUCKET_NAME.value)


def test_build_object(test_storage_instance: Storage, constants):
    file_object = test_storage_instance.build_object(constants.OBJECT_NAME.value, constants.BUCKET_NAME.value)

    assert isinstance(file_object, test_storage_instance.object_type)


# S3Storage
@pytest.fixture()
def storage():
    return S3Storage(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )


def test_build_resource_for_s3(storage: S3Storage):
    assert storage.resource.meta.service_name == 's3'  # type: ignore
