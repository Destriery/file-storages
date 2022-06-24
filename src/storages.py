import boto3

from .storage_objects import (
    StorageObject, S3StorageObject,
    S3Resource
)


class Storage:
    """Base class for storages"""
    object_type: type[StorageObject]

    def __init__(self, *args, **kwargs) -> None:
        raise NotImplementedError

    def build_object(self, path: str, *args, **kwargs) -> StorageObject:
        return self.object_type(path, *args, **kwargs)


class S3Storage(Storage):
    """Bulding s3 resources and objects"""
    object_type: type[S3StorageObject] = S3StorageObject

    def __init__(self, *args, **kwargs) -> None:
        self.resource = self.build_resource(*args, **kwargs)

    def build_resource(self, *args, **kwargs) -> S3Resource:
        return boto3.resource('s3', *args, **kwargs)  # type: ignore

    def build_object(self, path: str) -> S3StorageObject:
        return self.object_type(path, self.resource)
