import csv
import random

# Set to store generated car IDs
generated_ids = set()

# Function to generate unique car_id as a random 9-digit integer
def generate_car_id():
    while True:
        car_id = random.randint(10**8, 10**9 - 1)
        if car_id not in generated_ids:
            generated_ids.add(car_id)
            return car_id

# Function to generate random year in the range of 2010-2024
def generate_year():
    return random.randint(2010, 2024)

# Read data from CSV and generate SQL script
with open('Automobile.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    sql_script = "INSERT INTO Car (car_id, name, year, mpg, horsepower) VALUES\n"

    for row in reader:
        car_id = generate_car_id()
        name = f"'{row['name']}'" if row.get('name') else 'NULL'  # Check if 'name' field exists, if not, use 'NULL'
        year = generate_year()
        mpg = row.get('mpg', 'NULL') if row.get('mpg') else 'NULL'  # Check if 'mpg' field exists, if not, use 'NULL'
        horsepower = row.get('horsepower', 'NULL') if row.get('horsepower') else 'NULL'  # Check if 'horsepower' field exists, if not, use 'NULL'
        
        sql_script += f"({car_id}, {name}, {year}, {mpg}, {horsepower}),\n"

# Remove the last comma and add a semicolon
sql_script = sql_script.rstrip(',\n') + ';'

# Write SQL script to file
with open('CarPopulation.sql', 'w') as sqlfile:
    sqlfile.write(sql_script)

print("CarPopulation.sql file has been created.")
