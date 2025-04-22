import os
import subprocess
import platform

def ensure_dir(output_dir: str):
    if os.path.isfile(output_dir):
        raise Exception("Unable to extract to " + output_dir + ": not a directory")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

def convert_texture(src_file: str, target_file: str):
    astcenc_tool="./tools/astcenc-avx2.exe"
    if platform.system() != "Windows":
        raise NotImplementedError("Please run this script on Windows")
    
    if target_file.endswith(".dds"):
        subprocess.run(["magick", "-define", "dds:mipmaps=0", "-define", "dds:compression=dxt5", src_file, target_file], check=True)
    else:
        subprocess.run([astcenc_tool, "-cl", src_file, target_file, "4x4", "-thorough"], check=True)

def check_image_magick():
    result = subprocess.run(["magick", "-version"], capture_output=True, text=True)
    return result.returncode == 0