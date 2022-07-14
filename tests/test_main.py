import pytest

from src.main import File


@pytest.fixture()
def file_object(test_storage, constants):
    File.storage = test_storage()

    return File(constants.OBJECT_NAME.value, constants.BUCKET_NAME.value)


def test_write(file_object: File, constants):
    file_object.write(constants.CONTENT.value)


def test_read(file_object: File, constants):
    assert file_object.read() == constants.CONTENT.value


def test_delete(file_object: File):
    file_object.delete()
