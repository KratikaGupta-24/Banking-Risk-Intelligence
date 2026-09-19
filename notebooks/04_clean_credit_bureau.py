import pandas as pd

file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\raw\nigerian_credit_bureau_full.parquet"

df = pd.read_parquet(file_path)

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("Duplicate record_id:", df["record_id"].duplicated().sum())

print("Unique customers:", df["customer_id"].nunique())

print("Rows per customer:")
print(df.groupby("customer_id").size().describe())
print("Report date range:")
print("Min:", df["report_date"].min())
print("Max:", df["report_date"].max())

print("\nReport dates:")
print(df["report_date"].value_counts().sort_index())
print("Credit score < 300:", (df["credit_score"] < 300).sum())
print("Credit score > 850:", (df["credit_score"] > 850).sum())

print("\nCredit score summary:")
print(df["credit_score"].describe())

print("Negative total debt:", (df["total_debt_ngn"] < 0).sum())
print("Negative active accounts:", (df["active_accounts"] < 0).sum())
print("Negative delinquent accounts:", (df["delinquent_accounts"] < 0).sum())

print("\nDebt summary:")
print(df["total_debt_ngn"].describe())

print("Negative total debt:", (df["total_debt_ngn"] < 0).sum())
print("Negative active accounts:", (df["active_accounts"] < 0).sum())
print("Negative delinquent accounts:", (df["delinquent_accounts"] < 0).sum())

print("\nActive accounts summary:")
print(df["active_accounts"].describe())

print("\nDelinquent accounts summary:")
print(df["delinquent_accounts"].describe())

print("Negative total debt:", (df["total_debt_ngn"] < 0).sum())
print("Negative active accounts:", (df["active_accounts"] < 0).sum())
print("Negative delinquent accounts:", (df["delinquent_accounts"] < 0).sum())

print("\nActive accounts summary:")
print(df["active_accounts"].describe())
invalid_accounts = (
    df["delinquent_accounts"] > df["active_accounts"]
)

print("Delinquent accounts > active accounts:", invalid_accounts.sum())

invalid = df[df["delinquent_accounts"] > df["active_accounts"]]

print("Invalid records:", len(invalid))

print("\nSample records:")
print(
    invalid[
        [
            "customer_id",
            "report_date",
            "active_accounts",
            "delinquent_accounts",
            "total_debt_ngn",
            "high_risk"
        ]
    ].head(10)
)

print("\nHigh-risk distribution:")
print(invalid["high_risk"].value_counts())

df["account_count_anomaly"] = (
    df["delinquent_accounts"] > df["active_accounts"]
)

print(df["account_count_anomaly"].value_counts())

print("Credit utilization < 0:", (df["credit_utilization"] < 0).sum())
print("Credit utilization > 1:", (df["credit_utilization"] > 1).sum())

print("\nCredit utilization summary:")
print(df["credit_utilization"].describe())

print("High-risk distribution:")
print(df["high_risk"].value_counts())

print("\nAverage credit score by risk:")
print(df.groupby("high_risk")["credit_score"].mean())

print("\nAverage delinquent accounts by risk:")
print(df.groupby("high_risk")["delinquent_accounts"].mean())

print("\nAverage credit utilization by risk:")
print(df.groupby("high_risk")["credit_utilization"].mean())

print("Average credit score by risk:")
print(df.groupby("high_risk")["credit_score"].mean())

print("\nAverage delinquent accounts by risk:")
print(df.groupby("high_risk")["delinquent_accounts"].mean())

print("Payment history < 0:",
      (df["payment_history_months"] < 0).sum())

print("\nPayment history summary:")
print(df["payment_history_months"].describe())

df["credit_score_band"] = pd.cut(
    df["credit_score"],
    bins=[0, 579, 669, 739, 799, 850],
    labels=["Poor", "Fair", "Good", "Very Good", "Excellent"]
)

print(df["credit_score_band"].value_counts().sort_index())

df["avg_debt_per_active_account_ngn"] = (
    df["total_debt_ngn"] /
    df["active_accounts"].replace(0, pd.NA)
)

print("Missing average debt due to zero active accounts:",
      df["avg_debt_per_active_account_ngn"].isna().sum())

print("\nAverage debt per active account:")
print(df["avg_debt_per_active_account_ngn"].describe())

df["avg_debt_per_active_account_ngn"] = pd.to_numeric(
    df["avg_debt_per_active_account_ngn"],
    errors="coerce"
)

print(df["avg_debt_per_active_account_ngn"].describe())
print("\nData type:")
print(df["avg_debt_per_active_account_ngn"].dtype)

df["debt_burden_band"] = pd.cut(
    df["avg_debt_per_active_account_ngn"],
    bins=[-1, 50000, 200000, 500000, float("inf")],
    labels=["Low", "Moderate", "High", "Very High"]
)

print(df["debt_burden_band"].value_counts(dropna=False))

print("Final shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isna().sum())

output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\processed\credit_bureau_silver.parquet"

df.to_parquet(output_path, index=False)

print("Credit Bureau Silver saved successfully!")
print(output_path)