import csv
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://soen363prjoect2:fQqnbq4VU7LxmAO6@cluster0.y4umf8o.mongodb.net/')

# Select database and collection
db = client['soen363p2']
collection = db['Reservation']

# Read CSV file and insert data into MongoDB
with open('..\..\Database CSV Exported Data\Reservation.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        row['reservation_id'] = int(row['reservation_id']) 
        row['customer_id'] = int(row['customer_id']) 
        row['car_id'] = int(row['car_id'])  
        
        collection.insert_one(row)