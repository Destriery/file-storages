import boto3
from typing import Protocol


class Storage:
    """Base class for storages"""
    def __init__(self, path: str) -> None:
        raise NotImplementedError

    def read(self) -> bytes:
        raise NotImplementedError

    def write(self) -> None:
        raise NotImplementedError

    def delete(self) -> None:
        raise NotImplementedError


class S3Object(Protocol):
    """Result of the "S3Bucket.Object(...)" invocation"""
    def get(self) -> dict: ...
    def put(self, Body: bytes) -> dict: ...
    def delete(self) -> dict: ...


class S3Bucket(Protocol):
    """Result of the "S3Resource.Bucket(...)" invocation"""
    def Object(self, object_name: str): ...


class S3Resource(Protocol):
    """Result of the "boto3.resource('s3', ...)" invocation"""
    def Bucket(self, bucket_name: str) -> S3Bucket: ...


class S3Storage(Storage):
    """The class implements the capabilities of reading, writing and deleting s3 objects"""
    def __init__(self, path: str, resource: S3Resource | None = None) -> None:
        bucket_name, object_name = path.strip('/').split('/', maxsplit=1)

        resource = resource or self._build_resource()

        self._object = self._build_object(resource, bucket_name, object_name)

    def read(self) -> bytes:
        return self._object.get()['Body'].read()

    def write(self, content) -> None:
        self._object.put(Body=content)

    def delete(self) -> None:
        self._object.delete()

    def _build_resource(self) -> S3Resource:
        return boto3.resource('s3')  # type: ignore

    def _build_object(self, resource: S3Resource, bucket_name: str, object_name: str) -> S3Object:
        bucket = resource.Bucket(bucket_name)

        return bucket.Object(object_name)  # type: ignore
