"""Name-en-US: CSV Reader
Description-en-US: Ingests CSV data from a file, and uses it to change an object's PSR.'
"""

import c4d
import csv

def SetStatus(status):
    op[c4d.ID_USERDATA,3] = status

def main():
    # Init
    SetStatus("")

    # User Inputs
    csv_filename = op[c4d.ID_USERDATA,2]

    if not (csv_filename):
        SetStatus("Please load a *.csv file.")
        return

    sniffer = csv.Sniffer()
    sniff_range = 4096

    with open(csv_filename, 'r') as f:
        dialect = sniffer.sniff(
            f.read(sniff_range), delimiters=";,\t"
        )
        f.seek(0)  # Return to the start

        has_header = sniffer.has_header(f.read(sniff_range))
        f.seek(0)

        reader = csv.reader(f, dialect)
        for row in reader:
            print row

        # TODO: Read in data, and map it to fields by header name.