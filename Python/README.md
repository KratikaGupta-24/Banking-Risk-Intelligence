# Python Data Preparation

## Overview

Python and Pandas were used to inspect, clean, transform, and analyze the banking datasets before they were incorporated into the analytical solution.

The objective was to improve data quality and prepare structured datasets for banking risk and loan analytics.

## Data Processing Workflow

```text
Raw Banking Data
      ↓
Data Inspection
      ↓
Data Cleaning
      ↓
Data Validation
      ↓
Data Transformation
      ↓
Analytical Tables
      ↓
Microsoft Fabric / Power BI
```

## Processing Areas

The Python workflow covers datasets related to:

* Customer information
* Personal loans
* Credit bureau data
* Retail transactions

## Data Preparation Activities

Python/Pandas was used for activities such as:

* Inspecting dataset structure
* Checking data types
* Identifying missing values
* Validating records
* Cleaning inconsistent data
* Preparing analytical columns
* Creating structured datasets
* Performing exploratory analysis
* Supporting downstream BI analysis

## Python Scripts

The project includes the following processing scripts:

| Script                            | Purpose                                |
| --------------------------------- | -------------------------------------- |
| `01_raw_data_inspection.py`       | Initial data inspection and validation |
| `02_clean_personal_loans.py`      | Personal loan data preparation         |
| `03_clean_customer_360.py`        | Customer data preparation              |
| `04_clean_credit_bureau.py`       | Credit bureau data preparation         |
| `05_clean_retail_transactions.py` | Retail transaction data preparation    |
| `06_build_dim_customer.py`        | Customer dimension preparation         |
| `07_build_dim_date.py`            | Date dimension preparation             |
| `08_build_fact_loans.py`          | Loan fact table preparation            |
| `09_build_fact_transactions.py`   | Transaction fact table preparation     |
| `10_build_fact_credit_bureau.py`  | Credit bureau fact table preparation   |

## Analytical Output

The processed data was structured into analytical dimensions and fact tables that support:

* Customer analysis
* Loan analysis
* Credit risk analysis
* Default analysis
* Transaction analysis
* Repayment analysis

## Technology

* Python
* Pandas
* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* Analytical Data Preparation

## Portfolio Note

Large raw and processed datasets are excluded from the GitHub repository because of their size.

The repository contains the Python processing scripts and documentation so the data preparation approach can be reviewed without uploading the underlying banking datasets.

