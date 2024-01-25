#!/usr/bin/python3
import sys
import signal

def signal_handler(signal, frame):
    """signal handler for exiting

    Args:
        signal (signit): should be ^C
        frame (int): scope of exit
    """
    print("\n^C")
    print_statistics()
    sys.exit(0)
    
def print_statistics():
    """
    Print the statistics of the program execution:
    - Number of processed lines
    """
    print("File size:", total_size)
    sorted_status_codes = sorted(status_codes.keys)
    for code in sorted_status_codes:
        print("{}: {}".format(code, status_codes[code]))

def process_line(line):
    """processes each line that was parsed to print

    Args:
        line (str): line to be printed
    """
    parts = line.split()
    if len(parts) == 7:
        ip, date, _, status_code, size = parts[:5]
        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in valid_status_codes:
                global total_size
                total_size += int(size)
                status_codes[status_code] = status_codes.get(
                    status_code, 0) + 1

def main():
    """main function to run the file"""
    signal.signal(signal.SIGINT, signal_handler)
    
    line_count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            process_line(line)
            line_count += 1
            
            if line_count % 10 == 0:
                print_statistics()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting gracefully.")
    finally:
        print("\nFinal statistics:")
        print_statistics()


if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}