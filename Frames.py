import customtkinter as ctk
import os
from PIL import Image, ImageTk 
import time



file_path = os.path.dirname(os.path.realpath(__file__))
home_img = ctk.CTkImage(Image.open(file_path + "\\home.png"), size = (20, 20))
create_img = ctk.CTkImage(Image.open(file_path + "\\create.png"), size = (19, 19)) 
exp_img = ctk.CTkImage(Image.open(file_path + "\\exp.png"), size = (19, 19)) 
 

#MAIN FRAME
ctk.set_appearance_mode("system")  
root = ctk.CTk()
root.title("Sinh Test")
root.geometry("1250x700")
root.resizable(False, False)
root.iconbitmap(file_path+" \\icon.ico")

main_frame = ctk.CTkFrame(root)

tab_frame = ctk.CTkFrame(main_frame)


#CONTENT FRAME
content_frame = ctk.CTkFrame(main_frame)

home_frame = ctk.CTkFrame(content_frame)

create_frame = ctk.CTkFrame(content_frame)

example_frame = ctk.CTkFrame(content_frame)

algo_example = ctk.CTkFrame(content_frame)

basic1_menu = ctk.CTkFrame(content_frame)

basic2_menu = ctk.CTkFrame(content_frame)

norm_menu = ctk.CTkFrame(content_frame) 

accu = ctk.CTkFrame(content_frame)
# # delay(1000)
# time.sleep(1000)