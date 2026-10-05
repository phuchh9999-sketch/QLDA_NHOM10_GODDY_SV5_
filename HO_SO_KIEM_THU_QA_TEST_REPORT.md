# BỘ HỒ SƠ KIỂM THỬ CHẤT LƯỢNG PHẦN MỀM (QA TEST REPORT)
## Dự Án: Phần Mềm Quản Lý Hóa Đơn / Công Nợ Tuyển Dụng (GODDY Recruit)
**Giảng viên hướng dẫn (GVHD):** **ThS. Nguyễn Hữu Trung**  
**Đơn vị thực hiện:** Nhóm 10 – Lớp 23DTHC3 (Khoa CNTT - HUTECH)  
**Người thực hiện:** Huỳnh Nguyễn Vĩnh Phúc (MSSV: `2380614923`)  
**Vai trò:** Tester & Database Administrator (SV5 - Nhóm 10)  
**Tiêu chuẩn kiểm thử:** IEEE 829, OWASP Security, Quy tắc kiểm soát chất lượng Pareto 80/20  
**Trạng thái kiểm thử:** ✅ **100% TEST CASES PASS (19/19 Tự động + 20 Kịch bản Nghiệp vụ)**

---

### 1. TỔNG QUAN MÔI TRƯỜNG KIỂM THỬ (TEST ENVIRONMENT)
* **Ngôn ngữ & Runtime:** Node.js (v18+ / v20+)
* **Framework:** Express REST API + Sequelize ORM v6
* **Cơ sở dữ liệu:** SQLite portable (`database.sqlite`) & PostgreSQL (`database_supabase_postgres.sql`)
* **Test Runner:** Custom Test Engine (`node tests/run_all_tests.js`) & Jest Framework
* **Tỷ lệ bao phủ mã nguồn (Code Coverage):** **88.5%** (Vượt cam kết 85%)

---

### 2. DANH MỤC 20 TEST CASES NGHIỆP VỤ & KỸ THUẬT (TEST SPECIFICATION)

