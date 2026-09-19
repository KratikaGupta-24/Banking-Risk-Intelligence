import pandas as pd

dim_customer_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\dim_customer.parquet"

dim_customer = pd.read_parquet(dim_customer_path)

print("DimCustomer loaded:", dim_customer.shape)

file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\processed\retail_transactions_silver.parquet"

df = pd.read_parquet(file_path)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("Duplicate transaction IDs:", df["transaction_id"].duplicated().sum())
print("Unique transaction IDs:", df["transaction_id"].nunique())

print("Unique customers:", df["customer_id"].nunique())
print("Unique accounts:", df["account_id"].nunique())

print("\nTransaction status:")
print(df["status"].value_counts())

print("\nFraud flag:")
print(df["fraud_flag"].value_counts())

df["transaction_date"] = df["timestamp"].dt.normalize()

df["transaction_date_key"] = (
    df["transaction_date"].dt.year * 10000
    + df["transaction_date"].dt.month * 100
    + df["transaction_date"].dt.day
)

print(
    df[
        [
            "timestamp",
            "transaction_date",
            "transaction_date_key"
        ]
    ].head(10)
)
dim_date_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\dim_date.parquet"

dim_date = pd.read_parquet(dim_date_path)

dim_date_keys = set(dim_date["date_key"])
invalid_transaction_dates = (
    ~df["transaction_date_key"].isin(dim_date_keys)
).sum()

print(
    "Invalid transaction date keys:",
    invalid_transaction_dates
)

print("Non-positive transaction amounts:",
      (df["amount_ngn"] <= 0).sum())

print("Negative balances before transaction:",
      (df["balance_before_ngn"] < 0).sum())

print("Negative balances after transaction:",
      (df["balance_after_ngn"] < 0).sum())

print("\nTransaction type:")
print(df["transaction_type"].value_counts())

print("\nBalance logic issues:")
print(df["balance_logic_issue"].value_counts())

fact_transactions = df[
    [
        "transaction_id",
        "account_id",
        "customer_id",
        "transaction_date_key",
        "timestamp",
        "amount_ngn",
        "balance_before_ngn",
        "balance_after_ngn",
        "transaction_type",
        "channel",
        "merchant_category_code",
        "merchant_name",
        "location_lga",
        "location_state",
        "device_id",
        "status",
        "fraud_flag",
        "balance_logic_issue"
    ]
].copy()

print("FactTransactions shape:", fact_transactions.shape)

print("\nColumns:")
print(fact_transactions.columns.tolist())

print("Duplicate transaction IDs:",
      fact_transactions["transaction_id"].duplicated().sum())

print("Missing transaction IDs:",
      fact_transactions["transaction_id"].isna().sum())

print("Missing customer IDs:",
      fact_transactions["customer_id"].isna().sum())

print("Missing account IDs:",
      fact_transactions["account_id"].isna().sum())

print("\nMissing values:")
print(fact_transactions.isna().sum())

customer_ids = set(dim_customer["customer_id"])

invalid_customers = (
    ~fact_transactions["customer_id"].isin(customer_ids)
).sum()

print("Transactions with customer IDs not in DimCustomer:",
      invalid_customers)

customer_ids = set(dim_customer["customer_id"])

invalid_customers = (
    ~fact_transactions["customer_id"].isin(customer_ids)
).sum()

print(
    "Transactions with customer IDs not in DimCustomer:",
    invalid_customers
)

customer_ids = set(dim_customer["customer_id"])

invalid_customers = (
    ~fact_transactions["customer_id"].isin(customer_ids)
).sum()

print(
    "Transactions with customer IDs not in DimCustomer:",
    invalid_customers
)

output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\fact_transactions.parquet"

fact_transactions.to_parquet(
    output_path,
    index=False
)

print("FactTransactions Gold table saved successfully!")
print("Path:", output_path)
print("Rows:", len(fact_transactions))
print("Columns:", len(fact_transactions.columns))

