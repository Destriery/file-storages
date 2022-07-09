import boto3
from typing import Any


from .storage_objects import (
    StorageObject, S3StorageObject,
    BotoS3Resource
)


class Storage:
    resource: Any
    object_type: type[StorageObject]

    def __init__(self, *args, **kwargs) -> None:
        raise NotImplementedError

    def build_object(self, path: str, *args, **kwargs) -> StorageObject:
        return self.object_type(path, self.resource, *args, **kwargs)


class S3Storage(Storage):
    resource: BotoS3Resource
    object_type: type[S3StorageObject] = S3StorageObject

    def __init__(self, *args, **kwargs) -> None:
        self.resource = boto3.resource('s3', *args, **kwargs)  # type: ignore
