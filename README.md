# File Storages

## Usage

```Python
from file_storages import File
from file_storages import S3Storage

AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'

storage = S3Storage(
    'your_bucket_name',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

file = File('your_path_to_file', storage)
# or
file = File('your_path_to_file', 'another_bucket_name', storage)


# write
file.write(b'some_content')

# read
content: bytes = file.read()

# delete
file.delete()

```