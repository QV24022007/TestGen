# TestGen - Hướng Dẫn Sử Dụng  

## **Giới Thiệu**  
**TestGen** là phần mềm hỗ trợ sinh test case cho các bài toán lập trình. Với giao diện trực quan và tính năng đa dạng, TestGen cho phép bạn tùy chỉnh chi tiết các đối tượng và cấu hình sinh, đồng thời hỗ trợ kiểm tra lỗi trong quá trình sinh test.

---

## **Tính Năng Chính**  

1. Sinh Test Đa Dạng  
   - Hỗ trợ các đối tượng như mảng số, số ngẫu nhiên, chuỗi ký tự, đồ thị, bộ truy vấn.  
   - Cấu hình ràng buộc chi tiết và kiểm soát toàn diện quá trình sinh.  

2. Cấu Hình Sinh Test  
   - Xác định file code xử lý để sinh output.  
   - Chọn ngôn ngữ lập trình cho file code.  
   - Lựa chọn template (Themis, Word, Folder).  
   - Thiết lập số lượng test, tên file, và vị trí sinh file.  

3. Thư Viện Bài Mẫu 
   - Cung cấp bài toán mẫu ở nhiều cấp độ với đa dạng thuật toán.  

---

## **Sinh Test**  

### 1. Thiết Lập Đối Tượng và Ràng Buộc  

| **Đối Tượng Cần Tạo**            | **Ràng Buộc Đặc Biệt**                                                                                                                                                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Số phần tử (độ dài)**          | Ẩn/Hiện                                                                                                                                                                 |
| **Mảng số (nguyên/thực)**        | - **Cấu trúc mảng:** Không trùng nhau, Mảng tăng dần, Mảng giảm dần  <br> - **Tính chất mảng:** Toàn số lẻ, Toàn số chẵn, Không có số 0, Cấp số cộng, Số thực với chữ số thập phân |
| **Số ngẫu nhiên**                | Số thập phân, Số lẻ, Số chẵn, Số nguyên tố, Số chính phương                                                                                                             |
| **Xâu ký tự**                    | Độ dài xâu, Số lượng khoảng trắng giữa các từ, Ký tự không được bắt đầu                                                                                                 |
| **Ký tự**                        | Định nghĩa bộ ký tự: chữ cái, số, ký tự đặc biệt                                                                                                                         |
| **Mảng ký tự**                   | Cấu trúc mảng tương tự mảng số (không trùng, tăng dần, giảm dần)                                                                                                        |
| **Đồ thị**                       | - **Cài đặt cơ bản:** Đồ thị có hướng, Cho phép tự vòng, Cho phép nhiều cạnh <br> - **Yêu cầu:** Liên thông <br> - **Cài đặt trọng số:** Trọng số tối thiểu/tối đa      |
| **Số bộ truy vấn**               | Ẩn/Hiện                                                                                                                                                                 |
| **Bắt đầu và kết thúc truy vấn** | Giá trị bắt đầu và kết thúc được tùy chỉnh                                                                                                                              |

#### **Phụ: Đối Tượng Yêu Cầu Độ Dài**  
Các đối tượng yêu cầu độ dài bao gồm:  
- **Mảng số**, **Mảng ký tự**, **Xâu ký tự**, và **Đồ thị (số đỉnh)**  

Khi bạn chọn một trong các đối tượng này, sẽ xuất hiện một **OptionMenu (menu chọn)** để liên kết "Số phần tử (độ dài)" với đối tượng.  

- **Cách Hoạt Động:**  
  - Danh sách trong **OptionMenu** sẽ hiển thị tất cả các "Số phần tử (độ dài)" đã được thiết lập phía trên.  
  - Mỗi "Số phần tử (độ dài)" sẽ được đánh số thứ tự (1, 2, 3, ...) dựa trên thứ tự mà bạn đã thêm vào.  
  - Bạn chỉ cần chọn số thứ tự phù hợp để gán "Số phần tử (độ dài)" cho đối tượng yêu cầu độ dài.  

