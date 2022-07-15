from typing import Protocol

from ._base.storage import Storage
from ._base.storage_object import StorageObject

try:
    import boto3
except ImportError:
    ...
    # moving an error to initiation of the storage


class BotoS3Object(Protocol):
    """Result of the "S3Bucket.Object(...)" invocation"""
    def get(self) -> dict: ...
    def put(self, Body: bytes) -> dict: ...
    def delete(self) -> dict: ...


class BotoS3Bucket(Protocol):
    """Result of the "S3Resource.Bucket(...)" invocation"""
    def Object(self, object_name: str): ...


class BotoS3Resource(Protocol):
    """Result of the "boto3.resource('s3', ...)" invocation"""
    def Bucket(self, bucket_name: str) -> BotoS3Bucket: ...


class S3StorageObject(StorageObject):
    _object: BotoS3Object

    def __init__(self, path: str, base_path: str, resource: BotoS3Resource) -> None:
        self._object = resource.Bucket(base_path).Object(path)  # type: ignore

    def read(self) -> bytes:
        return self._object.get()['Body'].read()

    def write(self, content: bytes) -> None:
        self._object.put(Body=content)

    def delete(self) -> None:
        self._object.delete()


class S3Storage(Storage):
    object_type = S3StorageObject

    def _build_resource(self, *args, **kwargs) -> BotoS3Resource:
        try:
            return boto3.resource('s3', *args, **kwargs)  # type: ignore
        except NameError:
            raise ImportError('boto3 was not imported')
