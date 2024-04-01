import re
import random

# Function to generate unique review_id
def generate_review_id(existing_ids):
    while True:
        review_id = random.randint(1, 999999)
        if review_id not in existing_ids:
            existing_ids.add(review_id)
            return review_id

# Function to generate random rating between 1 and 5
def generate_rating():
    return round(random.uniform(1, 5), 1)

# Function to generate random description (can also be NULL)
def generate_description():
    if random.random() < 0.5:  # 50% chance of having a description
        return f"'Description {random.randint(1, 1000)}'"
    else:
        return 'NULL'

# Generate random text reviews
text_reviews = [
    "Great car rental experience, highly recommended!",
    "The car was clean and well-maintained. Excellent service!",
    "Smooth process from booking to return. Will rent again!",
    "Average car, but the customer service was fantastic.",
    "Very convenient and affordable. No complaints.",
    "Disappointing experience. The car had mechanical issues.",
    "Friendly staff and easy pickup/drop-off. Thank you!",
    "I had a great time driving the rental car. Thank you!",
    "The rental process was quick and hassle-free.",
    "Decent car for the price. Would consider renting again.",
    "Unprofessional service. Avoid if possible.",
    "The car was not cleaned properly. Disappointed.",
    "Excellent value for money. Will definitely use again!",
    "The car smelled like smoke. Not satisfied with the cleanliness.",
    "Smooth transaction. Good communication with the rental company.",
    "The car had low mileage and performed well.",
    "Rude staff and long wait times. Would not recommend.",
    "Average experience. Nothing exceptional but nothing terrible either.",
    "The rental was overpriced for the quality of the car.",
    "The rental company provided great customer service.",
]

# Read data from CustomerPopulation.sql to get a list of generated customer_ids
existing_customer_ids = set()
with open('CustomerPopulation.sql', 'r') as customer_sql_file:
    for line in customer_sql_file:
        match = re.match(r"\((\d+),", line.strip())
        if match:
            customer_id = int(match.group(1))
            existing_customer_ids.add(customer_id)

# Generate SQL script to insert records into Reviews table
sql_script = "INSERT INTO Reviews (review_id, customer_id, rating, description) VALUES\n"

existing_review_ids = set()

for _ in range(150):  # Generating around 150 reviews
    review_id = generate_review_id(existing_review_ids)
    customer_id = random.choice(list(existing_customer_ids))
    rating = generate_rating()
    description = generate_description()
    text_review = random.choice(text_reviews) if description != 'NULL' else 'NULL'
    
    sql_script += f"({review_id}, {customer_id}, {rating}, {description}),\n"

# Remove the last comma and add a semicolon
sql_script = sql_script.rstrip(',\n') + ';'

# Write SQL script to file
with open('ReviewsPopulation.sql', 'w') as sqlfile:
    sqlfile.write(sql_script)

print("ReviewsPopulation.sql file has been created.")
