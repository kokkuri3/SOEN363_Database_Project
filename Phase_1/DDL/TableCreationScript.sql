-- Car table
CREATE TABLE Car (
    car_id INT PRIMARY KEY,
    name VARCHAR(255),
    year INT,
    mpg INT,
    horsepower INT
);

-- User table
CREATE TABLE User (
    user_id INT PRIMARY KEY,
    name VARCHAR(255),
    contact_number VARCHAR(15),
    email VARCHAR(255)
);

-- Customer table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    user_id INT,
    premium BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Employee table
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    user_id INT,
    position ENUM('Manager', 'Salesperson', 'Mechanic'),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Reservation table
CREATE TABLE Reservation (
    reservation_id INT PRIMARY KEY,
    car_id INT,
    customer_id INT,
    rental_date DATE,
    return_date DATE,
    FOREIGN KEY (car_id) REFERENCES Car(car_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    INDEX covering_constraint (customer_id, car_id)
);

-- Reviews table (weak entity)
CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    customer_id INT,
    rating DECIMAL(2,1) CHECK (rating BETWEEN 1 AND 5),
    description VARCHAR(1000),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
