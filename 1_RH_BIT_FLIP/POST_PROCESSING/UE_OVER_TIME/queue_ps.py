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
    """ Extracts the fields 'bank', 'row', 'col', 'byteoffset', 'expected_value', 'flipped_value' from the row. """
    fields = row.split(',')
    return tuple(fields[4:10])  # Extracting the specific fields

def calculate_error_positions(expected_value, flipped_value):
    """ Calculate the positions of changed bits between expected and flipped values. """
    expected_value = int(expected_value, 16)
    flipped_value = int(flipped_value, 16)
    xor_result = expected_value ^ flipped_value
    bit_positions = []

    # Iterate over each bit position
    for i in range(8):
        # If the bit at position i is set in xor_result, it means this bit has changed
        if xor_result & (1 << i):
            bit_positions.append(i)

    return bit_positions


def process_data_with_logging(input_file_path, time_window):
    output_file_path = input_file_path + "_" + str(time_window) + "h" + ".log"
    
    queue = deque()
    unique_data = Counter()
    error_data = defaultdict(lambda: {'details': set(), 'last_updated': None})
    unique_ue_set = set()  # Set to keep track of unique UEs
    unique_ue_count = 0  # Count of unique UEs
    ue_details_list = []  # List to store details of each UE

    with open(input_file_path, 'r') as file, open(output_file_path, 'w') as output_file:
        next(file)  # Skip the header line
        for line in file:
            current_time = parse_time(line)
            unique_fields = extract_unique_fields(line)
            bank, row, col, byteoffset, expected_value, flipped_value = unique_fields
            error_positions = calculate_error_positions(expected_value, flipped_value)
            for error_pos in error_positions:
                unique_key = (bank, row, col, error_pos)

                unique_data[unique_key] += 1
                queue.append((current_time, unique_key))

                error_key = (bank, row, col)
                error_detail = (byteoffset, error_pos)
                error_data[error_key]['details'].add(error_detail)
                error_data[error_key]['last_updated'] = current_time

                if len(error_data[error_key]['details']) > 1:
                    if error_key not in unique_ue_set:
                        unique_ue_set.add(error_key)
                        unique_ue_count += 1
                        ue_details = f"Time: {format_timedelta(current_time)}, Bank: {bank}, Row: {row}, Col: {col}"
                        ue_details_list.append(ue_details)

            while queue and is_older_than_time_window(current_time, queue[0][0], time_window):
                old_time, old_unique_key = queue.popleft()
                unique_data[old_unique_key] -= 1
                if unique_data[old_unique_key] == 0:
                    del unique_data[old_unique_key]

                old_error_key = old_unique_key[:3]
                if old_error_key in error_data:
                    if error_data[old_error_key]['last_updated'] is not None and is_older_than_time_window(current_time, error_data[old_error_key]['last_updated'], 1):
                        del error_data[old_error_key]

            data_status = "New Data" if unique_data[unique_key] == 1 else "Existing Data"
            output_file.write(f"Time: {format_timedelta(current_time)}, Queue Size: {len(queue)}, Unique Data Count: {len(unique_data)}, Unique UE Count: {unique_ue_count}, Status: {data_status}\n")

    print("List of Unique Uncorrectable Errors (UEs):")
    for ue_detail in ue_details_list:
        print(ue_detail)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py input_file_name time_window_in_hours")
    else:
        input_file_path = sys.argv[1]
        time_window = int(sys.argv[2])
        process_data_with_logging(input_file_path, time_window)


