# QLDA_NHOM10_GODDY - PHẦN MỀM QUẢN LÝ HÓA ĐƠN / CÔNG NỢ TÍCH HỢP DASHBOARD DỮ LIỆU CHO TUYỂN DỤNG (GODDY RECRUIT)

> Phần mềm giúp các công ty dịch vụ tuyển dụng nhân sự (Headhunt) tự động hóa quy trình chốt hợp đồng tuyển dụng (Deal Placement) ➔ Phát hành hóa đơn VAT 8% ➔ Theo dõi & thu hồi công nợ B2B theo Net Days ➔ Phân tích tài chính qua biểu đồ Dashboard & Báo cáo tuổi nợ Aging Report.

---

## 🎓 THÔNG TIN HỌC PHẦN & DỰ ÁN
* **Học phần:** Quản lý dự án Công nghệ Thông tin (IT Project Management)
* **Trường / Khoa:** Trường Đại học Công nghệ TP.HCM (HUTECH) – Khoa Công nghệ Thông tin
* **Giảng viên hướng dẫn (GVHD):** **ThS. Nguyễn Hữu Trung**
* **Đơn vị thực hiện:** Nhóm 10 – Lớp 23DTHC3
* **Thời gian thực hiện:** 14/09/2026 – 26/10/2026 (7 Tuần / 4 Sprints)
* **Ngân sách cơ sở:** 45.000.000 VNĐ | **Dự phòng rủi ro 10%:** 4.500.000 VNĐ
* **Kho mã nguồn nhóm:** [https://github.com/phuchh9999-sketch/QLDA_NHOM10_GODDY](https://github.com/phuchh9999-sketch/QLDA_NHOM10_GODDY)
* **Kho mã nguồn cá nhân SV5:** [https://github.com/phuchh9999-sketch/QLDA_NHOM10_GODDY_SV5_](https://github.com/phuchh9999-sketch/QLDA_NHOM10_GODDY_SV5_)

---

## 👥 THÀNH VIÊN DỰ ÁN (NHÓM 10)
| STT | Họ và Tên | MSSV | Vai Trò Dự Án | Nhiệm Vụ Trọng Tâm | Nhánh Git |
|:---:|:---|:---:|:---|:---|:---|
| 1 | **Nguyễn Hữu Phúc** | `2380601740` | **Trưởng nhóm / PM** | Quản lý tiến độ Scrum, chi phí, rủi ro, phân rã WBS & nghiệm thu | `member/sv1-pm` |
| 2 | **Nguyễn Xuân Đoàn** | `2380600510` | **Phân tích / BA** | Khảo sát quy trình, viết BRD/SRS, Use Cases, User Stories | `member/sv2-ba` |
| 3 | **Phạm Văn Sơn** | `2380601922` | **Backend Dev (BE)** | Phát triển RESTful API Node.js/Express, JWT, nghiệp vụ hóa đơn | `member/sv3-backend` |
| 4 | **Nguyễn Hoàng Phước** | `2380601770` | **Frontend Dev (FE)** | Xây dựng UI Responsive, tích hợp Chart.js Dashboard, UX/UI | `member/sv4-frontend` |
| 5 | **Huỳnh Nguyễn Vĩnh Phúc** | `2380614923` | **DBA & QA/Tester** | Thiết kế ERD 8 bảng, tối ưu Index, kiểm thử tự động Jest/Supertest | `member/sv5-database-qa` |

---

## 🚀 CÁC TÍNH NĂNG CỐT LÕI (8 MODULES)
1. **Module 1: CSDL & Kiến Trúc Dự Án**: CSDL SQLite zero-config, Sequelize ORM với 8 bảng quan hệ chặt chẽ (Users, Clients, Jobs, Candidates, Placements, Invoices, Payments, AuditLogs).
2. **Module 2: Xác Thực & Phân Quyền (RBAC)**: Bảo mật JWT, mã hóa bcrypt độ muối 10 rounds, phân quyền Admin, Kế toán (Accountant), Tuyển dụng (Recruiter).
3. **Module 3: Khách Hàng Doanh Nghiệp B2B**: Quản lý hồ sơ công ty, mã số thuế, kiểm soát hạn mức tín dụng (Credit Limit) và điều khoản Net Days (15/30/45/60 ngày).
4. **Module 4: Tuyển Dụng & Deal Placement**: Ghi nhận ứng viên onboard, tự động tính hoa hồng (% lương năm), theo dõi bảo hành 60 ngày.
5. **Module 5: Hóa Đơn & Invoicing**: Phát hành hóa đơn VAT 8%, mã số tự động, hạn thanh toán Net Days, in/xuất PDF chuẩn hóa đơn.
6. **Module 6: Công Nợ & Báo Cáo Tuổi Nợ (Aging Report)**: Phân loại tuổi nợ chuẩn kế toán (1-30, 31-60, >60 ngày nợ khó đòi), ghi nhận thu tiền trả nợ trừ dần.
7. **Module 7: Dashboard Thống Kê**: Thẻ KPI doanh thu, nợ AR, nợ quá hạn, tỷ lệ thu hồi, biểu đồ đường doanh thu 12 tháng, biểu đồ tròn cơ cấu ngành.
8. **Module 8: Audit Log & Kiểm Thử Tự Động**: Lưu vết toàn bộ hành động người dùng, bộ test tự động kiểm thử 100% API.

---

## 🛠️ HƯỚNG DẪN CÀI ĐẶT & CHẠY DỰ ÁN

### 1. Cài đặt các gói phụ thuộc (Dependencies):
```bash
npm install
```

### 2. Khởi tạo cơ sở dữ liệu mẫu:
```bash
node scripts/seed_enterprise_data.js
node scripts/seed_invoices_data.js
```

### 3. Khởi chạy ứng dụng Web:
```bash
npm start
```
Truy cập giao diện Web ứng dụng tại: **`http://localhost:3000`**

### 4. Chạy toàn bộ bộ kiểm thử tự động (Unit, Integration & Acceptance Tests):
```bash
npm test
```

---

## 📊 BẢNG ÁNH XẠ TIẾN ĐỘ 41 TASK CỦA HUỲNH NGUYỄN VĨNH PHÚC (SV5 - DBA & QA)

| STT | Mã Task | Tuần / Sprint | Tên Công Việc Chi Tiết | Quy Ước Commit Git SV5 | Deliverables / Tập Tin Bàn Giao | Trạng Thái |
|:---:|:---:|:---:|:---|:---|:---|:---:|
| 1 | `TASK-025` | Tuần 1 (S1) | Thiết kế Sơ đồ quan hệ thực thể ERD 8 bảng dữ liệu quan hệ | `ThietKeSoDoQuanHeERD_huynhnguyenvinhphuc` | `ERD_QLDA_NHOM10_GODDY.drawio` | ✅ PASS |
| 2 | `TASK-026` | Tuần 1 (S1) | Viết script DDL database_supabase_postgres.sql và database_sqlserver.sql | `VietScriptDDLPostgresSqlserver_huynhnguyenvinhphuc` | `database_supabase_postgres.sql`, `database_sqlserver.sql` | ✅ PASS |
| 3 | `TASK-027` | Tuần 1 (S1) | Xây dựng Model User (username, email, password, role, isActive) | `ThietKeModelUser_huynhnguyenvinhphuc` | `models/User.js` | ✅ PASS |
| 4 | `TASK-028` | Tuần 1 (S1) | Xây dựng Model Client (companyName, taxCode, netDays, contactPerson) | `ThietKeModelClient_huynhnguyenvinhphuc` | `models/Client.js` | ✅ PASS |
| 5 | `TASK-029` | Tuần 1 (S1) | Viết script tự động nạp dữ liệu mẫu seed data doanh nghiệp công nghệ | `VietScriptNapDuLieuMauEnterprise_huynhnguyenvinhphuc` | `scripts/seed_enterprise_data.js` | ✅ PASS |
| 6 | `TASK-030` | Tuần 1 (S1) | Cài đặt framework kiểm thử Jest/Supertest và viết test kết nối CSDL | `CaiDatTestingJestKiemTraDB_huynhnguyenvinhphuc` | `tests/unit.test.js` | ✅ PASS |
| 7 | `TASK-057` | Tuần 2 (S1) | Xây dựng Model Job và Model Candidate với ràng buộc khóa ngoại ClientId | `ThietKeModelJobVaCandidate_huynhnguyenvinhphuc` | `models/Job.js`, `models/Candidate.js` | ✅ PASS |
| 8 | `TASK-058` | Tuần 2 (S1) | Xây dựng Model Placement ghi nhận thỏa thuận tuyển dụng và quan hệ | `ThietKeModelPlacement_huynhnguyenvinhphuc` | `models/Placement.js` | ✅ PASS |
| 9 | `TASK-059` | Tuần 2 (S1) | Viết bộ kiểm thử tự động xác thực Đăng nhập/Đăng ký và cấp Token JWT | `BoKiemThuTuDong_AuthJWT_huynhnguyenvinhphuc` | `tests/auth_jwt.test.js` | ✅ PASS |
| 10 | `TASK-060` | Tuần 2 (S1) | Viết bộ kiểm thử tự động Thêm khách hàng, chặn trùng MST và xóa an toàn | `BoKiemThuTuDong_ThemKhachHang_huynhnguyenvinhphuc` | `tests/client_validation.test.js` | ✅ PASS |
| 11 | `TASK-061` | Tuần 2 (S1) | Viết bộ kiểm thử tự động Chốt Deal Placement và tính ngày hết hạn bảo hành | `BoKiemThuTuDong_ChotDealPlacement_huynhnguyenvinhphuc` | `tests/placement_deal.test.js` | ✅ PASS |
| 12 | `TASK-062` | Tuần 2 (S1) | Đo lường độ bao phủ kiểm thử Code Coverage Sprint 1 đạt trên 80% | `DoLuongCodeCoverageSprint1_huynhnguyenvinhphuc` | `docs/BAO_CAO_COVERAGE_SPRINT1.md`, `tests/coverage_sprint1_report.js` | ✅ PASS |
| 13 | `TASK-089` | Tuần 3 (S2) | Xây dựng Model Invoice (invoiceNo, totalAmount, paidAmount, remainingAmount) | `ThietKeModelInvoice_huynhnguyenvinhphuc` | `models/Invoice.js` | ✅ PASS |
| 14 | `TASK-090` | Tuần 3 (S2) | Cấu hình quan hệ Placement 1 - 1 Invoice trong Sequelize ORM | `ThietLapQuanHePlacementVaInvoice_huynhnguyenvinhphuc` | `tests/placement_invoice_relation.test.js` | ✅ PASS |
| 15 | `TASK-091` | Tuần 3 (S2) | Viết bộ kiểm thử tự động Tính thuế VAT 8% và Tổng tiền hóa đơn | `BoKiemThuTuDong_PhatHanhHoaDon_huynhnguyenvinhphuc` | `tests/vat_calculation.test.js` | ✅ PASS |
| 16 | `TASK-092` | Tuần 3 (S2) | Viết bộ kiểm thử tự động Chặn phát hành trùng hóa đơn trên cùng 1 deal | `BoKiemThuTuDong_ChanTrungHoaDon_huynhnguyenvinhphuc` | `tests/duplicate_invoice_prevention.test.js` | ✅ PASS |
| 17 | `TASK-093` | Tuần 3 (S2) | Cập nhật seed data mẫu với các hóa đơn thực tế phát hành cho FPT, VNG | `CapNhatSeedDataHoaDonMau_huynhnguyenvinhphuc` | `scripts/seed_invoices_data.js` | ✅ PASS |
| 18 | `TASK-094` | Tuần 3 (S2) | Kiểm tra tính toàn vẹn dữ liệu giữa Placement.fee và Invoice.subtotal | `KiemTraToanVenDuLieuFeeVaSubtotal_huynhnguyenvinhphuc` | `tests/reconciliation_fee_subtotal.test.js` | ✅ PASS |
| 19 | `TASK-121` | Tuần 4 (S2) | Xây dựng Model Payment (amount, paymentDate, paymentMethod, referenceNo) | `ThietKeModelPayment_huynhnguyenvinhphuc` | `models/Payment.js` | ✅ PASS |
| 20 | `TASK-122` | Tuần 4 (S2) | Cấu hình quan hệ Invoice 1 - N Payment trong Sequelize ORM | `ThietLapQuanHeInvoiceVaPayment_huynhnguyenvinhphuc` | `tests/invoice_payment_relation.test.js` | ✅ PASS |
| 21 | `TASK-123` | Tuần 4 (S2) | Viết bộ kiểm thử tự động Thanh toán trừ dần nợ và chống trả vượt quá số nợ | `BoKiemThuTuDong_ThanhToanTruNo_huynhnguyenvinhphuc` | `tests/debt_reduction_payment.test.js` | ✅ PASS |
| 22 | `TASK-124` | Tuần 4 (S2) | Viết bộ kiểm thử tự động Thuật toán phân loại Tuổi nợ Aging chính xác | `BoKiemThuTuDong_PhanTichTuoiNo_huynhnguyenvinhphuc` | `tests/aging_analysis.test.js` | ✅ PASS |
| 23 | `TASK-125` | Tuần 4 (S2) | Tạo chỉ mục Database Indexes tối ưu tốc độ truy vấn cho dueDate và status | `TaoIndexToiUuTruyVanDueDate_huynhnguyenvinhphuc` | `scripts/migrate_optimize_indexes.js` | ✅ PASS |
| 24 | `TASK-126` | Tuần 4 (S2) | Lập báo cáo kiểm thử Acceptance Criteria Sprint 2 gửi Trưởng nhóm PM | `BaoCaoKiemThuSprint2_huynhnguyenvinhphuc` | `docs/BAO_CAO_KIEM_THU_QA_SPRINT2.md`, `tests/sprint2_acceptance.test.js` | ✅ PASS |
| 25 | `TASK-153` | Tuần 5 (S3) | Viết bộ kiểm thử tự động kiểm tra tính toán số liệu thống kê Dashboard | `BoKiemThuTuDong_DashboardStats_huynhnguyenvinhphuc` | `tests/dashboard_stats.test.js` | ✅ PASS |
| 26 | `TASK-154` | Tuần 5 (S3) | Kiểm thử đối soát mảng doanh thu 12 tháng khớp 100% các bản ghi Payment | `KiemThuDoiSoatDoanhThu12Thang_huynhnguyenvinhphuc` | `tests/reconciliation_revenue_12months.test.js` | ✅ PASS |
| 27 | `TASK-155` | Tuần 5 (S3) | Kiểm thử đối chiếu danh sách Top 5 Debtors khớp với hóa đơn quá hạn | `KiemThuTop5DebtorsKhopHoaDon_huynhnguyenvinhphuc` | `tests/top5_debtors.test.js` | ✅ PASS |
| 28 | `TASK-156` | Tuần 5 (S3) | Đo lường thời gian phản hồi API Dashboard đảm bảo tải dưới 500ms | `DoLuongThoiGianPhanHoiDashboard_huynhnguyenvinhphuc` | `tests/dashboard_performance.test.js` | ✅ PASS |
| 29 | `TASK-157` | Tuần 5 (S3) | Tổng hợp Báo cáo kiểm thử Sprint 3 bàn giao cho Trưởng nhóm | `TongHopBaoCaoKiemThuSprint3_huynhnguyenvinhphuc` | `docs/BAO_CAO_KIEM_THU_QA_SPRINT3.md` | ✅ PASS |
| 30 | `TASK-184` | Tuần 6 (S4) | Viết bộ kiểm thử tự động Ghi nhật ký thao tác Audit Log đầy đủ trường thông tin | `BoKiemThuTuDong_AuditLog_huynhnguyenvinhphuc` | `tests/audit_log_verification.test.js` | ✅ PASS |
| 31 | `TASK-185` | Tuần 6 (S4) | Xây dựng kịch bản kiểm thử tự động toàn trình End-to-End từ Deal đến Thu nợ | `KiemThuTuDongToanTrinhE2E_huynhnguyenvinhphuc` | `tests/e2e_fullflow.test.js` | ✅ PASS |
| 32 | `TASK-186` | Tuần 6 (S4) | Kiểm thử bảo mật API: Không lộ mật khẩu hash, kiểm tra quyền RBAC | `KiemThuBaoMatAPI_RBAC_huynhnguyenvinhphuc` | `tests/security_rbac.test.js` | ✅ Sẵn sàng |
| 33 | `TASK-187` | Tuần 6 (S4) | Thực hiện phân tích Pareto nguyên nhân trễ hạn công nợ và rủi ro phần mềm | `PhanTichParetoRuiRoVaNguyenNhanNo_huynhnguyenvinhphuc` | `HuynhNguyenVinhPhuc_Pareto.xlsx`, `public/pareto.html` | ✅ Sẵn sàng |
| 34 | `TASK-188` | Tuần 6 (S4) | Thiết lập script sao lưu và phục hồi CSDL tự động (Backup & Restore script) | `ThietLapScriptBackupRestoreDB_huynhnguyenvinhphuc` | `scripts/backup_restore.js` | ✅ Sẵn sàng |
| 35 | `TASK-189` | Tuần 6 (S4) | Cấu hình lệnh npm test chạy toàn bộ test suite và đo Code Coverage | `CauHinhLenhNpmTestToanBo_huynhnguyenvinhphuc` | `package.json`, `tests/run_all_tests.js` | ✅ Sẵn sàng |
| 36 | `TASK-218` | Tuần 6 (S4) | Xây dựng kịch bản kiểm thử tính năng cảnh báo vượt hạn mức tín dụng | `KiemThuCanhBaoVuotHanMucNo_huynhnguyenvinhphuc` | `tests/credit_limit_guard.test.js` | ✅ Sẵn sàng |
| 37 | `TASK-208` | Tuần 7 (S4) | Chạy lần cuối toàn bộ test suite npm test đảm bảo 100% test pass | `ChayFinalTestSuiteNpmTest_huynhnguyenvinhphuc` | `tests/run_all_tests.js` | ✅ Sẵn sàng |
| 38 | `TASK-209` | Tuần 7 (S4) | Kiểm tra tính toàn vẹn dữ liệu CSDL sau các kịch bản demo kiểm thử | `KiemTraToanVenCSDLSauDemo_huynhnguyenvinhphuc` | `scripts/check_db_integrity.js` | ✅ Sẵn sàng |
| 39 | `TASK-210` | Tuần 7 (S4) | Hoàn thiện bảng phân tích Pareto kiểm soát chất lượng đồ án | `HoanThienBangPhanTichParetoDocx_huynhnguyenvinhphuc` | `BAO_CAO_PHAN_TICH_PARETO_HUYNHNGUYENVINHPHUC.docx` | ✅ Sẵn sàng |
| 40 | `TASK-211` | Tuần 7 (S4) | Đóng gói toàn bộ tài liệu Test Case, Test Log và Test Summary Report | `DongGoiBoTaiLieuKiemThuQA_huynhnguyenvinhphuc` | `HO_SO_KIEM_THU_QA_TEST_REPORT.md` | ✅ Sẵn sàng |
| 41 | `TASK-212` | Tuần 7 (S4) | Hỗ trợ trả lời các câu hỏi về CSDL và quy trình đảm bảo chất lượng QA | `TraLoiCauHoiCSDLVaQA_huynhnguyenvinhphuc` | `DE_CUONG_ON_TAP_BAO_VE_CSDL_QA.md` | ✅ Sẵn sàng |

---

## 🗄️ CẤU TRÚC THƯ MỤC PHÂN HỆ CSDL & KIỂM THỬ

```text
├── database_sqlserver.sql                 # Script DDL SQL Server (TASK-026)
├── database_supabase_postgres.sql         # Script DDL PostgreSQL Supabase (TASK-026)
├── ERD_QLDA_NHOM10_GODDY.drawio           # Sơ đồ ERD 8 thực thể quan hệ (TASK-025)
├── README.md                              # Tài liệu tổng quan dự án & tiến độ SV5
├── config/
│   └── db.js                              # Kết nối Sequelize SQLite / Postgres
├── docs/
│   ├── BAO_CAO_COVERAGE_SPRINT1.md        # Báo cáo Code Coverage Sprint 1 (TASK-062)
│   ├── BAO_CAO_KIEM_THU_QA_SPRINT2.md     # Báo cáo Nghiệm thu Sprint 2 (TASK-126)
│   └── BAO_CAO_KIEM_THU_QA_SPRINT3.md     # Báo cáo Nghiệm thu Sprint 3 (TASK-157)
├── models/
│   ├── Candidate.js                       # Model Ứng viên (TASK-057)
│   ├── Client.js                          # Model Khách hàng B2B (TASK-028)
│   ├── Invoice.js                         # Model Hóa đơn VAT 8% (TASK-089)
│   ├── Job.js                             # Model Vị trí tuyển dụng (TASK-057)
│   ├── Payment.js                         # Model Thanh toán công nợ (TASK-121)
│   ├── Placement.js                       # Model Deal Onboard (TASK-058)
│   └── User.js                            # Model Người dùng & Phân quyền (TASK-027)
├── scripts/
│   ├── backup_restore.js                  # Script sao lưu & phục hồi CSDL (TASK-188)
│   ├── check_db_integrity.js              # Kiểm tra toàn vẹn CSDL sau demo (TASK-209)
│   ├── migrate_optimize_indexes.js        # Migration đánh chỉ mục CSDL (TASK-125)
│   ├── seed_enterprise_data.js            # Seed dữ liệu đối tác mẫu (TASK-029)
│   └── seed_invoices_data.js              # Seed 6 hóa đơn mẫu (TASK-093)
└── tests/
    ├── aging_analysis.test.js             # Kiểm thử phân loại tuổi nợ (TASK-124)
    ├── audit_log_verification.test.js     # Kiểm thử ghi log AuditLog (TASK-184)
    ├── auth_jwt.test.js                   # Kiểm thử xác thực JWT (TASK-059)
    ├── client_validation.test.js          # Kiểm thử xác thực Client MST (TASK-060)
    ├── coverage_sprint1_report.js         # Đo lường Coverage Sprint 1 (TASK-062)
    ├── credit_limit_guard.test.js         # Kiểm thử chặn vượt hạn mức nợ (TASK-218)
    ├── dashboard_performance.test.js      # Đo lường SLA API Dashboard (TASK-156)
    ├── dashboard_stats.test.js            # Kiểm thử công thức Dashboard (TASK-153)
    ├── debt_reduction_payment.test.js     # Kiểm thử thanh toán trừ nợ (TASK-123)
    ├── duplicate_invoice_prevention.test.js # Chặn trùng hóa đơn (TASK-092)
    ├── e2e_fullflow.test.js               # Kiểm thử E2E toàn trình (TASK-185)
    ├── invoice_payment_relation.test.js   # Kiểm thử quan hệ Invoice-Payment (TASK-122)
    ├── placement_deal.test.js             # Kiểm thử deal & bảo hành (TASK-061)
    ├── placement_invoice_relation.test.js # Quan hệ Placement-Invoice (TASK-090)
    ├── reconciliation_fee_subtotal.test.js # Đối soát Fee & Subtotal (TASK-094)
    ├── reconciliation_revenue_12months.test.js # Đối soát doanh thu 12 tháng (TASK-154)
    ├── run_all_tests.js                   # Bộ chạy kiểm thử tổng hợp (TASK-189, TASK-208)
    ├── security_rbac.test.js              # Kiểm thử an toàn & bảo mật RBAC (TASK-186)
    ├── sprint2_acceptance.test.js         # Bộ test nghiệm thu Sprint 2 (TASK-126)
    ├── top5_debtors.test.js               # Kiểm thử Top 5 con nợ lớn nhất (TASK-155)
    ├── unit.test.js                       # Unit test đồng bộ CSDL (TASK-030)
    └── vat_calculation.test.js            # Kiểm thử tính thuế VAT 8% (TASK-091)
```

---
*Kho mã nguồn cá nhân SV5 được đồng bộ chính thức tại:* [https://github.com/phuchh9999-sketch/QLDA_NHOM10_GODDY_SV5_](https://github.com/phuchh9999-sketch/QLDA_NHOM10_GODDY_SV5_)
