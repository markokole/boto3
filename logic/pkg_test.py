from botocore.exceptions import ClientError


class Logic:

    def __init(self):
        pass

    def list_buckets(self, s3_obj):

        try:

            # Call S3 to list current buckets
            response = s3_obj.list_buckets()

            # Get a list of all bucket names from the response
            buckets = [bucket['Name'] for bucket in response['Buckets']]

            # Print out the bucket list
            print("Bucket List: {}".format(buckets))
        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']
            print("Error code: {}. Error message: {}".format(error_code, error_message))
