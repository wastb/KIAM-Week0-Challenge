from scipy.stats import zscore

def outliers(cleaned_data, threshold=3):
    # Columns to analyze for outliers
    columns_to_analyze = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB']

    # Extract the relevant data
    data_for_zscore = cleaned_data[columns_to_analyze]  

    # Calculate Z-scores
    z_scores = data_for_zscore.apply(zscore)

    # Create a Boolean mask for outliers (any Z-score > threshold)
    outliers = (z_scores.abs() > threshold)

    # Replace outliers with the mean of the respective column
    for col in columns_to_analyze:
        cleaned_data[col] = cleaned_data[col].where(~outliers[col], cleaned_data[col].mean())

    return cleaned_data




