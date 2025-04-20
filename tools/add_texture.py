import argparse
import os
import math
import random
from PIL import Image
import subprocess
import format.ftb as ftb
import format.wta as wta
from format.utils import *

FTB_TEXTURE_SIZE = 16

def create_blank_texture(base_name: str, id: int) -> str:
	texture = Image.new("RGBA", (2048, 2048), (0, 0, 0, 0))
	texture.save(f"{base_name}_{id:03d}_temp.png")
	subprocess.run(["magick", "-define", "dds:mipmaps=0", "-define", "dds:compression=dxt5", f"{base_name}_{id:03d}_temp.png", f"{base_name}_{id:03d}.dds"], check=True)
	os.remove(f"{base_name}_{id:03d}_temp.png")
	return f"{base_name}_{id:03d}.dds"

def is_ktb_exists(path: str, font_id: str) -> bool:
	return os.path.exists(f"{path}/font_{font_id}.ktb")

def process(input_ftb: str, input_wta: str, input_wtp: str, output_ftb: str, output_wta: str, output_wtp: str) -> int:
	dat_dir = os.path.dirname(output_ftb)
	dtt_dir = os.path.dirname(output_wtp)
	if not os.path.exists(dat_dir):
		os.makedirs(dat_dir)
	if not os.path.exists(dtt_dir):
		os.makedirs(dtt_dir)

	font_id = os.path.basename(input_ftb).split("_")[1].split(".")[0]
	in_ftb = ftb.File.parse(open(input_ftb, "rb"))
	in_wta = wta.File.parse(open(input_wta, "rb"))
	in_wtp = open(input_wtp, "rb")
	out_wtp = open(output_wtp, "wb")

	textures_count = in_ftb.header.textures_count
	
	# create a 2048x2048 dxt5 DDS texture
	new_texture = create_blank_texture(output_wtp, textures_count)

	# update ftb header and texture
	new_ftb_texture_bytes = textures_count.to_bytes(2, byteorder="little") + in_ftb.textures[2:16]
	if len(new_ftb_texture_bytes) != FTB_TEXTURE_SIZE:
		raise ValueError(f"new_ftb_texture_bytes length is not {FTB_TEXTURE_SIZE} bytes")
	in_ftb.textures += new_ftb_texture_bytes
	in_ftb.header.textures_count = textures_count + 1
	in_ftb.header.chars_offset += FTB_TEXTURE_SIZE
	in_ftb.header.chars_offset2 += FTB_TEXTURE_SIZE

	# get the last location of the wtp file
	in_wtp.seek(0, os.SEEK_END)

	# update wta header and texture
	new_wta_texture = wta.Entry()
	new_wta_texture.offset = in_wtp.tell()
	new_wta_texture.size = int.from_bytes(b"\x80\x00\x40\x00", byteorder="little")
	new_wta_texture.flags = b"\x22\x00\x00\x22"
	new_wta_texture.idx = math.floor(random.random() * 0xFFFFFFFF).to_bytes(4, byteorder="little")
	new_wta_texture.info = b"\x4d\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00"
	in_wta.textures.append(new_wta_texture)
	in_wta.header.textures_count = textures_count + 1

	# write new files
	open(output_ftb, "wb").write(in_ftb.serialize())
	for id, f in enumerate(in_wta.textures):
		if id == textures_count:
			texture = open(new_texture, "rb").read()
			f.offset = out_wtp.tell()
			f.size = len(texture)
			out_wtp.write(texture)
			out_wtp.write(write_padding(out_wtp.tell(), 0x1000))
		else:
			in_wtp.seek(f.offset)
			texture = in_wtp.read(f.size)
			f.offset = out_wtp.tell()
			f.size = len(texture)
			out_wtp.write(texture)
			out_wtp.write(write_padding(out_wtp.tell(), 0x1000))
	open(output_wta, "wb").write(in_wta.serialize())

	# copy ktb file if exists
	in_ftb_dir = os.path.dirname(input_ftb)
	if is_ktb_exists(in_ftb_dir, font_id):
		with open(f"{in_ftb_dir}/font_{font_id}.ktb", "rb") as in_ktb:
			with open(f"{dat_dir}/font_{font_id}.ktb", "wb") as out_ktb:
				out_ktb.write(in_ktb.read())

	# close all files
	in_wtp.close()

	return textures_count

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("input_ftb", help="source font file")
	parser.add_argument("input_wta", help="source wta file")
	parser.add_argument("input_wtp", help="source wtp file")
	parser.add_argument("output_ftb", help="target font file (must not be the same as source)")
	parser.add_argument("output_wta", help="target wta file (must not be the same as source)")
	parser.add_argument("output_wtp", help="target wtp file (must not be the same as source)")

	args = parser.parse_args()

	process(args.input_ftb, args.input_wta, args.input_wtp, args.output_ftb, args.output_wta, args.output_wtp)