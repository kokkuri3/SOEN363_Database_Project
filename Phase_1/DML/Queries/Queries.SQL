-- Query 1 - Simple WHERE clause
SELECT *
FROM user u
WHERE u.name like 'B%';

-- Query 2 - Simple GROUP BY clause, Simple HAVING clause
SELECT *
FROM user u
GROUP BY u.user_id;

SELECT *
FROM user u
GROUP BY u.user_id
HAVING u.user_id >= 70000;

-- Query 3 - Simple cartesian product, Simple join
SELECT *
FROM customer c, reservation r
WHERE c.customer_id = r.customer_id;

SELECT * 
FROM customer c
JOIN reservation AS r ON c.customer_id = r.customer_id;

-- Query 4 - Various Join types and their result
SELECT *
FROM customer c
INNER JOIN reservation AS r ON c.customer_id = r.customer_id;

SELECT *
FROM customer c
RIGHT JOIN reservation AS r ON c.customer_id = r.customer_id;

SELECT *
FROM customer c
LEFT JOIN reservation AS r ON c.customer_id = r.customer_id;

-- Full join
SELECT *
FROM customer c, reservation r;

-- Query 5 - Correlated queries
-- Cars above the average price
SELECT c.name
FROM car c
WHERE c.car_id > (
	SELECT AVG(c2.car_id)
    FROM car c2
);

-- list of customers who made a single reservation
SELECT c.customer_id, u.name	
FROM customer c
JOIN user u on c.user_id = u.user_id
WHERE c.customer_id IN (
		SELECT r.customer_id
        FROM reviews r
)
GROUP BY c.customer_id, u.name
HAVING COUNT(c.customer_id) = 1
ORDER BY c.customer_id ASC;

-- list of customers who wrote any amount of reviews, along with the amount of reviews they made
SELECT c.customer_id, u.name, COUNT(DISTINCT c.customer_id) as amount_of_reviews
FROM customer c
JOIN user u on c.user_id = u.user_id
WHERE c.customer_id IN (
		SELECT r.customer_id
        FROM reservation r
)
GROUP BY c.customer_id, u.name
ORDER BY c.customer_id ASC;

-- Query 6 - Set operations
-- Intersect - emplouyees who are also customers
SELECT c.user_id  FROM customer c
INTERSECT
SELECT e.user_id FROM employee e;

SELECT c.user_id 
FROM customer c 
WHERE c.user_id IN (
	SELECT e.user_id 
    FROM employee e
);

-- UNION - all customer and all emplouyees
SELECT e.user_id FROM employee e
UNION
SELECT c.user_id FROM customer c;

SELECT DISTINCT e.user_id 
FROM employee e, customer c
ORDER BY e.user_id ASC;

-- DIFFERENCE - customers who did not leave reviews
SELECT c.customer_id FROM customer c
EXCEPT
SELECT r.customer_id FROM reservation r;

SELECT c.customer_id
FROM customer c
WHERE c.customer_id NOT IN (
	SELECT r.customer_id
    FROM reservation r
);

-- Query 7

-- Creating a view with premium customers only $$
CREATE VIEW premium_customers AS
    SELECT 
        *
    FROM
        Customer
    WHERE
        premium = TRUE;


-- Updating the view's definition...
DROP VIEW IF EXISTS premium_customers;
CREATE VIEW premium_customers AS
    SELECT 
        *
    FROM
        Customer
    WHERE
        premium = FALSE;

-- Now selecting from the view will reflect the non premium customers 🙂
SELECT 
    *
FROM
    premium_customers

-- Query 8

-- Part A
 --COMPLETING...

-- Part B
--COMPLETING...


-- Query 9

-- Check for overlapping reservations (same car & same customer)
SELECT 
    r1.*
FROM
    Reservation r1
        INNER JOIN
    Reservation r2 ON r1.car_id = r2.car_id
        AND r1.customer_id = r2.customer_id
WHERE
    r1.reservation_id <> r2.reservation_id
        AND r1.rental_date < r2.return_date
        AND r1.return_date > r2.rental_date;

-- Check covering constraints
--COMPLETING....


