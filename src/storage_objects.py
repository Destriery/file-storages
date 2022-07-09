from typing import Any, Protocol


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


class StorageObject:
    """Base class for file objects"""
    def __init__(self, path: str, resource: Any) -> None:
        raise NotImplementedError

    def read(self) -> bytes:
        raise NotImplementedError

    def write(self, content: bytes) -> None:
        raise NotImplementedError

    def delete(self) -> None:
        raise NotImplementedError


class S3StorageObject(StorageObject):
    _object: BotoS3Object

    def __init__(self, path: str, resource: BotoS3Resource) -> None:
        bucket_name, object_name = path.strip('/').split('/', maxsplit=1)

        self._object = resource.Bucket(bucket_name).Object(object_name)  # type: ignore

    def read(self) -> bytes:
        return self._object.get()['Body'].read()

    def write(self, content: bytes) -> None:
        self._object.put(Body=content)

    def delete(self) -> None:
        self._object.delete()
