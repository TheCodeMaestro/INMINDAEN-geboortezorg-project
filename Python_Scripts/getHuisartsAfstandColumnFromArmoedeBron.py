import pandas as pd

# Define file paths
input_file = r"C:\Users\gebruiker\Downloads\kwb-2023.xlsx"
output_file = r"C:\Users\gebruiker\Downloads\Afstand_tot_huisartsenpraktijk.xlsx"

# Load the Excel file
df = pd.read_excel(input_file)

# Check if required columns exist
required_columns = ['gwb_code_10', 'g_afs_hp']
if all(col in df.columns for col in required_columns):
    # Extract the columns
    df_selected = df[required_columns]  # ✅ Ensure brackets are closed properly
    
    # Save to a new Excel file
    df_selected.to_excel(output_file, index=False)
    print(f"Columns {required_columns} have been saved to {output_file}")
else:
    print("One or more required columns not found in the provided Excel file.")
