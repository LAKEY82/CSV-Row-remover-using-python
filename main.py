import pandas as pd
import os

# Set the input and output file paths
input_file = input("Enter file path:")

# Read the input CSV file using pandas
df = pd.read_csv(input_file)

# Prompt the user to enter a row number
row_number = int(input("Enter the row number to remove all the rows after that: "))

# Extract all the rows up to the specified row number
df_extracted = df.loc[:row_number-1]

# Prompt the user to enter the output directory
output_dir = input("Enter output directory path: ")

# Check if the output directory exists, create it if it doesn't
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# output file name
q = input("Do you want to rename (Y) or (N):")
if q.lower() == "y":
    pc = input("Enter the product code:")
    date = input("Enter naming convention date:")
    nofil = input("Enter the number of files:")
    curno = input ("Enter the current file number:")
    totrec=input("Enter the total records in the sequence:")
    output_file = os.path.join(output_dir, f"{pc}{date}_{nofil}_{curno}_{totrec}_{row_number}.csv")
elif q.lower()=="n":
    output_file = os.path.join(output_dir, f"Myfile_{row_number}.csv")
else:
    print("Sorry, we didn't understand your answer.")
# Write the extracted rows to the output CSV file
df_extracted.to_csv(output_file, index=False)

# Print the number of rows extracted
print(f"All rows up to row {row_number} extracted from '{input_file}' and saved to '{output_file}'.")
