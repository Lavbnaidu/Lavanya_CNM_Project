# Lavanya project 2
import boto3

newS3 = boto3.client('s3')
response=newS3.list_buckets()
bucketsList = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: %s" % bucketsList)
with open(r's3.txt', 'w') as fp:
    for item in bucketsList:
        # write each item on a new line
        fp.write("%s\n" % item)
print('Done')