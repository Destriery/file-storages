from typing import Any

from .storages import Storage


class FileObject:
    path: str
    storage: Storage

    def __init__(self, path: str, storage: Storage | None = None) -> None:
        self.path = path

        if storage:
            self.storage = storage

        if not getattr(self, 'storage'):
            raise ValueError('FileObject should have a storage property')

        self._object = self.storage.build_object(path)

    def read(self) -> bytes:
        return self._action('read')

    def write(self, content: bytes) -> None:
        self._action('write', content)

    def delete(self) -> None:
        self._action('delete')

    def _action(self, action: str, *args, **kwargs) -> Any:
        return getattr(self._object, action)(self._object, *args, **kwargs)
