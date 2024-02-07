import sys

def print_statistics(total_size, status_codes):
    """Prints the total file size and the number of occurrences for each status code."""
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    """Main function to read input lines and print statistics."""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        line_count = 0
        for line in sys.stdin:
            try:
                parts = line.split()
                size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += size
                status_codes[status_code] = status_codes.get(status_code, 0) + 1
                line_count += 1
                if line_count == 10:
                    /* Print statistics after every 10 lines */
                    print_statistics(total_size, status_codes)
                    line_count = 0
            except KeyboardInterrupt:
                /* If interrupted, print statistics and exit */
                print_statistics(total_size, status_codes)
                sys.exit(0)
    except KeyboardInterrupt:
        /*If interrupted, print statistics and exit */
        print_statistics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()
