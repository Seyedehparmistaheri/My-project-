import sys

import csv

from tabulate import tabulate

import os



def main():



    if len(sys.argv) != 2:

        print("Usage: python pizza.py <file.csv>", file=sys.stderr)

        sys.exit(1)



    csv_path = sys.argv[1]



    if not csv_path.lower().endswith(".csv"):

        print("Error: Not a CSV file.", file=sys.stderr)

        sys.exit(1)



    try:

        with open(csv_path, newline='', encoding='utf-8') as f:

            reader = csv.reader(f)

            rows = list(reader)



            if not rows:

                print(f"Error: CSV file '{csv_path}' is empty.", file=sys.stderr)

                sys.exit(1)



            headers = rows[0]

            data = rows[1:]



            print(tabulate(data, headers=headers, tablefmt="grid"))



    except FileNotFoundError:

        print(f"Error: File '{csv_path}' not found.", file=sys.stderr)

        sys.exit(1)

    except csv.Error:

        print("Error: File is not a valid CSV.", file=sys.stderr)

        sys.exit(1)

    except Exception as e:

        print(f"Error: Unexpected error: {e}", file=sys.stderr)

        sys.exit(1)



if __name__ == "__main__":

    main()
