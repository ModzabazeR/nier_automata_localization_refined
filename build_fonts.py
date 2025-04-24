from config import MyConsole, chars_to_add
import glob
import subprocess
import sys
import os
import platform
import shutil

# Add the tools directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
import tools.put_glyphs as ptglyphs
import tools.repack_wtp as rpckwtp
import tools.repack_dat as rpckdat
import tools.add_texture as addtex
import tools.utils as utils

console = MyConsole()

def repack_dat(font_id: str):
    console.print(f"repacking dat...")
    rpckdat.process(f"data/font/font_{font_id}.dat", f"output/font/font_{font_id}.dat", glob.glob(f"assembly/font/font_{font_id}.dat/*"))
    rpckdat.process(f"data/font/font_{font_id}.dtt", f"output/font/font_{font_id}.dtt", glob.glob(f"assembly/font/font_{font_id}.dtt/*.wtp"))

def build_font_with_new_texture(font_id: str):
    console.heading(f"Building font {font_id} with new texture")

    console.print("adding new texture...")
    page = addtex.process(
        input_ftb=f"unpacked/font/font_{font_id}.dat/font_{font_id}.ftb",
        input_wta=f"unpacked/font/font_{font_id}.dat/font_{font_id}.wta",
        input_wtp=f"unpacked/font/font_{font_id}.dtt/font_{font_id}.wtp",
        output_ftb=f"assembly/font/font_{font_id}_new.dat/font_{font_id}.ftb",
        output_wta=f"assembly/font/font_{font_id}_new.dat/font_{font_id}.wta",
        output_wtp=f"assembly/font/font_{font_id}_new.dtt/font_{font_id}.wtp",
    )

    console.print(f"putting glyphs to page {page}...")
    ptglyphs.process(
        input_ftb=f"assembly/font/font_{font_id}_new.dat/font_{font_id}.ftb",
        input_texture=f"assembly/font/font_{font_id}_new.dtt/font_{font_id}.wtp_00{page}.dds",
        output_ftb=f"assembly/font/font_{font_id}_new.dat/font_{font_id}.ftb",
        output_texture=f"assembly/font/font_{font_id}_new.dtt/font_{font_id}.wtp_00{page}.png",
        page=page,
        char=[
            (code, f"fonts/{font_id}/{code:04x}.png") for code in chars_to_add
        ]
    )

    console.print("converting textures...")
    utils.convert_texture(
        src_file=f"assembly/font/font_{font_id}_new.dtt/font_{font_id}.wtp_00{page}.png", 
        target_file=f"assembly/font/font_{font_id}_new.dtt/font_{font_id}.wtp_00{page}.dds"
    )

    console.print("repacking wtp...")
    utils.ensure_dir(f"assembly/font/font_{font_id}_new.dtt/final/")
    rpckwtp.process(
        input_wta=f"assembly/font/font_{font_id}_new.dat/font_{font_id}.wta", 
        input_wtp=f"assembly/font/font_{font_id}_new.dtt/font_{font_id}.wtp", 
        output_wta=f"assembly/font/font_{font_id}_new.dat/font_{font_id}.wta", 
        output_wtp=f"assembly/font/font_{font_id}_new.dtt/final/font_{font_id}.wtp", 
        texture=[
            (page, f"assembly/font/font_{font_id}_new.dtt/font_{font_id}.wtp_00{page}.dds"),
        ]
    )

    shutil.copy(f"assembly/font/font_{font_id}_new.dat/font_{font_id}.ftb", f"assembly/font/font_{font_id}.dat/font_{font_id}.ftb")
    shutil.copy(f"assembly/font/font_{font_id}_new.dat/font_{font_id}.wta", f"assembly/font/font_{font_id}.dat/font_{font_id}.wta")
    if font_id != "00":
        shutil.copy(f"unpacked/font/font_{font_id}.dat/font_{font_id}.ktb", f"assembly/font/font_{font_id}.dat/font_{font_id}.ktb")
    shutil.copy(f"assembly/font/font_{font_id}_new.dtt/final/font_{font_id}.wtp", f"assembly/font/font_{font_id}.dtt/font_{font_id}.wtp")

    console.print("repacking dat...")
    rpckdat.process(f"data/font/font_{font_id}.dat", f"output/font/font_{font_id}.dat", glob.glob(f"assembly/font/font_{font_id}_new.dat/*"))
    rpckdat.process(f"data/font/font_{font_id}.dtt", f"output/font/font_{font_id}.dtt", glob.glob(f"assembly/font/font_{font_id}_new.dtt/final/*.wtp"))

def build_font(font_id: str):
    console.heading(f"Building font {font_id}")
    utils.ensure_dir(f"assembly/font/font_{font_id}.dat/")
    utils.ensure_dir(f"assembly/font/font_{font_id}.dtt/")
    utils.ensure_dir(f"output/font/")

    # Check if ASTC files exist, otherwise use DDS
    astc_files = glob.glob(f"unpacked/font/font_{font_id}.dtt/*.astc")
    target_texture_ext = "astc" if astc_files else "dds"

    N = len(glob.glob(f"unpacked/font/font_{font_id}.dtt/*.dds")) - 1

    try:
        console.print(f"putting glyphs...")
        ptglyphs.process(
            input_ftb=f"unpacked/font/font_{font_id}.dat/font_{font_id}.ftb", 
            input_texture=f"unpacked/font/font_{font_id}.dtt/font_{font_id}.wtp_00{N}.dds", 
            output_ftb=f"assembly/font/font_{font_id}.dat/font_{font_id}.ftb", 
            output_texture=f"assembly/font/font_{font_id}.dtt/font_{font_id}.wtp_00{N}.png", 
            page=N, 
            char=[
                (code, f"fonts/{font_id}/{code:04x}.png") for code in chars_to_add
            ]
        )
    except Exception as e:
        console.print(f"[red]Error: {e}")
        # TODO: make a custom exception for this and handle it here
        if (str(e) == "cannot place character"):
            console.print("[yellow]You have too many glyphs to fit in the existing texture.")
            console.print(f"[yellow]Don't worry :) Falling back to build_font_with_new_texture()")
            build_font_with_new_texture(font_id)
        return

    console.print(f"converting textures...")
    utils.convert_texture(
        src_file=f"assembly/font/font_{font_id}.dtt/font_{font_id}.wtp_00{N}.png", 
        target_file=f"assembly/font/font_{font_id}.dtt/font_{font_id}.wtp_00{N}.{target_texture_ext}"
    )

    # we'll skip the original script's clone kernings part
    if font_id != "00":
        shutil.copy(f"unpacked/font/font_{font_id}.dat/font_{font_id}.ktb", f"assembly/font/font_{font_id}.dat/font_{font_id}.ktb")

    console.print(f"repacking wtp...")
    rpckwtp.process(
        input_wta=f"unpacked/font/font_{font_id}.dat/font_{font_id}.wta", 
        input_wtp=f"unpacked/font/font_{font_id}.dtt/font_{font_id}.wtp", 
        output_wta=f"assembly/font/font_{font_id}.dat/font_{font_id}.wta", 
        output_wtp=f"assembly/font/font_{font_id}.dtt/font_{font_id}.wtp", 
        texture=[
            (N, f"assembly/font/font_{font_id}.dtt/font_{font_id}.wtp_00{N}.{target_texture_ext}"),
        ]
    )

    repack_dat(font_id)

if __name__ == "__main__":
    console.heading("NieR Localization: Build Fonts")
    console.print("This script will build the font files.")
    utils.ensure_dir(f"output/font/")

    build_font("00")
    build_font("01")
    build_font("04")
    build_font("05")
    build_font("11")