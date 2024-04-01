import csv
import uuid
import random

# Function to generate unique car_id as UUID
def generate_car_id():
    return uuid.uuid4()  # Generate a random UUID (version 4)

# Function to generate random year in the range of 2010-2024
def generate_year():
    return random.randint(2010, 2024)

# Read data from CSV and generate SQL script
with open('Automobile.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    sql_script = "INSERT INTO Car (car_id, name, year, mpg, horsepower) VALUES\n"

    for row in reader:
        car_id = generate_car_id()
        name = row['name']
        year = generate_year()
        mpg = row['mpg']
        horsepower = row['horsepower']
        
        # Note: Use str() to convert UUID object to string representation
        sql_script += f"('{car_id}', '{name}', {year}, {mpg}, {horsepower}),\n"

# Remove the last comma and add a semicolon
sql_script = sql_script.rstrip(',\n') + ';'

# Write SQL script to file
with open('CarPopulation.sql', 'w') as sqlfile:
    sqlfile.write(sql_script)

print("CarPopulation.sql file has been created.")
