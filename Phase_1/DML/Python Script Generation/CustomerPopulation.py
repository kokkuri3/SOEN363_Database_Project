import re
import random

# Function to generate unique customer_id
def generate_customer_id(existing_ids):
    while True:
        customer_id = random.randint(1, 999999)
        if customer_id not in existing_ids:
            existing_ids.add(customer_id)
            return customer_id

# Function to generate random premium status (True or False)
def generate_premium():
    return random.choice([True, False])

# Read data from UserPopulation.sql to get a list of generated user_ids
existing_user_ids = set()
with open('UserPopulation.sql', 'r') as user_sql_file:
    for line in user_sql_file:
        match = re.match(r"\((\d+),", line.strip())
        if match:
            user_id = int(match.group(1))
            existing_user_ids.add(user_id)

# Generate SQL script to insert records into Customer table
sql_script = "INSERT INTO Customer (customer_id, user_id, premium) VALUES\n"

for user_id in existing_user_ids:
    customer_id = generate_customer_id(set())
    premium = generate_premium()
    
    sql_script += f"({customer_id}, {user_id}, {premium}),\n"

# Remove the last comma and add a semicolon
sql_script = sql_script.rstrip(',\n') + ';'

# Write SQL script to file
with open('CustomerPopulation.sql', 'w') as sqlfile:
    sqlfile.write(sql_script)

print("CustomerPopulation.sql file has been created.")
