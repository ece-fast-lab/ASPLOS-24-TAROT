import pandas as pd
import random
import os

# Read the CSV files
folder = "output"
file_names = ["EXAM0.csv", "EXAM1.csv", "EXAM2.csv", "EXAM3.csv", "EXAM4.csv", "EXAM5.csv"]
#file_names = ["A7.csv", "A8.csv"]
# Dictionary to store the DataFrames
df_dict = {}

# Load all the DataFrames
for file in file_names:
    df_dict[file] = pd.read_csv(file)

# Number of times to perform the tasks
num_runs = 32

# Run the task multiple times
for run in range(num_runs):

    # Create a new DataFrame to store the modified rows
    new_df = pd.DataFrame()

    # Set to store selected (file, byteoffset) combinations
    selected_combinations = set()

    # Perform the tasks 8 times
    for i in range(8):
        while True:
            # Randomly pick a file
            selected_file = random.choice(file_names)
            selected_df = df_dict[selected_file]

            # Randomly generate an integer ‘temp_offset’ in [0, 7]
            temp_offset = random.randint(0, 7)

            # Check if the combination (selected_file, temp_offset) is not already selected
            if (selected_file, temp_offset) not in selected_combinations:
                # If the combination is not in the set, break the loop
                break

        # Add the (selected_file, temp_offset) combination to the set
        selected_combinations.add((selected_file, temp_offset))

        print(
            f"Run {run + 1}, Iteration {i + 1}: selected file - {selected_file}, temp offset - {temp_offset}")

        # Modify the value in the "byteoffset" column
        modified_row = selected_df[selected_df["byteoffset"]
                                   == temp_offset].copy()
        modified_row["byteoffset"] = i

        # Append the modified row to the new file
        new_df = new_df.append(modified_row)

   # Generate the file name using the first two characters of the file name and the byteoffset value
    file_name_parts = [f"{file[:2]}_{offset}" for file,
                       offset in selected_combinations]
    output_file_name = "_".join(file_name_parts) + f".csv"

    # Save the new DataFrame to a CSV file with the custom file name
    new_df.to_csv(os.path.join(folder, output_file_name), index=False)
