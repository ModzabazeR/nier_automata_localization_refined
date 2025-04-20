#!/usr/bin/python3

import argparse
import os
import format.dat as dat

def process(input_file: str, output_file: str, replacement_files: list):
    file = open(input_file, "rb")
    parsed = dat.File.parse(file)

    for f in parsed.files:
        for replacement_file in replacement_files:
            if os.path.basename(replacement_file) == f.name:
                f.bytes = open(replacement_file, "rb").read()

    out_file = open(output_file, "wb")
    out_file.write(parsed.serialize())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help=".dat or .dtt file name")
    parser.add_argument("output_file", help="output .dat or .dtt file name")
    parser.add_argument("replacement_files", help="files to replace in ", nargs="+")

    args = parser.parse_args()
    process(args.input_file, args.output_file, args.replacement_files)