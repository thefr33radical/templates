
#### Upload File to S3 in CSV format from list to CSV
```
def uploadS3(value=[],timestamp=[],bucketname="",path="",id="",secretkey="",region=""):
    """
    value : list
    timestamp : list
    Both value, timestamp are of equal length
    """
    try:    
      # Ex list values, substitute with own
      value=["234","345","345","445","346"]
      timestamp= ["tue","wed","thu","fri","sat"]

      # Add comma seperator and new line for list value
      csv_file=""
      for i,j in zip(value,timestamp):
         csv_file+="i"+","+j
         csv_file+="\n"
       encoded_string = csvContent.encode("utf-8")

      # Upload using boto3 put
      session =boto3.Session(aws_access_key_id=id,aws_secret_access_key=secretkey,region_name=region)
      s3 = session.resource('s3')        
      obj = s3.Object(bucket_name, path)
      obj.put(Body=encoded_string)

      return 1
    except Exception as e:
        logging.error(e)
        return 0
```
