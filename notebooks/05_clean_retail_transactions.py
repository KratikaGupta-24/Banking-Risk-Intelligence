import pandas as pd

file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\raw\nigerian_retail_transactions_full.parquet"
df = pd.read_parquet(file_path)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("Duplicate transaction IDs:",
      df["transaction_id"].duplicated().sum())

print("Unique transaction IDs:",
      df["transaction_id"].nunique())

print("Rows:", len(df))

print("Amount <= 0:",
      (df["amount_ngn"] <= 0).sum())

print("\nAmount summary:")
print(df["amount_ngn"].describe())

debit_check = (
    (df["transaction_type"].str.lower() == "debit") &
    (abs(
        df["balance_after_ngn"] -
        (df["balance_before_ngn"] - df["amount_ngn"])
    ) > 0.01)
)

credit_check = (
    (df["transaction_type"].str.lower() == "credit") &
    (abs(
        df["balance_after_ngn"] -
        (df["balance_before_ngn"] + df["amount_ngn"])
    ) > 0.01)
)

print("Debit balance inconsistencies:", debit_check.sum())
print("Credit balance inconsistencies:", credit_check.sum())

print("Debit balance inconsistencies:", debit_check.sum())

df["balance_logic_issue"] = debit_check | credit_check
print(df["balance_logic_issue"].value_counts())

print(df["transaction_type"].value_counts())

print(df["channel"].value_counts())

print(df["status"].value_counts())

print(df["fraud_flag"].value_counts())

print("Min timestamp:", df["timestamp"].min())
print("Max timestamp:", df["timestamp"].max())

print("Unique states:", df["location_state"].nunique())
print("\nTop states:")
print(df["location_state"].value_counts().head(15))

print("Unique merchant categories:", df["merchant_category_code"].nunique())
print("\nTop merchant categories:")
print(df["merchant_category_code"].value_counts().head(15))

print(
    df.loc[
        df["merchant_category_code"].eq(""),
        ["transaction_type", "channel", "status"]
    ].value_counts().head(20)
)

print("Blank merchant names:", (df["merchant_name"] == "").sum())
print("Unique merchant names:", df["merchant_name"].nunique())

print("\nTop merchant names:")
print(df["merchant_name"].value_counts().head(15))

print("Unique devices:", df["device_id"].nunique())
print("Blank device IDs:", (df["device_id"] == "").sum())

print(
    df.loc[
        df["device_id"] == "",
        ["channel", "transaction_type", "status"]
    ].value_counts().head(20)
)

print("Unique customers:", df["customer_id"].nunique())
print("Unique accounts:", df["account_id"].nunique())

print("\nTransactions per customer:")
print(df.groupby("customer_id").size().describe())

print("\nTransactions per account:")
print(df.groupby("account_id").size().describe())

print(
    df.groupby(["customer_id", "account_id"])
      .size()
      .sort_values(ascending=False)
      .head(10)
)

customer_amount = (
    df.groupby("customer_id")["amount_ngn"]
      .sum()
      .sort_values(ascending=False)
)

print(customer_amount.head(10))


df["balance_logic_issue"] = debit_check | credit_check

df["balance_logic_issue"] = debit_check | credit_check

output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\processed\retail_transactions_silver.parquet"

df.to_parquet(output_path, index=False)

print("Retail Transactions Silver saved successfully!")
print("Shape:", df.shape)
print("Saved to:", output_path)