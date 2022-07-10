import pytest

from src.main import FileObject


@pytest.fixture()
def file_object(test_storage, constants):
    FileObject.storage = test_storage()

    return FileObject(constants.OBJECT_NAME.value, constants.BUCKET_NAME.value)


def test_write(file_object: FileObject, constants):
    file_object.write(constants.CONTENT.value)


def test_read(file_object: FileObject, constants):
    assert file_object.read() == constants.CONTENT.value


def test_delete(file_object: FileObject):
    file_object.delete()
