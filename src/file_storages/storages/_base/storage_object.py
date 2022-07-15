from typing import Any


class StorageObject:
    """Base class for file objects"""
    def __init__(self, path: str, base_path: str, resource: Any = None) -> None:
        raise NotImplementedError

    def read(self) -> bytes:
        raise NotImplementedError

    def write(self, content: bytes) -> None:
        raise NotImplementedError

    def delete(self) -> None:
        raise NotImplementedError
