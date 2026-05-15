import pandas as pd
import glob

files = glob.glob("data/*.csv")
print("Files found:", files)

df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

df.columns = df.columns.str.strip().str.lower()
print("Columns found:", df.columns.tolist())

df = df[df["product"].str.lower().str.strip() == "pink morsel"]

df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).astype(float)
df["sales"] = df["price"] * df["quantity"]

output_df = df[["sales", "date", "region"]]
output_df.to_csv("formatted_sales_data.csv", index=False)

print(output_df.head())
print("formatted_sales_data.csv created successfully")
