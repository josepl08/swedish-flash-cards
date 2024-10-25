import pandas as pd

def check_duplicates(file_path):
    # Load the file
    data = pd.read_csv(file_path)

    # Check if the first column has duplicate values
    first_column = data.iloc[:, 0]  # Select the first column
    duplicates = first_column[first_column.duplicated()]

    if not duplicates.empty:
        print("Duplicate entries found in the first column:")
        print(duplicates)
    else:
        print("No duplicates found in the first column.")

# Example usage
file_path = 'data/swe-verbs.csv'  # Replace with the path to your file
check_duplicates(file_path)
