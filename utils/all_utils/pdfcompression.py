import os, sys, shutil, gzip
def compress(input_file,outputfile_name,ext):
        filename_in = input_file
        filename_out = os.getcwd()+"/assets/Compressed_Files/"+outputfile_name+ext+".tar.gz"

        with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb",compresslevel=9) as fout:
            shutil.copyfileobj(fin, fout)
        print(f"Uncompressed size: {os.stat(filename_in).st_size}")
        print(f"Compressed size: {os.stat(filename_out).st_size}")

        with gzip.open(filename_out, "rb") as fin:
            data = fin.read()
            print(f"Decompressed size: {sys.getsizeof(data)}")
            sys.exit("compress Sucess !!")
    
def decompress(input_file,outputfile_name,ext):
        filename_in = input_file
        filename_out = os.getcwd()+"/assets/Decompressed_Files/"+outputfile_name+ext
        with gzip.open(filename_in, 'rb') as f_in:
            with open(filename_out, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                sys.exit("decompress Sucess !!")