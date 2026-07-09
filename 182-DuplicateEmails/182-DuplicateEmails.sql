-- Last updated: 7/9/2026, 10:07:37 AM
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;