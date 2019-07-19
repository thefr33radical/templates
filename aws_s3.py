
# Upload File to S3 in CSV format from list to CSV
def uploadS3(value=[],timestamp=[],bucketname="",path=""):
    """
    value : list
    timestamp : list
    Both value, timestamp are of equal length
    """
    try:
    
      value=["234","345","345","445","346"]
      timestamp= ["tue","wed","thu","fri","sat"]

      csv_file=""
      for i,j in zip(value,timestamp):
         csv_file+="i"+","+j
         csv_file+="\n"

      # Method 1: Object.put()
      s3 = boto3.resource('s3')
      obj = s3.Object(bucketname, path)
      obj.put(Body=csv_file)
      return 1
    except Exception as e:
        logging.error(e)
        return 
