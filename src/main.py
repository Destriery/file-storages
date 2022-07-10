from typing import Any

from .storages import Storage


class FileObject:
    storage: Storage

    def __init__(
        self,
        path: str,
        base_path: str | None = None,
        storage: Storage | None = None
    ) -> None:

        if storage: self.storage = storage

        self._object = self.storage.build_object(path, base_path)

    def read(self) -> bytes:
        return self._action('read')

    def write(self, content: bytes) -> None:
        self._action('write', content)

    def delete(self) -> None:
        self._action('delete')

    def _action(self, action: str, *args, **kwargs) -> Any:
        return getattr(self._object, action)(*args, **kwargs)
