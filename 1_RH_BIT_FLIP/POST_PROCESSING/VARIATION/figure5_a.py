import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def read_and_process_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    info, errors_str = parts
                    info = info.replace("Byte ", "")  # Removing "Byte " prefix
                    chip, bank = [x.strip() for x in info.split(',')]
                    # Attempting to extract and convert the error count
                    error_count_str = errors_str.strip().split(' ')[0]
                    if error_count_str.isdigit():
                        errors = int(error_count_str)
                        data.append({'Chip': chip, 'Bank': bank, 'Errors': errors})
                    else:
                        print(f"Skipping line due to unexpected format: {line.strip()}")
            except ValueError as e:
                print(f"Error processing line: {line.strip()} | Error: {e}")
                continue  # Skip to the next line if an error occurs

    return pd.DataFrame(data)


def plot_error_distribution(df, output_file):
    # Adjusting labels for the plot
    df['Chip_Bank'] = df.apply(lambda x: f"{x['Chip']}_{x['Bank']}", axis=1)
    plt.figure(figsize=(14, 8))
    plt.scatter(df['Chip_Bank'], df['Errors'], color='red')
    plt.title('Error Distribution by Chip and Bank')
    plt.xlabel('Chip and Bank Combination')
    plt.ylabel('Number of Errors')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('figure_5.png')
    plt.close()


def plot_geometric_mean(df, output_file):
    # Ensure that 'Errors' is numeric
    df['Errors'] = pd.to_numeric(df['Errors'], errors='coerce')

    # Calculating geometric mean of errors per chip
    df['LogErrors'] = np.log(df['Errors'])
    geo_mean = df.groupby('Chip')['LogErrors'].mean().apply(np.exp).reset_index(name='GeoMeanErrors')

    plt.figure(figsize=(10, 6))
    plt.bar(geo_mean['Chip'], geo_mean['GeoMeanErrors'], color='skyblue')  # Use 'GeoMeanErrors' here
    plt.title('Geometric Mean of Errors Per Chip')
    plt.xlabel('Chip')
    plt.ylabel('Geometric Mean of Errors')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py file_path")
        sys.exit(1)

    file_path = sys.argv[1]
    df = read_and_process_data(file_path)
    
    if df.empty:
        print("No data to process. Please check your input file.")
        sys.exit(1)

    base_file_name = file_path.rsplit('.', 1)[0]
    plot_error_distribution(df, base_file_name)
    plot_geometric_mean(df, base_file_name)