![Hình ảnh minh họa](https://i.imgur.com/nJNjBVy.png)
> Hình ảnh thực tiễn .


Ví dụ:  
- Bạn có ba "Số phần tử (độ dài)" đã được thiết lập trước:  
  - **Số phần tử 1:** 10  
  - **Số phần tử 2:** 20  
  - **Số phần tử 3:** 30  
- Khi thiết lập cho "Mảng số," bạn chọn "Số phần tử 2" trong **OptionMenu** để gán độ dài là 20 cho mảng này.

**Lưu ý:** Việc sử dụng **OptionMenu** giúp tránh nhầm lẫn và đồng bộ hóa cấu hình giữa các đối tượng.

---

### **2. Cấu Hình Test Case**  

Trước khi sinh test, bạn cần cấu hình các thông số:  

- **File Code Sinh Output:**  
  - Nhập địa chỉ của file code (file code xử lý) nếu bạn muốn sinh output song song với input.  
  - Nếu không nhập, chương trình chỉ sinh file input.  

- **Ngôn Ngữ File Code:**  
  - Chọn ngôn ngữ lập trình của file code (C++, Python, Java, v.v.).  

- **Template Sinh:**  
  - Themis: Dùng cho các bài chấm tự động.  
  - Word: Xuất test case dưới dạng docx, trong file docx sẽ tạo ra table chia ra hai bên, một bên là input và bên còn lại là output.  
  - Folder: Lưu các file test trong thư mục cụ thể.  

- **Vị Trí File Sinh:**  
  - Chọn thư mục nơi các file test sẽ được lưu.  

- **Số Lượng Test:**  
  - Nhập số lượng test case muốn sinh.  

- **Tên File Tổng Thể:**  
  - Tên chung cho các file. Ví dụ, nếu tên là `name`, các file sinh ra sẽ là:  
    - Input: `name1.INP`, `name2.INP`, …  
    - Output (nếu có): `name1.OUT`, `name2.OUT`, …  
  - Thư mục chứa file sẽ được đặt tên là `name`.  

**Lưu ý:**  
- File input mặc định có đuôi `.INP`.  
- File output mặc định có đuôi `.OUT`.  

### **3. Log Kiểm Tra Lỗi**  
- Kế bên UI sinh test sẽ có hộp thoại log.  
- Log hiển thị các bước thực hiện và thông báo lỗi (nếu có).  
- Nếu quá trình sinh gặp lỗi (ví dụ lỗi biên dịch file code), log sẽ thông báo ngay để người dùng xử lý.

---

## **Thông Tin Về Tác Giả và Phần Mềm**  

### **Thông Tin Cá Nhân** 
- Họ và tên: Lương Gia Bửu
- Thông tin liên lạc: [Facebook](https://www.facebook.com/profile.php?id=100014067391747)
- Chức danh hoặc vai trò: UI/UX Designer, Frontend Developer

### **Thông Tin Cá Nhân**  
- Họ và tên: Trần Thái Quốc Việt 
- Thông tin liên lạc: [Facebook](https://www.facebook.com/viet.tran.482153)
- Chức danh hoặc vai trò: Frontend Developer, Backend Developer

### **Thông Tin Về Phần Mềm**
- Ý tưởng: TestGen được phát triển để hỗ trợ lập trình viên trong việc tự động sinh test case cho các bài toán lập trình, từ đó giúp tiết kiệm thời gian và nâng cao hiệu quả làm việc.  
- Mục tiêu: Mang lại công cụ đơn giản nhưng mạnh mẽ để tạo ra các test case phù hợp với từng loại bài toán và yêu cầu, giúp các lập trình viên chuẩn bị bài kiểm tra hoặc thuật toán dễ dàng hơn.

### **Lịch Sử và Kinh Nghiệm**  
- Kinh nghiệm lập trình: 2 năm học tập trong lĩnh vực lập trình python.  
- Dự án trước đây: Tham gia phát triển một ứng dụng dạng Quizz với ngôn ngữ C++ cùng thư viện Window Form.  

### **Động Lực và Tầm Nhìn**  
- Lý do phát triển phần mềm: Quá trình phát triển phần **mềm** này bắt nguồn từ nhu cầu tự động hóa việc tạo test case cho các giáo viên, học sinh, sinh viên và những người học tập về toán rời rạc, các bài lập trình thi đấu hay giảng dạy về các bài tập trong lĩnh vực lập trình thi đấu. Mục tiêu là tiết kiệm thời gian cho họ, giúp họ tập trung vào việc giải quyết bài toán thay vì phải tốn thời gian chuẩn bị dữ liệu test case cho các bài toán lập trình thi đấu hay các bài toán liên quan đến tư duy logic. Ngoài ra, phần mềm này còn được thiết kế để đảm bảo hiệu năng cao: chạy nhanh, không yêu cầu kết nối wifi, nhẹ và không cần thiết bị quá đắt đỏ, giúp người dùng có thể sử dụng trên nhiều loại máy tính với cấu hình không quá cao.
- Tầm nhìn: TestGen hướng đến trở thành một công cụ phổ biến giúp các lập trình viên trên toàn thế giới dễ dàng tạo test case cho các bài toán lập trình, từ đó cải thiện hiệu quả làm việc và chất lượng sản phẩm phần mềm.

### **Thông Tin Liên Hệ**  
- Email: apptestgenreport@gmail.com

### **Lời Cảm Ơn và Lời Nhắn**  
- Lời cảm ơn: Cảm ơn mọi người đã đồng hành cùng tôi trong suốt quá trình phát triển phần mềm này. Cảm ơn cộng đồng lập trình viên đã cung cấp nhiều tài nguyên quý giá giúp tôi hoàn thiện sản phẩm.  
- Lời nhắn: "Hy vọng TestGen sẽ là công cụ hữu ích cho bạn trong việc tạo test case và giải quyết các vấn đề lập trình!"  

### **Bản Quyền**  
- Tuyên bố bản quyền: Phần mềm được phát triển bởi Lương Gia Bửu và Trần Thái Quốc Việt.  
- Ngày phát hành: 01/12/2024  
