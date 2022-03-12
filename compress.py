from utils import filecompression as fc, func
import sys
 
def main():
    print("Enter Input_File_name :" )
    file_path,file_name_in,ext= func.browseFiles() #input("Enter Input_File_name : ")
    output_file_name=input("Enter_output_File_name (Without Extension) : ")
    if ext in ['.mp4','.mov','.mkv','.jpeg', '.bmp', '.jpg', '.png']:
        print("\nChoose What action you want to perform : \n\n Enter 1 for Compression \n Enter 0 to Exit \n\n")
    else:
        print("\nChoose What action you want to perform : \n\n Enter 1 for Compression \n Enter 2 for Decompression \n Enter 0 to Exit \n\n")
    while True:
        try:
            action = int(input("Enter your option here =  "))
        except ValueError:
            print("Sorry, I didn't understand that.,press 0 to exit.\n")
            continue
        
        if action in [1,2]:
            fc.compress(file_path,file_name_in,output_file_name,ext,action)
        elif action == 0:
            sys.exit("\n-> Successfully Exited from program, Thank You...")

        else:
            print("\nSelect any one option either 1 or 2, otherwise enter 0 to exit\n")
            continue

main()
