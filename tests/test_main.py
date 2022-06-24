import pytest

from src.main import FileObject


@pytest.fixture()
def file_object(test_storage, constants):
    path = f'{constants.BUCKET_NAME.value}/{constants.OBJECT_NAME.value}'

    FileObject.storage = test_storage()

    return FileObject(path)


def test_write(file_object: FileObject, constants):
    file_object.write(constants.CONTENT.value)


def test_read(file_object: FileObject, constants):
    assert file_object.read() == constants.CONTENT.value


def test_delete(file_object: FileObject):
    file_object.delete()
