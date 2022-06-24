import pytest

from src.storages import S3Storage
from src.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


@pytest.fixture()
def storage():
    return S3Storage(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )


def test_build_resource(storage: S3Storage):
    assert storage.resource.meta.service_name == 's3'  # type: ignore


def test_build_object(storage: S3Storage, constants):
    path = f'{constants.BUCKET_NAME.value}/{constants.OBJECT_NAME.value}'

    file_object = storage.build_object(path)

    assert isinstance(file_object, storage.object_type)
