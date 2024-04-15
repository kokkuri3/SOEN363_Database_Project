import csv
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://soen363prjoect2:fQqnbq4VU7LxmAO6@cluster0.y4umf8o.mongodb.net/')

# Select database and collection
db = client['soen363p2']
collection = db['User']

# Read CSV file and insert data into MongoDB
with open('..\..\Database CSV Exported Data\User.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        row['user_id'] = int(row['user_id'])
        
        collection.insert_one(row)