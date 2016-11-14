import boto3
import json
from decimal import *
import argparse
from decimal import *

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")

table = dynamodb.Table('demo')


with open("/Users/uashfaq/rnd/python/data/json/d.json") as json_file:
    file = json.load(json_file)

k = []
v = []

for f in file:
 for x in range( len ( f.keys() ) ):
     k.append(f.keys()[x])

 for x in range( len ( f.keys() ) ):
     if type(f[f.keys()[x]])==float:
      v.append(Decimal(f[f.keys()[x]]))
     else:
      v.append(f[f.keys()[x]])

 print ("adding:", dict(zip(k,v)))
 table.put_item(Item=dict(zip(k,v)))
