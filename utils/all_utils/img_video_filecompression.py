import zlib,base64
import PIL
import os,sys
import subprocess
from PIL import Image


def compressvid(filename_in,filename_out,ext): 
    directory = os.getcwd()
    crf = 30
    for subdir, dir, all_files in os.walk(directory):
        for file_in_dir in all_files:
            if file_in_dir == filename_in:
                    inp=subdir+ "/"+ file_in_dir
                    out = os.getcwd()+"/assets/Compressed_Files/"+ filename_out+ext
                    subprocess.run(f'ffmpeg -i "{inp}" -vcodec libx264 -crf {crf} "{out}"', shell=True)
    sys.exit("compress Sucess !!")     
     
def compressimg(filepath,filename_out,ext):
    picture = Image.open(filepath)
    picture.save(os.getcwd()+"/assets/Compressed_Files/"+filename_out+ext,optimize=True,quality=50) 
    sys.exit("compress Sucess !!")
  