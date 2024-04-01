-- Car table
CREATE TABLE Car (
    car_id UUID PRIMARY KEY DEFAULT UUID_GENERATE_V4(),
    name VARCHAR(255),
    year INT,
    mpg INT,
    horsepower INT
);

-- User table
CREATE TABLE User (
    user_id UUID PRIMARY KEY DEFAULT UUID_GENERATE_V4(),
    name VARCHAR(255),
    contact_number VARCHAR(15),
    email VARCHAR(255)
);

-- Customer table
CREATE TABLE Customer (
    customer_id UUID PRIMARY KEY DEFAULT UUID_GENERATE_V4(),
    user_id UUID,
    premium BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Employee table
CREATE TABLE Employee (
    employee_id UUID PRIMARY KEY DEFAULT UUID_GENERATE_V4(),
    user_id UUID,
    position ENUM('Manager', 'Salesperson', 'Mechanic'),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Reservation table
CREATE TABLE Reservation (
    reservation_id UUID PRIMARY KEY DEFAULT UUID_GENERATE_V4(),
    car_id UUID,
    customer_id UUID,
    rental_date DATE,
    return_date DATE,
    FOREIGN KEY (car_id) REFERENCES Car(car_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- Reviews table (weak entity)
CREATE TABLE Reviews (
    review_id UUID PRIMARY KEY DEFAULT UUID_GENERATE_V4(),
    customer_id UUID,
    rating DECIMAL(2,1) CHECK (rating BETWEEN 1 AND 5),
    description VARCHAR(1000),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
