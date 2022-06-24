# File Objects

## Usage

```Python
from src.main import FileObject
from src.storages import S3Storage

AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'

FileObject.storage = S3Storage(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

file = FileObject('your_bucket_name/{your_path_to_file')


# write
file.write(b'some_content')

# read
content: bytes = file.read()

# delete
file.delete()

```