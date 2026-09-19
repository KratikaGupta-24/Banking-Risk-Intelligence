import pandas as pd

file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\processed\customer_360_silver.parquet"

df = pd.read_parquet(file_path)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


dim_customer = df[
    [
        "customer_id",
        "snapshot_date",
        "age",
        "gender",
        "monthly_income_ngn",
        "state",
        "kyc_tier",
        "account_age_days",
        "products_count",
        "has_savings_account",
        "has_current_account",
        "has_loan",
        "has_debit_card",
        "has_credit_card",
        "has_wallet",
        "has_investment",
        "total_balance_ngn",
        "transaction_count_30d",
        "transaction_volume_ngn_30d",
        "days_since_last_transaction",
        "dormant_flag",
        "digital_engagement_score",
        "churn_30d",
        "churn_90d",
        "customer_activity_status",
        "digital_engagement_segment"
    ]
].copy()

print("DimCustomer shape:", dim_customer.shape)
print("\nDuplicate customer IDs:", dim_customer["customer_id"].duplicated().sum())


dim_customer.insert(
    0,
    "customer_key",
    range(1, len(dim_customer) + 1)
)

print(dim_customer.head())
print("\nCustomer key unique:", dim_customer["customer_key"].is_unique)
print("Customer key nulls:", dim_customer["customer_key"].isna().sum())

output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\dim_customer.parquet"

dim_customer.to_parquet(
    output_path,
    index=False
)

print("DimCustomer Gold table saved successfully!")
print("Path:", output_path)
print("Rows:", len(dim_customer))
print("Columns:", len(dim_customer.columns))