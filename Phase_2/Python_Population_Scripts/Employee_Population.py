import csv
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://soen363prjoect2:fQqnbq4VU7LxmAO6@cluster0.y4umf8o.mongodb.net/')

# Select database and collection
db = client['soen363p2']
collection = db['Employee']

# Read CSV file and insert data into MongoDB
with open('..\..\Database CSV Exported Data\Employee.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        row['employee_id'] = int(row['employee_id'])  
        row['user_id'] = int(row['user_id'])  
        
        collection.insert_one(row)