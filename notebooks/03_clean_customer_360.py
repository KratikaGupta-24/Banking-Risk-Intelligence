import pandas as pd

# Raw Customer 360 file
file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\raw\nigerian_customer_360_full.parquet"
# Load raw data
df = pd.read_parquet(file_path)

print("Raw Customer 360 data loaded successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())
print("\nCustomer 360 Dataset Overview:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Customer IDs:")
print(df["customer_id"].duplicated().sum())
print("\nSnapshot Date:")
print(df["snapshot_date"].value_counts())
print("\nGender Values:")
print(df["gender"].value_counts())

print("\nKYC Tier Values:")
print(df["kyc_tier"].value_counts())

print("\nNumber of States:")
print(df["state"].nunique())

print("\nNumeric Column Summary:")
print(
    df[
        [
            "age",
            "monthly_income_ngn",
            "account_age_days",
            "products_count",
            "total_balance_ngn",
            "transaction_count_30d",
            "transaction_volume_ngn_30d",
            "days_since_last_transaction",
            "digital_engagement_score"
        ]
    ].describe()
)

product_columns = [
    "has_savings_account",
    "has_current_account",
    "has_loan",
    "has_debit_card",
    "has_credit_card",
    "has_wallet",
    "has_investment"
]

df["calculated_products_count"] = df[product_columns].sum(axis=1)

print("\nProducts Count Validation:")
print(
    (df["products_count"] == df["calculated_products_count"])
    .value_counts()
)

df["product_count_difference"] = (
    df["products_count"] - df["calculated_products_count"]
)

print("\nProduct Count Difference:")
print(df["product_count_difference"].value_counts().sort_index())

print("\nProduct Flag Values:")

for column in product_columns:
    print(column, df[column].unique())

    print("\nDormant Flag vs Days Since Last Transaction:")

print(
    df.groupby("dormant_flag")["days_since_last_transaction"]
      .describe()
)
print("\nChurn Flag Distribution:")

print("Churn 30D:")
print(df["churn_30d"].value_counts())

print("\nChurn 90D:")
print(df["churn_90d"].value_counts())

print("\nChurn 30D vs Churn 90D:")
print(pd.crosstab(df["churn_30d"], df["churn_90d"]))
print("\nTransaction Activity Validation:")

zero_transactions = df["transaction_count_30d"] == 0

print("Customers with zero transactions:")
print(zero_transactions.sum())

print("\nTransaction volume for zero-transaction customers:")
print(
    df.loc[zero_transactions, "transaction_volume_ngn_30d"]
      .value_counts()
      .head(10)
)
print("\nTransaction Activity Validation:")

zero_transactions = df["transaction_count_30d"] == 0

print("Customers with zero transactions:")
print(zero_transactions.sum())

print("\nTransaction volume for zero-transaction customers:")
print(
    df.loc[zero_transactions, "transaction_volume_ngn_30d"]
      .value_counts()
      .head(10)
)
# Remove temporary validation columns
df = df.drop(
    columns=[
        "calculated_products_count",
        "product_count_difference"
    ]
)

print("\nTemporary validation columns removed")
print("Rows:", len(df))
print("Columns:", len(df.columns))
# Create customer activity status
df["customer_activity_status"] = df["dormant_flag"].map({
    False: "Active",
    True: "Dormant"
})

print("\nCustomer Activity Status:")
print(df["customer_activity_status"].value_counts())

# Create digital engagement segment
df["digital_engagement_segment"] = pd.cut(
    df["digital_engagement_score"],
    bins=[-1, 30, 60, 100],
    labels=["Low", "Medium", "High"]
)

print("\nDigital Engagement Segment:")
print(df["digital_engagement_segment"].value_counts().sort_index())

print("Monthly Income <= 0:", (df["monthly_income_ngn"] <= 0).sum())
print("Total Balance < 0:", (df["total_balance_ngn"] < 0).sum())
print("Age < 18:", (df["age"] < 18).sum())
print("Age > 100:", (df["age"] > 100).sum())
print("KYC Tier values:")
print(df["kyc_tier"].value_counts())
product_columns = [
    "has_savings_account",
    "has_current_account",
    "has_loan",
    "has_debit_card",
    "has_credit_card",
    "has_wallet",
    "has_investment"
]

for col in product_columns:
    print(f"\n{col}:")
    print(df[col].value_counts())
    output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\processed\customer_360_silver.parquet"

df.to_parquet(output_path, index=False)

print("\nCustomer 360 Silver saved successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Output:", output_path)