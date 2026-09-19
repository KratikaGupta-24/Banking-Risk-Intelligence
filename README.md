# 🏦 Banking Risk Intelligence

An end-to-end banking risk and loan analytics solution built using **Python, Microsoft Fabric, SQL Analytics Endpoint, and Power BI**.

The project analyzes loan applications, customer profiles, credit information, repayment behavior, transaction activity, defaults, and risk indicators to support data-driven banking decisions.

---

## 📌 Project Overview

Banks need to monitor lending performance, customer risk, loan approvals and rejections, defaults, and repayment behavior across different customer and geographic segments.

**Banking Risk Intelligence** was developed to transform raw banking data into business-ready insights through data preparation, analytical modeling, Power BI reporting, security, and deployment across multiple environments.

### Key Business Questions

* How many loan applications are being processed?
* What is the approval vs. rejection pattern?
* Which factors are associated with loan rejection and customer risk?
* How many customers are exposed to loans?
* Which customers or segments show higher default risk?
* How is repayment and collection performance?
* Which customers have missed or delayed payments?
* What patterns can be observed in transaction activity?
* How does risk vary by state or customer segment?
* How can access to sensitive banking insights be controlled?

---

## 🏗️ Solution Architecture

```text
Banking CSV Data
       │
       ▼
Python / Pandas
Data Cleaning & Analysis
       │
       ▼
Microsoft Fabric / OneLake
       │
       ▼
Fabric Lakehouse
Banking_Risk_Lakehouse
       │
       ▼
Fabric Notebook
01_Banking_Raw_Data_Inspection
       │
       ▼
SQL Analytics Endpoint
       │
       ▼
Analytical / Semantic Layer
       │
       ├── Banking_Risk_Intelligence_Model
       │
       └── Banking_Risk_Semantic_Model
       │
       ▼
Power BI
Executive Banking Risk & Loan Intelligence
       │
       ▼
Business Users

Deployment:
Development → Test → Production
Microsoft Fabric Deployment Pipeline
```

---

## 🛠️ Technology Stack

### Data Preparation & Analysis

* Python
* Pandas
* Data Cleaning
* Data Validation
* Exploratory Data Analysis

### Microsoft Fabric

* Microsoft Fabric
* OneLake
* Lakehouse
* Fabric Notebooks
* SQL Analytics Endpoint
* Semantic Models
* Workspaces
* Deployment Pipelines

### Power BI

* Power BI
* Power Query
* Data Modeling
* DAX
* Interactive Dashboards
* Row-Level Security (RLS)

### Deployment & Security

* Development / Test / Production environments
* Microsoft Fabric Deployment Pipelines
* Row-Level Security
* Role-based data access

---

## 📂 Data Model

The analytical solution uses multiple banking datasets representing different business domains.

| Entity        | Purpose                                                    |
| ------------- | ---------------------------------------------------------- |
| Customer      | Customer demographic and profile information               |
| Loans         | Loan applications, amounts, status and lending information |
| Credit Bureau | Credit history and risk-related information                |
| Transactions  | Customer transaction activity                              |
| Date          | Time-based analysis and reporting                          |

The model is structured to support analysis across customers, loans, credit information, transactions, geography, and time.

---

## 🔄 Data Processing

The data processing workflow was designed in multiple stages.

### 1. Raw Data

Original banking datasets were used as the source layer.

### 2. Data Cleaning

Python/Pandas was used for data inspection, cleaning, transformation, and analysis.

### 3. Fabric Lakehouse

Processed data was organized within the Microsoft Fabric Lakehouse environment.

### 4. Analytical Layer

The SQL Analytics Endpoint and semantic models provide a structured layer for analytical querying and Power BI reporting.

### 5. Business Intelligence

Power BI transforms the analytical data into interactive business dashboards and risk insights.

---

## 📊 Power BI Dashboard

### Executive Banking Risk & Loan Intelligence

The Power BI report provides an executive-level view of banking and lending performance.

Key analysis areas include:

* Loan application volume
* Approved vs. rejected loans
* Loan exposure and amounts
* Customer analysis
* Default risk
* Credit risk indicators
* Repayment performance
* Missed and delayed payments
* Transaction activity
* Collection performance
* State-level risk analysis
* Rejection and risk patterns

---

## 🔐 Row-Level Security

A Row-Level Security role named:

`State_Manager_RLS`

was implemented in the Power BI semantic model.

The role applies a state-based filter using the:

`state`

column.

