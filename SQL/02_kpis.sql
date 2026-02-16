--•	Top 3 Customers with the Highest Total Balance Across All Accounts 

SELECT 
      TOP 3
	  c.CustomerID,
	  c.FullName,
	  SUM( a.Balance ) AS TotalBalance
FROM Customers AS c
INNER JOIN Accounts AS a ON c.CustomerID = a.CustomerID
GROUP BY c.CustomerID,c.FullName
ORDER BY TotalBalance DESC

--•	Customers Who Have More Than One Active Loan

SELECT 
      c.FullName,
	  l.CustomerID,
	  COUNT( l.Status ) AS Number_Of_Status
FROM Customers AS c
INNER JOIN Loans AS l on c.CustomerID = l.CustomerID
WHERE l.Status = 'Active'
GROUP BY c.FullName,l.CustomerID
HAVING COUNT( l.Status ) > 1

--•	Transactions That Were Flagged as Fraudulent     

SELECT 
      c.CustomerID,
	  c.FullName,
	  f.TransactionID,
	  f.RiskLevel
FROM Customers AS c
INNER JOIN FraudDetection AS f ON c.CustomerID = f.CustomerID
WHERE f.RiskLevel = 4

--•	Total Loan Amount Issued Per Branch

SELECT 
      b.BranchID,
	  b.BranchName,
	  SUM( l.Amount ) AS Total_Amount_Per_Branch
FROM Branches AS b
INNER JOIN Accounts AS a ON b.BranchID = a.BranchID
INNER JOIN Customers AS c ON c.CustomerID = a.CustomerID
INNER JOIN Loans AS l ON c.CustomerID = l.CustomerID
GROUP BY b.BranchID,b.BranchName

--•	Customers who made multiple large transactions (above $10,000) within a short time frame (less than 1 hour apart)

SELECT 
      c.CustomerID,
	  c.FullName,
	  t1.TransactionID,
	  t2.TransactionID,
	  t1.Amount AS FirstAmount,
	  t2.Amount AS SecondAmount,
	  t1.Date AS FirstDate,
	  t2.Date AS SecondDate,
	  DATEDIFF(MINUTE,t1.Date,t2.Date) AS MinutesBetween
FROM Transactions AS t1
INNER JOIN Transactions AS t2 ON t1.TransactionID < t2.TransactionID
INNER JOIN Accounts AS a1 ON t1.AccountID = a1.AccountID
INNER JOIN Accounts AS a2 ON t2.AccountID = a2.AccountID
INNER JOIN Customers AS c ON a1.CustomerID = c.CustomerID
WHERE 
     a1.CustomerID = a2.CustomerID
	 AND
     t1.Amount > 10000
	 AND
	 t2.Amount > 10000
	 AND
	 DATEDIFF(MINUTE,t1.Date,t2.Date) < 60
ORDER BY c.CustomerID,t1.Date ASC

--•	 Find employees who earn more than average salary than their department.

SELECT * FROM Employees AS e1
WHERE Salary > ( SELECT AVG( Salary ) FROM Employees AS e2 WHERE e1.Department = e2.Department )

--• Calculate the number of position for per department

SELECT 
      Department,
	  COUNT( Position ) AS Number_Of_Postions_Per_Department
FROM Employees
GROUP BY Department

--• Find top 3 employees in each department with the highest salary

GO
WITH CTE_RESULT AS (
					SELECT 
					      EmployeeID,
						  FullName,
						  Position,
						  Department,
						  Salary,
						  ROW_NUMBER() OVER ( PARTITION BY Department ORDER BY Salary DESC ) AS rwn
						  FROM Employees )
						  SELECT * FROM CTE_RESULT
						  WHERE rwn <= 3
