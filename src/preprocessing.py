def view_data(data):
    """
    View basic information about the dataset without transforming it.
    - Display the first few rows of the data.
    - Show info about the data (columns, types, and non-null counts).
    - Show summary statistics.
    """
    print("Data Overview:")
    print(data.head())  # Display first 5 rows
    print("\nData Info:")
    print(data.info())  # Display basic info about the dataset
    print("\nSummary Statistics:")
    print(data.describe())  # Show summary statistics for numeric columns
    print("\nMissing Values Per Column:")
    print(data.isna().sum())  # Check for missing values
    print("\nUnique Values Per Column:")
    print(data.nunique())  # Check for unique values per column
    print("\nColumns in the Dataset:")
    print(data.columns)  # Display the column names
