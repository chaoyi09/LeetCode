SELECT e1.name
FROM Employee AS e1
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) AS t
ON e1.id = t.managerId;
