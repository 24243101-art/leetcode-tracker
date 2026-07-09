-- Last updated: 7/9/2026, 10:07:36 AM
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
);