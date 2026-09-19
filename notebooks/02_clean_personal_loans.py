import pandas as pd

# Raw Personal Loans file
file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\raw\nigerian_personal_loans_full.parquet"

# Load raw data
df = pd.read_parquet(file_path)

print("Raw Personal Loans data loaded successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Convert date columns to datetime
df["application_date"] = pd.to_datetime(df["application_date"])
df["disbursement_date"] = pd.to_datetime(df["disbursement_date"])

print("\nDate columns converted successfully")

print(df[["application_date", "disbursement_date"]].dtypes)

print("\nUnique Loan Status Values:")
print(df["loan_status"].unique())

print("\nUnique Employment Type Values:")
print(df["employment_type"].unique())

print("\nUnique Loan Purpose Values:")
print(df["loan_purpose"].unique())

# Create disbursement indicator
df["is_disbursed"] = df["disbursement_date"].notna()

print("\nDisbursement Indicator:")
print(df["is_disbursed"].value_counts())

print("\nLoan Status vs Disbursement Indicator:")

print(
    pd.crosstab(
        df["loan_status"],
        df["is_disbursed"]
    )
)
# Create credit score bands
df["credit_score_band"] = pd.cut(
    df["credit_score"],
    bins=[0, 579, 669, 739, 799, 850],
    labels=["Poor", "Fair", "Good", "Very Good", "Excellent"],
    include_lowest=True
)

print("\nCredit Score Band created successfully")
print(df["credit_score_band"].value_counts().sort_index())

# Create DTI risk bands
df["dti_band"] = pd.cut(
    df["debt_to_income_ratio"],
    bins=[0, 0.20, 0.40, 0.60, float("inf")],
    labels=["Low", "Medium", "High", "Very High"],
    include_lowest=True
)

print("\nDTI Band created successfully")
print(df["dti_band"].value_counts().sort_index())

# Calculate total scheduled repayment
df["total_scheduled_payment_ngn"] = (
    df["monthly_payment_ngn"] * df["tenor_months"]
)

print("\nTotal Scheduled Payment calculated successfully")

print(
    df["total_scheduled_payment_ngn"]
      .describe()
)

# Save Silver layer dataset
output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\processed\personal_loans_silver.parquet"

df.to_parquet(output_path, index=False)

print("\nSilver Personal Loans dataset saved successfully")
print("Output:", output_path)
print("Rows:", len(df))
print("Columns:", len(df.columns))