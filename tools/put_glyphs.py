#!/usr/bin/python3

import argparse
import format.ftb as ftb
from PIL import Image


def add_glyphs(font, texture, page, chars):
    for char, glyph in chars:
        x, y = font.find_space_for_glyph(glyph.size, texture.size, page)
        font.add_character(char, page, glyph.width, glyph.height, x, y)
        texture.paste(glyph, (x, y))

def process(input_ftb: str, input_texture: str, output_ftb: str, output_texture: str, page: int, char: list):
    font = None
    with open(input_ftb, "rb") as f:
        font = ftb.File.parse(f)
    texture = Image.open(input_texture)

    chars = [(chr(int(c)), Image.open(tex)) for c, tex in char]

    add_glyphs(font, texture, page, chars)

    with open(output_ftb, "wb") as f:
        f.write(font.serialize())
    texture.save(output_texture)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_ftb", help="source font file")
    parser.add_argument("input_texture", help="source texture file (can be .dds)")
    parser.add_argument("output_ftb", help="target font file")
    parser.add_argument(
        "output_texture",
        help="target texture file (cannot be .dds, but .png can be used)",
    )
    parser.add_argument(
        "--page", help="texture number", required=True, type=int,
    )
    parser.add_argument(
        "--char",
        help="character id and glyph image",
        metavar=("CHARID", "CHARIMG"),
        nargs=2,
        action="append",
    )

    args = parser.parse_args()
    process(args.input_ftb, args.input_texture, args.output_ftb, args.output_texture, args.page, args.char)