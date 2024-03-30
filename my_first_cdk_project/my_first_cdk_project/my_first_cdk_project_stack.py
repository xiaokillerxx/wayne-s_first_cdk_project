from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as _s3
)
from constructs import Construct

class MyFirstCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="wane-testing-cdk-bucket",
            versioned=True,
            encryption=_s3.BucketEncryption.S3_MANAGED
        )
