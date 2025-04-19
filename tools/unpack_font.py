#!/usr/bin/python3

import argparse
import format.ftb as ftb
import format.mcd as mcd
from PIL import Image
import os

def ensure_dir(output_dir):
    if os.path.isfile(output_dir):
        raise Exception("Unable to extract to " + output_dir + ": not a directory")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

def get_parsed_ftb(ftb_path: str, texture_paths: list) -> ftb.File:
    parsed = ftb.File.parse(open(ftb_path, "rb"))
    if len(texture_paths) != parsed.header.textures_count:
        raise Exception(
            f"Invalid number of image files: was {len(texture_paths)}, expected {parsed.header.textures_count}"
        )
    return parsed

def get_parsed_mcd(mcd_path: str, texture_paths: list) -> mcd.File:
    parsed = mcd.File.parse(open(mcd_path, "rb"))

    if len(texture_paths) != 1:
        raise Exception(
            f"Invalid number of image files: was {len(texture_paths)}, expected 1"
        )

    return parsed

def process(font_file_path: str, texture_paths: list, font_id: int, out_dir: str, skip_cjk: bool = False, achar: int = None):
    parsed = None
    ext = os.path.splitext(font_file_path)[1]
    if ext == ".ftb":
        parsed = get_parsed_ftb(font_file_path, texture_paths)
    elif ext == ".mcd":
        parsed = get_parsed_mcd(font_file_path, texture_paths)
    else:
        raise Exception("Unknown file type for: " + font_file_path)

    textures = []
    for texture_file in texture_paths:
        textures.append(Image.open(texture_file))

    ensure_dir(out_dir)

    for char, glyph in parsed.get_glyphs(textures, font_id).items():
        if achar and achar != ord(char):
            continue
        if skip_cjk and (
            (ord(char) >= 0x2E80 and ord(char) <= 0x9FFF)
            or (ord(char) >= 0xAC00 and ord(char) <= 0xD7FF)
        ):
            continue
        outfile = os.path.join(out_dir, f"{ord(char):04x}.png")
        glyph.save(outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-cjk", help="skip CJK characters", action="store_true")
    parser.add_argument(
        "--font-id", help="font number (relevant for .mcd)", default=0, type=int
    )
    parser.add_argument(
        "--char", help="extract only the character specified by code point", type=int
    )
    parser.add_argument("font_file", help=".ftb or .mcd file name")
    parser.add_argument(
        "directory", help="output directory that will contain separated glyphs"
    )
    parser.add_argument(
        "image_files", help="list of image file names (.dds or .png)", nargs="+"
    )

    args = parser.parse_args()

    process(args.font_file, args.image_files, args.font_id, args.directory, args.skip_cjk, args.char)
