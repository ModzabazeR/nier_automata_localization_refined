#!/usr/bin/python3

import argparse
import format.wta as wta
from format.utils import *
import swizzle


def repack_wtp(parsed_wta, in_wtp, out_wtp, textures):
    for id, f in enumerate(parsed_wta.textures):
        if id in textures:
            texture = None
            with open(textures[id], "rb") as texture_file:
                texture = texture_file.read()
            if f.is_astc():
                size_range = 4 if f.tex_height() >= 512 else 3
                texture = swizzle.swizzle(
                    f.tex_width(), f.tex_height(), 4, 4, 16, 0, size_range, texture[16:]
                )
            f.offset = out_wtp.tell()
            f.size = len(texture)
            if f.is_astc():
                f.update_astc_info()
            out_wtp.write(texture)
            out_wtp.write(write_padding(out_wtp.tell(), 0x1000))
        else:
            in_wtp.seek(f.offset)
            texture = in_wtp.read(f.size)
            f.offset = out_wtp.tell()
            f.size = len(texture)
            out_wtp.write(texture)
            out_wtp.write(write_padding(out_wtp.tell(), 0x1000))

def process(input_wta: str, input_wtp: str, output_wta: str, output_wtp: str, texture: list):
    textures = {int(id): filename for id, filename in texture}

    wta_file = open(input_wta, "rb")
    in_wtp = open(input_wtp, "rb")
    parsed_wta = wta.File.parse(wta_file)

    out_wtp = open(output_wtp, "wb")
    repack_wtp(parsed_wta, in_wtp, out_wtp, textures)
    open(output_wta, "wb").write(parsed_wta.serialize())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_wta", help="source wta file")
    parser.add_argument("input_wtp", help="source wtp file")
    parser.add_argument("output_wta", help="target wta file")
    parser.add_argument("output_wtp", help="target wtp file")
    parser.add_argument(
        "--texture",
        help="texture id and texture image (must be .dds)",
        metavar=("ID", "TEXTURE"),
        nargs=2,
        action="append",
    )

    args = parser.parse_args()

    process(args.input_wta, args.input_wtp, args.output_wta, args.output_wtp, args.texture)
