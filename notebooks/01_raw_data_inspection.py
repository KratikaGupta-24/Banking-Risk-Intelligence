import pandas as pd

file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\raw\nigerian_personal_loans_full.parquet"

df = pd.read_parquet(file_path)

print("Personal Loans dataset loaded successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nLoan Status vs Missing Disbursement Date:")

print(
    df.groupby("loan_status")["disbursement_date"]
      .apply(lambda x: x.isna().sum())
)

print("\nDuplicate Loan IDs:")
print(df["loan_id"].duplicated().sum())

print("\nUnique Customers:")
print(df["customer_id"].nunique())

print("\nLoans per Customer:")
print(df.groupby("customer_id")["loan_id"].count().describe())

print("\nLoan Status Distribution:")
print(df["loan_status"].value_counts())

print("\nLoan Status Percentage:")
print(df["loan_status"].value_counts(normalize=True).mul(100).round(2))

print("\nFinancial & Risk Summary:")

print(df[
    [
        "principal_ngn",
        "interest_rate_annual",
        "tenor_months",
        "monthly_payment_ngn",
        "salary_ngn",
        "debt_to_income_ratio",
        "credit_score"
    ]
].describe())

print("\nDate Range:")

print("Application Date:")
print("Min:", df["application_date"].min())
print("Max:", df["application_date"].max())

print("\nDisbursement Date:")
print("Min:", df["disbursement_date"].min())
print("Max:", df["disbursement_date"].max())
print("\nLoan Purpose Distribution:")
print(df["loan_purpose"].value_counts())

print("\nEmployment Type Distribution:")
print(df["employment_type"].value_counts())

print("\nState Distribution:")
print(df["state"].value_counts().head(15))

print("\nRisk Fields Summary:")

print("\nDPD Current:")
print(df["dpd_current"].describe())

print("\nDPD Max 90 Days:")
print(df["dpd_max_90d"].describe())

print("\nDefault 90 Days:")
print(df["default_90d"].value_counts())

print("\nDefault 180 Days:")
print(df["default_180d"].value_counts())

print("\nDefault Rate by DPD Current:")

print(
    df.groupby("default_90d")["dpd_current"]
      .agg(["count", "mean", "median", "max"])
)

print("\nDefault Rate by DPD Max 90 Days:")

print(
    df.groupby("default_90d")["dpd_max_90d"]
      .agg(["count", "mean", "median", "max"])
)

print("\nCredit Score Bands:")

df["credit_score_band"] = pd.cut(
    df["credit_score"],
    bins=[0, 579, 669, 739, 799, 850],
    labels=["Poor", "Fair", "Good", "Very Good", "Excellent"]
)

print(df["credit_score_band"].value_counts().sort_index())

print("\n90-Day Default Rate by Credit Score Band:")

print(
    df.groupby("credit_score_band", observed=False)["default_90d"]
      .mean()
      .mul(100)
      .round(2)
)

print("\nDTI Bands:")

df["dti_band"] = pd.cut(
    df["debt_to_income_ratio"],
    bins=[0, 0.20, 0.40, 0.60, float("inf")],
    labels=["Low", "Medium", "High", "Very High"],
    include_lowest=True
)

print(df["dti_band"].value_counts().sort_index())

print("\n90-Day Default Rate by DTI Band:")

print(
    df.groupby("dti_band", observed=False)["default_90d"]
      .mean()
      .mul(100)
      .round(2)
)

print("\n90-Day Default Rate by Employment Type:")

print(
    df.groupby("employment_type")["default_90d"]
      .mean()
      .mul(100)
      .round(2)
)

print("\n90-Day Default Rate by Loan Purpose:")

print(
    df.groupby("loan_purpose")["default_90d"]
      .mean()
      .mul(100)
      .round(2)
      .sort_values(ascending=False)
)