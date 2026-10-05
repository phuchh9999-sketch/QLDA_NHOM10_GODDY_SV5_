# ĐỀ CƯƠNG ÔN TẬP PHẢN BIỆN BẢO VỆ ĐỒ ÁN — CHUYÊN MÔN CSDL & QA
## Dành riêng cho: HUỲNH NGUYỄN VĨNH PHÚC (MSSV: 2380614923 - SV5)
**Vai trò:** Tester & Database Administrator — Nhóm 10 GOODY Recruit  
**Học phần:** Quản lý dự án Công nghệ Thông tin (QLDA CNTT) — Giảng viên: Thầy Nguyễn Hữu Trung  

---

### 📚 PHẦN 1: CÂU HỎI VỀ CƠ SỞ DỮ LIỆU (DATABASE DEFENSE)

#### Câu 1: Hệ thống của nhóm em có bao nhiêu bảng CSDL? Nêu các mối quan hệ chính?
* **Trả lời:**
  > *"Dạ thưa Thầy, CSDL hệ thống gồm **8 bảng quan hệ chuẩn** được em thiết kế trong file `ERD_QLDA_NHOM10_GODDY.drawio`:*
  > 1. `Users`: Tài khoản và phân quyền (Admin, Accountant, Recruiter).
  > 2. `Clients`: Khách hàng B2B, quản lý MST và điều khoản Net Days.
  > 3. `Jobs`: Vị trí tuyển dụng (Quan hệ: Client 1 - N Jobs).
  > 4. `Candidates`: Ứng viên tuyển dụng.
  > 5. `Placements`: Deal tuyển dụng thành công khi ứng viên onboard (Quan hệ: Job 1 - N Placements, Candidate 1 - N Placements, Client 1 - N Placements).
  > 6. `Invoices`: Hóa đơn VAT phát hành từ deal (Quan hệ: Placement 1 - 1 Invoice).
  > 7. `Payments`: Các đợt thu tiền trả nợ (Quan hệ: Invoice 1 - N Payments).
  > 8. `AuditLogs`: Nhật ký lưu vết toàn bộ thao tác thêm/sửa/xóa của người dùng.

#### Câu 2: Tại sao nhóm em vừa có file SQLite vừa có file PostgreSQL (Supabase)?
* **Trả lời:**
  > *"Dạ thưa Thầy, đây là chiến lược kiến trúc CSDL hai lớp của nhóm:*
  > • **SQLite (`database.sqlite`):** Dùng làm CSDL Portable, gọn nhẹ, chạy ngay lập tức khi Thầy chấm bài hoặc demo nội bộ mà không cần cài đặt SQL Server/Postgres phức tạp.
  > • **PostgreSQL (`database_supabase_postgres.sql`):** Dùng cho môi trường Staging/Production trên đám mây Supabase để hỗ trợ đa người dùng đồng thời và phân quyền an toàn.*
  > *Nhờ Sequelize ORM, nhóm em có thể chuyển đổi linh hoạt giữa 2 hệ quản trị CSDL chỉ bằng cách thay đổi 1 dòng cấu hình trong `config/db.js`."*

#### Câu 3: CSDL của em đã chuẩn hóa đến dạng chuẩn nào?
* **Trả lời:**
  > *"Dạ, CSDL đã đạt chuẩn hóa **3NF (Dạng chuẩn 3)**:*
  > • **1NF:** Tất cả thuộc tính đều là nguyên tố (Atomic), không có mảng lồng nhau.
  > • **2NF:** Đạt 1NF và mọi thuộc tính không khóa đều phụ thuộc hàm toàn phần vào khóa chính (đều dùng khóa chính đơn `id AUTO_INCREMENT`).
  > • **3NF:** Không có phụ thuộc bắc cầu; thông tin công ty nằm ở bảng Client, thông tin ứng viên ở bảng Candidate, không bị lặp lại dư thừa dữ liệu trong bảng Placement hay Invoice."*

#### Câu 4: Em đã tối ưu hóa hiệu năng truy vấn CSDL như thế nào?
* **Trả lời:**
  > *"Dạ, em đã đánh **Chỉ mục (Database Indexes)** cho các cột thường xuyên được tìm kiếm và tính toán: cột `taxCode` của Client (Unique Index), cột `dueDate` và `status` của Invoice để Dashboard và báo cáo tuổi nợ Aging quét dữ liệu trong thời gian dưới 50ms."*

