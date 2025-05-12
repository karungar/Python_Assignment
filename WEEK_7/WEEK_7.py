# Iris Dataset Analysis with Pandas and Matplotlib

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from pathlib import Path

# Define constants for file paths
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)  # Create output directory if it doesn't exist

LINE_CHART_FILE = OUTPUT_DIR / 'iris_line_chart.png'
BAR_CHART_FILE = OUTPUT_DIR / 'iris_bar_chart.png'
HISTOGRAM_FILE = OUTPUT_DIR / 'iris_histogram.png'
SCATTER_PLOT_FILE = OUTPUT_DIR / 'iris_scatter_plot.png'
MISSING_VALUES_FILE = OUTPUT_DIR / 'iris_missing_values.png'
IMPUTATION_COMPARISON_FILE = OUTPUT_DIR / 'iris_imputation_comparison.png'
CLEANED_DATA_FILE = OUTPUT_DIR / 'iris_cleaned.csv'
MEANS_BY_SPECIES_FILE = OUTPUT_DIR / 'iris_means_by_species.png'

# Question 1: Load and explore the dataset
def load_and_explore_dataset():
    print("Loading the Iris dataset...")
    iris = load_iris()

    # Create a DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    # Display the first few rows of the dataset
    print("\n1. DISPLAYING THE FIRST 5 ROWS OF THE DATASET")
    print("-" * 60)
    print(df.head())

    return df, iris

# Introduce missing values
def introduce_missing_values(df):
    print("\nIntroducing some random missing values for demonstration purposes...")
    df_with_missing = df.copy()
    np.random.seed(42)

    for column in df_with_missing.columns[:-1]:  # Skip the species column
        mask = np.random.random(len(df_with_missing)) < 0.05  # 5% of values
        df_with_missing.loc[mask, column] = np.nan

    return df_with_missing

# Clean the dataset
def clean_dataset(df_with_missing):
    print("\n3. CLEANING THE DATASET")
    print("-" * 60)

    # Method 1: Drop rows with missing values
    df_dropped = df_with_missing.dropna()
    print(f"\nMethod 1: Dropping rows with missing values")
    print(f"Shape before dropping: {df_with_missing.shape}")
    print(f"Shape after dropping: {df_dropped.shape}")
    print(f"Number of rows removed: {df_with_missing.shape[0] - df_dropped.shape[0]}")

    # Method 2: Fill missing values with mean of each column
    df_filled_mean = fill_missing_values(df_with_missing, method='mean')
    print(f"\nMethod 2: Filling missing values with column means")
    print("Checking if any missing values remain:")
    print(df_filled_mean.isnull().sum())

    # Method 3: Fill missing values with median of each column
    df_filled_median = fill_missing_values(df_with_missing, method='median')
    print(f"\nMethod 3: Filling missing values with column medians")
    print("Checking if any missing values remain:")
    print(df_filled_median.isnull().sum())

    return df_dropped, df_filled_mean, df_filled_median

# Helper function to fill missing values
def fill_missing_values(df, method='mean'):
    df_filled = df.copy()
    for column in df_filled.columns[:-1]:  # Skip the species column
        if method == 'mean':
            value = df_filled[column].mean()
        elif method == 'median':
            value = df_filled[column].median()
        else:
            raise ValueError("Invalid method. Use 'mean' or 'median'.")
        df_filled[column].fillna(value, inplace=True)
    return df_filled

# Visualize missing values
def visualize_missing_values(df_with_missing):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_with_missing.isnull(), cmap='viridis', cbar=False, yticklabels=False)
    plt.title('Missing Values in Iris Dataset')
    plt.tight_layout()
    plt.savefig(MISSING_VALUES_FILE)
    plt.close()

# Visualize imputation comparison
def visualize_imputation_comparison(df, df_filled_mean, df_filled_median):
    plt.figure(figsize=(15, 10))

    # Original data without missing values
    plt.subplot(2, 2, 1)
    sns.histplot(df['sepal length (cm)'], kde=True)
    plt.title('Original Data')
    plt.xlabel('Sepal Length (cm)')

    # Mean imputation
    plt.subplot(2, 2, 2)
    sns.histplot(df_filled_mean['sepal length (cm)'], kde=True)
    plt.title('After Mean Imputation')
    plt.xlabel('Sepal Length (cm)')

    # Median imputation
    plt.subplot(2, 2, 3)
    sns.histplot(df_filled_median['sepal length (cm)'], kde=True)
    plt.title('After Median Imputation')
    plt.xlabel('Sepal Length (cm)')

    plt.tight_layout()
    plt.savefig(IMPUTATION_COMPARISON_FILE)
    plt.close()

