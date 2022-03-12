from utils.all_utils import pdfcompression as pdf
from utils.all_utils import img_video_filecompression as img_vid

def compress(filepath,filename_in, filename_out, ext, action):
    
    if ext in ['.pdf','.txt','.docx','.pptx']:
        if action == 1:
            pdf.compress(filepath, filename_out,ext)
        else:
            pdf.decompress(filepath, filename_out,ext)
    
    elif ext in ['.mp4','.mov','.mkv']:
        if action == 1:
            img_vid.compressvid(filename_in, filename_out,ext)
        else:
            print("\nPlease select either 1 or 0 to proceed...\n")   
    
    elif ext in ['.jpeg', '.bmp', '.jpg', '.png']:
        if action == 1:
            img_vid.compressimg(filepath, filename_out,ext)
        else:
            print("\nPlease select either 1 or 0 to proceed...\n")   
    
    else:
        print("File Format not supported !!")

    
        