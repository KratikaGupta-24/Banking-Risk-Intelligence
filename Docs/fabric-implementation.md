# Microsoft Fabric Implementation

## Overview

The Banking Risk Intelligence solution was implemented using Microsoft Fabric to provide a scalable analytics environment for banking risk, loan, customer, and transaction analysis.

The solution follows a Development → Test → Production workflow using Microsoft Fabric Deployment Pipelines.

## Architecture

The overall solution flow is:

Downloaded Banking Data
→ Python/Pandas Data Cleaning & Analysis
→ Microsoft Fabric / OneLake
→ Fabric Lakehouse
→ SQL Analytics Endpoint
→ Semantic Model
→ Power BI Report
→ Row-Level Security (RLS)
→ Deployment Pipeline

## Microsoft Fabric Components

### OneLake

Microsoft Fabric OneLake provides the centralized storage layer for the banking analytics solution.

### Lakehouse

**Banking_Risk_Lakehouse** is used as the central analytical storage layer for the project.

It supports structured banking data used for customer, loan, credit bureau, and transaction analysis.

### Notebook

The project includes the Fabric notebook:

`01_Banking_Raw_Data_Inspection`

The notebook is used for inspecting and validating the banking data within the Fabric environment.

### SQL Analytics Endpoint

The Lakehouse SQL Analytics Endpoint provides a SQL-based querying layer for analytical workloads and reporting.

### Semantic Model

The project uses a semantic modeling layer containing banking dimensions and fact tables.

Key analytical tables include:

* `dimcustomer`
* `dimdate`
* `factloans`
* `facttransactions`

The semantic model supports relationships, business logic, reporting measures, and controlled access.

## Row-Level Security

A role named:

`State_Manager_RLS`

was created to demonstrate row-level security.

The role applies a filter on the `state` column.

Example configuration:

`state = Uttar Pradesh`

The purpose is to demonstrate how users can be restricted to the data relevant to their assigned business region.

## Deployment Pipeline

A Microsoft Fabric Deployment Pipeline was configured with three environments:

1. Development
2. Test
3. Production

Pipeline name:

**Banking Analytics Deployment Pipeline**

The solution was promoted through:

**Development → Test → Production**

This demonstrates an environment-based deployment workflow for Power BI and Fabric artifacts.

## Production Deployment

The solution was successfully deployed from Test to Production.

The deployment included the major Fabric and Power BI artifacts required for the Banking Risk Intelligence solution.

## Business Purpose

The Fabric implementation supports analysis of:

* Loan applications
* Loan approvals and rejections
* Customer risk
* Credit behavior
* Defaults
* Repayments
* Missed or delayed payments
* Transactions
* State-level banking performance

## Key Skills Demonstrated

* Microsoft Fabric
* OneLake
* Fabric Lakehouse
* Fabric Notebooks
* SQL Analytics Endpoint
* Semantic Modeling
* Power BI
* Row-Level Security
* Deployment Pipelines
* Development / Test / Production workflow
* Python/Pandas data preparation
* Banking risk analytics
