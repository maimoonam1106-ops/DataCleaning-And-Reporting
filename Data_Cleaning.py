import pandas as pd

# Load dataset
df = pd.read_csv("EmployeeData.csv")

print("Original Data")
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Save cleaned file
df.to_csv("Cleaned_EmployeeData.csv", index=False)

print("Data Cleaning Completed")
print("Cleaned file saved as Cleaned_EmployeeData.csv")
