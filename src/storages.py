import boto3
from typing import Any


from .storage_objects import (
    StorageObject, S3StorageObject, OSStorageObject,
    BotoS3Resource
)


class Storage:
    base_path: str
    resource: Any
    object_type: type[StorageObject]

    def __init__(self, base_path: str | None = None, *args, **kwargs) -> None:
        self.resource = self._build_resource(*args, **kwargs)

        if base_path: self.base_path = base_path

    def build_object(self, path: str, base_path: str | None = None) -> StorageObject:
        return self.object_type(path, base_path or self.base_path, self.resource)

    def _build_resource(*args, **kwargs) -> Any:
        return None


class S3Storage(Storage):
    object_type = S3StorageObject

    def _build_resource(self, *args, **kwargs) -> BotoS3Resource:
        return boto3.resource('s3', *args, **kwargs)  # type: ignore


class OSStorage(Storage):
    base_path = ''
    object_type = OSStorageObject
