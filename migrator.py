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

#Key list
k = []
# Values for corresponding keys
v = []

for f in file:
 for x in range( len ( f.keys() ) ):
     k.append(f.keys()[x])

 for x in range( len ( f.keys() ) ):
    # Dyanamo does not support float types so check if value is float , if yes then convert to decimal 
    if type(f[f.keys()[x]])==float:
      v.append(Decimal(f[f.keys()[x]]))
     
    else:
      v.append(f[f.keys()[x]])

 print ("adding:", dict(zip(k,v)))
 #Write request to dynamo
 table.put_item(Item=dict(zip(k,v)))
