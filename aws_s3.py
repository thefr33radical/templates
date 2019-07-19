
import boto3
import logging

# Upload File to S3 in CSV format from list to CSV
def uploadS3(value=[],timestamp=[],bucketname="",path=""):
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
            
      # Upload using boto3 put
      s3 = boto3.resource('s3')
      obj = s3.Object(bucketname, path)
      obj.put(Body=csv_file)
      return 1
    except Exception as e:
        logging.error(e)
        return 0
