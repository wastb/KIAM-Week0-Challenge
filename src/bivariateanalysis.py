import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pairplots(data):

    # Select columns for solar radiation and temperature correlation analysis
    solar_temp_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']

    # Compute the correlation matrix
    correlation_matrix = data[solar_temp_columns].corr()

    # Plot the correlation matrix heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix: Solar Radiation and Temperature')
    plt.show()

    # Select columns for wind and solar irradiance analysis
    wind_solar_columns = ['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']

    # Create a pair plot for wind conditions and solar irradiance
    sns.pairplot(data[wind_solar_columns], diag_kind='kde', corner=True)
    plt.suptitle('Scatter Matrix: Wind Conditions and Solar Irradiance', y=1.02)
    plt.show()
