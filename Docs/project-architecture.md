# Banking Risk Intelligence — Project Architecture

## Solution Overview

Banking Risk Intelligence is an end-to-end analytics solution designed to analyze banking customers, loans, credit behavior, defaults, repayments, and transactions.

The project combines Python/Pandas, Microsoft Fabric, SQL, Power BI, DAX, Row-Level Security, and deployment workflows.

## End-to-End Architecture

```text
Banking Data
     │
     ▼
Python / Pandas
Data Cleaning & Analysis
     │
     ▼
Microsoft Fabric / OneLake
     │
     ▼
Banking_Risk_Lakehouse
     │
     ▼
SQL Analytics Endpoint
     │
     ▼
Semantic Model
     │
     ├── Customer Analysis
     ├── Loan Analysis
     ├── Credit Risk Analysis
     └── Transaction Analysis
     │
     ▼
Power BI
Executive Banking Risk & Loan Intelligence
     │
     ▼
Row-Level Security
     │
     ▼
Business Users
```

## Development Lifecycle

```text
Development
     │
     ▼
Test
     │
     ▼
Production
```

The environments are managed using the Microsoft Fabric Deployment Pipeline:

**Banking Analytics Deployment Pipeline**

## Data Layer

The project uses banking datasets covering areas such as:

* Customer information
* Personal loans
* Credit bureau information
* Retail transactions

Python/Pandas was used for data cleaning, preparation, and analysis before the data was incorporated into the analytical solution.

Large source and processed datasets are intentionally excluded from the GitHub repository because of their size.

## Analytical Layer

The Fabric Lakehouse provides the central analytical storage environment.

The SQL Analytics Endpoint provides SQL-based access for analytical querying.

The semantic model organizes the data into reusable dimensions and facts for Power BI reporting.

## Reporting Layer

The Power BI report provides an executive view of:

* Loan applications
* Approval and rejection
* Customer risk
* Defaults
* Repayments
* Missed payments
* Transactions
* State-level analysis

## Security Layer

Row-Level Security is implemented using:

`State_Manager_RLS`

The role demonstrates state-based access restrictions using the `state` field.

## Deployment Layer

Microsoft Fabric Deployment Pipelines are used to promote the solution between:

**Development → Test → Production**

This demonstrates a controlled

