from faker import Faker
import mysql.connector
from datetime import datetime, timedelta
import random

# Initialize Faker
fake = Faker()

# Establish database connection
db_connection = mysql.connector.connect(
    host="localhost",         #Change all the information Accordingly
    port= 3306,
    user="root",              
    password="password",      #Change this to the Password of your database
    database="database_name"  #Change this for the name of your database
)
cursor = db_connection.cursor()

# Generate and insert data into User table
for _ in range(550000):
    user_id = random.randint(1, 999999)
    # Check if user_id already exists in the database
    while True:
        cursor.execute("SELECT COUNT(*) FROM User WHERE user_id = %s", (user_id,))
        if cursor.fetchone()[0] == 0:
            break  # user_id is unique, exit the loop
        else:
            user_id = random.randint(1, 999999)  # Generate a new user_id

    name = fake.name()
    contact_number = fake.phone_number()[:10]
    email = fake.email()

    sql = "INSERT INTO User (user_id, name, contact_number, email) VALUES (%s, %s, %s, %s)"
    values = (user_id, name, contact_number, email)
    cursor.execute(sql, values)
print("1. User Table Insert Complete")

# Generate and insert data into Car table
for _ in range(550000):
    car_id = random.randint(10**8, 10**9 - 1)
    # Check if car_id already exists in the database
    while True:
        cursor.execute("SELECT COUNT(*) FROM Car WHERE car_id = %s", (car_id,))
        if cursor.fetchone()[0] == 0:
            break  # car_id is unique, exit the loop
        else:
            car_id = random.randint(10**8, 10**9 - 1)  # Generate a new car_id

    name = fake.company()
    year = fake.year()
    mpg = random.uniform(10, 40)
    horsepower = random.randint(50, 300)

    sql = "INSERT INTO Car (car_id, name, year, mpg, horsepower) VALUES (%s, %s, %s, %s, %s)"
    values = (car_id, name, year, mpg, horsepower)
    cursor.execute(sql, values)
print("2. Car Table Insert Complete")

# Generate and insert data into Customer table
for _ in range(550000):
    customer_id = random.randint(1, 999999)
    # Check if customer_id already exists in the database
    while True:
        cursor.execute("SELECT COUNT(*) FROM Customer WHERE customer_id = %s", (customer_id,))
        if cursor.fetchone()[0] == 0:
            break  # customer_id is unique, exit the loop
        else:
            customer_id = random.randint(1, 999999)  # Generate a new customer_id

    # Generate a user_id that exists in the user table
    user_id = random.randint(1, 999999)
    while True:
        cursor.execute("SELECT COUNT(*) FROM User WHERE user_id = %s", (user_id,))
        if cursor.fetchone()[0] == 1:
            break  # user_id exists, exit the loop
        else:
            user_id = random.randint(1, 999999)  # Generate a new user_id

    premium = random.choice([True, False])

    sql = "INSERT INTO Customer (customer_id, user_id, premium) VALUES (%s, %s, %s)"
    values = (customer_id, user_id, premium)
    cursor.execute(sql, values)
print("3. Customer Table Insert Complete")

# Generate and insert data into Employee table
positions = ['Manager', 'Salesperson', 'Mechanic']
for _ in range(550000):
    employee_id = random.randint(1, 999999)
    # Check if employee_id already exists in the database
    while True:
        cursor.execute("SELECT COUNT(*) FROM Employee WHERE employee_id = %s", (employee_id,))
        if cursor.fetchone()[0] == 0:
            break  # employee_id is unique, exit the loop
        else:
            employee_id = random.randint(1, 999999)  # Generate a new employee_id

    # Generate a user_id that exists in the user table
    user_id = random.randint(1, 999999)
    while True:
        cursor.execute("SELECT COUNT(*) FROM User WHERE user_id = %s", (user_id,))
        if cursor.fetchone()[0] == 1:
            break  # user_id exists, exit the loop
        else:
            user_id = random.randint(1, 999999)  # Generate a new user_id

    position = random.choice(positions)

    sql = "INSERT INTO Employee (employee_id, user_id, position) VALUES (%s, %s, %s)"
    values = (employee_id, user_id, position)
    cursor.execute(sql, values)
print("4. Employee Table Insert Complete")

# Generate and insert data into Reservation table
for _ in range(550000):
    reservation_id = random.randint(1, 999999)
    # Check if reservation_id already exists in the database
    while True:
        cursor.execute("SELECT COUNT(*) FROM Reservation WHERE reservation_id = %s", (reservation_id,))
        if cursor.fetchone()[0] == 0:
            break  # reservation_id is unique, exit the loop
        else:
            reservation_id = random.randint(1, 999999)  # Generate a new reservation_id

    # Generate a customer_id that exists in the customer table
    customer_id = random.randint(1, 999999)
    while True:
        cursor.execute("SELECT COUNT(*) FROM Customer WHERE customer_id = %s", (customer_id,))
        if cursor.fetchone()[0] == 1:
            break  # customer_id exists, exit the loop
        else:
            customer_id = random.randint(1, 999999)  # Generate a new customer_id

    rental_date = fake.date_this_year()
    return_date = rental_date + timedelta(days=random.randint(1, 14))

    sql = "INSERT INTO Reservation (reservation_id, customer_id, rental_date, return_date) VALUES (%s, %s, %s, %s)"
    values = (reservation_id, customer_id, rental_date, return_date)
    cursor.execute(sql, values)
print("5. Reservation Table Insert Complete")

# Generate and insert data into Reviews table
for _ in range(550000):
    review_id = random.randint(1, 999999)
    # Check if review_id already exists in the database
    while True:
        cursor.execute("SELECT COUNT(*) FROM Reviews WHERE review_id = %s", (review_id,))
        if cursor.fetchone()[0] == 0:
            break  # review_id is unique, exit the loop
        else:
            review_id = random.randint(1, 999999)  # Generate a new review_id

    # Generate a customer_id that exists in the customer table
    customer_id = random.randint(1, 999999)
    while True:
        cursor.execute("SELECT COUNT(*) FROM Customer WHERE customer_id = %s", (customer_id,))
        if cursor.fetchone()[0] == 1:
            break  # customer_id exists, exit the loop
        else:
            customer_id = random.randint(1, 999999)  # Generate a new customer_id

    # Generate rating within the allowed range (1 to 5)
    rating = round(random.uniform(1, 5), 1)

    # Decide whether description should be NULL or not (50% chance)
    if random.random() < 0.5:
        description = None
    else:
        description = fake.text()

    sql = "INSERT INTO Reviews (review_id, customer_id, rating, description) VALUES (%s, %s, %s, %s)"
    values = (review_id, customer_id, rating, description)
    cursor.execute(sql, values)
print("6. Reviews Table Insert Complete")

# Commit changes
db_connection.commit()
cursor.close()
db_connection.close()

print("Data inserted successfully")
