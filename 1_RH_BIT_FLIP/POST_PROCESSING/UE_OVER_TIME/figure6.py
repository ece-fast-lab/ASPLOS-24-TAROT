import sys
import matplotlib.pyplot as plt

def time_to_hours(time_str):
    """Converts a time string HH:MM:SS to hours."""
    h, m, s = map(int, time_str.split(':'))
    return h + m / 60 + s / 3600

def seconds_to_hours(seconds):
    """Converts seconds to hours."""
    return seconds / 3600

def plot_errors(file_name, end_time_hours, output_file):
    times = []
    with open(file_name, 'r') as file:
        next(file)  # Skip the first line
        for line in file:
            time_str = line.split(',')[0].strip().split(' ')[1]
            times.append(time_to_hours(time_str))

    times.sort()
    new_times = []
    counts = []

    for i, time in enumerate(times):
        new_times.append(time)
        counts.append(i + 1)
        # Insert an intermediate time one second before the next time, if there is a next time
        if i + 1 < len(times):
            # Calculate the intermediate time as one second less than the next time in hours
            next_time = times[i + 1]
            intermediate_time = next_time - seconds_to_hours(1)  # Subtract one second (converted to hours)
            new_times.append(intermediate_time)
            counts.append(i + 1)

    # Add the end of time with the same count as the last event
    new_times.append(end_time_hours)
    counts.append(counts[-1])

    # Plot the cumulative counts with only a line
    plt.plot(new_times, counts, linestyle='-', color='blue')

    plt.xlabel('Time (hours)')
    plt.ylabel('# of Unique RH-UE-vulnerable Addresses')
    plt.title('# of Unique RH-UE-vulnerable Addresses Over Time')
    plt.xlim(0, max(new_times) + 1)  # Adjust x-axis to include all times
    plt.ylim(0, max(counts) + 1)  # Adjust y-axis to include all counts

    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script_name.py <file_name> <end_of_time_in_hours> <output_file>")
    else:
        file_name = sys.argv[1]
        end_time_hours = float(sys.argv[2])
        output_file = sys.argv[3]
        plot_errors(file_name, end_time_hours, output_file)
