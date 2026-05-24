import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def missing_values(df):
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100

    return pd.DataFrame({
        "missing_count": missing,
        "missing_percent": missing_percent
    }).sort_values(by="missing_percent", ascending=False)

def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], bins=30, kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()


def plot_box(df, column):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()

def plot_bar(df, column):
    plt.figure(figsize=(10, 5))
    df[column].value_counts().head(10).plot(kind="bar")
    plt.title(f"Top Categories in {column}")
    plt.xticks(rotation=45)
    plt.show()