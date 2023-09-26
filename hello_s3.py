"""
Build an S3 list tool that lists all the buckets in my account
"""
import boto3


# build a connection to s3 as a function
def s3_connection():
    s3 = boto3.resource("s3")
    return s3


# build a function to list s3 buckets
def s3_list_buckets(s3):
    """List buckets in my account"""
    for bucket in s3.buckets.all():
        print(bucket.name)


# invoke main function
def main():
    s3 = s3_connection()
    s3_list_buckets(s3)


if __name__ == "__main__":
    main()
