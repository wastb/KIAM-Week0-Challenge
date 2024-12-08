import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from windrose import WindroseAxes

def monthly_patterns(data):
    """Plot monthly averages of GHI, DNI, DHI, and Tamb."""
    data.set_index('Timestamp', inplace=True)
    monthly_data = data[['GHI', 'DNI', 'DHI', 'Tamb']].resample('M').mean()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_data, markers=True)
    plt.title('Monthly Average of GHI, DNI, DHI, and Tamb')
    plt.xlabel('Month')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

def hourly_patterns(data):
    """Plot hourly patterns of GHI, DNI, DHI, and Tamb."""
    hourly_data = data.groupby(data.index.hour).mean()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=hourly_data[['GHI', 'DNI', 'DHI', 'Tamb']], markers=True)
    plt.title('Diurnal Patterns of GHI, DNI, DHI, and Tamb')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

def cleaning_effect(data):
    """Compare sensor readings for cleaned and uncleaned panels."""
    cleaned = data[data['Cleaning'] == 1]
    uncleaned = data[data['Cleaning'] == 0]
    cleaned_means = cleaned[['ModA', 'ModB']].mean()
    uncleaned_means = uncleaned[['ModA', 'ModB']].mean()

    print("Cleaned Means:\n", cleaned_means)
    print("Uncleaned Means:\n", uncleaned_means)

    plt.figure(figsize=(8, 6))
    x = range(len(cleaned_means))
    plt.bar(x, cleaned_means, width=0.4, label='Cleaned', align='center')
    plt.bar(x, uncleaned_means, width=0.4, label='Uncleaned', align='edge')
    plt.xticks(x, ['ModA', 'ModB'])
    plt.ylabel('Average Sensor Readings')
    plt.title('Impact of Cleaning on Sensor Readings')
    plt.legend()
    plt.grid(True)
    plt.show()

def wind_rose(data):
    """Create a wind rose plot for wind speed and direction."""
    wind_data = data[['WS', 'WD']].dropna()
    plt.figure(figsize=(8, 8))
    ax = WindroseAxes.from_ax()
    ax.bar(wind_data['WD'], wind_data['WS'], normed=True, opening=0.8, edgecolor='black')
    ax.set_title('Wind Rose: Wind Speed and Direction')
    ax.set_legend(title="Wind Speed (m/s)", loc='lower right', bbox_to_anchor=(1.3, 0))
    plt.show()

def relative_humidity_effect(data):
    """Create scatter plots for relative humidity against temperature and GHI."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data['RH'], y=data['Tamb'], alpha=0.6, color='blue')
    plt.title('Relative Humidity vs Ambient Temperature')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Ambient Temperature (°C)')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data['RH'], y=data['GHI'], alpha=0.6, color='orange')
    plt.title('Relative Humidity vs Global Horizontal Irradiance (GHI)')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('GHI (W/m²)')
    plt.grid(True)
    plt.show()

def bubble_chart(data):
    """Create a bubble chart for GHI vs Tamb, with bubble size as RH and color as WS."""
    bubble_data = data[['GHI', 'Tamb', 'WS', 'RH']].dropna()
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(
        bubble_data['GHI'], bubble_data['Tamb'],
        s=bubble_data['RH'] * 10, c=bubble_data['WS'],
        cmap='viridis', alpha=0.7, edgecolors='w'
    )
    plt.colorbar(scatter, label="Wind Speed (m/s)")
    plt.title('Bubble Chart: GHI vs Tamb with Bubble Size as RH')
    plt.xlabel('Global Horizontal Irradiance (GHI)')
    plt.ylabel('Ambient Temperature (Tamb)')
    plt.grid(True)
    plt.show()

