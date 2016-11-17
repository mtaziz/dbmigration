import boto3
import json
from decimal import *
import argparse
from decimal import *

#create a boto3 resource for Dynamo
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")

# Set the the target table for the boto3 resource (dynamo)
table = dynamodb.Table('targetTable')


parser = argparse.ArgumentParser(description="Simple migration script.")
parser.add_argument("-i", "--input", dest='input', action='store',help='input file')
args = parser.parse_args()

with open(args.input) as json_file:
  file = json.load(json_file)

for obj in file:
      
        key1 = obj['key1']
        key2= obj['key2']
        key3 = obj['key3']
        key4 = obj['key4']
        key5 = obj['key5']
        key5 = obj['key6']
        print("Adding :", key1, key2, key3, key4,key5,key6)
        table.put_item(
           Item={
               'key1': key1,
               'key2': key2,
               'key3': key3,
               'key4': key4,
               'key5': key5,
               'key6': key6
            }
        )
