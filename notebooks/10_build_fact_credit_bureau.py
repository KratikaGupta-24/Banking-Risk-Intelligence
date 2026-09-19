import pandas as pd

file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\processed\credit_bureau_silver.parquet"

df = pd.read_parquet(file_path)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("Duplicate record IDs:",
      df["record_id"].duplicated().sum())

print("Unique record IDs:",
      df["record_id"].nunique())

print("Unique customers:",
      df["customer_id"].nunique())

print("\nReports per customer:")
print(df.groupby("customer_id").size().describe())

df["report_date_key"] = (
    df["report_date"].dt.year * 10000
    + df["report_date"].dt.month * 100
    + df["report_date"].dt.day
)

print(
    df[
        [
            "report_date",
            "report_date_key"
        ]
    ].head(10)
)

dim_date_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\dim_date.parquet"

dim_date = pd.read_parquet(dim_date_path)

valid_date_keys = set(dim_date["date_key"])

invalid_dates = (~df["report_date_key"].isin(valid_date_keys)).sum()

print("Invalid report date keys:", invalid_dates)

fact_credit_bureau = df[
    [
        "record_id",
        "customer_id",
        "report_date_key",
        "report_date",
        "credit_score",
        "total_debt_ngn",
        "active_accounts",
        "delinquent_accounts",
        "payment_history_months",
        "credit_utilization",
        "high_risk",
        "account_count_anomaly",
        "credit_score_band",
        "avg_debt_per_active_account_ngn",
        "debt_burden_band"
    ]
].copy()

print("FactCreditBureau shape:", fact_credit_bureau.shape)
print("\nColumns:")
print(fact_credit_bureau.columns.tolist())

dim_customer_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\dim_customer.parquet"

dim_customer = pd.read_parquet(dim_customer_path)

valid_customer_ids = set(dim_customer["customer_id"])

invalid_customers = (
    ~fact_credit_bureau["customer_id"].isin(valid_customer_ids)
).sum()

print("Invalid customer IDs:", invalid_customers)


print("FactCreditBureau customer_id type:")
print(fact_credit_bureau["customer_id"].dtype)

print("\nDimCustomer customer_id type:")
print(dim_customer["customer_id"].dtype)

print("\nFactCreditBureau sample:")
print(fact_credit_bureau["customer_id"].head())

print("\nDimCustomer sample:")
print(dim_customer["customer_id"].head())

credit_ids = set(fact_credit_bureau["customer_id"])
customer_ids = set(dim_customer["customer_id"])

overlap = credit_ids.intersection(customer_ids)

print("Credit Bureau unique customers:", len(credit_ids))
print("DimCustomer unique customers:", len(customer_ids))
print("Matching customer IDs:", len(overlap))

loans_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\fact_loans.parquet"

fact_loans = pd.read_parquet(loans_path)

loan_ids = set(fact_loans["customer_id"])

bureau_ids = set(fact_credit_bureau["customer_id"])

print("Loan unique customers:", len(loan_ids))
print("Credit Bureau unique customers:", len(bureau_ids))
print("Matching customer IDs:", len(loan_ids.intersection(bureau_ids)))

print("Duplicate record IDs:",
      fact_credit_bureau["record_id"].duplicated().sum())

print("Missing record IDs:",
      fact_credit_bureau["record_id"].isna().sum())

print("Missing customer IDs:",
      fact_credit_bureau["customer_id"].isna().sum())

print("Invalid credit scores:",
      ((fact_credit_bureau["credit_score"] < 300) |
       (fact_credit_bureau["credit_score"] > 850)).sum())

print("Invalid credit utilization:",
      ((fact_credit_bureau["credit_utilization"] < 0) |
       (fact_credit_bureau["credit_utilization"] > 1)).sum())

output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\fact_credit_bureau.parquet"

fact_credit_bureau.to_parquet(
    output_path,
    index=False
)

print("FactCreditBureau saved successfully!")
print("Final shape:", fact_credit_bureau.shape)
print("Saved to:", output_path)