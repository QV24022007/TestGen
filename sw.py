import customtkinter as ctk
import os 
import time 
from Frames import root,file_path,home_img,create_img,exp_img,content_frame,home_frame,create_frame,example_frame,algo_example,basic1_menu,basic2_menu,norm_menu,main_frame,tab_frame,accu  
from labels import home_label,home1_text2,separator,home2_text1,home2_text2,home2_text3,home3_text2,home3_text3,create_label1,create_label2,create_label3
import config
import threading
from Data import Combo_list,value_of_array_in_test,Checkbox_list,Func_limit_list,FuncItem,Func_list
from PIL import Image, ImageTk 
from handlers import cons_click, limit_click, create_buttons, add_inputs, remove_inputs, combo_click,Func_limit_list,tao_test,choose_browser_folder,create_file_test_threaded,choose_browser_file



current_dialog = None
main_frame.pack(expand=1, fill="both", padx=10, pady=10)
 
tab_frame.pack(side="left", fill="y", padx=(0, 10))
 
content_frame.pack(side="left",  fill="both", expand=1)
 

main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1)


def show_frame(frame):
    frame.tkraise()

val = ["Số phân tử (độ dài)", "Mảng số (nguyên/thực)", "Số ngẫu nhiên",
       "Xâu kí tự", "Kí tự", "Mảng kí tự","Đồ thị","Số bộ truy vấn","Bắt đầu truy vấn","Kết thúc truy vấn"]

#main_func 

row_counter = 1
widget_rows = {}   
 

def plus_button_click():
    global row_counter
    rown = row_counter
    add_inputs(create_frame, row_counter, widget_rows, val, Combo_list)
    row_counter += 1
    # print(row_counter)
 
def minus_button_click():
    global row_counter
    if row_counter > 1:
        Combo_list.pop()
        Func_limit_list.pop()
        row_counter -= 1
        remove_inputs(widget_rows, row_counter)


def testing():
    # print(value_final)
    # for v in value_final:
    #     print(v + "_")
    for limit in Func_limit_list:
        array1 = []
        array2 = []
        array1 = (limit[0].get()).split()
        array2 = (limit[1].get()).split()
        # print(array1)
        # print(array2)
plus = ctk.CTkButton(create_frame,
                    width = 30,
                    height = 30, 
                    text='+', 
                    fg_color="#2eb309", hover_color = "#3a9421",
                    command=lambda: plus_button_click())
plus.grid(row=1, column=4, padx=10, pady=10, sticky="w")

minus = ctk.CTkButton(create_frame,
                    width = 30,
                    height = 30, 
                    text='—',  
                    fg_color="#eb4034", hover_color="#b82828", 
                    command=lambda: minus_button_click())
minus.grid(row=1, column=5, pady=10, sticky="w")
  






#Testing_button = ctk.CTkButton(create_frame, width = 50, height = 50, text='Testing' , command = lambda :testing())
# Testing_button.grid(row=120, column= 20, sticky="se")

#algo_example

algo_example = ctk.CTkFrame(content_frame)
algo_example.grid(row=0, column=0, sticky="nsew")






def create_file_test_with_thread(template, language, dir_file_code, number_of_test, name_file, dir_folder, progress_bar, textbox):
    """Tạo luồng riêng để chạy hàm tạo test."""
    thread = threading.Thread(
        target=create_file_test_threaded,
        args=(template, language, dir_file_code, number_of_test, name_file, dir_folder, progress_bar, textbox)
    )
    thread.start()





