# used for catapult coding test
import boto3
import datetime

def getObjects(client,bucket,token=None,objects=[]):
    if(token):
        response = client.list_objects_v2(Bucket=bucket,ContinuationToken=token)
    else:
        response = client.list_objects_v2(Bucket=bucket)
    try:
        objects += response['Contents']
    except KeyError as e:
        #nothing in the bucket
        return objects
    if(response['IsTruncated']):
        getObjects(client,bucket,response['NextContinuationToken'],objects)
    else:
        return objects

def calcTotalSize(objects):
    totalSize = 0
    for obj in objects:
        totalSize += obj['Size']
    return totalSize

def calcLastModifiedDate(objects):
    latestModifiedDate = None
    for obj in objects:
        if latestModifiedDate:
            if latestModifiedDate < obj['LastModified']:
                latestModifiedDate = obj['LastModified']
        else:
            latestModifiedDate = obj['LastModified']
    return latestModifiedDate

def calcCost(client):
    cost = 0.0
    token = None
    results = []
    now = datetime.datetime.now()
    while True:
        if token:
            kwargs = {'NextPageToken': token}
        else:
            kwargs = {}
        data = client.get_cost_and_usage(TimePeriod={'Start': '2018-11-20', 'End': now.strftime("%Y-%m-%d")}, Granularity='DAILY', Metrics=['UnblendedCost'], GroupBy=[{'Type': 'DIMENSION', 'Key': 'LINKED_ACCOUNT'}, {'Type': 'DIMENSION', 'Key': 'SERVICE'}], **kwargs)
        results += data['ResultsByTime']
        token = data.get('NextPageToken')
        if not token:
            for result in results:
                for group in result['Groups']:
                    for key in group['Keys']:
                        if "Amazon Simple Storage Service" in key:
                            cost =+ float(group['Metrics']['UnblendedCost']['Amount'])
            return cost

def calcRow(bucket,objects):
    bucketdict = {}
    bucketdict['BucketName']=bucket['Name']
    bucketdict['CreationDate']=str(bucket['CreationDate'])
    bucketdict['NumFiles']=str(len(objects))
    bucketdict['TotalSize']=calcTotalSize(objects)
    bucketdict['LastModifiedDate']=str(calcLastModifiedDate(objects))
    return bucketdict

def catapult():
    rows = []
    cost = 0
    # if any of the s3 calls throw up just return empty table
    try:
        client = boto3.client('s3')
        ceClient = boto3.client('ce')
        cost = calcCost(ceClient)
        response = client.list_buckets()
        for bucket in response['Buckets']:
            objects = getObjects(client,bucket['Name'],None,[])
            rows.append(calcRow(bucket,objects))
    except Exception as e:
        return rows
    return (cost,rows)