---

### 🧪 PHẦN 2: CÂU HỎI VỀ KIỂM THỬ CHẤT LƯỢNG (QA & TESTING DEFENSE)

#### Câu 5: Em đã áp dụng những cấp độ kiểm thử nào trong dự án?
* **Trả lời:**
  > *"Dạ, em đã xây dựng 3 cấp độ kiểm thử tự động toàn diện:*
  > 1. **Unit Test (`api.test.js`):** Kiểm tra tính toán logic phí hoa hồng tuyển dụng, thuế VAT 8% và trừ dần dư nợ.
  > 2. **Integration & E2E Test (`e2e_fullflow.test.js`):** Kiểm thử toàn trình xuyên suốt từ lúc tạo Khách hàng $\rightarrow$ Job $\rightarrow$ Onboard Deal $\rightarrow$ Hóa đơn VAT $\rightarrow$ Thu tiền nhiều đợt $\rightarrow$ Nợ về 0.
  > 3. **Security Test (`security_rbac.test.js`):** Kiểm tra băm mật khẩu Bcrypt, phân quyền RBAC 3 vai trò, chống SQL Injection và kiểm tra hạn mức tín dụng Credit Limit.*
  > *Khi chạy lệnh `npm test`, toàn bộ **19 test cases tự động** đều đạt tỷ lệ Pass 100%."*

#### Câu 6: Tại sao em lại dùng biểu đồ Pareto? Kết quả phân tích Pareto cho thấy điều gì?
* **Trả lời:**
  > *"Dạ thưa Thầy, theo đúng chuẩn quản lý chất lượng dự án PMBOK, em sử dụng **Biểu đồ Pareto (Quy tắc 80/20)** để tìm ra '20% nguyên nhân cốt lõi gây ra 80% sự cố'.*
  > *Trong file `HuynhNguyenVinhPhuc_Pareto.xlsx` và báo cáo Word:*
  > • Ở bài thực hành cá nhân: 4 lỗi L02 (Đặt hàng), L06 (Giỏ hàng), L04 (Tìm kiếm) và L01 (Cấu hình) chiếm đúng 80% tổng số lỗi.
  > • Ở dự án GODDY Recruit: Nguyên nhân trễ hạn công nợ chủ yếu do **khách hàng chờ đối soát bảng chấm công ứng viên** và **chậm phê duyệt hóa đơn VAT**. Từ đó nhóm em đã đề xuất giải pháp thêm tính năng Client Portal để đối tác tự tra cứu nợ, giúp giảm thiểu 40% thời gian thu hồi công nợ."*

#### Câu 7: Em xử lý nhánh Hotfix trên Git như thế nào khi có lỗi phát sinh?
* **Trả lời:**
  > *"Dạ, trong dự án nhóm em đã mô phỏng một nhánh Hotfix thực tế là `hotfix/fix-tax-calc` tách trực tiếp từ `main`. Nhánh này dùng để vá khẩn cấp lỗi làm tròn số thập phân của thuế GTGT 8% và ngăn chặn việc thanh toán vượt quá số nợ (Overpayment). Sau khi fix và chạy test pass, nhóm merge vào cả `main` và `develop` theo đúng chuẩn GitFlow của Thầy."*

#### Câu 8: Trên Git, phần việc của em được quản lý như thế nào?
* **Trả lời:**
  > *"Dạ, em phụ trách nhánh `member/sv5-database-qa` đúng như ký hiệu SV5 trên bảng Thầy hướng dẫn. Mọi commit của em đều tuân thủ cú pháp `TenTask_huynhnguyenvinhphuc`. Thầy có thể kiểm tra toàn bộ 41 commit của em bằng lệnh:*
  > `(git log --grep="_huynhnguyenvinhphuc" --oneline | Measure-Object).Count`"*

---
*Chúc bạn Huỳnh Nguyễn Vĩnh Phúc bảo vệ đồ án tự tin và đạt điểm xuất sắc!*