def show_create_test():
    global current_dialog
    if current_dialog is not None and current_dialog.winfo_exists():
        current_dialog.destroy()
    ctk.set_appearance_mode("system")  
    dialog = ctk.CTkToplevel()
    dialog.geometry("750x500")  # Tăng chiều rộng cửa sổ để thêm thanh bên phải
    dialog.title("Hộp thoại Tạo Test")
    dialog.resizable(False, False)
    dialog.transient(root)
    dialog.lift()
    dialog.focus_force()
    current_dialog = dialog
    # Frame chính, chia thành 2 cột
    cusframe = ctk.CTkFrame(dialog)
    cusframe.pack(padx=20, pady=20, fill="both", expand=True) 
    
    # Frame bên trái (chứa thông tin)
    left_frame = ctk.CTkFrame(cusframe)
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Frame bên phải (chứa progress bar và textbox)
    right_frame = ctk.CTkFrame(cusframe)
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Cấu hình cột và hàng để chia đều không gian
    cusframe.columnconfigure(0, weight=3)  # Bên trái chiếm 3 phần
    cusframe.columnconfigure(1, weight=2)  # Bên phải chiếm 2 phần
    cusframe.rowconfigure(0, weight=1)

    # ------------------ Nội dung bên trái ------------------
    title_label = ctk.CTkLabel(left_frame, text="Tạo Test", font=("Arial", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    check1 = ctk.CTkComboBox(left_frame, values=["Xuất Folder", "Xuất Word", "Xuất Themis"])
    check1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    check2 = ctk.CTkComboBox(left_frame, values=["Ngôn ngữ", "C++", "Python", "Java", "Pascal"])
    check2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    path_label = ctk.CTkLabel(left_frame, text="Đường dẫn file code:")
    path_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    path1 = ctk.CTkEntry(left_frame)
    path1.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    butz = ctk.CTkButton(left_frame, width=150, height=30, text="Chọn file code", 
                         command=lambda: choose_browser_file(path1))
    butz.grid(row=3, column=0, columnspan=2, pady=10)

    label_test_count = ctk.CTkLabel(left_frame, text="Số lượng test:")
    label_test_count.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    test_count_entry = ctk.CTkEntry(left_frame)
    test_count_entry.grid(row=4, column=1, padx=10, pady=5)

    label_file_name = ctk.CTkLabel(left_frame, text="Tên file:")
    label_file_name.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    file_name_entry = ctk.CTkEntry(left_frame)
    file_name_entry.grid(row=5, column=1, padx=10, pady=5)

    label_code_path = ctk.CTkLabel(left_frame, text="Đường dẫn folder:")
    label_code_path.grid(row=6, column=0, padx=10, pady=5, sticky="w")

    path2 = ctk.CTkEntry(left_frame)
    path2.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    butz2 = ctk.CTkButton(left_frame, width=150, height=30, text="Chọn folder", 
                          command=lambda: choose_browser_folder(path2))
    butz2.grid(row=7, column=0, columnspan=2, pady=10)

    create_test = ctk.CTkButton(
    left_frame,
    width=200,
    height=70,
    text="Tạo test",
    font=("Arial", 20, "bold"),
    border_color="white",
    border_width=2,
    command=lambda: create_file_test_threaded(
        template=check1.get(),
        language=check2.get(),
        dir_file_code=path1.get(),
        number_of_test=test_count_entry.get(),
        name_file=file_name_entry.get(),
        dir_folder=path2.get(),
        progress_bar=current_dialog.progress_bar,
        textbox = textbox
    )
    )
    create_test.grid(row=8, column=0, columnspan=2, pady=15)


    # ------------------ Nội dung bên phải ------------------
    # Progress bar
    progress_bar = ctk.CTkProgressBar(right_frame)
    progress_bar.pack(padx=10, pady=(10, 5), fill="x")
    progress_bar.set(0)  # Giá trị ban đầu (0%)

    # Textbox thông báo
    textbox = ctk.CTkTextbox(right_frame, width=300, height=300, activate_scrollbars = True)
    textbox.pack(padx=10, pady=(5, 10), fill="both", expand=True)
    textbox.insert("1.0", "Log thông báo sẽ xuất hiện tại đây...\n")  # Nội dung mẫu
    textbox.configure(state="disabled")
    # Lưu thông tin các phần tử nếu cần
    current_dialog.progress_bar = progress_bar
    current_dialog.textbox = textbox
button_for_open_cusframe = ctk.CTkButton(create_frame,text = "Sinh test", width = 150, height = 100,font=("Arial", 20, "bold"),border_color = "white",border_width= 2, command = lambda : show_create_test())
button_for_open_cusframe.place(x = 900, y = 550)


#basic1

def show_new_frame(target):
    show_frame(target) 

def close_new_frame():
    show_frame(example_frame)


for frame in [algo_example, basic1_menu, basic2_menu, norm_menu, accu]:
    frame.grid(row=0, column=0, sticky="nsew")


but1 = ctk.CTkButton(example_frame,
                     width=150, height=40,
                     text="Cơ bản 1",
                     command=lambda: show_new_frame(basic1_menu))
but1.pack(pady=15)

but2 = ctk.CTkButton(example_frame,
                     width=150, height=40,
                     text="Cơ bản 2",
                     command=lambda: show_new_frame(basic2_menu))
but2.pack(pady=15)

but3 = ctk.CTkButton(example_frame,
                     width=150, height=40,
                     text="Trung bình",
                     command=lambda: show_new_frame(norm_menu))
but3.pack(pady=15)

# Close Button in Basic1 Menu
close_button = ctk.CTkButton(basic1_menu,
                             width=50, height=30,
                             text="Đóng",
                             command=close_new_frame)
close_button.pack(padx=10, pady=10, anchor="ne")

# Create Buttons in Submenus
buttons1 = create_buttons(basic1_menu, config.button_texts, algo_example)
buttons2 = create_buttons(basic2_menu, config.button_texts2, algo_example)
buttons3 = create_buttons(norm_menu, config.button_texts3, algo_example)

# Sidebar Buttons
home_button = ctk.CTkButton(tab_frame, 
                            image=home_img,
                            text="Trang chủ",
                            anchor="w",
                            command=lambda: show_frame(home_frame))
home_button.pack(fill="x", pady=5)

create_button = ctk.CTkButton(tab_frame, 
                              image=create_img,
                              text="Sinh test",
                              anchor="w",
                              command=lambda: show_frame(create_frame))
create_button.pack(fill="x", pady=5)

example_button = ctk.CTkButton(tab_frame, 
                               image=exp_img,
                               text="Bài mẫu",
                               anchor="w",
                               command=lambda: show_frame(example_frame))
example_button.pack(fill="x", pady=5)
  


show_frame(home_frame)
# print()
root.mainloop()
