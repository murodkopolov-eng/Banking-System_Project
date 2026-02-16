Banking-System

Modern Banking Analytics Using Business Intelligence (BI)

Project Overview

This project simulates a modern banking system to demonstrate how Business Intelligence (BI) can be used to analyze operational, financial, and customer data. The system consists of 30 tables representing accounts, loans, customers, transactions, branches, and other relevant banking entities. All tables are populated with realistic synthetic data generated using Python's Faker library.

The database is structured using a Star Schema to enable efficient analytics and KPI computation.

#Objectives

Create a realistic banking data warehouse with multiple related tables. Implement a Star Schema to optimize queries and analytics. Populate tables with synthetic data using Python Faker. Calculate key performance indicators (KPIs) to simulate real-world banking analytics.

Star Schema Structure

Fact Tables: Transactions, Loans, Account Balances Dimension Tables: Customers, Branches, Accounts, Loan Types, etc. Relationships: Primary and foreign keys are defined to link dimensions with fact tables, supporting efficient joins for KPI calculations.
