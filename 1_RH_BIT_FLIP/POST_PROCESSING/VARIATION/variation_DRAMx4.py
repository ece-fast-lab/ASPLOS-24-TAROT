import csv
import sys

def get_chip_number(byteoffset, expected_value, flipped_value):
    xor_result = int(expected_value, 16) ^ int(flipped_value, 16)
    error_position = 'first' if xor_result >= 16 else 'second'
    return f'chip{byteoffset}_{error_position}'

def count_errors_by_chip(file_path):
    error_counts = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chip = get_chip_number(row['byteoffset'], row['expected_value'], row['flipped_value'])
            if chip not in error_counts:
                error_counts[chip] = 0
            error_counts[chip] += 1
    return error_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    error_counts = count_errors_by_chip(file_path)

    sorted_error_counts = sorted(error_counts.items(), key=lambda x: x[0])

    for chip, count in sorted_error_counts:
        print(f"{chip}: {count} errors")

if __name__ == "__main__":
    main()

