import pandas as pd
from datetime import timedelta
import os
import sys

def parse_time(hour, min, sec):
    """Parse time directly from given hour, min, sec integers into a timedelta object."""
    return timedelta(hours=hour, minutes=min, seconds=sec)

def is_older_than_time_window(current_time, old_time, hours):
    """Check if old_time is more than 'hours' hours older than current_time."""
    return current_time - old_time > timedelta(hours=hours)

def process_data_with_logging(input_file_path, slice_time=24):
    """Slices the data from the input CSV file every 24 hours and saves to separate files without changing the format and contents."""
    df = pd.read_csv(input_file_path)
    df['time'] = df.apply(lambda row: parse_time(row['hour'], row['min'], row['sec']), axis=1)
    
    start_time = df['time'].min()
    end_time = df['time'].max()
    current_start = start_time
    
    slice_index = 0
    while current_start <= end_time:
        next_start = current_start + timedelta(hours=slice_time)
        slice_df = df[(df['time'] >= current_start) & (df['time'] < next_start)]
        
        # Exclude the 'time' column added for slicing before saving
        slice_df = slice_df.drop(columns=['time'])
        
        output_file_name = f"{os.path.splitext(input_file_path)[0]}_slice_{slice_index}.csv"
        slice_df.to_csv(output_file_name, index=False, header=True)
        print(f"Data sliced and saved to {output_file_name}")
        
        current_start = next_start
        slice_index += 1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python slice_data.py input_file_name.csv time_window_in_hours")
    else:
        input_file_path = sys.argv[1]
        time_window = int(sys.argv[2])
        process_data_with_logging(input_file_path, time_window)

