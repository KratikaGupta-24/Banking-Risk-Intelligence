import pandas as pd

start_date = pd.Timestamp("2021-01-01")
end_date = pd.Timestamp("2025-01-13")

date_range = pd.date_range(
    start=start_date,
    end=end_date,
    freq="D"
)

dim_date = pd.DataFrame({
    "date": date_range
})

print("DimDate shape:", dim_date.shape)
print("\nFirst date:", dim_date["date"].min())
print("Last date:", dim_date["date"].max())

dim_date["date_key"] = (
    dim_date["date"].dt.year * 10000
    + dim_date["date"].dt.month * 100
    + dim_date["date"].dt.day
)

dim_date["year"] = dim_date["date"].dt.year
dim_date["quarter"] = "Q" + dim_date["date"].dt.quarter.astype(str)
dim_date["month_number"] = dim_date["date"].dt.month
dim_date["month_name"] = dim_date["date"].dt.month_name()
dim_date["year_month"] = dim_date["date"].dt.strftime("%Y-%m")
dim_date["day"] = dim_date["date"].dt.day
dim_date["day_name"] = dim_date["date"].dt.day_name()
dim_date["day_of_week"] = dim_date["date"].dt.dayofweek + 1

print(dim_date.head())
print("\nColumns:")
print(dim_date.columns.tolist())

dim_date["is_weekend"] = dim_date["day_of_week"] >= 6

dim_date["month_start_date"] = dim_date["date"].dt.to_period("M").dt.to_timestamp()

print(dim_date.head())
print("\nWeekend count:", dim_date["is_weekend"].sum())
print("\nMonth start examples:")
print(dim_date["month_start_date"].drop_duplicates().head())

print("Duplicate dates:", dim_date["date"].duplicated().sum())
print("Duplicate date keys:", dim_date["date_key"].duplicated().sum())
print("Missing dates:", dim_date["date"].isna().sum())

output_path = r"C:\Users\Krati\OneDrive\Desktop\Banking_Risk_Intelligence\data\output\dim_date.parquet"

dim_date.to_parquet(
    output_path,
    index=False
)

print("DimDate Gold table saved successfully!")
print("Path:", output_path)
print("Rows:", len(dim_date))
print("Columns:", len(dim_date.columns))