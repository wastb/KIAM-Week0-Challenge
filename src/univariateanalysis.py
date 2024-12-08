import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_data(cleaned_data):
    # List of columns to plot boxplots
    outlier_columns = ['ModA', 'ModB', 'WS', 'WSgust', 'WD', 'WSstdev', 'WDstdev']

    # Set the style of seaborn plots
    sns.set(style="whitegrid")

    # Create a figure with subplots for the boxplots
    plt.figure(figsize=(12, 8))

    # Loop through each column to create boxplots
    for i, col in enumerate(outlier_columns, 1):
        plt.subplot(2, 4, i)  # 2 rows and 4 columns for the subplots
        sns.boxplot(data=cleaned_data, x=col, color='skyblue')  # Use seaborn's boxplot function
        plt.title(f'Boxplot for {col}')
        plt.xlabel(col)  # Label the x-axis

    # Adjust layout to prevent overlap of titles and labels
    plt.tight_layout()

    # Show the boxplots together
    plt.show()

    # Select the columns for histograms
    columns_for_hist = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb', 'TModA', 'TModB']
    data_for_hist = cleaned_data[columns_for_hist]

    # Create histograms for each variable
    plt.figure(figsize=(12, 10))
    for i, var in enumerate(columns_for_hist, 1):
        plt.subplot(3, 3, i)  # Create a grid of 3x3 subplots
        plt.hist(data_for_hist[var], bins=30, alpha=0.7, color='blue', edgecolor='black')
        plt.title(f'Histogram of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.grid(axis='y')

    # Adjust layout to prevent overlap of titles and labels
    plt.tight_layout()

    # Show the histograms together
    plt.show()
