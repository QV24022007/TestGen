import customtkinter as ctk
import tkinter as tk
import os 
import string
import config 
import copy
from Data import Combo_list,value_of_array_in_test,Checkbox_list,Func_limit_list,FuncItem,Func_list
from Frames import root,file_path,home_img,create_img,exp_img,content_frame,home_frame,create_frame,example_frame,algo_example,basic1_menu,basic2_menu,norm_menu,main_frame,tab_frame
# import sw
current_popup = None
value_0 = []
value_1 = []
value_2 = []
value_3 = []
value_4 = []
value_final = []
def content_ucln(frame):
    label_title = ctk.CTkLabel(frame, text="Tìm Ước Chung Lớn Nhất và Bội Chung Nhỏ Nhất", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Bạn cần nhập vào hai số nguyên dương a và b.\n"
        "Tìm ước chung lớn nhất (UCLN) và bội chung nhỏ nhất (BCNN) của hai số này.\n\n"
        "Yêu cầu:\n"
        " - UCLN là số nguyên dương lớn nhất chia hết cho cả a và b.\n"
        " - BCNN là số nguyên dương nhỏ nhất mà cả hai số a và b đều chia hết.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng duy nhất gồm hai số nguyên dương a và b.\n\n"
        "Dữ liệu đầu ra:\n"
        " - UCLN và BCNN của hai số a và b.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ a, b ≤ 10⁹.\n\n" 
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input: 4 6 (hai số nguyên dương)\n"
        "Output: 2 12 (UCLN = 2, BCNN = 12)"),
        font=("Arial", 14))
    label_input_details.pack(anchor="w")


def content_birthday(frame):
    label_title = ctk.CTkLabel(frame, text="Sinh Nhật", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Bạn được cung cấp một ngày hiện tại và sinh nhật của bạn Nam.\n"
        "Tính xem còn bao nhiêu ngày nữa là đến sinh nhật.\n\n"
        "Yêu cầu:\n"
        " - Ngày sinh nhật có thể nằm trong năm hiện tại hoặc năm sau.\n"
        " - Nếu ngày hiện tại là sinh nhật, số ngày còn lại là 0.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Ngày hiện tại gồm ngày, tháng, năm theo định dạng d/m/y.\n"
        " - Ngày sinh nhật gồm ngày và tháng theo định dạng d/m.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Số ngày còn lại cho đến ngày sinh nhật.\n\n"
        "Điều kiện:\n"
        " - Ngày, tháng hợp lệ theo lịch dương.\n"
        " - 1 ≤ d, m ≤ 31, 1 ≤ y ≤ 9999.\n\n" 
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input: 10 10 2023 (ngày hiện tại), 25 12 (ngày sinh nhật)\n"
        "Output: 76 ngày"), 
        font=("Arial", 14))
    label_input_details.pack(anchor="w")


