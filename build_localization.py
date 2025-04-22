from config import MyConsole, langFormats, gameStrings, srcLang, targetLang
import glob
import shutil
import sys
import os
import platform

# Add the tools directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
import tools.unpack_font as unpkfnt
import tools.repack_dat as rpckdat
import tools.put_strings_mcd as putmcd
import tools.repack_wtp as rpckwtp
import tools.put_strings as putstr
import tools.utils as utils

console = MyConsole()

def repack_dat(file_path: str):
    utils.ensure_dir(os.path.dirname(f"output/{file_path}"))
    rpckdat.process(f"data/{file_path}", f"output/{file_path}", glob.glob(f"assembly/{file_path}/*"))

def put_strings(dat_file: str, name: str, ext: str):
    console.print(f"building {name}...")

    if ext == "txt":
        utils.ensure_dir(f"output/novel")
        shutil.copy(f"target/{name}.{ext}", f"output/novel/{name}.{ext}")
    elif ext == "mcd":
        dtt_file = dat_file.replace(".dat", ".dtt")
        utils.ensure_dir(f"assembly/{dat_file}/")
        utils.ensure_dir(f"assembly/{dtt_file}/")

        putmcd.process(
            input_mcd=f"unpacked/{dat_file}/{name}.mcd",
            strings=f"target/{name}_{targetLang}.properties",
            fonts_json="fonts/fonts.json",
            output_mcd=f"assembly/{dat_file}/{name}.mcd",
            output_texture=f"assembly/{dtt_file}/{name}.wtp_000.png",
        )

        astc_files = glob.glob(f"unpacked/{dtt_file}/*.astc")
        target_texture_ext = "astc" if astc_files else "dds"
        utils.convert_texture(
            src_file=f"assembly/{dtt_file}/{name}.wtp_000.png",
            target_file=f"assembly/{dtt_file}/{name}.wtp_000.{target_texture_ext}"
        )

        rpckwtp.process(
            input_wta=f"unpacked/{dat_file}/{name}.wta",
            input_wtp=f"unpacked/{dtt_file}/{name}.wtp",
            output_wta=f"assembly/{dat_file}/{name}.wta",
            output_wtp=f"assembly/{dtt_file}/{name}.wtp",
            texture=[
                (0, f"assembly/{dtt_file}/{name}.wtp_000.{target_texture_ext}"),
            ]
        )

        utils.ensure_dir(os.path.dirname(f"output/{dat_file}"))
        utils.ensure_dir(os.path.dirname(f"output/{dtt_file}"))
        rpckdat.process(f"data/{dat_file}", f"output/{dat_file}", glob.glob(f"assembly/{dat_file}/*"))
        rpckdat.process(f"data/{dtt_file}", f"output/{dtt_file}", glob.glob(f"assembly/{dtt_file}/{name}.wtp"))
    else:
        utils.ensure_dir(f"assembly/{dat_file}")
        putstr.insert_strings_to_file(
            input_filename=f"unpacked/{dat_file}/{name}.{ext}",
            properties_filename=f"target/{name}_{targetLang}.properties",
            output_filename=f"assembly/{dat_file}/{name}.{ext}",
        )
        if ext in ["tmd", "smd"]:
            utils.ensure_dir(os.path.dirname(f"output/{dat_file}"))
            rpckdat.process(f"data/{dat_file}", f"output/{dat_file}", glob.glob(f"assembly/{dat_file}/{name}.{ext}"))

if __name__ == "__main__":
    console.heading("NieR Localization: Build Localization")

    # (*.dat, {
    #       ext: [file1, file2, ...],
    #       ext2: [...],
    #       ...,
    # })
    for dat_file, data in gameStrings.items():
        files_to_build = [f"ui/ui_title{langFormats[srcLang]["default"]}.dat", f"subtitle/subtitle0010{langFormats[srcLang]["default"]}.dat"]
        if dat_file not in files_to_build:
            continue

        extensions = data.keys()

        # (ext, [file1, file2,...])
        for ext, files in data.items():
            for file in files:
                put_strings(dat_file, file, ext)
        
        if "bin" in extensions:
            repack_dat(dat_file)

    console.heading("Done! You can now copy folders in output/ to the game directory")