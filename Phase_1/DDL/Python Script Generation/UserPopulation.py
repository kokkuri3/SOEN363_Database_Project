import csv
import random

# Function to generate unique user_id
def generate_user_id(existing_ids):
    while True:
        user_id = random.randint(1, 999999)
        if user_id not in existing_ids:
            existing_ids.add(user_id)
            return user_id

# Function to generate random phone number
def generate_phone_number():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

# Read data from CSV and generate SQL script
with open('car_purchasing.csv', newline='', encoding='latin-1') as csvfile:
    reader = csv.DictReader(csvfile)

    existing_ids = set()

    sql_script = "INSERT INTO User (user_id, name, contact_number, email) VALUES\n"

    for row in reader:
        user_id = generate_user_id(existing_ids)
        name = row['customer name']
        contact_number = generate_phone_number()
        email = row['customer e-mail']

        sql_script += f"({user_id}, '{name}', '{contact_number}', '{email}'),\n"

# Remove the last comma and add a semicolon
sql_script = sql_script.rstrip(',\n') + ';'

# Write SQL script to file
with open('UserPopulation.sql', 'w') as sqlfile:
    sqlfile.write(sql_script)

print("UserPopulation.sql file has been created.")
