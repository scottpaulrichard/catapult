# used for catapult coding test
import boto3
import time

filename = 'file.txt'
client = boto3.client('s3')

#create buckets for testing
for x in range(20):
    bucket_name = 'catapult-test-bucket-{}'.format(str(x))
    print(bucket_name)
    client.create_bucket(Bucket=bucket_name)
    with open(filename,mode='w') as f:
        f.write('hello_world_{}'.format(str(x)))
    print(bucket_name)
    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    client.upload_file(filename, bucket_name, '{}_{}'.format(filename,str(x)))

"""
#delete buckets for testing
for x in range(100):
    bucket_name = 'scrichar-test-bucket-{}'.format(str(x))
    print(bucket_name)
    filename_w_prefix = '{}_{}'.format(filename,str(x))
    try:
        client.delete_object(Bucket=bucket_name, Key=filename_w_prefix)
    except Exception as e:
        print(str(e))
    try:
        client.delete_bucket(Bucket=bucket_name)
    except Exception as e:
        print(str(e))
"""
