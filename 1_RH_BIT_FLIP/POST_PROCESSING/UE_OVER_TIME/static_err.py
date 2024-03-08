import sys
from collections import deque, Counter, defaultdict
from datetime import timedelta

def parse_time(row):
    """ Parse time from the row into a timedelta object. """
    hour, min, sec = map(int, row.split(',')[10:13])
    return timedelta(hours=hour, minutes=min, seconds=sec)

def format_timedelta(td):
    """ Format a timedelta object to a string with hours, minutes, and seconds. """
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def is_older_than_time_window(current_time, old_time, hours):
    """ Check if old_time is more than 'hours' hours older than current_time. """
    return current_time - old_time > timedelta(hours=hours)

def extract_unique_fields(row):
    """ Extracts 'bank', 'row', 'col', 'byteoffset' and the XOR of 'expected_value' and 'flipped_value' from the row. """
    fields = row.split(',')
    bank, row, col, byteoffset = fields[4:8]
    expected_value = int(fields[8], 16)
    flipped_value = int(fields[9], 16)
    xor_result = expected_value ^ flipped_value
    return (bank, row, col, byteoffset, xor_result)

def process_data_with_logging(input_file_path, time_window_hours):
    output_file_path = input_file_path + "_RepeatedErrors_" + str(time_window_hours) + "h" + ".log"
    
    error_occurrences = defaultdict(deque)  # Stores timestamps of each error occurrence

    with open(input_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
        next(file)  # Skip the header line
        for line in file:
            current_time = parse_time(line)
            error_key = extract_unique_fields(line)  # (bank, row, col, byteoffset, xor_result)

            # Add the current time to the deque for this error
            error_occurrences[error_key].append(current_time)

            # Remove occurrences outside the time window
            while error_occurrences[error_key] and is_older_than_time_window(current_time, error_occurrences[error_key][0], time_window_hours):
                error_occurrences[error_key].popleft()

            # Check for repeated errors within the time window
            if len(error_occurrences[error_key]) > 1:
                repeated_error_info = f" - Repeated Errors Count: {len(error_occurrences[error_key])}"
            else:
                repeated_error_info = f" - Repeated Errors Count: {0}"

            # Print the same line with added information about repeated errors
            output_file.write(line.strip() + repeated_error_info + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py input_file_name time_window_in_hours")
    else:
        input_file_path = sys.argv[1]
        time_window_hours = int(sys.argv[2])
        process_data_with_logging(input_file_path, time_window_hours)
