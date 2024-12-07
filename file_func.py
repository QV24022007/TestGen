import os
import tkinter as tk
from tkinter import  filedialog
import customtkinter as ctk
import subprocess
# rename file
def rename_file(old_name,new_name):
	os.rename(old_name,new_name)

# delete file
def delete_file(file_dir):
	os.delete(file_dir)
	
# get directory_folder by browse_folder
def browse_folder(): 
    # Tạo một cửa sổ ẩn để tránh hiển thị cửa sổ Tkinter chính
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ gốc
    
    # Mở cửa sổ "Browse for Folder" và lấy đường dẫn
    folder_path = filedialog.askdirectory(title="Select a Folder")
    
    # Kiểm tra xem người dùng đã chọn thư mục hay chưa
    if folder_path:
        while(folder_path.find('/') != -1):
            folder_path = folder_path.replace('/',chr(92) + chr(92))
        return folder_path + '\\' + '\\'
    else:
        return "none"
    # Đóng cửa sổ gốc
    root.destroy()


def browse_file(check):
    # Tạo một cửa sổ ẩn để tránh hiển thị cửa sổ Tkinter chính
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ gốc

    # Mở cửa sổ "Open File" và lấy đường dẫn tệp
    file_path = filedialog.askopenfilename(title="Select a File")
    
    # Kiểm tra xem người dùng đã chọn tệp hay chưa
    if file_path:
        # Thay thế một dấu gạch chéo ngược bằng hai dấu gạch chéo ngược
        escaped_file_path = file_path.replace('/', '\\\\')
        
        # Lấy tên tệp từ đường dẫn
        file_name = file_path.split('/')[-1]
        
        # print(f"Selected file path: {escaped_file_path}")
        # print(f"Selected file name: {file_name}")
    else:
        return "none"
    
    # Đóng cửa sổ gốc
    root.destroy()
    if(check):
        return file_path
    else:
        return file_name





# Tạo file với tên và folder cụ thể
def create_file(file_name,file_dir,file_inp):
	#get name and dir
	path = file_dir + file_name
	os.makedirs(os.path.dirname(path), exist_ok=True)
	with open(path, "w", encoding="utf-8") as file:
   		file.write(file_inp)

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
            print("File content:\n", content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_code_program(dir_file,text):
    try:
        result = subprocess.run([ dir_file ],input = text, capture_output=True, text=True)
        return result.stdout
        print("Errors:\n", result.stderr)
    except FileNotFoundError:
        print("File not found. Please check the path to the executable.")
    except Exception as e:
        print(f"An error occurred: {e}")



# rebuild to get file program.exe (CPP)
def rebuild_cpp_code(source_file, output_file):
    try:
        # Compile the C++ source file
        subprocess.run(['g++', source_file, '-o', output_file], check=True)
        print(f"Successfully rebuilt {source_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during rebuild: {e}")

# rebuild to get file program.exe (C)
def rebuild_c_code(source_file, output_file):
    try:
        subprocess.run(['gcc', source_file, '-o', output_file], check=True)
        print(f"Successfully rebuilt {source_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during rebuild: {e}")


# rebuild to get file program.exe (Java)
def rebuild_java_code(source_file):
    try:
        subprocess.run(['javac', source_file], check=True)
        print(f"Successfully rebuilt {source_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during rebuild: {e}")


# rebuild to get file program.exe (py)
def rebuild_python_code(source_file):
    try:
        subprocess.run(['python', '-m', 'py_compile', source_file], check=True)
        print(f"Successfully rebuilt {source_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during rebuild: {e}")

# rebuild to get file program.exe (pas)
def rebuild_pascal_code(source_file, output_file):
    try:
        # Compile the Pascal source file using fpc
        subprocess.run(['fpc', source_file, '-o' + output_file], check=True)
        print(f"Successfully rebuilt {source_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during rebuild: {e}")