def content_consecutive_sum(frame):
    label_title = ctk.CTkLabel(frame, text="Liên Tiếp", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho một số nguyên dương n, tìm số cách phân tích n thành tổng của ít nhất 2 số nguyên liên tiếp.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Một số nguyên dương n.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Số lượng cách phân tích n thành ít nhất 2 số nguyên liên tiếp.\n\n" 
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input: 12\n"
        "Output: 1 (12 = 3 + 4 + 5)"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")


def content_sum_of_divisors(frame):
    label_title = ctk.CTkLabel(frame, text="Tính Tổng Các Ước Dương Của n", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho một số nguyên dương n, tính tổng tất cả các ước dương của n.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Một số nguyên dương n.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Tổng các ước dương của n.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input: 6\n"
        "Output: 12 (12 = 1 + 2 + 3 + 6)"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")


def content_divisible_by_3(frame):
    label_title = ctk.CTkLabel(frame, text="Đếm Số Cặp Chỉ Số Có Tổng Chia Hết Cho 3", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho mảng A gồm n phần tử nguyên, đếm số cặp chỉ số i < j sao cho A[i] + A[j] chia hết cho 3.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm số nguyên n.\n"
        " - Dòng thứ hai gồm n số nguyên A[i].\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra một số nguyên là số lượng cặp chỉ số thỏa mãn.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10^5.\n"
        " - 1 ≤ A[i] ≤ 10^9.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3\n"
        "1 2 3\n\n"
        "Output:\n"
        "1"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")


#########################

def content_prefix_sum(frame):
    label_title = ctk.CTkLabel(frame, text="Tổng Tiền Tố", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho mảng A gồm n số nguyên và q truy vấn có dạng (l, r), tính tổng A[l] + A[l+1] + … + A[r].\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu gồm 2 số nguyên dương n, q.\n"
        " - Dòng thứ hai gồm n số nguyên A[i].\n"
        " - Mỗi dòng trong q dòng tiếp theo gồm 2 số nguyên l, r thể hiện một truy vấn.\n\n"
        "Dữ liệu đầu ra:\n"
        " - q dòng mỗi dòng một số nguyên là kết quả cho các truy vấn.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n, q ≤ 10^5.\n"
        " - 1 ≤ A[i] ≤ 10^9.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "5 3\n"
        "1 3 -2 3 4\n"
        "2 3\n"
        "1 4\n"
        "3 5\n\n"
        "Output:\n"
        "1\n"
        "5\n"
        "5"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_2d_prefix_sum(frame):
    label_title = ctk.CTkLabel(frame, text="Tính Tổng Bảng Con Trong Mảng 2 Chiều", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho mảng 2 chiều nguyên A và q truy vấn có dạng (a, b, c, d),\n"
        "tính tổng bảng con có góc trái trên (a, b) và góc phải dưới (c, d).\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu gồm 3 số nguyên n, m, q.\n"
        " - Mỗi dòng trong n dòng tiếp theo gồm m số nguyên A[i][j].\n"
        " - Mỗi dòng trong q dòng tiếp theo gồm 4 số nguyên a, b, c, d.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra q dòng, dòng thứ i là kết quả của truy vấn i.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n, m ≤ 1000.\n"
        " - 1 ≤ q ≤ 10^5.\n"
        " - 1 ≤ A[i][j] ≤ 10^9.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "2 3 2\n"
        "1 4 3\n"
        "2 2 3\n"
        "1 1 2 2\n"
        "2 1 2 3\n\n"
        "Output:\n"
        "9\n"
        "7"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_substring_ratio(frame):
    label_title = ctk.CTkLabel(frame, text="Đếm Số Lượng Xâu Con Tỉ Lệ", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho một xâu nhị phân độ dài n, đếm số lượng xâu con liên tiếp có tỉ lệ giữa số 0 và số 1 là x/y.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm hai số nguyên x, y.\n"
        " - Dòng thứ hai gồm xâu nhị phân độ dài n.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra số lượng xâu con liên tiếp thỏa mãn.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ x, y ≤ n ≤ 100000.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "1 2\n"
        "1010\n\n"
        "Output:\n"
        "1"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

########################

def content_sort_points(frame):
    label_title = ctk.CTkLabel(frame, text="Sắp Xếp Điểm Trên Lưới Tọa Độ 3 Chiều", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho n điểm trên lưới tọa độ 3 chiều, hãy sắp xếp các điểm tăng dần theo x,\n"
        "theo y (nếu có điểm cùng giá trị x), và theo z (nếu có điểm cùng cả x và y).\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu gồm số nguyên n.\n"
        " - Mỗi dòng trong n dòng tiếp theo gồm 3 số nguyên x, y, z.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra các điểm sau khi sắp xếp.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 100000.\n"
        " - 1 ≤ x, y, z ≤ 10^9.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3\n"
        "3 4 3\n"
        "2 4 3\n"
        "2 1 6\n\n"
        "Output:\n"
        "2 1 6\n"
        "2 4 3\n"
        "3 4 3"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")


def content_min_possible(frame):
    label_title = ctk.CTkLabel(frame, text="Nhỏ Nhất Có Thể", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho một số nguyên n, hãy sắp xếp lại các chữ số của n để thu được số nhỏ nhất có thể.\n"
        "Chú ý: Không được có chữ số 0 đứng đầu.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Một số nguyên n.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Số nhỏ nhất có thể sau khi sắp xếp lại các chữ số trong n.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10^5000000.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3210\n\n"
        "Output:\n"
        "1023"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_medicine_mixture(frame): 
    label_title = ctk.CTkLabel(frame, text="Pha Thuốc", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Mai có n cây nấm, mỗi cây nặng A_i. Bây giờ Mai muốn pha thuốc từ n cây nấm này.\n"
        "Mỗi chai thuốc được pha từ không quá 2 cây nấm và cân nặng của chúng cũng không được vượt quá k.\n"
        "Số chai thuốc ít nhất Mai có thể pha từ tất cả n cây nấm là bao nhiêu?\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu gồm 2 số nguyên n, k.\n"
        " - Dòng tiếp theo gồm n số nguyên A_i.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra 1 số nguyên là số lượng chai thuốc ít nhất có thể.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10^5.\n"
        " - 1 ≤ A_i ≤ k ≤ 10^9.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "5 7\n"
        "1 2 3 5 7\n\n"
        "Output:\n"
        "3"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

################

def content_subset_sum(frame):
    label_title = ctk.CTkLabel(frame, text="Tổng Tập Con", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho mảng A có n phần tử. Hãy xác định xem có tồn tại một tập con của A mà có tổng bằng k không.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm hai số nguyên n, k.\n"
        " - Dòng thứ hai gồm n số nguyên A_i.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra YES nếu tồn tại một tập con của A mà tổng của nó bằng k, ngược lại in ra NO.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 20.\n"
        " - 1 ≤ A_i, k ≤ 10^18.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "4 7\n"
        "1 2 3 4\n\n"
        "Output:\n"
        "YES"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_knight_tour(frame):
    label_title = ctk.CTkLabel(frame, text="Mã Đi Tuần", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho bàn cỡ vua kích cỡ n × m. Bạn được đặt một quân mã vào vị trí bất kì trên bàn cờ trống.\n"
        "Hãy tìm đường đi qua tất cả các ô trên bàn cờ, mỗi ô đúng một lần.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Một dòng gồm hai số nguyên n, m.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra một ma trận n dòng, m cột là thứ tự thăm các ô của con mã, bắt đầu từ 1.\n"
        " - Có thể in ra cách đi bất kì.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n, m ≤ 7.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "5 5\n\n"
        "Output:\n"
        "  1   6  15  10  21 \n"
        " 14   9  20   5  16\n"
        " 19   2   7  22  11\n"
        "  8  13  24  17   4\n"
        " 25  18   3  12  23"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_knapsack(frame):
    label_title = ctk.CTkLabel(frame, text="Cái Túi", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Có n món đồ, món đồ thứ i có cân nặng w_i và giá trị v_i.\n"
        "Bạn có thể chọn số lượng món đồ túy ý miễn cân nặng không quá S.\n"
        "Hãy tìm cách chọn đồ để có được giá trị lớn nhất.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm 2 số nguyên n, S.\n"
        " - Mỗi dòng trong n dòng tiếp theo gồm 2 số nguyên w_i, v_i.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Một số nguyên duy nhất giá trị lớn nhất có thể đạt được.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 20,\n"
        " - S ≤ 10^9.\n"
        " - 1 ≤ w_i, v_i ≤ 10^9.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3 5\n"
        "1 4\n"
        "4 1\n"
        "2 100\n\n"
        "Output:\n"
        "104"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_mushroom(frame):
    label_title = ctk.CTkLabel(frame, text="Hái Nấm", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Khu rừng có dạng một bảng 4x4. Ở mỗi ô (i, j) Khiết có thể đến ô (i + 1, j) hoặc (i, j + 1).\n"
        "Ô (i, j) có A[i][j] cây nấm. Hành trình của Khiết bắt đầu từ (1, 1) và kết thúc ở (4, 4).\n"
        "Hỏi Khiết có thể hái được nhiều nhất bao nhiêu cây nấm?\n\n"
        "Dữ liệu đầu vào:\n"
        " - 4 dòng, mỗi dòng gồm 4 số nguyên.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Một số nguyên duy nhất số cây nấm lớn nhất Khiết có thể hái.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ A[i][j] ≤ 10^9.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "2 2 2 1\n"
        "1 1 2 1\n"
        "1 1 2 1\n"
        "1 1 2 2\n\n"
        "Output:\n"
        "14"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_n_queens(frame):
    label_title = ctk.CTkLabel(frame, text="Bài Toán N Quân Hậu", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Đếm số lượng cách đặt n quân hậu trên bàn cờ kích cỡ n x n sao cho không có 2 quân hậu nào tấn công được nhau.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Một số nguyên n.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Một số nguyên duy nhất là số lượng cách đặt n quân hậu.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "5\n\n"
        "Output:\n"
        "10"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

###################

def content_permutations(frame):
    label_title = ctk.CTkLabel(frame, text="Bài Toán Hoán Vị", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "In ra tất cả các hoán vị của tập S = {1, 2, …, n}.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Một số nguyên n.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Tất cả các hoán vị của S, theo thứ tự từ điển.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 9.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3\n\n"
        "Output:\n"
        "1 2 3\n"
        "1 3 2\n"
        "2 1 3\n"
        "2 3 1\n"
        "3 1 2\n"
        "3 2 1"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_scheduling(frame):
    label_title = ctk.CTkLabel(frame, text="Bài Toán Lập Lịch", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Mai muốn đóng chai n lọ thuốc. Mỗi lọ thuốc mất A[i] để đổ đầy và B[i] giây để dán nhãn.\n"
        "Một lọ thuốc cần được đổ đầy trước khi dán nhãn.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Một số nguyên n.\n"
        " - n dòng tiếp theo, mỗi dòng gồm hai số nguyên A[i], Bi.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Thời gian tối thiểu để đóng chai hết n lọ thuốc.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10.\n"
        " - 1 ≤ A[i], B[i] ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "2\n"
        "1 3\n"
        "2 3\n\n"
        "Output:\n"
        "7"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

#################

def content_merge_arrays(frame):
    label_title = ctk.CTkLabel(frame, text="Gộp Mảng", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho hai mảng A, B gồm các phần tử nguyên không giảm.\n"
        "Hãy ghép chúng lại thành một mảng số nguyên không giảm.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Một số nguyên n.\n"
        " - Dòng thứ hai chứa n số nguyên A[i].\n"
        " - Dòng thứ ba chứa n số nguyên B[i].\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra n×2 số nguyên là mảng kết quả.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ A[i], B[i] ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3\n"
        "1 3 4\n"
        "1 2 3\n\n"
        "Output:\n"
        "1 1 2 3 3 4"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_sum_of_three(frame):
    label_title = ctk.CTkLabel(frame, text="Tổng Ba Giá Trị", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho mảng A gồm n số nguyên. Tìm 3 chỉ số i, j, k sao cho A[i] + A[j] + A[k] = x.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm 2 số nguyên n, x.\n"
        " - Dòng thứ hai gồm n số nguyên A[i].\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra i, j, k (nếu có nhiều kết quả, in ra bất kì).\n"
        " - Đảm bảo tồn tại ít nhất 1 kết quả.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 5000.\n"
        " - 1 ≤ A[i], x ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "4 8\n"
        "1 2 5 7\n\n"
        "Output:\n"
        "1 2 3"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_medicine_mixture_2(frame):
    label_title = ctk.CTkLabel(frame, text="Pha Thuốc 2", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Mai có n cây nấm, cây nấm thứ i nặng A[i].\n"
        "Cô muốn pha một lọ thuốc dùng một số lượng nấm bất kỳ, nhưng hai cây nấm có cân nặng chênh lệch quá k\n"
        "không thể dùng cùng một lọ thuốc. Tối đa bao nhiêu cây nấm có thể được dùng để làm một lọ thuốc?\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm hai số nguyên n, k.\n"
        " - Dòng thứ hai gồm n số nguyên A[i].\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra số lượng cây nấm nhiều nhất có thể sử dụng.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ k, A[i] ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "6 6\n"
        "1 2 5 7 9 10\n\n"
        "Output:\n"
        "4"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_largest_submatrix(frame):
    label_title = ctk.CTkLabel(frame, text="Ma Trận Con Lớn Nhất", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho ma trận nhị phân gồm n dòng và m cột. Tìm ma trận con có diện tích lớn nhất chứa tối đa k số 1.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm ba số nguyên n, m, k.\n"
        " - Dòng thứ hai gồm n số nguyên Ai.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra số lượng cặp (i, j).\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n, m ≤ 500.\n"
        " - 1 ≤ k ≤ n × m.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3 3 2\n"
        "100\n"
        "100\n"
        "001\n\n"
        "Output:\n"
        "6"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_medicine_mixture_3(frame):
    label_title = ctk.CTkLabel(frame, text="Pha Thuốc 3", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Mai có n cây nấm, cây nấm thứ i nặng A[i].\n"
        "Cô muốn pha một lọ thuốc dùng một số lượng nấm bất kỳ, nhưng hai cây nấm có cân nặng chênh lệch quá k\n"
        "không thể dùng cùng một lọ thuốc. Tối đa bao nhiêu cây nấm có thể được dùng để làm hai lọ thuốc?\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm số nguyên n.\n"
        " - Dòng thứ hai gồm n số nguyên A[i].\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra số lượng cây nấm nhiều nhất có thể sử dụng.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ k, A[i] ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "6 3\n"
        "1 2 5 7 9 10\n\n"
        "Output:\n"
        "5"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

########################

def content_knapsack_2(frame): 
    label_title = ctk.CTkLabel(frame, text="Bài Toán Cái Túi 2", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Có n món đồ, món đồ thứ i có cân nặng wi và giá trị v[i].\n"
        "Bạn có thể chọn số lượng món đồ tùy ý miễn cân nặng không quá S.\n"
        "Hãy tìm cách chọn đồ để có được giá trị lớn nhất.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm 2 số nguyên n, S.\n"
        " - Mỗi dòng trong n dòng tiếp theo gồm 2 số nguyên w[i], v[i].\n\n"
        "Dữ liệu đầu ra:\n"
        " - Một số nguyên duy nhất giá trị lớn nhất có thể đạt được.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 100,\n"
        " - S ≤ 10⁵.\n"
        " - 1 ≤ w[i], v[i] ≤ 10⁵.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3 5\n"
        "1 4\n"
        "4 1\n"
        "2 100\n\n"
        "Output:\n"
        "104"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")


def content_stairs(frame):
    label_title = ctk.CTkLabel(frame, text="Bài Toán Trèo Bậc Thang", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Lan cần phải trèo n bậc thang mới có thể đến được ngôi chùa trên ngọn núi.\n"
        "Nếu cô bước 1, 2 hoặc 3 bước mỗi lần, có bao nhiêu cách để cô có thể đến ngôi chùa?\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm số nguyên n.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra một số nguyên, modulo 10⁹ + 7 do đáp án có thể rất lớn.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "4\n\n"
        "Output:\n"
        "7"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")


def content_longest_increasing_subsequence(frame):
    label_title = ctk.CTkLabel(frame, text="Bài Toán Dãy Con Tăng Dài Nhất", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho một mảng A gồm n phần tử, tìm dãy con tăng dài nhất (LIS) của dãy A.\n"
        "Nói cách khác, tìm k lớn nhất sao cho tồn tại k chỉ số i1 < i2 < … < ik mà A[i1] < A[i2] < … < A[ik].\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm số nguyên n.\n"
        " - Dòng thứ hai gồm n số nguyên Ai.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra độ dài LIS.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 1000.\n"
        " - 1 ≤ Ai ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "5\n"
        "3 7 2 1 8\n\n"
        "Output:\n"
        "3\n"
        "Chú ý: LIS là (3, 7, 8)."),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_longest_path_2(frame):
    label_title = ctk.CTkLabel(frame, text="Đường Đi Lớn Nhất 2", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Khu rừng là một bảng n x n. Từ ô (i, j), Minh có thể đi đến ô (i + 1, j) hoặc (i, j + 1).\n"
        "Ô (i, j) có A[i][j] cây nấm. Hành trình của Minh bắt đầu từ (1, 1) và kết thúc tại (n, n).\n"
        "Số nấm tối đa anh ấy có thể thu thập được là bao nhiêu?\n\n"
        "Dữ liệu đầu vào:\n"
        " - n dòng, mỗi dòng chứa n số nguyên.\n\n"
        "Dữ liệu đầu ra:\n"
        " - Số nấm tối đa Minh có thể thu thập được.\n\n"
        "Ràng buộc:\n"
        " - 1 ≤ n ≤ 1000.\n"
        " - 1 ≤ A[i][j] ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "4\n"
        "2 2 2 1\n"
        "1 1 2 1\n"
        "1 1 2 1\n"
        "1 1 2 2\n\n"
        "Output:\n"
        "14"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_happiness(frame): 
    label_title = ctk.CTkLabel(frame, text="Niềm Vui Tối Đa", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Có n ngày. Ngày thứ i, Nam có thể ghé thăm 'hàng xóm 1' để nhận A[i] niềm vui,\n"
        "hoặc ghé thăm 'hàng xóm 2' để nhận B[i] niềm vui. Nhưng nếu Nam ghé thăm\n"
        "một người từ 3 ngày liên tiếp trở lên, người còn lại sẽ cảm thấy cô đơn.\n\n"
        "Hỏi giá trị niềm vui lớn nhất Nam có thể nhận được là bao nhiêu,\n"
        "và không được làm cho ai cô đơn?\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm số nguyên n.\n"
        " - Dòng thứ hai gồm n số nguyên A[i].\n"
        " - Dòng thứ ba gồm n số nguyên B[i].\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra giá trị niềm vui lớn nhất Marisa có thể nhận được.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ A[i], B[i] ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "4\n"
        "4 4 4 1\n"
        "1 1 1 4\n\n"
        "Output:\n"
        "13"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

################

def content_tree(frame):
    label_title = ctk.CTkLabel(frame, text="Cây", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho đồ thị gồm n đỉnh và m cạnh. Xác định xem đồ thị đã cho có phải cây không.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm số nguyên n.\n"
        " - n dòng tiếp theo, mỗi dòng gồm 2 số nguyên u, v, có cạnh nối giữa u và v.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra YES nếu đồ thị đã cho là cây, ngược lại in ra NO.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n, m ≤ 10⁵.\n"
        " - 1 ≤ u, v ≤ n.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "6 5\n"
        "1 2\n"
        "2 3\n"
        "3 4\n"
        "4 5\n"
        "5 6\n\n"
        "Output:\n"
        "YES"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_leaves(frame):
    label_title = ctk.CTkLabel(frame, text="Lá", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho một cây n đỉnh. Bạn có thể tùy ý chọn đỉnh gốc của cây,\n"
        "tìm ra số lượng lá lớn nhất có thể.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm một số nguyên n.\n"
        " - n − 1 dòng tiếp theo, mỗi dòng gồm hai số nguyên u, v,\n"
        "có cạnh nối giữa u và v.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra một số nguyên là số lượng lá lớn nhất có thể của cây.\n\n"
        "Ràng buộc:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ u, v ≤ n.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "3\n"
        "1 2\n"
        "1 3\n\n"
        "Output:\n"
        "2"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_depth(frame):
    label_title = ctk.CTkLabel(frame, text="Độ Sâu", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho một cây n đỉnh có đỉnh gốc là 1. Xác định độ sâu của mỗi đỉnh.\n"
        "Độ sâu của một đỉnh là số lượng cạnh trên đường đi từ đỉnh gốc đến nó.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm một số nguyên n.\n"
        " - n − 1 dòng tiếp theo, mỗi dòng gồm hai số nguyên u, v,\n"
        "có một cạnh giữa u và v.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra n số nguyên, số nguyên thứ i là độ sâu của đỉnh i.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ u, v ≤ n.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "5\n"
        "1 2\n"
        "1 3\n"
        "3 4\n"
        "3 5\n\n"
        "Output:\n"
        "0 1 1 2 2"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_tree_diameter(frame):
    label_title = ctk.CTkLabel(frame, text="Bài Toán Đường Kính Của Cây", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho cây gồm n đỉnh. Hãy tính đường kính của cây.\n"
        "Đường kính của cây là khoảng cách xa nhất giữa 2 đỉnh.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm số nguyên n.\n"
        " - n − 1 dòng tiếp theo, mỗi dòng gồm 2 số nguyên u, v,\n"
        "có cạnh nối giữa u và v.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra số nguyên, đường kính của cây.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ u, v ≤ n.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "6\n"
        "1 2\n"
        "2 3\n"
        "3 4\n"
        "4 5\n"
        "5 6\n\n"
        "Output:\n"
        "5"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_white_path(frame):
    label_title = ctk.CTkLabel(frame, text="Bài Toán Đường Đi Trắng", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Cho một cây n đỉnh, mỗi đỉnh được tô một trong hai màu đen trắng.\n"
        "Hãy xác định số lượng đỉnh u, mà trên đường đi từ 1 tới u,\n"
        "số lượng đỉnh màu trắng nhiều hơn số lượng đỉnh màu đen.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm một số nguyên n.\n"
        " - Dòng thứ hai gồm một xâu nhị phân độ dài n,\n"
        "thể hiện màu của các đỉnh, kí tự thứ i thể hiện màu của đỉnh i.\n"
        "1 là màu đen và 0 là màu trắng.\n"
        " - n − 1 dòng tiếp theo, mỗi dòng gồm hai số nguyên u, v,\n"
        "có cạnh nối giữa u và v.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra số lượng đỉnh thỏa mãn.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ u, v ≤ n.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "4\n"
        "0110\n"
        "1 2\n"
        "2 3\n"
        "2 4\n\n"
        "Output:\n"
        "2"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

#######################

def content_dynamic_seas(frame):
    label_title = ctk.CTkLabel(frame, text="Biển Động", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Đại dương được biểu diễn bằng ma trận A kích cỡ n×n. Có một số cơn bão, được biểu diễn bằng kí tự X. \n"
        "Các cơn bão có bán kính r. Hay nói cách khác, nếu cơn bão ở vị trí (i, j) thì các vị trí (i', j') với \n"
        "|i − i'| + |j − j'| ≤ r sẽ bị ảnh hưởng.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm 2 số nguyên n, r.\n"
        " - n dòng tiếp theo là ma trận A, mỗi dòng gồm một xâu độ dài n chỉ gồm 2 kí tự '.' và 'X'.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra số vùng không bị ảnh hưởng.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 5000.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "4 1\n"
        "..X.\n"
        "X...\n"
        "....\n"
        "..X.\n\n"
        "Output:\n"
        "4"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_ice_floats(frame):
    label_title = ctk.CTkLabel(frame, text="Băng Trôi", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Một hồ nước được biểu diễn bởi ma trận A cỡ n×m. Trong đó:\n"
        " - 'X' biểu diễn một tảng băng.\n"
        " - '.' là khu vực bình thường.\n"
        "Sau một ngày, những tảng băng kề cạnh với nước sẽ tan chảy. Từ một ô, bạn có thể đi đến được ô bất kì trong\n "
        "4 ô kề cạnh miễn nó không chứa băng.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm số nguyên n.\n"
        " - n dòng tiếp theo, mỗi dòng gồm một xâu m kí tự. Có chính xác hai kí tự 'L'.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra sau bao nhiêu ngày thì có thể đi lại giữa hai điểm 'L'.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n, m ≤ 1500.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "5 5\n"
        "L....\n"
        "XXXXX\n"
        "XXXXX\n"
        "XXXXX\n"
        "....L\n\n"
        "Output:\n"
        "2"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_power_plant(frame):
    label_title = ctk.CTkLabel(frame, text="Nhà Máy Điện", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Một đất nước có thể được biểu diễn bởi một đồ thị n đỉnh và m cạnh, mỗi đỉnh là một thành phố. Chính phủ có kế hoạch \n"
        "xây dựng k nhà máy điện. Nhà máy thứ i nằm ở thành phố Ai và có bán kính Ri (những thành phố có khoảng cách đến Ai\n "
        "không quá Ri sẽ nhận được điện từ nhà máy này).\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm 3 số nguyên n, m, k.\n"
        " - m dòng tiếp theo, mỗi dòng gồm 2 số nguyên u, v, có cạnh nối đỉnh u và v.\n"
        " - k dòng tiếp theo, mỗi dòng gồm 2 số nguyên Ai, Ri.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra số lượng thành phố có điện.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n, m, k ≤ 10⁵.\n"
        " - 1 ≤ u, v, Ai, Ri ≤ n.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "6 5 2\n"
        "1 2\n"
        "1 3\n"
        "3 4\n"
        "3 5\n"
        "2 6\n"
        "1 1\n"
        "6 2\n\n"
        "Output:\n"
        "4"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")

def content_restaurant(frame):
    label_title = ctk.CTkLabel(frame, text="Nhà Hàng", font=("Arial", 18, "bold"))
    label_title.pack(pady=5, anchor="w")

    label_description = ctk.CTkLabel(frame, text=(
        "Một đất nước có n thành phố và m con đường 2 chiều, có trọng số. Có k loại nguyên liệu, thành phố thứ i chỉ bán loại\n"
        "nguyên liệu Ai. Một đầu bếp muốn mở một nhà hàng ở thành phố nào đó. Mỗi sáng, anh cần mua đủ k loại nguyên liệu về\n"
        "nhà hàng. Chi phí vận chuyển nguyên liệu từ thành phố u về thành phố v chính là khoảng cách ngắn nhất giữa chúng.\n\n"
        "Dữ liệu đầu vào:\n"
        " - Dòng đầu tiên gồm 3 số nguyên n, m, k.\n"
        " - Dòng thứ hai gồm n số nguyên Ai.\n"
        " - m dòng tiếp theo, mỗi dòng gồm 3 số nguyên u, v, w, có đường đi dài wi nối giữa u và v.\n\n"
        "Dữ liệu đầu ra:\n"
        " - In ra thành phố tối ưu để mở nhà hàng. Nếu có nhiều thành phố tối ưu, in ra thành phố có chỉ số nhỏ nhất.\n\n"
        "Điều kiện:\n"
        " - 1 ≤ n ≤ 10⁵.\n"
        " - 1 ≤ k ≤ 50.\n"
        " - 1 ≤ Ai ≤ k.\n"
        " - 1 ≤ u, v ≤ n.\n"
        " - 1 ≤ w ≤ 10⁹.\n\n"
    ), justify="left", font=("Arial", 14))
    label_description.pack(anchor="w")

    label_input_example = ctk.CTkLabel(frame, text="Ví dụ:", font=("Arial", 16, "bold"))
    label_input_example.pack(pady=10, anchor="w")

    label_input_details = ctk.CTkLabel(frame, text=(
        "Input:\n"
        "6 9 3\n"
        "1 2 3 2 1 2\n"
        "1 2 3\n"
        "2 4 1\n"
        "4 6 3\n"
        "4 1 4\n"
        "2 5 3\n"
        "5 1 2\n"
        "2 6 3\n"
        "1 3 5\n"
        "2 3 3\n\n"
        "Output:\n"
        "2"),
        justify="left", font=("Arial", 14))
    label_input_details.pack(anchor="w")



# Dictionary to map button texts (from config.math) to content functions
content_dict = {
    config.math[0]: content_ucln,
    config.math[1]: content_birthday,
    config.math[2]: content_consecutive_sum,
    config.math[3]: content_sum_of_divisors,
    config.math[4]: content_divisible_by_3,

    config.refixsum[0]: content_prefix_sum,
    config.refixsum[1]: content_2d_prefix_sum,
    config.refixsum[2]: content_substring_ratio,

    config.sort[0]: content_sort_points,
    config.sort[1]: content_min_possible,
    config.sort[2]: content_medicine_mixture,

    config.recur[0]: content_subset_sum,
    config.recur[1]: content_knight_tour,
    config.recur[2]: content_knapsack,
    config.recur[3]: content_mushroom,
    config.recur[4]: content_n_queens,

    config.permu[0]: content_permutations,
    config.permu[1]: content_scheduling,

    config.cursor[0]: content_merge_arrays,
    config.cursor[1]: content_medicine_mixture_2,
    config.cursor[2]: content_sum_of_three,
    config.cursor[3]: content_medicine_mixture_3,
    config.cursor[4]: content_largest_submatrix,

    config.dp[0]: content_stairs,
    config.dp[1]: content_knapsack_2,
    config.dp[2]: content_longest_increasing_subsequence,
    config.dp[3]: content_longest_path_2,
    config.dp[4]: content_happiness,

    config.tree[0]: content_tree,
    config.tree[1]: content_leaves,
    config.tree[2]: content_depth,
    config.tree[3]: content_tree_diameter,
    config.tree[4]: content_white_path,

    config.search[0]: content_dynamic_seas,
    config.search[1]: content_ice_floats,
    config.search[2]: content_power_plant,
    config.search[3]: content_restaurant
}




# Function to display content based on button text
def display_content(frame, button_text):
    # Clear current content in frame
    for widget in frame.winfo_children():
        widget.destroy()
    # print(button_text)
    # Fetch and call the content function from the dictionary
    content_function = content_dict.get(button_text)
    if content_function:
        for widget in frame.winfo_children():
            widget.destroy()

        content_function(frame)  


def on_off(frame):
    global value_0
    value_0.clear()

    # Newline Settings Frame
    newline_frame = ctk.CTkFrame(frame)
    newline_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Title for settings
    newline_title = ctk.CTkLabel(newline_frame, text="Cài đặt", font=("Arial", 16, "bold"))
    newline_title.grid(row=0, column=0, pady=5, sticky="w")

    # Switch to toggle visibility
    switch = ctk.CTkSwitch(
        newline_frame, 
        text="Ẩn/Hiện nội dung",
        fg_color="red", 
        progress_color="green"
    )
    switch.grid(row=1, column=0, pady=10, sticky="w")
    value_0.append(switch)
    
def numb_array(frame):
    global value_1

    # Xóa danh sách cũ
    value_1.clear()

    # Frame Layout: Main Frame with 2 Columns
    main_frame = ctk.CTkFrame(frame)
    main_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Left Column (2 Frames)
    left_frame = ctk.CTkFrame(main_frame)
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Right Column (2 Frames)
    right_frame = ctk.CTkFrame(main_frame)
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Group: Array structure - Left Frame
    structure_frame = ctk.CTkFrame(left_frame)
    structure_frame.pack(pady=5, fill="x")

    structure_title = ctk.CTkLabel(structure_frame, text="Cấu trúc mảng", font=("Arial", 16, "bold"))
    structure_title.pack(anchor="w", pady=5)

    checkbox_texts_structure = ["Mỗi phân tử trên 1 dòng", "Không trùng nhau", "Mảng tăng dần", "Mảng giảm dần"]
    for text in checkbox_texts_structure:
        checkbox = ctk.CTkCheckBox(structure_frame, text=text)
        checkbox.pack(anchor="w", pady=5)
        value_1.append(checkbox)

    # Exclusive checkboxes for ascending/descending
    def toggle_exclusive_structure(checkbox_1, checkbox_2):
        if checkbox_1.get() == 1:
            checkbox_2.deselect()

    value_1[2].configure(command=lambda: toggle_exclusive_structure(value_1[2], value_1[3]))
    value_1[3].configure(command=lambda: toggle_exclusive_structure(value_1[3], value_1[2]))

    # Group: Array properties - Right Frame
    properties_frame = ctk.CTkFrame(right_frame)
    properties_frame.pack(pady=5, fill="x")

    properties_title = ctk.CTkLabel(properties_frame, text="Tính chất mảng", font=("Arial", 16, "bold"))
    properties_title.pack(anchor="w", pady=5)

    checkbox_texts_properties = ["Toàn số lẻ", "Toàn số chẵn", "Không có số 0", "Cấp số cộng với công sai ngẫu nhiên trong khoảng:"]
    for text in checkbox_texts_properties:
        checkbox = ctk.CTkCheckBox(properties_frame, text=text)
        checkbox.pack(anchor="w", pady=5)
        value_1.append(checkbox)

    # Exclusive checkboxes for odd/even
    def toggle_exclusive_properties(checkbox_1, checkbox_2):
        if checkbox_1.get() == 1:
            checkbox_2.deselect()

    value_1[4].configure(command=lambda: toggle_exclusive_properties(value_1[4], value_1[5]))
    value_1[5].configure(command=lambda: toggle_exclusive_properties(value_1[5], value_1[4]))

    # Group: Entry for random range - Left Frame
    entry_frame = ctk.CTkFrame(left_frame)
    entry_frame.pack(pady=5, anchor="w")

    entry_label = ctk.CTkLabel(entry_frame, text="Nhập khoảng công sai:")
    entry_label.pack(side="left", padx=5)

    entry1 = ctk.CTkEntry(entry_frame, placeholder_text="Min")
    entry1.pack(side="left", padx=5)
    value_1.append(entry1)

    entry2 = ctk.CTkEntry(entry_frame, placeholder_text="Max")
    entry2.pack(side="left", padx=5)
    value_1.append(entry2)

    # Group: Decimal number option - Right Frame
    decimal_frame = ctk.CTkFrame(right_frame)
    decimal_frame.pack(pady=5, anchor="w")

    decimal_checkbox = ctk.CTkCheckBox(decimal_frame, text="Số thực với số chữ số thập phân:")
    decimal_checkbox.pack(side="left", padx=10)
    value_1.append(decimal_checkbox)

    decimal_entry = ctk.CTkEntry(decimal_frame, placeholder_text="Số chữ số thập phân")
    decimal_entry.pack(side="left", padx=10)
    value_1.append(decimal_entry)


def rand_num(frame):
    global value_2

    def toggle_exclusive_checkboxes(checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5):
        if checkbox_1.get() == 1:
            checkbox_2.deselect()
            checkbox_3.deselect()
            checkbox_4.deselect()
            checkbox_5.deselect()

    value_2.clear()

    # Group: Decimal settings
    decimal_frame = ctk.CTkFrame(frame)
    decimal_frame.pack(pady=10, padx=10, fill="x")

    g1_1 = ctk.CTkCheckBox(decimal_frame, text="Số thực với số chữ số thập phân:")
    g1_1.pack(side="left", padx=10)
    value_2.append(g1_1)

    g1_2 = ctk.CTkEntry(decimal_frame, placeholder_text="Nhập số chữ số thập phân")
    g1_2.pack(side="left", padx=10)
    value_2.append(g1_2)

    # Group: Exclusive options
    exclusive_frame = ctk.CTkFrame(frame)
    exclusive_frame.pack(pady=10, padx=10, fill="x")

    exclusive_title = ctk.CTkLabel(exclusive_frame, text="Chọn tính chất số (chỉ chọn 1)", font=("Arial", 16, "bold"))
    exclusive_title.pack(anchor="w", pady=5)

    checkbox_texts = ["Số lẻ", "Số chẵn", "Số nguyên tố", "Số chính phương"]
    checkboxes = []

    for index, text in enumerate(checkbox_texts, start=1):
        checkbox = ctk.CTkCheckBox(exclusive_frame, text=text, height=20)
        checkbox.pack(anchor='w', pady=5)
        value_2.append(checkbox)
        checkboxes.append(checkbox)

    # Configure exclusive behavior
    value_2[0].configure(command = lambda :toggle_exclusive_checkboxes(value_2[0],value_2[2],value_2[3],value_2[4],value_2[5]))
    value_2[2].configure(command = lambda :toggle_exclusive_checkboxes(value_2[2],value_2[0],value_2[3],value_2[4],value_2[5]))
    value_2[3].configure(command = lambda :toggle_exclusive_checkboxes(value_2[3],value_2[2],value_2[0],value_2[4],value_2[5]))
    value_2[4].configure(command = lambda :toggle_exclusive_checkboxes(value_2[4],value_2[2],value_2[3],value_2[0],value_2[5]))
    value_2[5].configure(command = lambda :toggle_exclusive_checkboxes(value_2[5],value_2[2],value_2[3],value_2[4],value_2[0]))



def string(frame):
    global value_3
    value_3.clear()
    # frame.geometry("400x400") 
    # Frame: Multi-word string option
    multi_word_frame = ctk.CTkFrame(frame)
    multi_word_frame.pack(pady=5, padx=5, fill="x")

    g1_1 = ctk.CTkCheckBox(multi_word_frame, text="Tạo xâu có nhiều từ")
    g1_1.pack(anchor='w', pady=2)
    value_3.append(g1_1)

    # Frame: Settings for each word
    word_settings_frame = ctk.CTkFrame(frame)
    word_settings_frame.pack(pady=5, padx=5, fill="both", expand=True)

    word_settings_title = ctk.CTkLabel(word_settings_frame, text="Cài đặt cho từng từ", font=("Arial", 14, "bold"))
    word_settings_title.pack(anchor="w", pady=3)

    texts = ["Độ dài mỗi từ", "Số khoảng trắng ở giữa", "Số khoảng trắng ở đầu"]
    word_settings_grid = ctk.CTkFrame(word_settings_frame)
    word_settings_grid.pack(fill="x")

    for index, text in enumerate(texts, start=1):
        label = ctk.CTkLabel(word_settings_grid, text=text, anchor="w")
        label.grid(row=index, column=0, padx=5, pady=2, sticky="w")

        p1 = ctk.CTkEntry(word_settings_grid, placeholder_text="Tối thiểu", width=100)
        p1.grid(row=index, column=1, padx=5, pady=2)

        p2 = ctk.CTkEntry(word_settings_grid, placeholder_text="Tối đa", width=100)
        p2.grid(row=index, column=2, padx=5, pady=2)

        value_3.append([p1, p2])

    # Frame: Forbidden starting characters
    forbidden_frame = ctk.CTkFrame(frame)
    forbidden_frame.pack(pady=5, padx=5, fill="x")

    forbidden_title = ctk.CTkLabel(forbidden_frame, text="Cài đặt ký tự bắt đầu", font=("Arial", 14, "bold"))
    forbidden_title.pack(anchor="w", pady=3)

    forbidden_inner_frame = ctk.CTkFrame(forbidden_frame)
    forbidden_inner_frame.pack(fill="x")

    g2_1 = ctk.CTkCheckBox(forbidden_inner_frame, text="Không được bắt đầu bằng:")
    g2_1.grid(row=0, column=0, padx=5, sticky="w")

    g2_2 = ctk.CTkEntry(forbidden_inner_frame, placeholder_text="Nhập ký tự cấm", width=150)
    g2_2.grid(row=0, column=1, padx=5, sticky="w")

    value_3.append([g2_1, g2_2])

    # Frame: Additional options
    additional_frame = ctk.CTkFrame(frame)
    additional_frame.pack(pady=5, padx=5, fill="x")

    g3_1 = ctk.CTkCheckBox(additional_frame, text="Ghi liền vào nội dung trước đó")
    g3_1.pack(anchor='w', pady=2)
    value_3.append(g3_1)



def graph(frame):
    global value_4
    value_4.clear()

    # Main container frame
    main_container = ctk.CTkFrame(frame)
    main_container.pack(pady=10, padx=10, fill="both", expand=True)

    # Left and Right frames
    left_frame = ctk.CTkFrame(main_container)
    left_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    right_frame = ctk.CTkFrame(main_container)
    right_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    # Adjust weight for equal column space
    main_container.columnconfigure(0, weight=1)
    main_container.columnconfigure(1, weight=1)

    # Left Column: Basic Settings and Weight Settings
    # Group: Basic Settings
    basic_settings_frame = ctk.CTkFrame(left_frame)
    basic_settings_frame.pack(pady=10, padx=10, fill="both", expand=True)

    basic_title = ctk.CTkLabel(basic_settings_frame, text="Cài đặt cơ bản", font=("Arial", 16, "bold"))
    basic_title.grid(row=0, column=0, columnspan=2, pady=5)

    g3_2 = ctk.CTkCheckBox(basic_settings_frame, text="Đồ thị có hướng")
    g3_2.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    value_4.append(g3_2)

    g4_2 = ctk.CTkCheckBox(basic_settings_frame, text="Cho phép cạnh nối đỉnh với chính nó")
    g4_2.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    value_4.append(g4_2)

    g5_2 = ctk.CTkCheckBox(basic_settings_frame, text="Cho phép nhiều cạnh giữa 2 đỉnh")
    g5_2.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    value_4.append(g5_2)

    g6_2 = ctk.CTkCheckBox(basic_settings_frame, text="Yêu cầu đồ thị liên thông")
    g6_2.grid(row=4, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    value_4.append(g6_2)

    # Group: Weight Settings
    weight_settings_frame = ctk.CTkFrame(left_frame)
    weight_settings_frame.pack(pady=10, padx=10, fill="both", expand=True)

    weight_title = ctk.CTkLabel(weight_settings_frame, text="Cài đặt trọng số", font=("Arial", 16, "bold"))
    weight_title.grid(row=0, column=0, columnspan=2, pady=5)

    g7_2 = ctk.CTkCheckBox(weight_settings_frame, text="Đồ thị có trọng số")
    g7_2.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    value_4.append(g7_2)

    min_weight_label = ctk.CTkLabel(weight_settings_frame, text="Trọng số nhỏ nhất:")
    min_weight_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    min_weight_entry = ctk.CTkEntry(weight_settings_frame, placeholder_text="Nhập giá trị nhỏ nhất")
    min_weight_entry.grid(row=2, column=1, padx=5, pady=5)

    max_weight_label = ctk.CTkLabel(weight_settings_frame, text="Trọng số lớn nhất:")
    max_weight_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)

    max_weight_entry = ctk.CTkEntry(weight_settings_frame, placeholder_text="Nhập giá trị lớn nhất")
    max_weight_entry.grid(row=3, column=1, padx=5, pady=5)
    value_4.append([min_weight_entry,max_weight_entry])


    # Right Column: Graph Type
    graph_type_frame = ctk.CTkFrame(right_frame)
    graph_type_frame.pack(pady=10, padx=10, fill="both", expand=True)

    graph_type_title = ctk.CTkLabel(graph_type_frame, text="Loại đồ thị", font=("Arial", 16, "bold"))
    graph_type_title.grid(row=0, column=0, columnspan=2, pady=5)

    graph_type_var = ctk.StringVar(value="random")
    graph_types = [("Random", "random"), ("Tree", "tree"), ("Grid", "grid"), ("Cycle", "cycle")]

    def get_selected_graph_type():
        global temp3
        temp3 = graph_type_var.get()  # Lấy giá trị từ biến

    for i, (text, value) in enumerate(graph_types):
        rb = ctk.CTkRadioButton(graph_type_frame, text=text, variable=graph_type_var, value=value, command=get_selected_graph_type)
        rb.grid(row=i + 1, column=0, sticky="w", padx=5, pady=5)
    value_4.append(graph_type_var)




cons_dict = {
    "Số phân tử (độ dài)": on_off,
    "Mảng số (nguyên/thực)": numb_array,
    "Số ngẫu nhiên": rand_num,
    "Xâu kí tự": string,
    "Số bộ truy vấn": on_off,
    "Đồ thị": graph,
}

def dict_to_nums(name):
    if(name == "Số phân tử (độ dài)"): return value_0
    if(name == "Mảng số (nguyên/thực)"): return value_1
    if(name == "Số ngẫu nhiên"): return value_2
    if(name == "Xâu kí tự"): return value_3
    if(name == "Đồ thị"): return value_4



def cons_click(row, case): 
    global current_popup
    if current_popup is not None and current_popup.winfo_exists():
        current_popup.destroy()
    popup = ctk.CTkToplevel()
    popup.title("Ràng buộc")
    popup.transient(root)
    popup.lift()
    popup.focus_force()
    current_popup = popup
    cons_function = cons_dict.get(case)
    if cons_function:
        cons_function(popup)
    button_confirm = ctk.CTkButton(popup,text = "Xác nhận",width = 200, height = 50,font=("Arial", 20, "bold"),border_color = "white",border_width= 2, command = lambda: button_confirm_rangcuoc(popup,dict_to_nums(case),row))
    button_confirm.pack()

def button_confirm_rangcuoc(frame, value, row):
    global value_final
    value_final.clear()
    if value not in ["Kí tự", "Mảng kí tự"]:
        for v in value:
            # Nếu không phải danh sách và là số hoặc chuỗi rỗng
            if not isinstance(v, list) and (v.get() == 0 or v.get() == ""):
                value_final.append(False)
            # Nếu là danh sách (cặp giá trị min/max)
            elif isinstance(v, list):
                temp1 = v[0].get()
                temp2 = v[1].get()
                # Chuyển đổi an toàn
                temp1 = int(temp1) if isinstance(temp1, str) and temp1.isdigit() else temp1
                temp2 = int(temp2) if isinstance(temp2, str) and temp2.isdigit() else temp2
                value_final.append([temp1, temp2])
            else:
                # Chuyển đổi an toàn
                val = v.get()
                if isinstance(val, str) and val.isdigit():  # Chỉ chuyển đổi nếu là chuỗi số
                    value_final.append(int(val))
                else:
                    value_final.append(val)  # Lưu nguyên giá trị nếu không phải số

        # Tạo một bản sao của value_final trước khi gán
        Combo_list[row - 1][1] = copy.deepcopy(value_final)
    
    # print(value_final)
    frame.destroy()
