import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from windrose import WindroseAxes
import seaborn as sns
from scipy import stats
from scipy.stats import zscore

def merge_country_datasets():
    #importing the cleaned country datasets
    df_benin = pd.read_csv('data/cleaned/benin_cleaned.csv')
    df_sierraleone = pd.read_csv('data/cleaned/sierraleone_cleaned.csv')
    df_togo = pd.read_csv('data/cleaned/Togo_cleaned.csv')
    
    # Adding a country column
    df_benin['country'] = 'benin'
    df_sierraleone['country'] = 'sierraleone'
    df_togo['country'] = 'togo'

    # merging all the country datasets
    df = pd.concat([df_benin, df_sierraleone, df_togo], ignore_index=True)
    return df

def plot_solar_data_resampled(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)

    # Resample daily
    daily_df = df[['GHI', 'DNI', 'DHI', 'Tamb']].resample('D').mean().dropna()

    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.plot(daily_df.index, daily_df['GHI'], label='GHI', color='tab:blue')
    ax1.plot(daily_df.index, daily_df['DNI'], label='DNI', color='tab:orange')
    ax1.plot(daily_df.index, daily_df['DHI'], label='DHI', color='tab:green')
    ax1.set_ylabel('Irradiance (W/m²)')
    ax1.set_xlabel('Date')
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(daily_df.index, daily_df['Tamb'], label='Tamb', color='tab:red')
    ax2.set_ylabel('Temperature (°C)', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2,labels1 + labels2, loc='upper right')

    plt.title('Daily Avg GHI, DNI, DHI and Tamb')
    plt.tight_layout()
    return fig

def plot_monthly_solar_data(df):
    # Resample to monthly averages
    monthly_df = df[['GHI', 'DNI', 'DHI', 'Tamb']].resample('ME').mean().dropna()

    # Plot
    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.plot(monthly_df.index, monthly_df['GHI'], label='GHI', color='tab:blue', marker='o')
    ax1.plot(monthly_df.index, monthly_df['DNI'], label='DNI', color='tab:orange', marker='o')
    ax1.plot(monthly_df.index, monthly_df['DHI'], label='DHI', color='tab:green', marker='o')
    ax1.set_ylabel('Irradiance (W/m²)')
    ax1.set_xlabel('Month')
    ax1.grid(True)

    # Secondary Y-axis for Tamb
    ax2 = ax1.twinx()
    ax2.plot(monthly_df.index, monthly_df['Tamb'], label='Tamb', color='tab:red', marker='o')
    ax2.set_ylabel('Temperature (°C)', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    # Formatting
    plt.title('Monthly Average of GHI, DNI, DHI, and Ambient Temperature (Tamb)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def Heatmap(df):
    # Select relevant columns
    cols = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
    corr_matrix = df[cols].corr()
    
    # Plot heatmap
    fig = plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    return fig

def Scatter_Plots(df):
    # Sample the dataset for clarity
    sample_df = df[['WS', 'WSgust', 'WD', 'GHI', 'RH', 'Tamb']].dropna().sample(1000, random_state=42)
    figs = []
    # WS vs GHI
    fig1 = plt.figure(figsize=(8, 6))
    sns.scatterplot(data=sample_df, x='WS', y='GHI', alpha=0.4, s=30)
    plt.title('WS vs GHI')
    plt.grid(True)
    figs.append(fig1)
    
    # WSgust vs GHI
    fig2 = plt.figure(figsize=(8, 6))
    sns.scatterplot(data=sample_df, x='WSgust', y='GHI', alpha=0.4, s=30)
    plt.title('WSgust vs GHI')
    plt.grid(True)
    figs.append(fig2)
    
    # WD vs GHI
    fig3 = plt.figure(figsize=(8, 6))
    sns.scatterplot(data=sample_df, x='WD', y='GHI', alpha=0.4, s=30)
    plt.title('WD vs GHI')
    plt.grid(True)
    figs.append(fig3)
    
    # RH vs Tamb
    fig4 = plt.figure(figsize=(8, 6))
    sns.scatterplot(data=sample_df, x='RH', y='Tamb', alpha=0.4, s=30)
    plt.title('RH vs Tamb')
    plt.grid(True)
    figs.append(fig4)
    
    # RH vs GHI
    fig5 = plt.figure(figsize=(8, 6))
    sns.scatterplot(data=sample_df, x='RH', y='GHI', alpha=0.4, s=30)
    plt.title('RH vs GHI')
    plt.grid(True)
    figs.append(fig5)
    return figs

def Wind_rose(df):
    # Load and drop missing values
    wind_data = df[['WS', 'WD']].dropna()
    
    # Create wind rose
    fig = plt.figure(figsize=(8, 8))
    ax = WindroseAxes.from_ax(fig=fig)
    ax.bar(wind_data['WD'], wind_data['WS'], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.title('Wind Rose: Wind Direction and Speed')
    return fig

def Hist_GHI(df):
    # Drop missing values
    hist_data = df[['GHI', 'WS']].dropna()
    figs = []
    # GHI Histogram
    fig1 = plt.figure(figsize=(8, 5))
    sns.histplot(hist_data['GHI'], bins=50, kde=True, color='orange')
    plt.title('Histogram of GHI')
    plt.xlabel('GHI')
    plt.ylabel('Frequency')
    plt.grid(True)
    figs.append(fig1)
    
    # WS Histogram
    fig2 = plt.figure(figsize=(8, 5))
    sns.histplot(hist_data['WS'], bins=50, kde=True, color='skyblue')
    plt.title('Histogram of Wind Speed (WS)')
    plt.xlabel('Wind Speed')
    plt.ylabel('Frequency')
    plt.grid(True)
    figs.append(fig2)
    return figs

def Bubble_chart(df):
    # Load and clean
    bubble_df = df[['GHI', 'Tamb', 'RH']].dropna().sample(2000, random_state=42)  # sample for clarity
    
    # Plot
    fig = plt.figure(figsize=(10, 7))
    scatter = plt.scatter(
        bubble_df['GHI'],
        bubble_df['Tamb'],
        s=bubble_df['RH'],  # Bubble size = RH
        alpha=0.4,
        c=bubble_df['RH'],  # Color mapped to RH too
        cmap='coolwarm',
        edgecolors='w'
    )
    
    plt.colorbar(label='Relative Humidity (%)')
    plt.xlabel("GHI")
    plt.ylabel("Ambient Temperature (Tamb)")
    plt.title("Bubble Chart: GHI vs Tamb (Bubble Size = RH)")
    plt.grid(True)
    plt.tight_layout()
    return fig

def Boxplts_byCountry(df):
    sns.set(style="whitegrid")
    figs = []
    for metric in ['GHI', 'DNI', 'DHI']:
        fig = plt.figure(figsize=(8, 5))
        sns.boxplot(data=df, x='country', y=metric,hue='country', palette='Set2')
        plt.title(f'Boxplot of {metric} by country')
        plt.ylabel(metric)
        plt.xlabel('country')
        plt.grid(True)
        plt.tight_layout()
        figs.append(fig)
    return figs

def flag_outliers_by_zscore(df, columns, threshold=3):
    # Compute Z-scores for the selected columns
    z_scores = df[columns].apply(zscore)
    
    # True if any |z| > threshold across the columns
    outlier = (np.abs(z_scores) > threshold).any(axis=1)
    
    # Add a new column to flag outliers
    df['is_outlier'] = outlier
    
    return df
