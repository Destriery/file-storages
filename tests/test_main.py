import pytest

from src.main import FileObject
from src.storages import Storage


@pytest.fixture()
def storage(constants):
    class TestStorage(Storage):
        def __init__(self, path: str) -> None:
            ...

        def read(self) -> bytes:
            return constants.CONTENT.value

        def write(self, content: bytes) -> None:
            pass

        def delete(self) -> None:
            pass

    return TestStorage


@pytest.fixture()
def file_object(storage, constants):
    path = f'{constants.BUCKET_NAME.value}/{constants.OBJECT_NAME.value}'

    FileObject.storage = storage

    return FileObject(path)


def test_write(file_object: FileObject, constants):
    file_object.write(constants.CONTENT.value)


def test_read(file_object: FileObject, constants):
    assert file_object.read() == constants.CONTENT.value


def test_delete(file_object: FileObject):
    file_object.delete()
