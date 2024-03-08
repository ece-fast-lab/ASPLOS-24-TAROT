import csv
import sys

def get_chip_number(byteoffset):
    # Directly using byteoffset as chip number
    return f'chip{byteoffset}'

def count_errors_by_bank_and_chip(file_path):
    error_counts = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bank = row['bank']
            chip = get_chip_number(row['byteoffset'])  # Using byteoffset for chip number
            key = (bank, chip)

            if key not in error_counts:
                error_counts[key] = 0
            error_counts[key] += 1
    return error_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    error_counts = count_errors_by_bank_and_chip(file_path)

    # Sorting the error counts by chip and then by bank
    sorted_error_counts = sorted(error_counts.items(), key=lambda x: (x[0][1], x[0][0]))

    for (bank, chip), count in sorted_error_counts:
        print(f"Byte {chip}, Bank {bank}: {count} errors")

if __name__ == "__main__":
    main()

