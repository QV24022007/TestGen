import customtkinter as ctk
from Frames import root,file_path,home_img,create_img,exp_img,content_frame,home_frame,create_frame,example_frame,algo_example,basic1_menu,basic2_menu,norm_menu,main_frame,tab_frame
home_label = ctk.CTkLabel(home_frame, text="GIỚI THIỆU", font=("Arial", 18, "bold"))

home1_text2 = ctk.CTkLabel(home_frame, text=("    TestGen là một phần mềm giúp học sinh và giáo viên linh hoạt hơn trong việc sinh test cho các bài tập lập trình thi đấu.\n"
                                             "    Phần mềm bao gồm:\n"
                                             "        1. Giao diện dễ sử dụng và thao tác.\n"
                                             "        2. Tạo input/output cho các bài tập một cách linh hoạt.\n"
                                             "        3. Cung cấp bộ đề mẫu giúp học sinh luyện tập."),
                           font=("Arial", 14), justify="left", anchor="w")
separator = ctk.CTkLabel(home_frame, text="--------------------------------------------")

home2_text1 = ctk.CTkLabel(home_frame, text="HƯỚNG DẪN SỬ DỤNG", font=("Arial", 18, "bold"))

home2_text2 = ctk.CTkLabel(home_frame, text="1. Bộ sinh test\n    - Bộ sinh test gồm 3 phần chính:", justify="left", anchor="w", font=("Arial", 14))

home2_text3 = ctk.CTkLabel(home_frame, text=("       + Đối tượng cần tạo: các đối tượng có trong bộ test cần tạo như 'Số phân tử (độ dài)', 'Mảng số', 'Số ngẫu nhiên',...\n"
                                             "       + Ràng buộc: nhấn vào để lựa chọn các ràng buộc cần thiết cho mỗi đối tượng (nếu có),\n"
                                             "       + Giới hạn: nhấn vào để lựa chọn các giới hạn cho mỗi đối tượng (nếu có)\n"

                                             "   - Chọn cách thức lưu file: \n"
                                             "       + Sau khi nhập xong cấu hình, nhấn vào nút Sinh test để lưu file. \n"
                                             "       + Hộp thoại Tạo Test sẽ xuất hiện. Hiện tại, phần mềm có 3 cách thức lưu file khác nhau bao gồm Xuất folder, Xuất Word, Xuất Themis. \n" 
                                             "       + Ngôn ngữ được hỗ trợ bao gồm C++, Python, Pascal và Java. Người dùng chỉ để chọn ngôn ngữ và đường dẫn file code nếu có nhu cầu sinh output.\n"
                                             "       + Trong trường hợp đó, file code được chọn là file code chuẩn của người dùng, không do phần mềm cung cấp.\n"
                                             "       + Người dùng chọn các cách thức, đường dẫn file, số lượng test, tên file,... phù hợp và nhấn “Tạo test” để bắt đầu quá trình tạo test.\n"
                                             "       + Test được tạo sẽ nằm ở folder đã được người dùng chọn trước đó. "   


                                             ),
                           font=("Arial", 14), anchor="w", justify="left")

home3_text2 = ctk.CTkLabel(home_frame, text="2. Bộ bài mẫu\n      - Bộ bài mẫu gồm 3 phần chính:", justify="left", anchor="w", font=("Arial", 14))
home3_text3 = ctk.CTkLabel(home_frame, text=("          + Cơ bản 1: các thuật toán cơ bản như sắp xếp, tổng tiền tố, các bài số học cơ bản với các dạng bài cơ bản\n"
                                             "          + Cơ bản 2: nâng cao hơn Cơ bản 1 như quay lui, hoán vị, các thuật toán phức tạp hơn nhưng bài tập vẫn nằm ở dạng biết và hiểu\n"
                                             "          + Trung bình: các thuật toán nâng cao như BFS/DFS và các dạng bài tập nằm ở dạng hiểu và vận dụng"),
                           font=("Arial", 14), anchor="w", justify="left")



#CREATE FRAME
create_label1 = ctk.CTkLabel(create_frame, text="Đối tượng cần tạo")

create_label2 = ctk.CTkLabel(create_frame, text="Ràng buộc")

create_label3 = ctk.CTkLabel(create_frame, text="Giới hạn")

#overall frames
home_frame.grid(row=0, column=0, sticky="nsew")

create_frame.grid(row=0, column=0, sticky="nsew")

example_frame.grid(row=0, column=0, sticky="nsew")

home_label.pack(pady=20, padx=20, anchor="nw")

home1_text2.pack(pady=20, padx=20, anchor="nw")

separator.pack(pady=10, padx=20, anchor="nw")

home2_text1.pack(pady=5, padx=20, anchor="nw")

home2_text2.pack(pady=5, padx=20, anchor="nw")

home2_text3.pack(pady=5, padx=20, anchor="nw")

home3_text2.pack(pady=5, padx=20, anchor="nw")


home3_text3.pack(pady=5, padx=20, anchor="nw")

#create
create_label1.grid(row=0, column=0, padx=10,  sticky="w")   


create_label2.grid(row=0, column=1, padx=5,   sticky="w")   


create_label3.grid(row=0, column=2, padx=10,  sticky="w") 