import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_histogram_all_values(file_name):
    # Read the CSV file
    df = pd.read_csv(file_name)

    # Ensure CNT_UE_GEN is of a numeric type, for further processing
    df['CNT_UE_GEN'] = pd.to_numeric(df['CNT_UE_GEN'], errors='coerce').dropna()

    # Plotting the histogram of all CNT_UE_GEN values
    plt.figure(figsize=(8, 6))
    plt.hist(df["CNT_UE_GEN"], bins=range(int(df["CNT_UE_GEN"].min()), int(df["CNT_UE_GEN"].max()) + 2), alpha=0.75, edgecolor='black')
    plt.title('Histogram of All CNT_UE_GEN Values')
    plt.xlabel('CNT_UE_GEN Values (128MB)')
    plt.ylabel('Frequency')
    plt.xticks(range(int(df["CNT_UE_GEN"].min()), int(df["CNT_UE_GEN"].max()) + 1))
    plt.grid(axis='y', alpha=0.75)
    
    # Save the figure to a PNG file
    output_file_name = "histogram_all_values.png"
    plt.savefig(output_file_name)
    print(f"Figure saved to {output_file_name}")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py file_name")
    else:
        file_name = sys.argv[1]
        plot_histogram_all_values(file_name)

