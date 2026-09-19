# Power BI Dashboard

## Report Name

**Executive Banking Risk & Loan Intelligence**

## Overview

The Power BI report provides an executive-level view of banking risk, loan performance, customer exposure, repayment behavior, and transaction activity.

The report is connected to the analytical data model created for the Banking Risk Intelligence solution.

## Business Questions

The dashboard is designed to answer questions such as:

* How many loan applications are being processed?
* What is the approval versus rejection trend?
* What factors are associated with loan rejection?
* How much loan exposure exists?
* Which customers represent higher risk?
* How many customers are defaulting?
* How are repayments performing?
* Where are missed or delayed payments occurring?
* How is banking activity distributed across states and customers?
* What patterns can be identified from transaction activity?

## Dashboard Analysis Areas

### Loan Performance

Analysis of loan applications, loan amounts, approval status, rejection status, and overall loan activity.

### Customer Risk

Analysis of customer-level exposure and risk-related characteristics to identify potentially higher-risk customer segments.

### Default Analysis

Analysis of defaulting customers and loan repayment behavior.

### Collections & Repayments

Analysis of payment activity, missed payments, delayed payments, and repayment performance.

### Transaction Analysis

Analysis of retail transaction activity to provide additional customer and banking behavior insights.

### Geographic Analysis

State-level analysis supports comparison of banking activity and risk across geographic regions.

## Data Model

The Power BI solution uses a structured analytical model with dimension and fact tables.

Key tables include:

* `dimcustomer`
* `dimdate`
* `factloans`
* `facttransactions`

The model is designed to support interactive analysis and reusable business measures.

## DAX & Business Logic

DAX is used to create analytical measures and business calculations required for executive reporting.

The model supports calculations related to:

* Loan volumes
* Loan amounts
* Approval and rejection analysis
* Customer exposure
* Default analysis
* Payment performance
* Transaction activity
* Risk analysis

## Row-Level Security

The solution includes a role named:

`State_Manager_RLS`

The role uses the `state` field to de
