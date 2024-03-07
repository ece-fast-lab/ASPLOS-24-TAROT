import sys

def parse_line(line):
    """Parse a line from the log file into a dictionary."""
    # Initialize an empty dictionary to hold the parsed data
    data = {}
    # Split the line into parts based on ", " as the separator
    parts = line.strip().split(', ')
    for part in parts:
        # Split each part into key and value based on ": "
        key_value = part.split(': ')
        if len(key_value) == 2:  # Check if the part correctly splits into key and value
            key, value = key_value
            # Special handling for "Time" key to keep it as a string
            if key == 'Time':
                data[key] = value
            else:  # Convert other values to int
                try:
                    data[key] = int(value)
                except ValueError:
                    # Handle cases where conversion to int fails
                    print(f"Warning: Unable to convert value '{value}' to int for key '{key}'.")
    return data

def remove_duplicates(input_file_path):
    seen = set()
    unique_lines = []

    with open(input_file_path, 'r') as file:
        for line in file:
            data = parse_line(line)
            # Only proceed if the necessary keys exist in the parsed data
            if 'Bank' in data and 'Row' in data and 'Col' in data:
                key = (data['Bank'], data['Row'], data['Col'])
                if key not in seen:
                    seen.add(key)
                    unique_lines.append(line)

    # Generate the output file name
    output_file_name = input_file_path.replace('.out', '_filtered.out')

    # Save the unique lines to a new file
    with open(output_file_name, 'w') as file:
        file.writelines(unique_lines)
    print(f'Filtered file created: {output_file_name}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file_name")
    else:
        input_file_path = sys.argv[1]
        remove_duplicates(input_file_path)
