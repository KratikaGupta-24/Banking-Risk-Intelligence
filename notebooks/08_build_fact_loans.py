import pandas as pd

dim_date_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\dim_date.parquet"

dim_date = pd.read_parquet(dim_date_path)

print("DimDate loaded:", dim_date.shape)

file_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\processed\personal_loans_silver.parquet"

df = pd.read_parquet(file_path)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("Duplicate loan IDs:", df["loan_id"].duplicated().sum())
print("Unique loan IDs:", df["loan_id"].nunique())
print("Unique customers:", df["customer_id"].nunique())

print("\nLoan status:")
print(df["loan_status"].value_counts())

df["application_date_key"] = (
    df["application_date"].dt.year * 10000
    + df["application_date"].dt.month * 100
    + df["application_date"].dt.day
)

df["disbursement_date_key"] = (
    df["disbursement_date"].dt.year * 10000
    + df["disbursement_date"].dt.month * 100
    + df["disbursement_date"].dt.day
)

print(
    df[
        [
            "application_date",
            "application_date_key",
            "disbursement_date",
            "disbursement_date_key"
        ]
    ].head(10)
)

date_disbursed_check = df["disbursement_date"].notna()

print(
    "is_disbursed mismatches:",
    (df["is_disbursed"] != date_disbursed_check).sum()
)

print("\nDisbursed flag:")
print(df["is_disbursed"].value_counts())

print(
    "is_disbursed mismatches:",
    (df["is_disbursed"] != df["disbursement_date"].notna()).sum()
)

fact_loans = df[
    [
        "loan_id",
        "customer_id",
        "application_date_key",
        "disbursement_date_key",
        "loan_status",
        "principal_ngn",
        "interest_rate_annual",
        "tenor_months",
        "monthly_payment_ngn",
        "salary_ngn",
        "debt_to_income_ratio",
        "credit_score",
        "employment_type",
        "loan_purpose",
        "state",
        "salary_detected",
        "dpd_current",
        "dpd_max_90d",
        "default_90d",
        "default_180d",
        "is_disbursed",
        "credit_score_band",
        "dti_band",
        "total_scheduled_payment_ngn"
    ]
].copy()

print("FactLoans shape:", fact_loans.shape)
print("\nColumns:")
print(fact_loans.columns.tolist())

print("Duplicate loan IDs:", fact_loans["loan_id"].duplicated().sum())

print("Missing loan IDs:", fact_loans["loan_id"].isna().sum())

print("Missing customer IDs:", fact_loans["customer_id"].isna().sum())

print("\nMissing values:")
print(fact_loans.isna().sum())

print("\nNegative principal:", (fact_loans["principal_ngn"] < 0).sum())

print("Negative monthly payment:", (fact_loans["monthly_payment_ngn"] < 0).sum())

print("Credit score outside 300-850:",
      ((fact_loans["credit_score"] < 300) |
       (fact_loans["credit_score"] > 850)).sum())

print("DTI outside 0-2:",
      ((fact_loans["debt_to_income_ratio"] < 0) |
       (fact_loans["debt_to_income_ratio"] > 2)).sum())

dim_date_keys = set(dim_date["date_key"])

application_invalid = (
    ~fact_loans["application_date_key"].isin(dim_date_keys)
).sum()

disbursement_invalid = (
    fact_loans["disbursement_date_key"].notna()
    & ~fact_loans["disbursement_date_key"].isin(dim_date_keys)
).sum()

print("Invalid application date keys:", application_invalid)
print("Invalid disbursement date keys:", disbursement_invalid)

output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\fact_loans.parquet"

fact_loans.to_parquet(
    output_path,
    index=False
)

print("FactLoans Gold table saved successfully!")
print("Path:", output_path)
print("Rows:", len(fact_loans))
print("Columns:", len(fact_loans.columns))
