# dbmigration
Migration script from MongoDB to DynamoDB

---------Migration Instructions----------

1.Get a Mongo dump of your existing Mongo databases

$ mongodump --db db_name --collection collection_name --host hostname:port --out /path/to/dir

2.Convert the BSON file/s to JSON with the bsondump utility:

$bsondump /path/to/dir/name_of_bson_file.bson > /path/to/dir/name_of_json_file.json

3.Get a temporary AWStoken to get credentials to use AWS SDK for Python

4.Run migrator.py :

$ ./migrator.py -i name_of_json_file.json