# Visualize dataset
def visualize_dataset(df, iris):
    # 1. LINE CHART - Growth rates over time
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', periods=50, freq='D')
    growth_data = pd.DataFrame({
        'date': np.tile(dates, 3),
        'species': np.repeat(iris.target_names, 50),
        'growth_rate': np.concatenate([
            np.random.normal(0.2, 0.05, 50),  # Setosa growth rate
            np.random.normal(0.3, 0.07, 50),  # Versicolor growth rate
            np.random.normal(0.4, 0.08, 50)   # Virginica growth rate
        ])
    })

    plt.figure(figsize=(12, 6))
    for species in iris.target_names:
        species_data = growth_data[growth_data['species'] == species]
        plt.plot(species_data['date'], species_data['growth_rate'], 
                 label=species, linewidth=2, marker='o', markersize=4)

    plt.title('Iris Species Growth Rate Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Daily Growth Rate (cm)', fontsize=14)
    plt.legend(title='Species', title_fontsize=13, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(LINE_CHART_FILE)
    plt.close()

    # 2. BAR CHART - Average measurements by species
    feature_means = df.groupby('species').mean().reset_index()
    feature_means_melted = pd.melt(feature_means, id_vars=['species'], 
                                   value_vars=iris.feature_names,
                                   var_name='measurement', value_name='average_value')

    plt.figure(figsize=(14, 8))
    sns.barplot(x='species', y='average_value', hue='measurement', 
                data=feature_means_melted, palette='viridis')

    plt.title('Average Measurements by Iris Species', fontsize=16)
    plt.xlabel('Species', fontsize=14)
    plt.ylabel('Average Measurement (cm)', fontsize=14)
    plt.legend(title='Feature', title_fontsize=13, fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(BAR_CHART_FILE)
    plt.close()

    # 3. HISTOGRAM - Distribution of petal length
    plt.figure(figsize=(12, 6))
    for i, species in enumerate(iris.target_names):
        species_data = df[df['species'] == species]
        plt.hist(species_data['petal length (cm)'], bins=15, alpha=0.7, 
                 label=species, edgecolor='black', linewidth=1.2)

    plt.title('Distribution of Petal Length by Species', fontsize=16)
    plt.xlabel('Petal Length (cm)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend(title='Species', title_fontsize=13, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(HISTOGRAM_FILE)
    plt.close()

    # 4. SCATTER PLOT - Relationship between sepal length and petal length
    plt.figure(figsize=(12, 8))
    scatter = sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', 
                               hue='species', data=df, palette='viridis',
                               s=100, alpha=0.8, edgecolor='black', linewidth=1)

    plt.title('Relationship Between Sepal Length and Petal Length', fontsize=16)
    plt.xlabel('Sepal Length (cm)', fontsize=14)
    plt.ylabel('Petal Length (cm)', fontsize=14)
    plt.legend(title='Species', title_fontsize=13, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    for species in iris.target_names:
        species_data = df[df['species'] == species]
        x = species_data['sepal length (cm)']
        y = species_data['petal length (cm)']
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        plt.plot(x, p(x), linestyle='--', linewidth=2)

    plt.tight_layout()
    plt.savefig(SCATTER_PLOT_FILE)
    plt.close()

# Main function
def main():
    df, iris = load_and_explore_dataset()
    df_with_missing = introduce_missing_values(df)
    visualize_missing_values(df_with_missing)
    df_dropped, df_filled_mean, df_filled_median = clean_dataset(df_with_missing)
    visualize_imputation_comparison(df, df_filled_mean, df_filled_median)
    df_filled_median.to_csv(CLEANED_DATA_FILE, index=False)
    visualize_dataset(df, iris)

if __name__ == "__main__":
    main()