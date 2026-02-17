Banking-System

Modern Banking Analytics Using Business Intelligence (BI)

Project Overview

This project simulates a modern banking system to demonstrate how Business Intelligence (BI) can be used to analyze operational, financial, and customer data. The system consists of 30 tables representing accounts, loans, customers, transactions, branches, and other relevant banking entities. All tables are populated with realistic synthetic data generated using Python's Faker library.

The database is structured using a Star Schema to enable efficient analytics and KPI computation.

#Objectives

Create a realistic banking data warehouse with multiple related tables. Implement a Star Schema to optimize queries and analytics. Populate tables with synthetic data using Python Faker. Calculate key performance indicators (KPIs) to simulate real-world banking analytics.

Star Schema Structure

Fact Tables: Transactions, Loans, Account Balances Dimension Tables: Customers, Branches, Accounts, Loan Types, etc. Relationships: Primary and foreign keys are defined to link dimensions with fact tables, supporting efficient joins for KPI calculations.

KPIs Computed

- Top 3 Customers with the Highest Total Balance Across All Accounts. 

- Customers Who Have More Than One Active Loan.

- Transactions That Were Flagged as Fraudulent.

- Total Loan Amount Issued Per Branch.

- Customers who made multiple large transactions (above $10,000) within a short time frame (less than 1 hour apart).

- Find employees who earn more than average salary than their department.

- Calculate the number of position for per department.

- Find top 3 employees in each department with the highest salary

Tools and Technologies

- Python for data generation (Faker library) 

- SQL Server for database and SQL queries 

- SQL for analytics and KPI calculations

