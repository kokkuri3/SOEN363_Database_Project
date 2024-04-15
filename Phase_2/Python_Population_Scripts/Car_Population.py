import csv
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://soen363prjoect2:fQqnbq4VU7LxmAO6@cluster0.y4umf8o.mongodb.net/')

# Select database and collection
db = client['soen363p2']
collection = db['Car']

# Read CSV file and insert data into MongoDB
with open('..\..\Database CSV Exported Data\Car.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        row['car_id'] = int(row['car_id'])  
        row['year'] = int(row['year']) 
        row['mpg'] = int(row['mpg']) 
        row['horespower'] = int(row['horespower']) 
        
        collection.insert_one(row)