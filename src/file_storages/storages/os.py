import os
from typing import Any

from ._base.storage import Storage
from ._base.storage_object import StorageObject


class OSStorageObject(StorageObject):
    _path: str

    def __init__(self, path: str, base_path: str = '', resource: Any = None) -> None:
        self._path = os.path.join(base_path, path)

    def read(self) -> bytes:
        with open(self._path, 'rb') as file:
            return file.read()

    def write(self, content: bytes) -> None:
        os.makedirs(os.path.dirname(self._path), exist_ok=True)

        with open(self._path, 'wb') as file:
            file.write(content)

    def delete(self) -> None:
        os.remove(self._path)


class OSStorage(Storage):
    base_path = ''
    object_type = OSStorageObject