| Mã TC | Phân Hệ | Mục Tiêu Kiểm Thử | Các Bước Thực Hiện | Kết Quả Kỳ Vọng | Kết Quả Thực Tế | Trạng Thái |
|:---:|:---|:---|:---|:---|:---|:---:|
| **TC-01** | CSDL & Seed | Khởi tạo CSDL SQLite & nạp dữ liệu mẫu | Chạy script seed dữ liệu mẫu | CSDL nạp đủ >= 4 doanh nghiệp FPT, VNG, Shopee | Khởi tạo 4 client, 6 job, 5 placement mẫu | ✅ PASS |
| **TC-02** | Khách hàng | Tạo mới khách hàng B2B có Net Days | Gọi API POST /api/clients kèm MST | Tạo record thành công, status Active | Client được tạo đúng thông tin | ✅ PASS |
| **TC-03** | Khách hàng | Chặn tạo trùng Mã số thuế (MST) | Nhập MST đã tồn tại trong CSDL | Báo lỗi 400 và chặn ghi đè | Hệ thống trả lỗi "MST đã tồn tại" | ✅ PASS |
| **TC-04** | Khách hàng | Chặn xóa khách hàng còn dư nợ | Gọi DELETE /api/clients/:id còn hóa đơn nợ | Từ chối xóa, báo lỗi 400 | Chặn xóa thành công, bảo toàn công nợ | ✅ PASS |
| **TC-05** | Tuyển dụng | Chốt Deal Placement thành công | Chọn Job, Candidate, nhập lương | Tạo Deal, tự tính fee theo % | Tính phí hoa hồng chuẩn toán học | ✅ PASS |
| **TC-06** | Tuyển dụng | Tự động tính hạn bảo hành 60 ngày | Nhập onboardDate | `warrantyEndDate = onboard + 60d` | Hạn bảo hành được cộng đúng 60 ngày | ✅ PASS |
| **TC-07** | Tuyển dụng | Cập nhật trạng thái ứng viên Placed | Chốt deal placement thành công | Candidate.status chuyển thành 'Placed' | Ứng viên đổi sang trạng thái Placed | ✅ PASS |
| **TC-08** | Hóa đơn | Phát hành hóa đơn VAT 8% từ Deal | Chọn Placement chưa xuất HĐ | Tạo Invoice, sinh mã INV-YYYY-XXXX | Mã hóa đơn tuần tự, không trùng lặp | ✅ PASS |
| **TC-09** | Hóa đơn | Chặn xuất nhiều hóa đơn cho 1 deal | Gọi API xuất HĐ lần 2 trên 1 Deal | Báo lỗi 400 quan hệ 1:1 | Chặn thành công, không tạo trùng | ✅ PASS |
| **TC-10** | Hóa đơn | Tự tính Due Date theo Net Days | Ngày phát hành + Client.paymentTermDays | Hạn thanh toán đúng Net 15/30/45/60 | Due Date khớp chính xác số ngày Net | ✅ PASS |
| **TC-11** | Hóa đơn | Khớp toán học Thuế GTGT 8% | `vatAmount = subtotal * 8%` | `totalAmount = subtotal + vatAmount` | Tổng tiền khớp 100%, không lệch số lẻ | ✅ PASS |
| **TC-12** | Thanh toán | Thanh toán nợ từng đợt (Partial) | Thu nợ đợt 1 < tổng tiền | `paidAmount` tăng, status thành 'Partial' | Hóa đơn chuyển trạng thái Partial | ✅ PASS |
| **TC-13** | Thanh toán | Thanh toán tất toán nợ (Paid) | Thu nốt số dư còn lại | `remainingAmount = 0`, status 'Paid' | Hóa đơn chuyển trạng thái Paid | ✅ PASS |
| **TC-14** | Thanh toán | Chặn trả thừa tiền (Overpayment) | Nhập số tiền trả > `remainingAmount` | Trả mã lỗi 400 từ chối thanh toán | Không cho phép trả vượt số nợ | ✅ PASS |
| **TC-15** | Công nợ | Phân loại 3 xô tuổi nợ Aging | So sánh ngày hiện tại với `dueDate` | Gom đúng 3 xô: 1-30, 31-60, >60 ngày | Phân loại chính xác 100% mốc ngày | ✅ PASS |
| **TC-16** | Công nợ | Gửi thông báo nhắc nợ khách hàng | Bấm nút Nhắc nợ trên từng dòng nợ | Ghi nhận thời điểm nhắc & Audit log | Gửi thành công, có log nhắc nợ | ✅ PASS |
| **TC-17** | Dashboard | Tổng hợp 4 chỉ số tài chính KPI | Gọi GET /api/dashboard/stats | Trả Đã thu, Còn nợ, Quá hạn, Placements | Số liệu khớp 100% với bảng Invoices | ✅ PASS |
| **TC-18** | Dashboard | Doanh thu 12 tháng & Top 5 Debtors | Truy vấn thống kê aggregate | Mảng 12 tháng và Top 5 đối tác nợ | Dữ liệu sẵn sàng cho Chart.js vẽ biểu đồ | ✅ PASS |
| **TC-19** | Bảo mật | Mật khẩu hash Bcrypt & RBAC | Kiểm tra User model và JWT token | Không lộ mật khẩu, phân quyền 3 role | Mật khẩu băm Bcrypt 10 rounds an toàn | ✅ PASS |
| **TC-20** | Hạn mức | Cảnh báo vượt Credit Limit (TASK-218) | Khách nợ vượt hạn mức tín dụng | Hệ thống cảnh báo nợ vượt trần cho phép | Phát hiện chính xác số tiền vượt hạn mức | ✅ PASS |

---

### 3. TỔNG KẾT KẾT QUẢ THỰC THI KIỂM THỬ (TEST SUMMARY REPORT)
* **Tổng số test cases:** 20 Test Cases
* **Số lượng Đạt (Passed):** 20/20 (100%)
* **Số lượng Thất bại (Failed):** 0
* **Thời gian thực thi trọn bộ:** ~5.4 giây
* **Đánh giá mức độ hoàn thiện:** Toàn bộ các phân hệ nghiệp vụ theo đặc tả BRD/SRS v5.0 đều hoạt động ổn định, chính xác và an toàn.

---
*Hồ sơ kiểm thử được ký xác nhận bởi QA Tester: **Huỳnh Nguyễn Vĩnh Phúc** (SV5 - Nhóm 10).*
