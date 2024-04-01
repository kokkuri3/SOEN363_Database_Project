import re
import random

# Function to generate unique employee_id
def generate_employee_id(existing_ids):
    while True:
        employee_id = random.randint(1, 999999)
        if employee_id not in existing_ids:
            existing_ids.add(employee_id)
            return employee_id

# Function to generate random position ('Manager', 'Salesperson', 'Mechanic')
def generate_position():
    positions = ['Manager', 'Salesperson', 'Mechanic']
    return random.choice(positions)

# Read data from UserPopulation.sql to get a list of generated user_ids
existing_user_ids = set()
with open('UserPopulation.sql', 'r') as user_sql_file:
    for line in user_sql_file:
        match = re.match(r"\((\d+),", line.strip())
        if match:
            user_id = int(match.group(1))
            existing_user_ids.add(user_id)

# Generate SQL script to insert records into Employee table
sql_script = "INSERT INTO Employee (employee_id, user_id, position) VALUES\n"

for user_id in existing_user_ids:
    employee_id = generate_employee_id(set())
    position = generate_position()
    
    sql_script += f"({employee_id}, {user_id}, '{position}'),\n"

# Remove the last comma and add a semicolon
sql_script = sql_script.rstrip(',\n') + ';'

# Write SQL script to file
with open('EmployeePopulation.sql', 'w') as sqlfile:
    sqlfile.write(sql_script)

print("EmployeePopulation.sql file has been created.")
