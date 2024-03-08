import sys

def parse_line_to_key(line):
    """Parse a line and return a key based on Bank, Row, and Col."""
    parts = line.strip().split(', ')
    data = {part.split(': ')[0]: int(part.split(': ')[1]) for part in parts if part.split(': ')[0] in ['Bank', 'Row', 'Col']}
    return (data['Bank'], data['Row'], data['Col'])

def filter_lines(file1, file2, output_file):
    # Read the second file and store the keys (Bank, Row, Col) in a set for quick lookup
    keys_in_second_file = set()
    with open(file2, 'r') as f2:
        for line in f2:
            if "Bank" in line:  # Ensure the line contains necessary information
                key = parse_line_to_key(line)
                keys_in_second_file.add(key)
    
    # Now, read the first file and write matched lines to the output file
    with open(file1, 'r') as f1, open(output_file, 'w') as out:
        out.write("List of Unique Uncorrectable Errors (UEs):\n")  # Assuming we want to keep the header
        for line in f1:
            if "Bank" in line:  # Ensure the line contains necessary information
                key = parse_line_to_key(line)
                if key in keys_in_second_file:
                    out.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py first_input_file second_input_file")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        output_file = "output.txt"  # Define your output file name
        filter_lines(file1, file2, output_file)

