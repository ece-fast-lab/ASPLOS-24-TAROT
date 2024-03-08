import pandas as pd

# Assuming your data is in a CSV file named 'data.csv'
input_file = 'result_mod.csv'
output_file = 'cnt_result_mod.csv'

# Read the data
df = pd.read_csv(input_file)

# Add a new column for row count
# The row count starts from 1 and increments for each row
df['hammering'] = range(1, len(df) + 1)

# Save the modified data to a new file
df.to_csv(output_file, index=False)

print(f"Modified data saved to {output_file}")
