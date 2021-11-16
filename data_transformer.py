import json
import boto3
import yfinance as yf 

kinesis = boto3.client('kinesis', "us-east-2")

def lambda_handler(event, context):
    data = ['FB','SHOP','BYND','NFLX','PINS','SQ','TTD','OKTA','SNAP','DDOG']
    for val in data:
        tickers=yf.Ticker(val)
        hist=tickers.history(interval='5m', start='2021-05-11', end='2021-05-12')
        for index, row in hist.iterrows():
            values={'high':round(row['High'],2),
                'low':round(row['Low'],2),
                'ts':index.strftime('%Y-%m-%d %X'),
                'name':val}
            convert=json.dumps(values)+"\n"
                
            kinesis.put_record(
                StreamName="kinesis_stream_finance",
                Data=convert,
                PartitionKey="partitionkey")
        
    return {
        'statusCode': 200,
        'body': json.dumps("Complete!")
    }
    
    