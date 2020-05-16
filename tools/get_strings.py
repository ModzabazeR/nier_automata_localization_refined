#!/usr/bin/python3

import argparse
import os

import format.smd as smd
import format.tmd as tmd
import format.bin as bin
import format.mcd as mcd
import format.properties as properties


def extract_strings_to_file(input_filename, output_filename, lang="en"):
    # TODO: support extracting different languages from .bin files
    if lang not in {"jp", "en", "fr", "it", "de", "es"}:
        raise Exception("Language " + lang + " is not supported")

    file_ext = os.path.splitext(input_filename)[1]

    parsed = None
    with open(input_filename, "rb") as in_file:
        if file_ext == ".bin":
            parsed = bin.File.parse(in_file)
        elif file_ext == ".smd":
            parsed = smd.File.parse(in_file)
        elif file_ext == ".tmd":
            parsed = tmd.File.parse(in_file)
        elif file_ext == ".mcd":
            parsed = mcd.File.parse(in_file)
        else:
            raise Exception(
                "Unable to extract " + input_filename + ": unknown file extenstion"
            )

    with open(output_filename, "wb") as out_file:
        out_file.write(properties.serialize_properties(parsed.get_strings()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="source file name")
    parser.add_argument("output", help="target file name (*.properties)")
    parser.add_argument("--lang", help="source laguage", default="en")

    args = parser.parse_args()
    extract_strings_to_file(args.input, args.output, args.lang)
    file_ext = os.path.splitext(args.input)[1]

    parsed = None
    with open(args.input, "rb") as in_file:
        if file_ext == ".bin":
            parsed = bin.File.parse(in_file)
        elif file_ext == ".smd":
            parsed = smd.File.parse(in_file)
        elif file_ext == ".tmd":
            parsed = tmd.File.parse(in_file)
        elif file_ext == ".mcd":
            parsed = mcd.File.parse(in_file)
        else:
            raise Exception(
                "Unable to extract " + args.input + ": unknown file extenstion"
            )

    with open(args.output, "wb") as out_file:
        out_file.write(properties.serialize_properties(parsed.get_strings()))
