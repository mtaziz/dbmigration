#!/usr/bin/env python
import argsparse
import boto3
from decimal import *
import json



dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
table = dynamodb.Table('targetTable')
parser = argparse.ArgumentParser(description="Mongo data migrator.")
parser.add_argument("-i", "--input", dest='input', action='store',help='Input file name')
args = parser.parse_args()

with open(args.input) as json_file:
    file = json.load(json_file)

    for f in file:
        v=f.values()
        for value in f.values():
            if type(value)==float:
                index = v.index(value)
                val = Decimal(value)
                v.pop(index)
                v.insert(index,val)
                print ("Adding:",dict(zip(f.keys(),v)))
                table.put_item(Item=dict(zip(f.keys(),v)))

        if any(isinstance(value,float) for value in f.values()) is not True:
         print ("Adding:",dict(zip(f.keys(),v)))
         table.put_item(Item=dict(zip(f.keys(),v)))
