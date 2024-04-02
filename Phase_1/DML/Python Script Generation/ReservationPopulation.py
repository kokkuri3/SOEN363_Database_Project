import re
import random
from datetime import datetime, timedelta

# Function to generate unique reservation_id
def generate_reservation_id(existing_ids):
    while True:
        reservation_id = random.randint(1, 999999)
        if reservation_id not in existing_ids:
            existing_ids.add(reservation_id)
            return reservation_id

# Function to generate random rental_date within a given range
def generate_rental_date():
    start_date = datetime(2022, 1, 1)  # Start date range (adjust as needed)
    end_date = datetime(2024, 12, 31)   # End date range (adjust as needed)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Function to generate random return_date within a given range from rental_date
def generate_return_date(rental_date):
    return rental_date + timedelta(days=random.randint(1, 14))  # Return date within 1 to 14 days from rental_date

# Read data from CarPopulation.sql to get a list of generated car_ids
existing_car_ids = set()
with open('CarPopulation.sql', 'r') as car_sql_file:
    for line in car_sql_file:
        match = re.match(r"\((\d+),", line.strip())
        if match:
            car_id = int(match.group(1))
            existing_car_ids.add(car_id)

# Read data from CustomerPopulation.sql to get a list of generated customer_ids
existing_customer_ids = set()
with open('CustomerPopulation.sql', 'r') as customer_sql_file:
    for line in customer_sql_file:
        match = re.match(r"\((\d+),", line.strip())
        if match:
            customer_id = int(match.group(1))
            existing_customer_ids.add(customer_id)

# Generate SQL script to insert records into Reservation table
sql_script = "INSERT INTO Reservation (reservation_id, car_id, customer_id, rental_date, return_date) VALUES\n"

existing_reservation_ids = set()

for _ in range(100):  # Change 100 to the desired number of reservations
    reservation_id = generate_reservation_id(existing_reservation_ids)
    car_id = random.choice(list(existing_car_ids))
    customer_id = random.choice(list(existing_customer_ids))
    rental_date = generate_rental_date()
    return_date = generate_return_date(rental_date)
    
    sql_script += f"({reservation_id}, {car_id}, {customer_id}, '{rental_date.strftime('%Y-%m-%d')}', '{return_date.strftime('%Y-%m-%d')}'),\n"

# Remove the last comma and add a semicolon
sql_script = sql_script.rstrip(',\n') + ';'

# Write SQL script to file
with open('ReservationPopulation.sql', 'w') as sqlfile:
    sqlfile.write(sql_script)

print("ReservationPopulation.sql file has been created.")
