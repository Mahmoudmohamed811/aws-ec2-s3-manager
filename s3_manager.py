import boto3

class S3Manager:
    def __init__(self):
        self.s3_client = boto3.client("s3")

    def create_bucket(self, bucket_name):
        try:
            if self.s3_client.meta.region_name == "us-east-1":
                # No LocationConstraint for us-east-1
                self.s3_client.create_bucket(Bucket=bucket_name)
            else:
                # Include LocationConstraint for other regions
                self.s3_client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={
                        "LocationConstraint": self.s3_client.meta.region_name
                    }
                )
            print(f"Created bucket: {bucket_name}")
        except Exception as e:
            print(f"Error creating bucket: {str(e)}")

    def list_buckets(self):
        try:
            response = self.s3_client.list_buckets()
            if response["Buckets"]:
                print("S3 Buckets:")
                for bucket in response["Buckets"]:
                    print(f" - {bucket['Name']}")
            else:
                print("No buckets found.")
        except Exception as e:
            print(f"Error listing buckets: {str(e)}")

    def delete_bucket(self, bucket_name):
        try:
            self.s3_client.delete_bucket(Bucket=bucket_name)
            print(f"Deleted bucket: {bucket_name}")
        except Exception as e:
            print(f"Error deleting bucket: {str(e)}")