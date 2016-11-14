import boto3
import json
import argparse
from decimal import *

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")

table = dynamodb.Table('targetTable')

parser = argparse.ArgumentParser(description="Data Migration Script.")
parser.add_argument("-i", "--input", dest='input', action='store',help='input file')
args = parser.parse_args()

with open(args.input) as json_file:
  file = json.load(json_file)


key = []
value = []

for f in file:
 for x in range( len ( f.keys() ) ):

       list1.append(f.keys()[x])

 for x in range( len ( f.keys() ) ):
     
     if type(f[f.keys()[x]])==float:
     
      list2.append(Decimal(f[f.keys()[x]]))
     
     else:
     
      list2.append(f[f.keys()[x]])

 print ("adding:", dict(zip(key,value)))
 
 table.put_item(Item = dict(zip(key,value)))
