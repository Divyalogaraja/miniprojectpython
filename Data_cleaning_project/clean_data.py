import pandas as pd
from colorama import Fore, Style, init

init()
# Load dataset
df = pd.read_csv("data/messy_data.csv")

# Remove spaces
df["Name"] = df["Name"].fillna("Unknown").str.strip().str.title()
df["City"] = df["City"].fillna("Unknown").str.strip().str.title()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean()).round().astype(int)

df["Salary"] = (
    df["Salary"]
    .fillna(df["Salary"].mean())
    .round()
    .astype(int)
)

# Standardize dates
df["Date"] = pd.to_datetime(
    df["Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
).dt.strftime("%Y-%m-%d")

# Remove duplicates AFTER cleaning
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)
print(Fore.GREEN + "✓ Missing values fixed")
print(Fore.RED + "✓ Duplicates removed")
print(Fore.YELLOW + "✓ Dates standardized")
print(Fore.CYAN + "✓ Text standardized")
print(Fore.MAGENTA + "✓ Cleaned file saved successfully")
print(Style.RESET_ALL)
print(df)
print("\nData cleaned successfully!")
report = f"""
=================================
      DATA CLEANING REPORT
=================================

Original Records : 8
Final Records    : {len(df)}

Tasks Completed:
✓ Missing values handled
✓ Duplicate records removed
✓ Date formats standardized
✓ Text standardized
✓ Cleaned dataset generated

Output File:
data/cleaned_data.csv

Status:
Data cleaning completed successfully!

=================================
"""

with open("cleaning_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("📄 Cleaning report generated: cleaning_report.txt")