Example:

```text
State_Manager_RLS
        │
        ▼
state = Uttar Pradesh
```

This demonstrates how sensitive banking analytics can be restricted according to a user's authorized geographic scope.

---

## 🚀 Deployment Pipeline

The solution was deployed through a Microsoft Fabric Deployment Pipeline with three environments:

```text
Development
     │
     ▼
Test
     │
     ▼
Production
```

### Development

Used for development and implementation of the solution.

### Test

Used to validate the solution before production deployment.

### Production

Used for the final business-ready version.

This demonstrates an environment-based **CI/CD workflow within Microsoft Fabric**.

---

## 📁 Project Structure

```text
Banking_Risk_Intelligence/
│
├── Data/
│   └── Source and processed datasets
│
├── Docs/
│   └── Project documentation
│
├── Fabric/
│   └── Microsoft Fabric project documentation
│
├── notebooks/
│   └── Python/Pandas data preparation scripts
│
├── Power bi/
│   └── Power BI documentation and related files
│
├── Python/
│   └── Python analysis and scripts
│
├── screen shots/
│   └── Dashboard and Microsoft Fabric screenshots
│
├── .gitignore
└── README.md
```

> **Note:** Large source and processed datasets are excluded from the GitHub repository because of file-size considerations. The repository focuses on the analytical code, documentation, architecture, and implementation approach.

---

## 💡 Key Skills Demonstrated

* Python & Pandas
* Data Cleaning & Transformation
* Exploratory Data Analysis
* Microsoft Fabric
* OneLake
* Lakehouse Architecture
* Fabric Notebooks
* SQL Analytics Endpoint
* Power BI
* DAX
* Data Modeling
* Semantic Models
* Row-Level Security
* Deployment Pipelines
* Development / Test / Production workflow
* Banking & Loan Risk Analytics
* KPI Development
* Business Intelligence

---

## 🎯 Business Value

The solution demonstrates how banking data can be transformed into an analytics platform that helps stakeholders understand:

**Lending → Risk → Approval/Rejection → Customer Exposure → Repayment → Default → Collections**

The objective is to provide a structured view of loan and customer risk while enabling secure, interactive, and scalable business reporting.

---

## 📸 Project Screenshots
## 📸 Project Screenshots

### Power BI Executive Dashboard

The executive dashboard provides an interactive view of loan performance, customer risk, defaults, repayments, transactions, and state-level analysis.

![Power BI Executive Dashboard](screen%20shots/01_powerbi_dashboard.png)

### Microsoft Fabric Lakehouse

The Fabric Lakehouse provides the centralized analytical storage layer for the banking solution.

![Microsoft Fabric Lakehouse](screen%20shots/02_fabric_lakehouse.png)

### Fabric Notebook

The Fabric notebook is used for data inspection and validation within the Microsoft Fabric environment.

![Fabric Notebook](screen%20shots/03_fabric_notebook.png)

### Semantic Model

The semantic model provides the structured analytical layer used for Power BI reporting.

![Semantic Model](screen%20shots/04_semantic_model.png)

### Row-Level Security

The `State_Manager_RLS` role demonstrates state-based access control using the `state` field.

![Row-Level Security](screen%20shots/05_rls.png)

### Deployment Pipeline

The solution is promoted across Development, Test, and Production using a Microsoft Fabric Deployment Pipeline.

![Deployment Pipeline](screen%20shots/06_deployment_pipeline.png)

### Additional Dashboard Views

Additional Power BI dashboard views are included in the repository for further exploration.

![Power BI Dashboard View](screen%20shots/02_powerbi_dashboard.png)

![Power BI Dashboard View](screen%20shots/03_powerbi_dashboard.png)

![Power BI Dashboard View](screen%20shots/04_powerbi_dashboard.png)


### Power BI Executive Dashboard

*Add dashboard screenshot here.*

### Microsoft Fabric Lakehouse

*Add Lakehouse screenshot here.*

### Semantic Model

*Add semantic model screenshot here.*

### Row-Level Security

*Add RLS screenshot here.*

### Deployment Pipeline

*Add Development → Test → Production screenshot here.*

---

## 👩‍💻 Author

**Kratika**

**Data Analyst | Power BI Developer | Business Intelligence & Reporting Analyst**

**Skills:** Python • Pandas • Power BI • DAX • Microsoft Fabric • Data Modeling • SQL • Business Intelligence

---

⭐ If you find this project useful, feel free to explore the repository and connect with me.
