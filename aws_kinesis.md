### References

* https://streamsets.com/blog/creating-dataflow-pipelines-amazon-kinesis/

~ 
#### Decoding Kinesis Stream Data
def Decode_Kinesis(kinesis_stream_data):
    try:
        text = kinesis_stream_data
        bin_data = base64.b64decode(text)
        json_data = json.loads(bin_data)
        logging.info(" RECEIVED JSON : ", json_data)
        values = DecodeData(json_data[0]["data"])
        timestamp = json_data[0]["published_at"]
        logging.info(" PLAIN TEXT : ",normal_text)
        return values,timestamp
    except Exception as e:
        logging.error(e)
        return [], None

~
