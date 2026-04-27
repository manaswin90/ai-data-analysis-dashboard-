import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column):
    sns.histplot(df[column])
    plt.title(f"Distribution of {column}")
    return plt

def correlation_heatmap(df):
    sns.heatmap(df.corr(), annot=True)
    plt.title("Correlation Matrix")
    return plt
