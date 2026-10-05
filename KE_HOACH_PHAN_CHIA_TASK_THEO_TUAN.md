# KẾ HOẠCH PHÂN CHIA CHI TIẾT 220 TASK THEO 7 TUẦN DỰ ÁN QLDA - NHÓM 10
## Đề Tài: Phần Mềm Quản Lý Hóa Đơn / Công Nợ Tích Hợp Dashboard Dữ Liệu Cho Tuyển Dụng (GODDY Recruit)
**Đơn vị thực hiện:** Nhóm 10 - Lớp 23DTHC3 - Khoa Công nghệ Thông tin - Trường ĐH Công nghệ TP.HCM (HUTECH)  
**Thời gian thực hiện:** 14/09/2026 – 26/10/2026 (7 tuần / 43 ngày lịch / 37 ngày công)  
**Ngân sách cơ sở:** 45.000.000 VNĐ | Dự phòng rủi ro 10%: 4.500.000 VNĐ  
**Tổng số công việc:** **220 Tasks** (Đạt chuẩn phân rã WBS & bám sát BRD/SRS v5, Product Backlog Excel và Ma trận RACI)

---

### 👥 DANH SÁCH 5 THÀNH VIÊN & VAI TRÒ DỰ ÁN
1. **Nguyễn Hữu Phúc** (MSSV: `2380601740`) – **Project Manager (PM)**: Quản lý dự án, lập kế hoạch WBS, kiểm soát tiến độ, quản lý rủi ro & báo cáo PMBOK.
2. **Nguyễn Xuân Đoàn** (MSSV: `2380600510`) – **Business Analyst (BA)**: Khảo sát nghiệp vụ, đặc tả BRD/SRS, Product Backlog, User Stories & UAT.
3. **Phạm Văn Sơn** (MSSV: `2380601922`) – **Backend Developer (BE)**: Kiến trúc Node.js/Express, Sequelize ORM, RESTful API Auth/RBAC, Invoicing, Payment, Aging, Docker.
4. **Nguyễn Hoàng Phước** (MSSV: `2380601770`) – **Frontend Developer (FE)**: Wireframe Figma, HTML5/CSS3 Responsive, Web Dashboard, Invoices UI, Chart.js, PDF Export.
5. **Huỳnh Nguyễn Vĩnh Phúc** (MSSV: `2380614923`) – **Tester & Database Admin (DB/QA)**: Quản trị PostgreSQL/Supabase & SQLite, ERD, Unit Test Jest, Integration Test, Pareto Analysis.

---

### 📌 QUY ƯỚC ĐẶT TÊN GIT COMMIT
Mỗi khi thành viên hoàn thành task, tiến hành commit theo cú pháp:
`git commit -m "TenTask_tenthanhvien"`  
*Ví dụ:* `git commit -m "API_PhatHanhHoaDonTuDealPlacement_phamson"`  
*Ví dụ:* `git commit -m "ThietKeBangDanhSachHoaDonUI_nguyenhoangphuoc"`  
*Ví dụ:* `git commit -m "BoKiemThuTuDong_PhatHanhHoaDon_huynhnguyenvinhphuc"`

---

### 📊 BẢNG TỔNG HỢP TIẾN ĐỘ 7 TUẦN

| Tuần | Khoảng Thời Gian | Sprint / Giai Đoạn | Trọng Tâm Nghiệp Vụ & Kỹ Thuật | Số Lượng Task | Trạng Thái |
|:---:|:---:|:---:|:---|:---:|:---:|
| **Tuần 1** | 14/09 – 20/09/2026 | Khởi tạo & Sprint 1 | Project Charter, BRD/SRS v4, WBS, ERD CSDL, Khung Express MVC, Wireframe Figma | 30 Tasks | Đã hoàn thành |
| **Tuần 2** | 21/09 – 27/09/2026 | Sprint 1 (Hoàn tất) | Auth JWT/RBAC 3 role, Khách hàng B2B, Tuyển dụng & Deal Placement, Sprint Review 1 | 32 Tasks | Đã hoàn thành |
| **Tuần 3** | 28/09 – 04/10/2026 | Sprint 2 (Phần 1) | Phát hành Hóa đơn Invoicing, Thuế VAT 8%, Net Days Due Date, Mẫu in PDF, Thanh toán | 32 Tasks | Đã hoàn thành |
| **Tuần 4** | 05/10 – 11/10/2026 | Sprint 2 (P.2) & Sprint 3 | Đối soát công nợ, Tuổi nợ Aging 3 xô (1-30, 31-60, >60), Nhắc nợ, Nghiệm thu Sprint 2 | 30 Tasks | Đã hoàn thành |
| **Tuần 5** | 12/10 – 18/10/2026 | Sprint 3 (Hoàn tất) | Dashboard 4 KPI, Biểu đồ Chart.js doanh thu 12 tháng, Cơ cấu ngành, Top 5 Debtors | 31 Tasks | Đã hoàn thành |
| **Tuần 6** | 19/10 – 25/10/2026 | Sprint 4 | Email nhắc nợ, Audit Log hoàn chỉnh, Client Portal, Tối ưu & Đóng gói Docker Staging | 38 Tasks | Đang thực hiện |
| **Tuần 7** | 26/10/2026 | Nghiệm thu & Bảo vệ | Đóng gói mã nguồn, User Manual, Báo cáo PMBOK, Gantt Chart, Slide bảo vệ đồ án | 27 Tasks | Kế hoạch |
| **TỔNG** | **7 Tuần** | **4 Sprints** | **Toàn bộ chu trình phát triển phần mềm chuẩn PMBOK & Scrum** | **220 Tasks** | **>= 200 Tasks** |

---

### 📈 BẢNG PHÂN BỔ KHỐI LƯỢNG CÔNG VIỆC THEO THÀNH VIÊN

| Thành Viên | Vai Trò Chính | Số Lượng Task | Tỷ Lệ (%) | Tổng Story Points | Trọng Trách Chính |
|:---|:---|:---:|:---:|:---:|:---|
| **Nguyễn Hữu Phúc** | Project Manager (PM) | 43 Tasks | 19.5% | 88 SP | Điều phối, WBS, EVM, Lịch trình, Rủi ro, Báo cáo PMBOK |
| **Nguyễn Xuân Đoàn** | Business Analyst (BA) | 41 Tasks | 18.6% | 97 SP | Khảo sát, Đặc tả BRD/SRS v5, Product Backlog, UAT |
| **Phạm Văn Sơn** | Backend Developer (BE) | 48 Tasks | 21.8% | 118 SP | Express REST API, RBAC, Invoicing, Debt, Aging, Docker |
| **Nguyễn Hoàng Phước** | Frontend Developer (FE) | 47 Tasks | 21.4% | 105 SP | Figma, Giao diện Web Responsive, Invoices UI, Chart.js |
| **Huỳnh Nguyễn Vĩnh Phúc** | Tester & Database (QA/DB) | 41 Tasks | 18.6% | 87 SP | CSDL PostgreSQL/SQLite, Jest Unit Test, E2E, Pareto |
| **TỔNG CỘNG** | **5 Thành Viên** | **220 Tasks** | **100%** | **495 SP** | **Phân chia đồng đều, minh bạch, đúng chuyên môn** |

---

## 📋 CHI TIẾT 220 TASK PHÂN BỔ THEO TỪNG TUẦN


---

### 🗓️ TUẦN 1 (Khởi tạo & Sprint 1)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-001** | **Soạn thảo Tuyên bố dự án (Project Charter) theo chuẩn PMBOK**<br>`KhoiTaoProjectCharter_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1.1) | 14/09/2026 | 14/09/2026 | 3 | 8h | Văn bản Project Charter 8 mục hoàn chỉnh | ✅ Đã hoàn thành |
| **TASK-002** | **Xác lập 4 mục tiêu SMART về thời gian, chi phí, phạm vi và chất lượng**<br>`XacLapMucTieuSMART_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1.1) | 14/09/2026 | 14/09/2026 | 2 | 4h | Bảng mục tiêu SMART và chỉ số đo lường | ✅ Đã hoàn thành |
| **TASK-003** | **Phân rã cấu trúc công việc WBS 3 cấp tuân thủ quy tắc 100% và 8/80**<br>`PhanRaWBS3Cap_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1.3) | 15/09/2026 | 15/09/2026 | 3 | 8h | Sơ đồ và bảng WBS 6 gói công việc | ✅ Đã hoàn thành |
| **TASK-004** | **Thiết lập ma trận phân công trách nhiệm RACI cho 5 thành viên**<br>`ThietLapMaTranRACI_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1.3) | 15/09/2026 | 15/09/2026 | 2 | 4h | Bảng ma trận RACI dự án Nhóm 10 | ✅ Đã hoàn thành |
| **TASK-005** | **Dự toán ngân sách tổng thể 45 triệu và kế hoạch dự phòng 10%**<br>`DuToanNganSachDuAn_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1.3) | 15/09/2026 | 15/09/2026 | 2 | 6h | Bảng dự toán chi phí theo WBS | ✅ Đã hoàn thành |
| **TASK-006** | **Tổ chức họp Kickoff dự án và phê duyệt Kế hoạch cơ sở (Milestone 1)**<br>`HopKickoffPheDuyetKeHoach_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1.4) | 15/09/2026 | 15/09/2026 | 1 | 3h | Biên bản họp Kickoff và ký duyệt Kế hoạch | ✅ Đã hoàn thành |
| **TASK-007** | **Khảo sát quy trình chốt deal và thu hồi công nợ doanh nghiệp Headhunt**<br>`KhaoSatQuyTrinhHeadhunt_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 1.2) | 14/09/2026 | 14/09/2026 | 3 | 8h | Báo cáo khảo sát thực trạng nghiệp vụ | ✅ Đã hoàn thành |
| **TASK-008** | **Soạn thảo tài liệu đặc tả yêu cầu nghiệp vụ BRD & SRS v4.0**<br>`SoanThaoBRD_SRS_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 1.2) | 14/09/2026 | 15/09/2026 | 5 | 12h | Tài liệu BRD-SRS v4.0 đầy đủ 12 mục | ✅ Đã hoàn thành |
| **TASK-009** | **Xác định danh mục Business Rules BR-01 đến BR-07 cốt lõi**<br>`XacDinhBusinessRules_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 1.2) | 15/09/2026 | 15/09/2026 | 2 | 4h | Bảng 7 quy tắc nghiệp vụ hệ thống | ✅ Đã hoàn thành |
| **TASK-010** | **Viết User Stories US-01 đến US-04 cho Module Auth, B2B và Tuyển dụng**<br>`VietUserStoriesGiaiDoan1_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 2.1) | 16/09/2026 | 17/09/2026 | 3 | 6h | Tài liệu User Stories và Acceptance Criteria | ✅ Đã hoàn thành |
| **TASK-011** | **Xây dựng Product Backlog ban đầu trên Excel (PB-01 đến PB-14)**<br>`XayDungProductBacklogExcel_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 1.2) | 16/09/2026 | 17/09/2026 | 3 | 6h | File GOODY_Product_Backlog.xlsx | ✅ Đã hoàn thành |
| **TASK-012** | **Định nghĩa tiêu chuẩn hoàn thành Definition of Done (DoD) cho User Story**<br>`DinhNghiaTieuChuanDoD_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 2.1) | 17/09/2026 | 18/09/2026 | 2 | 4h | Bộ tiêu chí DoD kiểm thử chấp nhận | ✅ Đã hoàn thành |
| **TASK-013** | **Khởi tạo repository Git và cấu trúc thư mục Node.js Express MVC chuẩn**<br>`KhoiTaoCauTrucThuMucDuAn_phamson` | Phạm Văn Sơn (BE) | Kiến trúc & CSDL<br>(WBS 2.2) | 16/09/2026 | 16/09/2026 | 2 | 4h | Cấu trúc thư mục controllers, models, routes | ✅ Đã hoàn thành |
| **TASK-014** | **Cấu hình Sequelize ORM kết nối CSDL SQLite portable và Supabase**<br>`KetNoiCoSoDuLieuSequelize_phamson` | Phạm Văn Sơn (BE) | Kiến trúc & CSDL<br>(WBS 2.2) | 16/09/2026 | 17/09/2026 | 3 | 6h | File config/database.js hoạt động mượt mà | ✅ Đã hoàn thành |
| **TASK-015** | **Cấu hình CORS, Express JSON Parser và URL-encoded parser**<br>`CauHinhCorsVaExpressParser_phamson` | Phạm Văn Sơn (BE) | Kiến trúc & CSDL<br>(WBS 2.2) | 17/09/2026 | 17/09/2026 | 1 | 2h | Middleware parser tích hợp trong server.js | ✅ Đã hoàn thành |
| **TASK-016** | **Cấu hình phục vụ Static Assets thư mục public cho Web Dashboard**<br>`CauHinhPhucVuStaticAssetsPublic_phamson` | Phạm Văn Sơn (BE) | Kiến trúc & CSDL<br>(WBS 2.2) | 17/09/2026 | 18/09/2026 | 1 | 2h | Route express.static cho public folder | ✅ Đã hoàn thành |
| **TASK-017** | **Thiết lập cấu hình biến môi trường an toàn với file .env**<br>`ThietLapBienMoiTruongDotenv_phamson` | Phạm Văn Sơn (BE) | Kiến trúc & CSDL<br>(WBS 2.2) | 18/09/2026 | 18/09/2026 | 1 | 2h | File .env và .env.example mẫu | ✅ Đã hoàn thành |
| **TASK-018** | **Xây dựng middleware xử lý lỗi tập trung Error Handling và format JSON chuẩn**<br>`XayDungMiddlewareErrorHandler_phamson` | Phạm Văn Sơn (BE) | Kiến trúc & CSDL<br>(WBS 2.2) | 18/09/2026 | 19/09/2026 | 2 | 4h | Middleware errorHandler trả format { success, error } | ✅ Đã hoàn thành |
| **TASK-019** | **Phác thảo Wireframe Prototype UI hệ thống trên Figma**<br>`ThietKeWireframeFigmaUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.1) | 16/09/2026 | 17/09/2026 | 3 | 8h | Bản thiết kế Figma các màn hình cốt lõi | ✅ Đã hoàn thành |
| **TASK-020** | **Xây dựng Design System, biến CSS Token và bảng màu Slate/Indigo hiện đại**<br>`XayDungDesignSystemCssToken_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.1) | 17/09/2026 | 18/09/2026 | 2 | 6h | File public/css/style.css định nghĩa biến chuẩn | ✅ Đã hoàn thành |
| **TASK-021** | **Dựng khung bố cục giao diện dùng chung Layout: Sidebar + Top Header**<br>`DungKhungBoCucSidebarHeader_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 18/09/2026 | 19/09/2026 | 2 | 6h | Khung Sidebar có nav link và badge thông báo | ✅ Đã hoàn thành |
| **TASK-022** | **Tạo trang khung Dashboard dữ liệu skeleton index.html**<br>`TaoTrangDashboardSkeleton_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 19/09/2026 | 19/09/2026 | 2 | 4h | Giao diện khung ban đầu public/index.html | ✅ Đã hoàn thành |
| **TASK-023** | **Tạo trang khung Quản lý Khách hàng skeleton clients.html**<br>`TaoTrangKhachHangSkeleton_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 19/09/2026 | 20/09/2026 | 2 | 4h | Giao diện khung ban đầu public/clients.html | ✅ Đã hoàn thành |
| **TASK-024** | **Tích hợp icon thư viện Lucide / FontAwesome và Google Font Inter**<br>`TichHopFontVaIcons_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.1) | 20/09/2026 | 20/09/2026 | 1 | 2h | Giao diện hiển thị font chữ Inter sắc nét | ✅ Đã hoàn thành |
| **TASK-025** | **Thiết kế Sơ đồ quan hệ thực thể ERD 8 bảng dữ liệu quan hệ**<br>`ThietKeSoDoQuanHeERD_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 16/09/2026 | 17/09/2026 | 3 | 8h | File ERD_QLDA_NHOM10_GODDY.drawio | ✅ Đã hoàn thành |
| **TASK-026** | **Viết script DDL database_supabase_postgres.sql và database_sqlserver.sql**<br>`VietScriptDDLPostgresSqlserver_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 17/09/2026 | 17/09/2026 | 3 | 6h | Script SQL khởi tạo bảng, khóa chính, khóa ngoại | ✅ Đã hoàn thành |
| **TASK-027** | **Xây dựng Model User (username, email, password, role, isActive)**<br>`ThietKeModelUser_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.2) | 17/09/2026 | 18/09/2026 | 2 | 4h | File models/User.js hoàn chỉnh | ✅ Đã hoàn thành |
| **TASK-028** | **Xây dựng Model Client (companyName, taxCode, netDays, contactPerson)**<br>`ThietKeModelClient_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.2) | 18/09/2026 | 18/09/2026 | 2 | 4h | File models/Client.js đầy đủ trường | ✅ Đã hoàn thành |
| **TASK-029** | **Viết script tự động nạp dữ liệu mẫu seed data doanh nghiệp công nghệ**<br>`VietScriptNapDuLieuMauEnterprise_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.2) | 18/09/2026 | 19/09/2026 | 2 | 4h | Seed script nạp sẵn FPT, VNG, Shopee, Viettel | ✅ Đã hoàn thành |
| **TASK-030** | **Cài đặt framework kiểm thử tự động Jest/Supertest và viết test kết nối CSDL**<br>`CaiDatTestingJestKiemTraDB_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 2.4) | 19/09/2026 | 20/09/2026 | 2 | 4h | Bộ test tests/unit.test.js kiểm tra đồng bộ CSDL | ✅ Đã hoàn thành |

---

### 🗓️ TUẦN 2 (Sprint 1)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-031** | **Điều phối phiên họp Sprint 1 Planning và gán Story Points PB-01 -> PB-04**<br>`DieuPhoiHopSprint1Planning_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1) | 21/09/2026 | 21/09/2026 | 2 | 4h | Kế hoạch Sprint 1 Backlog và phân chia công việc | ✅ Đã hoàn thành |
| **TASK-032** | **Theo dõi tiến độ commit git hàng ngày theo cú pháp TenTask_tenthanhvien**<br>`TheoDoiTienDoCommitHangNgay_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1) | 21/09/2026 | 25/09/2026 | 2 | 6h | Bảng theo dõi số lượng commit của từng thành viên | ✅ Đã hoàn thành |
| **TASK-033** | **Rà soát rủi ro xung đột dữ liệu giữa Client và Deal Placement**<br>`RaSoatRuiRoXungDotDuLieu_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1) | 22/09/2026 | 23/09/2026 | 2 | 4h | Ghi nhận Risk Log và biện pháp giảm thiểu | ✅ Đã hoàn thành |
| **TASK-034** | **Kiểm tra chất lượng mã nguồn tuân thủ coding convention nhóm**<br>`KiemTraChatLuongCodeSprint1_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1) | 24/09/2026 | 25/09/2026 | 2 | 4h | Báo cáo Code Review Sprint 1 | ✅ Đã hoàn thành |
| **TASK-035** | **Tổ chức họp Sprint 1 Review nghiệm thu tính năng Khách hàng & Tuyển dụng**<br>`HopSprint1ReviewNghiemThu_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 2.4) | 26/09/2026 | 26/09/2026 | 2 | 4h | Biên bản nghiệm thu hoàn thành 18 Story Points | ✅ Đã hoàn thành |
| **TASK-036** | **Tổ chức họp Sprint 1 Retrospective rút kinh nghiệm quy trình phối hợp**<br>`HopSprint1Retrospective_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 2.4) | 26/09/2026 | 27/09/2026 | 1 | 3h | Bảng đúc kết bài học What went well / Need improvement | ✅ Đã hoàn thành |
| **TASK-037** | **Đặc tả chi tiết các yêu cầu chức năng FR-AUTH-01 đến 06 cho phân hệ RBAC**<br>`DacTaChiTietFR_AUTH_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 2.1) | 21/09/2026 | 21/09/2026 | 2 | 4h | Tài liệu đặc tả FR-AUTH 3 vai trò | ✅ Đã hoàn thành |
| **TASK-038** | **Đặc tả chi tiết các yêu cầu chức năng FR-CUS-01 đến 07 cho Khách hàng B2B**<br>`DacTaChiTietFR_CUS_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 2.1) | 21/09/2026 | 22/09/2026 | 2 | 4h | Tài liệu đặc tả nghiệp vụ Client B2B | ✅ Đã hoàn thành |
| **TASK-039** | **Đặc tả chi tiết các yêu cầu chức năng FR-REC-01 đến 07 cho Tuyển dụng & Deal**<br>`DacTaChiTietFR_REC_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 2.1) | 22/09/2026 | 23/09/2026 | 3 | 6h | Tài liệu đặc tả Job, Candidate & Placement | ✅ Đã hoàn thành |
| **TASK-040** | **Xác định công thức tính phí hoa hồng Headhunt và quy tắc bảo hành 60 ngày**<br>`XacDinhCongThucPhiVaBaoHanh_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 2.1) | 23/09/2026 | 23/09/2026 | 2 | 4h | Công thức serviceFee và warrantyEndDate | ✅ Đã hoàn thành |
| **TASK-041** | **Xây dựng kịch bản kiểm thử chấp nhận UAT cho phân hệ Khách hàng B2B**<br>`XayDungKichBanUAT_Client_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 2.4) | 24/09/2026 | 25/09/2026 | 2 | 4h | Kịch bản UAT-01 kiểm tra Client và MST | ✅ Đã hoàn thành |
| **TASK-042** | **Thực hiện nghiệm thu chấp nhận người dùng UAT cho chốt Deal Placement**<br>`NghiemThuUAT_DealPlacement_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 2.4) | 25/09/2026 | 26/09/2026 | 2 | 4h | Biên bản nghiệm thu UAT-02 Deal Placement | ✅ Đã hoàn thành |
| **TASK-043** | **Cài đặt thư viện bcryptjs và viết hàm băm mật khẩu độ muối 10 rounds**<br>`VietHamMaHoaMatKhauBcrypt_phamson` | Phạm Văn Sơn (BE) | Xác thực RBAC<br>(WBS 2.2) | 21/09/2026 | 21/09/2026 | 2 | 4h | Hàm hashPassword và comparePassword | ✅ Đã hoàn thành |
| **TASK-044** | **Viết API Đăng nhập hệ thống POST /api/auth/login cấp JWT token 7 ngày**<br>`API_DangNhapHeThong_phamson` | Phạm Văn Sơn (BE) | Xác thực RBAC<br>(WBS 2.2) | 21/09/2026 | 22/09/2026 | 3 | 6h | Endpoint POST /api/auth/login hoàn chỉnh | ✅ Đã hoàn thành |
| **TASK-045** | **Viết Middleware verifyToken và requireRole phân quyền 3 cấp Admin/Kế toán/Recruiter**<br>`MiddlewarePhanQuyenTheoVaiTro_phamson` | Phạm Văn Sơn (BE) | Xác thực RBAC<br>(WBS 2.2) | 22/09/2026 | 22/09/2026 | 3 | 6h | Middleware middlewares/auth.js | ✅ Đã hoàn thành |
| **TASK-046** | **Viết API Đăng ký tài khoản POST /api/auth/register chặn trùng username**<br>`API_DangKyNhanVienMoi_phamson` | Phạm Văn Sơn (BE) | Xác thực RBAC<br>(WBS 2.2) | 22/09/2026 | 23/09/2026 | 2 | 4h | Endpoint POST /api/auth/register | ✅ Đã hoàn thành |
| **TASK-047** | **Xây dựng trọn bộ API CRUD Khách hàng B2B /api/clients kèm validate MST**<br>`API_QuanLyKhachHangB2B_phamson` | Phạm Văn Sơn (BE) | Khách hàng B2B<br>(WBS 2.2) | 23/09/2026 | 24/09/2026 | 3 | 8h | Routes routes/clients.js đầy đủ GET, POST, PUT, DELETE | ✅ Đã hoàn thành |
| **TASK-048** | **Xây dựng API Quản lý Vị trí tuyển dụng Job và Hồ sơ Ứng viên Candidate**<br>`API_QuanLyJobVaCandidate_phamson` | Phạm Văn Sơn (BE) | Tuyển dụng<br>(WBS 2.2) | 24/09/2026 | 25/09/2026 | 3 | 6h | Routes Job và Candidate trong routes/recruitment.js | ✅ Đã hoàn thành |
| **TASK-049** | **Xây dựng API Chốt Deal Tuyển dụng POST /api/recruitment/placements**<br>`API_GhiNhanDealTuyenDungMoi_phamson` | Phạm Văn Sơn (BE) | Tuyển dụng<br>(WBS 2.2) | 25/09/2026 | 26/09/2026 | 3 | 8h | Endpoint POST /api/recruitment/placements tự tính fee | ✅ Đã hoàn thành |
| **TASK-050** | **Thiết kế màn hình Đăng nhập login.html lưu trữ JWT vào localStorage**<br>`ThietKeGiaoDienDangNhap_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 21/09/2026 | 21/09/2026 | 2 | 5h | Trang public/login.html thẩm mỹ, có validate | ✅ Đã hoàn thành |
| **TASK-051** | **Cơ chế phân quyền giao diện: Tự động ẩn/hiện menu theo vai trò người dùng**<br>`PhanQuyenGiaoDienTheoRole_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 22/09/2026 | 22/09/2026 | 2 | 4h | Script phân quyền UI theo role Admin/Kế toán | ✅ Đã hoàn thành |
| **TASK-052** | **Xây dựng Bảng danh sách Khách hàng B2B clients.html kèm ô tìm kiếm realtime**<br>`ThietKeBangDanhSachKhachHangUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 23/09/2026 | 23/09/2026 | 3 | 6h | Bảng hiển thị đối tác, số thuế, Net days | ✅ Đã hoàn thành |
| **TASK-053** | **Thiết kế Modal Thêm mới Đối tác Doanh nghiệp kèm kiểm tra dữ liệu đầu vào**<br>`ThietKeModalThemKhachHangMoiUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 23/09/2026 | 24/09/2026 | 2 | 5h | Modal popup nhập MST, Tên công ty, Email | ✅ Đã hoàn thành |
| **TASK-054** | **Xây dựng chức năng Xuất danh sách khách hàng ra file CSV**<br>`XuatDanhSachKhachHangRaCSV_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 24/09/2026 | 24/09/2026 | 2 | 4h | Nút Export CSV xuất file client_list.csv | ✅ Đã hoàn thành |
| **TASK-055** | **Xây dựng Bảng danh sách Deal Tuyển dụng và Huy hiệu trạng thái bảo hành**<br>`ThietKeBangDanhSachDealUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 25/09/2026 | 25/09/2026 | 2 | 5h | Bảng Placement với badge thời hạn bảo hành | ✅ Đã hoàn thành |
| **TASK-056** | **Thiết kế Modal Chốt Deal: Tự động tải Job theo Khách hàng và ước tính phí**<br>`ThietKeModalChotDealPlacementUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 2.3) | 25/09/2026 | 26/09/2026 | 3 | 6h | Modal chốt deal tính nhanh phí hoa hồng | ✅ Đã hoàn thành |
| **TASK-057** | **Xây dựng Model Job và Model Candidate với ràng buộc khóa ngoại ClientId**<br>`ThietKeModelJobVaCandidate_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 21/09/2026 | 22/09/2026 | 2 | 5h | Files models/Job.js và models/Candidate.js | ✅ Đã hoàn thành |
| **TASK-058** | **Xây dựng Model Placement ghi nhận thỏa thuận tuyển dụng và quan hệ dữ liệu**<br>`ThietKeModelPlacement_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 22/09/2026 | 22/09/2026 | 2 | 4h | File models/Placement.js cấu hình quan hệ | ✅ Đã hoàn thành |
| **TASK-059** | **Viết bộ kiểm thử tự động xác thực Đăng nhập/Đăng ký và cấp Token JWT**<br>`BoKiemThuTuDong_AuthJWT_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 2.4) | 23/09/2026 | 24/09/2026 | 2 | 4h | Test suite cho /api/auth pass 100% | ✅ Đã hoàn thành |
| **TASK-060** | **Viết bộ kiểm thử tự động Thêm khách hàng, chặn trùng MST và xóa an toàn**<br>`BoKiemThuTuDong_ThemKhachHang_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 2.4) | 24/09/2026 | 25/09/2026 | 2 | 4h | Test suite cho Client MST validation | ✅ Đã hoàn thành |
| **TASK-061** | **Viết bộ kiểm thử tự động Chốt Deal Placement và tính ngày hết hạn bảo hành**<br>`BoKiemThuTuDong_ChotDealPlacement_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 2.4) | 25/09/2026 | 26/09/2026 | 2 | 4h | Test suite cho Placement fee và warranty | ✅ Đã hoàn thành |
| **TASK-062** | **Đo lường độ bao phủ kiểm thử Code Coverage Sprint 1 đạt trên 80%**<br>`DoLuongCodeCoverageSprint1_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 2.4) | 26/09/2026 | 27/09/2026 | 1 | 3h | Báo cáo Jest Coverage Report Sprint 1 | ✅ Đã hoàn thành |

---

### 🗓️ TUẦN 3 (Sprint 2)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-063** | **Khởi động Sprint 2: Phân công hạng mục Hóa đơn Invoicing & Thu hồi công nợ**<br>`KhoiDongSprint2_Invoicing_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3) | 28/09/2026 | 28/09/2026 | 2 | 4h | Bảng phân công Sprint 2 WBS 3.1 & 3.2 | ✅ Đã hoàn thành |
| **TASK-064** | **Theo dõi ngân sách chi phí Sprint 2 (kế hoạch 9.000.000 VNĐ)**<br>`TheoDoiNganSachChiPhiSprint2_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3) | 28/09/2026 | 02/10/2026 | 2 | 4h | Bảng theo dõi dòng tiền và chi phí thực tế | ✅ Đã hoàn thành |
| **TASK-065** | **Kiểm soát thay đổi phạm vi Scope Creep trong logic tự sinh mã hóa đơn**<br>`KiemSoatThayDoiScopeInvoicing_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3) | 29/09/2026 | 30/09/2026 | 2 | 4h | Tài liệu Scope Baseline cập nhật | ✅ Đã hoàn thành |
| **TASK-066** | **Tổ chức họp giao ban Daily Standup giải quyết vướng mắc xuất file PDF**<br>`HopDailyGiaiQuyetXuatPDF_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3) | 30/09/2026 | 01/10/2026 | 1 | 3h | Biên bản gỡ nút thắt in hóa đơn PDF | ✅ Đã hoàn thành |
| **TASK-067** | **Kiểm tra mốc tiến độ Milestone 2: Hoàn tất phân hệ Hóa đơn Invoicing**<br>`KiemTraMilestone2HoaDon_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3.1) | 02/10/2026 | 03/10/2026 | 2 | 4h | Biên bản nghiệm thu Milestone 2 | ✅ Đã hoàn thành |
| **TASK-068** | **Đánh giá tiến độ hoàn thành các task của 5 thành viên qua git commit**<br>`DanhGiaTienDoCommitTuan3_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3) | 03/10/2026 | 04/10/2026 | 1 | 3h | Báo cáo kiểm soát tiến độ Tuần 3 | ✅ Đã hoàn thành |
| **TASK-069** | **Đặc tả yêu cầu chức năng FR-INV-01 đến 09 cho phân hệ Hóa đơn**<br>`DacTaChiTietFR_INV_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.1) | 28/09/2026 | 28/09/2026 | 2 | 4h | Tài liệu đặc tả phát hành hóa đơn VAT | ✅ Đã hoàn thành |
| **TASK-070** | **Quy định định dạng sinh mã hóa đơn tự động duy nhất INV-YYYY-XXXX**<br>`QuyDinhMaHoaDonTuDong_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.1) | 28/09/2026 | 29/09/2026 | 2 | 3h | Quy tắc sinh số hóa đơn chuẩn kế toán | ✅ Đã hoàn thành |
| **TASK-071** | **Đặc tả công thức tính thuế GTGT 8% và tính Ngày đến hạn dueDate theo Net Days**<br>`DacTaCongThucVATVaDueDate_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.1) | 29/09/2026 | 29/09/2026 | 2 | 4h | Công thức vatAmount và dueDate | ✅ Đã hoàn thành |
| **TASK-072** | **Đặc tả yêu cầu mẫu in hóa đơn GTGT tiêu chuẩn điện tử và xuất PDF**<br>`DacTaMauInHoaDonDienTu_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.1) | 30/09/2026 | 01/10/2026 | 2 | 4h | Đặc tả bố cục hóa đơn A4 chuẩn | ✅ Đã hoàn thành |
| **TASK-073** | **Đặc tả quy trình thanh toán từng đợt FR-PAY và trừ dần nợ remainingAmount**<br>`DacTaQuyTrinhThanhToanFR_PAY_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.2) | 01/10/2026 | 02/10/2026 | 2 | 4h | Quy tắc đổi trạng thái Sent/Partial/Paid | ✅ Đã hoàn thành |
| **TASK-074** | **Xây dựng kịch bản kiểm thử nghiệp vụ cho quy trình xuất hóa đơn từ Deal**<br>`KichBanKiemThuHoaDonTuDeal_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.1) | 02/10/2026 | 03/10/2026 | 2 | 4h | Bộ Test Scenario UAT Invoicing | ✅ Đã hoàn thành |
| **TASK-075** | **Viết API Lấy danh sách hóa đơn GET /api/invoices kèm thông tin Client và Placement**<br>`API_LayDanhSachHoaDon_phamson` | Phạm Văn Sơn (BE) | Hóa đơn & Invoicing<br>(WBS 3.1) | 28/09/2026 | 28/09/2026 | 2 | 5h | Endpoint GET /api/invoices với include models | ✅ Đã hoàn thành |
| **TASK-076** | **Xây dựng thuật toán sinh mã hóa đơn tự động duy nhất INV-YYYY-XXXX**<br>`HamSinhMaHoaDonTuDong_phamson` | Phạm Văn Sơn (BE) | Hóa đơn & Invoicing<br>(WBS 3.1) | 28/09/2026 | 29/09/2026 | 2 | 4h | Hàm generateInvoiceNumber đảm bảo tính tuần tự | ✅ Đã hoàn thành |
| **TASK-077** | **Xây dựng hàm tính thuế VAT 8% (vatAmount) và tổng tiền thanh toán (totalAmount)**<br>`HamTinhTienThueVAT8PhanTram_phamson` | Phạm Văn Sơn (BE) | Hóa đơn & Invoicing<br>(WBS 3.1) | 29/09/2026 | 29/09/2026 | 2 | 4h | Logic tính thuế VAT chuẩn xác không làm tròn sai | ✅ Đã hoàn thành |
| **TASK-078** | **Viết logic tính ngày đến hạn dueDate = issueDate + client.netDays**<br>`TuDongGanHanThanhToanTheoNetDays_phamson` | Phạm Văn Sơn (BE) | Hóa đơn & Invoicing<br>(WBS 3.1) | 29/09/2026 | 30/09/2026 | 2 | 4h | Tính hạn thanh toán theo Net 15/30/45/60 | ✅ Đã hoàn thành |
| **TASK-079** | **Viết API Phát hành hóa đơn từ Placement POST /api/invoices/from-placement**<br>`API_PhatHanhHoaDonTuDealPlacement_phamson` | Phạm Văn Sơn (BE) | Hóa đơn & Invoicing<br>(WBS 3.1) | 30/09/2026 | 01/10/2026 | 3 | 8h | Endpoint tạo hóa đơn tự động từ deal | ✅ Đã hoàn thành |
| **TASK-080** | **Thêm kiểm tra an toàn: Chặn phát hành nhiều hóa đơn cho cùng 1 deal placement**<br>`ChanPhatHanhTrungHoaDonChoCung1Deal_phamson` | Phạm Văn Sơn (BE) | Hóa đơn & Invoicing<br>(WBS 3.1) | 01/10/2026 | 02/10/2026 | 2 | 4h | Ràng buộc 1:1 bảo đảm không tạo trùng lặp | ✅ Đã hoàn thành |
| **TASK-081** | **Viết API Hủy hóa đơn PUT /api/invoices/:id/cancel (chặn hủy nếu đã thanh toán)**<br>`API_HuyHoaDonDichVu_phamson` | Phạm Văn Sơn (BE) | Hóa đơn & Invoicing<br>(WBS 3.1) | 02/10/2026 | 03/10/2026 | 2 | 4h | Endpoint hủy hóa đơn kèm kiểm tra paidAmount | ✅ Đã hoàn thành |
| **TASK-082** | **Xây dựng Giao diện Bảng quản lý hóa đơn invoices.html chuyên nghiệp**<br>`ThietKeBangDanhSachHoaDonUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.1) | 28/09/2026 | 29/09/2026 | 3 | 7h | Giao diện public/invoices.html hiển thị tiền tệ VNĐ | ✅ Đã hoàn thành |
| **TASK-083** | **Thiết kế Huy hiệu trạng thái hóa đơn Sent (Lam), Partial (Cam), Paid (Lục), Overdue (Đỏ)**<br>`HienThiHuyHieuTrangThaiHoaDon_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.1) | 29/09/2026 | 30/09/2026 | 2 | 4h | Badges màu sắc trực quan theo chuẩn UI | ✅ Đã hoàn thành |
| **TASK-084** | **Thiết kế Modal xem chi tiết hóa đơn theo mẫu Hóa đơn GTGT chuẩn doanh nghiệp**<br>`ThietKeModalXemChiTietHoaDonUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.1) | 30/09/2026 | 01/10/2026 | 3 | 6h | Modal hiển thị đầy đủ MST bên bán, mua, chữ ký | ✅ Đã hoàn thành |
| **TASK-085** | **Viết CSS @media print tối ưu hóa hiển thị khi in ấn khổ giấy A4**<br>`MauInHoaDonDienTuStandard_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.1) | 01/10/2026 | 01/10/2026 | 2 | 4h | Bố cục in chuẩn trang, ẩn thanh điều hướng | ✅ Đã hoàn thành |
| **TASK-086** | **Tích hợp tính năng In trực tiếp và Xuất PDF hóa đơn bằng window.print()**<br>`ChucNangInHoaDonVaXuatPDF_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.1) | 01/10/2026 | 02/10/2026 | 2 | 4h | Nút In Hóa Đơn / Lưu PDF hoạt động mượt mà | ✅ Đã hoàn thành |
| **TASK-087** | **Thêm Bộ lọc hóa đơn theo trạng thái (Tất cả, Đã gửi, Trả 1 phần, Hoàn tất, Quá hạn)**<br>`BoLocHoaDonTheoTrangThaiUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.1) | 02/10/2026 | 03/10/2026 | 2 | 4h | Dropdown lọc dữ liệu hóa đơn realtime | ✅ Đã hoàn thành |
| **TASK-088** | **Xây dựng chức năng Xuất toàn bộ danh sách hóa đơn ra file CSV**<br>`XuatDanhSachHoaDonRaCSV_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.1) | 03/10/2026 | 03/10/2026 | 2 | 3h | Nút Export CSV xuất file invoices_list.csv | ✅ Đã hoàn thành |
| **TASK-089** | **Xây dựng Model Invoice (invoiceNo, totalAmount, paidAmount, remainingAmount, status)**<br>`ThietKeModelInvoice_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 28/09/2026 | 29/09/2026 | 2 | 5h | File models/Invoice.js chuẩn trường dữ liệu | ✅ Đã hoàn thành |
| **TASK-090** | **Cấu hình quan hệ Placement 1 - 1 Invoice trong Sequelize ORM**<br>`ThietLapQuanHePlacementVaInvoice_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 29/09/2026 | 29/09/2026 | 2 | 4h | Ràng buộc foreign key PlacementId trong Invoice | ✅ Đã hoàn thành |
| **TASK-091** | **Viết bộ kiểm thử tự động Tính thuế VAT 8% và Tổng tiền hóa đơn**<br>`BoKiemThuTuDong_PhatHanhHoaDon_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 3.4) | 30/09/2026 | 01/10/2026 | 2 | 4h | Test suite kiểm tra công thức VAT toán học | ✅ Đã hoàn thành |
| **TASK-092** | **Viết bộ kiểm thử tự động Chặn phát hành trùng hóa đơn trên cùng 1 deal**<br>`BoKiemThuTuDong_ChanTrungHoaDon_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 3.4) | 01/10/2026 | 02/10/2026 | 2 | 4h | Test case trả lỗi 400 khi tạo hóa đơn lần 2 | ✅ Đã hoàn thành |
| **TASK-093** | **Cập nhật seed data mẫu với các hóa đơn thực tế phát hành cho FPT, VNG, Shopee**<br>`CapNhatSeedDataHoaDonMau_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.2) | 02/10/2026 | 03/10/2026 | 2 | 4h | Seed 6 hóa đơn với đầy đủ trạng thái khác nhau | ✅ Đã hoàn thành |
| **TASK-094** | **Kiểm tra tính toàn vẹn dữ liệu giữa Placement.fee và Invoice.subtotal**<br>`KiemTraToanVenDuLieuFeeVaSubtotal_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 3.4) | 03/10/2026 | 04/10/2026 | 1 | 3h | Test case đối soát khớp số tiền 100% | ✅ Đã hoàn thành |

---

### 🗓️ TUẦN 4 (Sprint 2 & 3)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-095** | **Điều phối nghiệm thu các hạng mục công nợ & tuổi nợ WBS 3.3 và 3.4**<br>`DieuPhoiNghiemThuCongNoAging_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3) | 05/10/2026 | 06/10/2026 | 2 | 4h | Biên bản rà soát phân hệ Tuổi nợ | ✅ Đã hoàn thành |
| **TASK-096** | **Tổ chức họp Sprint 2 Review và đánh giá đạt 18 Story Points cam kết**<br>`HopSprint2ReviewNghiemThu_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3.4) | 07/10/2026 | 07/10/2026 | 2 | 4h | Biên bản nghiệm thu hoàn tất Sprint 2 | ✅ Đã hoàn thành |
| **TASK-097** | **Tổ chức họp Sprint 2 Retrospective nâng cao hiệu suất xử lý logic thanh toán**<br>`HopSprint2Retrospective_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 3.4) | 07/10/2026 | 08/10/2026 | 1 | 3h | Báo cáo cải tiến quy trình kỹ thuật | ✅ Đã hoàn thành |
| **TASK-098** | **Khởi động Sprint 3: Phân công xây dựng Dashboard KPI và Báo cáo trực quan**<br>`KhoiDongSprint3_Dashboard_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 4) | 08/10/2026 | 08/10/2026 | 2 | 4h | Kế hoạch Sprint 3 Backlog (PB-10, 11, 14) | ✅ Đã hoàn thành |
| **TASK-099** | **Cập nhật đường găng Critical Path và phân tích độ trễ Slack của dự án**<br>`CapNhatDuongGangCriticalPath_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1) | 09/10/2026 | 10/10/2026 | 2 | 5h | Bảng tính toán ES, EF, LS, LF, Slack | ✅ Đã hoàn thành |
| **TASK-100** | **Đánh giá các chỉ số giá trị thu được EVM (PV, EV, AC, SPI, CPI) giữa kỳ**<br>`DanhGiaChiSoEVMGiuaKy_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 1) | 10/10/2026 | 11/10/2026 | 2 | 5h | Báo cáo phân tích hiệu suất tài chính EVM | ✅ Đã hoàn thành |
| **TASK-101** | **Đặc tả yêu cầu chức năng FR-AGE-01 đến 05 cho phân tích tuổi nợ 3 bucket**<br>`DacTaChiTietFR_AGE_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.3) | 05/10/2026 | 05/10/2026 | 2 | 4h | Tài liệu đặc tả 3 xô tuổi nợ (1-30, 31-60, >60) | ✅ Đã hoàn thành |
| **TASK-102** | **Đặc tả chức năng gửi thông báo nhắc nợ khách hàng FR-REM-01 & 02**<br>`DacTaThongBaoNhacNoFR_REM_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.3) | 05/10/2026 | 06/10/2026 | 2 | 4h | Đặc tả mẫu lời nhắc nợ và tần suất gửi | ✅ Đã hoàn thành |
| **TASK-103** | **Viết User Stories US-08 (Thanh toán), US-09 (Aging), US-10 (Nhắc nợ)**<br>`VietUserStoriesGiaiDoan2_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.3) | 06/10/2026 | 07/10/2026 | 2 | 5h | Bộ User Stories & Acceptance Criteria chi tiết | ✅ Đã hoàn thành |
| **TASK-104** | **Khảo sát và đặc tả các chỉ số KPI cần hiển thị trên Dashboard tuyển dụng**<br>`DacTaKPIDashboardTuyenDung_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 4.1) | 08/10/2026 | 09/10/2026 | 2 | 4h | Tài liệu đặc tả FR-DASH-01 đến 07 | ✅ Đã hoàn thành |
| **TASK-105** | **Đặc tả thuật toán gom doanh thu thực tế theo 12 tháng từ các đợt thanh toán**<br>`DacTaDoanhThu12Thang_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 4.1) | 09/10/2026 | 10/10/2026 | 2 | 4h | Quy tắc thống kê doanh thu theo thời gian | ✅ Đã hoàn thành |
| **TASK-106** | **Thực hiện nghiệm thu chấp nhận UAT cho quy trình thanh toán và phân loại tuổi nợ**<br>`NghiemThuUAT_ThanhToanVaAging_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 3.4) | 10/10/2026 | 11/10/2026 | 2 | 4h | Biên bản nghiệm thu UAT-03 Công nợ Aging | ✅ Đã hoàn thành |
| **TASK-107** | **Xây dựng API Thu tiền thanh toán nợ POST /api/debt/payment**<br>`API_GhiNhanThanhToanCongNo_phamson` | Phạm Văn Sơn (BE) | Công nợ & Aging<br>(WBS 3.2) | 05/10/2026 | 05/10/2026 | 3 | 7h | Endpoint POST /api/debt/payment lưu bảng Payment | ✅ Đã hoàn thành |
| **TASK-108** | **Kiểm tra chặt chẽ số tiền thanh toán: Bắt buộc > 0 và không vượt remainingAmount**<br>`ValidateSoTienTraKhongVuotQuaNo_phamson` | Phạm Văn Sơn (BE) | Công nợ & Aging<br>(WBS 3.2) | 05/10/2026 | 06/10/2026 | 2 | 4h | Chặn overpayment trả về mã lỗi 400 | ✅ Đã hoàn thành |
| **TASK-109** | **Cập nhật trừ dần nợ: paidAmount += pay, remainingAmount -= pay và đổi trạng thái**<br>`TuDongTruDanDuNoHoaDon_phamson` | Phạm Văn Sơn (BE) | Công nợ & Aging<br>(WBS 3.2) | 06/10/2026 | 06/10/2026 | 2 | 5h | Logic tự chuyển trạng thái Paid hoặc Partial | ✅ Đã hoàn thành |
| **TASK-110** | **Xây dựng API Tổng hợp công nợ và phân loại tuổi nợ GET /api/debt/overview**<br>`API_BaoCaoTongHopCongNo_phamson` | Phạm Văn Sơn (BE) | Công nợ & Aging<br>(WBS 3.3) | 06/10/2026 | 07/10/2026 | 3 | 8h | Endpoint GET /api/debt/overview trả 3 xô tuổi nợ | ✅ Đã hoàn thành |
| **TASK-111** | **Thuật toán tính số ngày quá hạn và phân nhóm tự động 1-30, 31-60, >60 ngày**<br>`PhanTichTuoiNo3XoTuDong_phamson` | Phạm Văn Sơn (BE) | Công nợ & Aging<br>(WBS 3.3) | 07/10/2026 | 07/10/2026 | 2 | 5h | Logic so khớp dueDate với ngày hiện tại | ✅ Đã hoàn thành |
| **TASK-112** | **Viết API Gửi thông báo nhắc nợ POST /api/debt/remind ghi nhận thời điểm nhắc**<br>`API_GuiThongBaoNhacNo_phamson` | Phạm Văn Sơn (BE) | Công nợ & Aging<br>(WBS 3.3) | 08/10/2026 | 09/10/2026 | 2 | 4h | Endpoint nhắc nợ kèm ghi nhận Audit Log | ✅ Đã hoàn thành |
| **TASK-113** | **Bắt đầu xây dựng API Thống kê KPI Dashboard GET /api/dashboard/stats**<br>`API_LaySoLieuTongHopDashboard_phamson` | Phạm Văn Sơn (BE) | Dashboard<br>(WBS 4.1) | 09/10/2026 | 11/10/2026 | 3 | 7h | Khung API thống kê số liệu tổng hợp ban đầu | ✅ Đã hoàn thành |
| **TASK-114** | **Thiết kế Giao diện Quản lý Công nợ debt.html đồng bộ hệ thống**<br>`ThietKeGiaoDienQuanLyCongNoUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.3) | 05/10/2026 | 05/10/2026 | 3 | 6h | Trang public/debt.html trực quan, hiện đại | ✅ Đã hoàn thành |
| **TASK-115** | **Thiết kế 3 Thẻ chỉ số Tuổi nợ Aging: 1-30 ngày (Vàng), 31-60 (Cam), >60 (Đỏ)**<br>`ThietKe3CardTuoiNoAgingUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.3) | 05/10/2026 | 06/10/2026 | 2 | 4h | 3 card hiển thị tổng số tiền và số lượng hóa đơn | ✅ Đã hoàn thành |
| **TASK-116** | **Xây dựng Bảng chi tiết hóa đơn nợ hiển thị số ngày quá hạn và phân loại màu**<br>`ThietKeBangChiTietCongNoUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.3) | 06/10/2026 | 07/10/2026 | 3 | 6h | Bảng danh sách chi tiết các khoản nợ quá hạn | ✅ Đã hoàn thành |
| **TASK-117** | **Thiết kế Modal Thu tiền nợ: Hiển thị số nợ còn lại và nhập số tiền thanh toán**<br>`ThietKeModalThuTienTraNoUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.2) | 07/10/2026 | 07/10/2026 | 2 | 5h | Modal popup thu nợ hỗ trợ chuyển khoản/tiền mặt | ✅ Đã hoàn thành |
| **TASK-118** | **Tích hợp Nút Nhắc nợ trực tiếp trên từng dòng và gửi thông báo Toast**<br>`NutNhacNoTuDongTrenTungDong_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.3) | 08/10/2026 | 08/10/2026 | 2 | 4h | Nút thao tác nhắc nợ có loading spinner | ✅ Đã hoàn thành |
| **TASK-119** | **Xây dựng chức năng Xuất báo cáo Tuổi nợ Aging Report ra file CSV**<br>`XuatBaoCaoTuoiNoRaCSV_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 3.3) | 09/10/2026 | 09/10/2026 | 2 | 3h | Nút Export Aging CSV xuất aging_report.csv | ✅ Đã hoàn thành |
| **TASK-120** | **Chuẩn bị khung giao diện hiển thị 4 Card KPI và 2 biểu đồ cho Dashboard**<br>`ChuanBiKhungDashboardKPI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 4.2) | 10/10/2026 | 11/10/2026 | 2 | 5h | Layout khung cho Chart.js trên index.html | ✅ Đã hoàn thành |
| **TASK-121** | **Xây dựng Model Payment (amount, paymentDate, paymentMethod, referenceNo)**<br>`ThietKeModelPayment_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 05/10/2026 | 05/10/2026 | 2 | 4h | File models/Payment.js hoàn chỉnh | ✅ Đã hoàn thành |
| **TASK-122** | **Cấu hình quan hệ Invoice 1 - N Payment trong Sequelize ORM**<br>`ThietLapQuanHeInvoiceVaPayment_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 05/10/2026 | 06/10/2026 | 2 | 4h | Ràng buộc InvoiceId trong bảng Payments | ✅ Đã hoàn thành |
| **TASK-123** | **Viết bộ kiểm thử tự động Thanh toán trừ dần nợ và chống trả vượt quá số nợ**<br>`BoKiemThuTuDong_ThanhToanTruNo_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 3.4) | 06/10/2026 | 07/10/2026 | 2 | 5h | Test suite cho Payment và remainingAmount | ✅ Đã hoàn thành |
| **TASK-124** | **Viết bộ kiểm thử tự động Thuật toán phân loại Tuổi nợ Aging chính xác**<br>`BoKiemThuTuDong_PhanTichTuoiNo_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 3.4) | 07/10/2026 | 08/10/2026 | 2 | 5h | Test suite xác minh 3 bucket 1-30, 31-60, >60 | ✅ Đã hoàn thành |
| **TASK-125** | **Tạo chỉ mục Database Indexes tối ưu tốc độ truy vấn cho dueDate và status**<br>`TaoIndexToiUuTruyVanDueDate_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 2.1) | 09/10/2026 | 10/10/2026 | 2 | 4h | Migration script tạo index tăng tốc query nợ | ✅ Đã hoàn thành |
| **TASK-126** | **Lập báo cáo kiểm thử Acceptance Criteria Sprint 2 gửi Trưởng nhóm PM**<br>`BaoCaoKiemThuSprint2_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 3.4) | 10/10/2026 | 11/10/2026 | 1 | 3h | Báo cáo QA Sprint 2 đạt 100% test case pass | ✅ Đã hoàn thành |

---

### 🗓️ TUẦN 5 (Sprint 3)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-127** | **Điều phối tiến độ Sprint 3 Dashboard & Báo cáo theo kế hoạch WBS 4**<br>`DieuPhoiTienDoSprint3Dashboard_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 4) | 12/10/2026 | 12/10/2026 | 2 | 4h | Bảng theo dõi công việc Sprint 3 chi tiết | ✅ Đã hoàn thành |
| **TASK-128** | **Kiểm soát rủi ro không đồng nhất số liệu giữa Dashboard và Hóa đơn**<br>`KiemSoatRuiRoDongNhatDuLieu_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 4) | 13/10/2026 | 14/10/2026 | 2 | 4h | Biện pháp đối soát số liệu CSDL tập trung | ✅ Đã hoàn thành |
| **TASK-129** | **Theo dõi ngân sách chi phí Sprint 3 (kế hoạch 9.000.000 VNĐ)**<br>`TheoDoiChiPhiSprint3_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 4) | 14/10/2026 | 15/10/2026 | 1 | 3h | Bảng theo dõi chi phí nhân sự WBS 4.1 - 4.4 | ✅ Đã hoàn thành |
| **TASK-130** | **Tổ chức họp Sprint 3 Review nghiệm thu Dashboard và tính năng xuất dữ liệu**<br>`HopSprint3ReviewNghiemThu_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 4.4) | 17/10/2026 | 17/10/2026 | 2 | 4h | Biên bản nghiệm thu hoàn tất 13 Story Points | ✅ Đã hoàn thành |
| **TASK-131** | **Tổ chức họp Sprint 3 Retrospective đánh giá hiệu năng đồ họa biểu đồ**<br>`HopSprint3Retrospective_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 4.4) | 17/10/2026 | 18/10/2026 | 1 | 3h | Bảng đúc kết kinh nghiệm tối ưu Chart.js | ✅ Đã hoàn thành |
| **TASK-132** | **Chuẩn bị kế hoạch Sprint 4: Thông báo Email, Tối ưu & Đóng gói Staging**<br>`ChuanBiKeHoachSprint4_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5) | 18/10/2026 | 18/10/2026 | 2 | 4h | Kế hoạch Sprint 4 Backlog và nhân lực | ✅ Đã hoàn thành |
| **TASK-133** | **Đặc tả các công thức tính tỷ lệ tài chính: Tỷ lệ thu hồi & Tỷ lệ nợ xấu quá hạn**<br>`DacTaCongThucTyLeTaiChinh_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 4.1) | 12/10/2026 | 12/10/2026 | 2 | 4h | Công thức Collection Rate và Overdue Rate | ✅ Đã hoàn thành |
| **TASK-134** | **Đặc tả thuật toán xếp hạng Top 5 doanh nghiệp nợ nhiều nhất cần đòi**<br>`DacTaXepHangTop5Debtors_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 4.1) | 13/10/2026 | 13/10/2026 | 2 | 3h | Tiêu chí xếp hạng nợ theo số tiền còn lại | ✅ Đã hoàn thành |
| **TASK-135** | **Đặc tả cơ cấu ngành nghề doanh nghiệp (IT, Fintech, E-commerce, Viễn thông)**<br>`DacTaCoCauNganhNgheKhachHang_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 4.1) | 13/10/2026 | 14/10/2026 | 2 | 4h | Phân loại nhóm ngành phục vụ biểu đồ tròn | ✅ Đã hoàn thành |
| **TASK-136** | **Viết User Story US-11 cho Dashboard Quản trị và Giám đốc điều hành**<br>`VietUserStoryUS11Dashboard_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 4.1) | 14/10/2026 | 15/10/2026 | 2 | 4h | User Story US-11 kèm Acceptance Criteria | ✅ Đã hoàn thành |
| **TASK-137** | **Xây dựng kịch bản kiểm thử chấp nhận UAT cho Dashboard và Biểu đồ thống kê**<br>`KichBanUAT_DashboardBieuDo_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 4.4) | 15/10/2026 | 16/10/2026 | 2 | 4h | Bộ kịch bản UAT-04 kiểm tra số liệu Dashboard | ✅ Đã hoàn thành |
| **TASK-138** | **Thực hiện nghiệm thu tính nhất quán số liệu giữa Dashboard và Hóa đơn**<br>`NghiemThuNhatQuanSoLieuDashboard_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 4.4) | 16/10/2026 | 17/10/2026 | 2 | 4h | Biên bản nghiệm thu số liệu khớp 100% | ✅ Đã hoàn thành |
| **TASK-139** | **Viết hàm tính Tổng doanh thu đã thu thực tế từ CSDL**<br>`TongHopTongDoanhThuDaThu_phamson` | Phạm Văn Sơn (BE) | Dashboard<br>(WBS 4.1) | 12/10/2026 | 12/10/2026 | 2 | 4h | Truy vấn aggregate sum(paidAmount) | ✅ Đã hoàn thành |
| **TASK-140** | **Viết hàm tính Tổng công nợ phải thu AR và Tổng nợ quá hạn**<br>`TongHopTongCongNoPhaiThuAR_phamson` | Phạm Văn Sơn (BE) | Dashboard<br>(WBS 4.1) | 12/10/2026 | 13/10/2026 | 2 | 4h | Truy vấn aggregate sum(remainingAmount) | ✅ Đã hoàn thành |
| **TASK-141** | **Viết hàm đếm tổng số vị trí đã tuyển dụng thành công Placement**<br>`DemSoDealTuyenDungThanhCong_phamson` | Phạm Văn Sơn (BE) | Dashboard<br>(WBS 4.1) | 13/10/2026 | 13/10/2026 | 1 | 3h | Truy vấn đếm tổng số deal placement | ✅ Đã hoàn thành |
| **TASK-142** | **Viết hàm tính Tỷ lệ thu hồi nợ (%) và Tỷ lệ nợ quá hạn (%)**<br>`TinhTyLeThuHoiVaNoQuaHan_phamson` | Phạm Văn Sơn (BE) | Dashboard<br>(WBS 4.1) | 13/10/2026 | 14/10/2026 | 2 | 4h | Logic tính toán tỷ lệ tài chính chính xác | ✅ Đã hoàn thành |
| **TASK-143** | **Xây dựng logic gom nhóm và tính doanh thu thực tế theo 12 tháng từ bảng Payment**<br>`TinhDoanhThuThucTeTheo12Thang_phamson` | Phạm Văn Sơn (BE) | Dashboard<br>(WBS 4.1) | 14/10/2026 | 15/10/2026 | 3 | 7h | Mảng doanh thu 12 tháng trả về cho biểu đồ | ✅ Đã hoàn thành |
| **TASK-144** | **Xây dựng logic phân tích tỷ lệ khách hàng theo ngành nghề (IT, Viễn thông...)**<br>`ThongKeCoCauKhachHangTheoNganh_phamson` | Phạm Văn Sơn (BE) | Dashboard<br>(WBS 4.1) | 15/10/2026 | 16/10/2026 | 2 | 5h | Mảng tỷ lệ phần trăm các ngành nghề | ✅ Đã hoàn thành |
| **TASK-145** | **Xây dựng logic lọc và trả về Top 5 doanh nghiệp nợ nhiều nhất**<br>`Top5DoanhNghiepNoNhieuNhat_phamson` | Phạm Văn Sơn (BE) | Dashboard<br>(WBS 4.1) | 16/10/2026 | 16/10/2026 | 2 | 4h | Mảng Top 5 đối tác nợ lớn nhất kèm chi tiết | ✅ Đã hoàn thành |
| **TASK-146** | **Thiết kế 4 Thẻ KPI Dashboard với hiệu ứng gradient và icon hiện đại**<br>`ThietKe4CardKPIDashboardUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 4.2) | 12/10/2026 | 13/10/2026 | 2 | 5h | 4 card KPI: Đã thu, Tổng nợ, Quá hạn, Placements | ✅ Đã hoàn thành |
| **TASK-147** | **Thiết kế 2 Thanh tiến trình hiển thị Tỷ lệ thu hồi nợ và Tỷ lệ nợ quá hạn**<br>`ThietKe2TheTyLeThuHoiVaNoXau_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 4.2) | 13/10/2026 | 14/10/2026 | 2 | 4h | Progress bar có nhãn % và màu cảnh báo | ✅ Đã hoàn thành |
| **TASK-148** | **Tích hợp thư viện Chart.js vẽ Biểu đồ đường Doanh thu 12 tháng mượt mà**<br>`VeBieuDoDuongDoanhThuTheoThang_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 4.2) | 14/10/2026 | 15/10/2026 | 3 | 7h | Line Chart doanh thu có tooltip hiển thị tiền tệ | ✅ Đã hoàn thành |
| **TASK-149** | **Vẽ Biểu đồ tròn Doughnut Chart thể hiện Cơ cấu ngành nghề đối tác**<br>`VeBieuDoTronCoCauNganhNghe_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 4.2) | 15/10/2026 | 15/10/2026 | 2 | 5h | Doughnut Chart phối màu theo Palette chuẩn | ✅ Đã hoàn thành |
| **TASK-150** | **Thiết kế Bảng Top 5 Con Nợ lớn nhất kèm nút xem chi tiết nhanh**<br>`ThietKeBangTop5DebtorsTrenDashboard_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 4.2) | 15/10/2026 | 16/10/2026 | 2 | 4h | Bảng Top Debtors với số tiền format VNĐ | ✅ Đã hoàn thành |
| **TASK-151** | **Tạo Nút Làm mới Dữ liệu Dashboard với hiệu ứng xoay loading mượt**<br>`NutLamMoiDuLieuDashboard_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 4.2) | 16/10/2026 | 16/10/2026 | 1 | 3h | Nút Refresh gọi lại API và cập nhật chart | ✅ Đã hoàn thành |
| **TASK-152** | **Tối ưu hóa hiển thị giao diện Dashboard Responsive trên màn hình di động**<br>`ToiUuGiaoDienDashboardResponsive_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 4.2) | 16/10/2026 | 17/10/2026 | 2 | 5h | Layout tự động co giãn đẹp mắt trên Mobile/Tablet | ✅ Đã hoàn thành |
| **TASK-153** | **Viết bộ kiểm thử tự động kiểm tra tính toán số liệu thống kê Dashboard**<br>`BoKiemThuTuDong_DashboardStats_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 4.4) | 12/10/2026 | 13/10/2026 | 2 | 5h | Test suite kiểm tra API /api/dashboard/stats | ✅ Đã hoàn thành |
| **TASK-154** | **Kiểm thử đối soát mảng doanh thu 12 tháng khớp 100% các bản ghi Payment**<br>`KiemThuDoiSoatDoanhThu12Thang_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 4.4) | 14/10/2026 | 15/10/2026 | 2 | 4h | Test case đối soát tổng doanh thu từng tháng | ✅ Đã hoàn thành |
| **TASK-155** | **Kiểm thử đối chiếu danh sách Top 5 Debtors khớp với hóa đơn quá hạn**<br>`KiemThuTop5DebtorsKhopHoaDon_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 4.4) | 15/10/2026 | 16/10/2026 | 2 | 4h | Test case kiểm tra thứ tự sắp xếp nợ giảm dần | ✅ Đã hoàn thành |
| **TASK-156** | **Đo lường thời gian phản hồi API Dashboard đảm bảo tải dưới 500ms**<br>`DoLuongThoiGianPhanHoiDashboard_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 4.4) | 16/10/2026 | 17/10/2026 | 1 | 3h | Báo cáo Performance Test API Dashboard | ✅ Đã hoàn thành |
| **TASK-157** | **Tổng hợp Báo cáo kiểm thử Sprint 3 bàn giao cho Trưởng nhóm**<br>`TongHopBaoCaoKiemThuSprint3_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 4.4) | 17/10/2026 | 18/10/2026 | 1 | 3h | Báo cáo chất lượng Sprint 3 hoàn chỉnh | ✅ Đã hoàn thành |

---

### 🗓️ TUẦN 6 (Sprint 4)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-158** | **Khởi động Sprint 4 hoàn tất dự án theo kế hoạch WBS 5**<br>`KhoiDongSprint4_HoanTatDuAn_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5) | 19/10/2026 | 19/10/2026 | 2 | 4h | Kế hoạch Sprint 4 chi tiết và phân công nhân sự | ✅ Đã hoàn thành |
| **TASK-159** | **Theo dõi ngân sách chi phí Sprint 4 (kế hoạch 7.500.000 VNĐ)**<br>`TheoDoiChiPhiSprint4_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5) | 19/10/2026 | 22/10/2026 | 2 | 4h | Bảng theo dõi chi phí nhân sự WBS 5.1 - 5.4 | ✅ Đã hoàn thành |
| **TASK-160** | **Giám sát tích hợp hệ thống tổng thể và chuẩn bị môi trường Staging Demo**<br>`GiamSatTichHopVaStagingDemo_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.2) | 21/10/2026 | 23/10/2026 | 2 | 5h | Môi trường Staging sẵn sàng demo cho giảng viên | ✅ Đã hoàn thành |
| **TASK-161** | **Rà soát ma trận rủi ro cập nhật và kiểm tra quỹ dự phòng 4.5 triệu VNĐ**<br>`RaSoatMaTranRuiRoCapNhat_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 6) | 23/10/2026 | 24/10/2026 | 2 | 4h | Sổ đăng ký rủi ro Risk Register cập nhật lần cuối | ✅ Đã hoàn thành |
| **TASK-162** | **Tổ chức họp bàn giao sản phẩm kỹ thuật trước buổi nghiệm thu chính thức**<br>`HopBanGiaoSanPhamKyThuat_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 24/10/2026 | 25/10/2026 | 1 | 3h | Biên bản bàn giao sản phẩm giữa các thành viên | ✅ Đã hoàn thành |
| **TASK-163** | **Tổng kết đánh giá hiệu quả phối hợp và mức độ hoàn thành nhiệm vụ Sprint 4**<br>`TongKetDanhGiaSprint4_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 25/10/2026 | 25/10/2026 | 1 | 3h | Báo cáo nghiệm thu hoàn thành 5 Story Points Sprint 4 | ✅ Đã hoàn thành |
| **TASK-164** | **Đặc tả mẫu nội dung email thông báo phát hành hóa đơn và email nhắc nợ**<br>`DacTaMauEmailThongBaoVaNhacNo_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.1) | 19/10/2026 | 20/10/2026 | 2 | 4h | Nội dung template email chuyên nghiệp | ✅ Đã hoàn thành |
| **TASK-165** | **Đặc tả phân hệ Cổng thông tin Khách hàng (Client Portal) tra cứu riêng**<br>`DacTaPhanHeClientPortal_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.1) | 20/10/2026 | 21/10/2026 | 2 | 5h | Tài liệu đặc tả FR-PORTAL-01 & 02 | ✅ Đã hoàn thành |
| **TASK-166** | **Đặc tả danh mục các hành động nghiệp vụ bắt buộc phải ghi vết Audit Log**<br>`DacTaHanhDongBatBuocAuditLog_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.1) | 21/10/2026 | 22/10/2026 | 2 | 4h | Bảng ma trận hành động và phân hệ Audit Log | ✅ Đã hoàn thành |
| **TASK-167** | **Cập nhật và hoàn thiện tài liệu Đặc tả BRD & SRS v5.0 chính thức**<br>`HoanThienBRD_SRS_v5_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.4) | 22/10/2026 | 23/10/2026 | 3 | 8h | File BRD-SRS_GOODY_QLHDCN_CHUC_NANG_THEO_SOURCE_v5.docx | ✅ Đã hoàn thành |
| **TASK-168** | **Xây dựng kịch bản kiểm thử chấp nhận người dùng UAT toàn diện hệ thống**<br>`XayDungKichBanUATToanDien_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.3) | 23/10/2026 | 24/10/2026 | 3 | 6h | Bộ tài liệu UAT đầy đủ từ Auth -> Deal -> Hóa đơn -> Nợ | ✅ Đã hoàn thành |
| **TASK-169** | **Hỗ trợ người dùng thử nghiệm và ghi nhận phản hồi đóng góp (Feedback Log)**<br>`HoTroNguoiDungThuNghiemFeedback_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.3) | 24/10/2026 | 25/10/2026 | 2 | 4h | Bảng tổng hợp ý kiến người dùng và đề xuất | ✅ Đã hoàn thành |
| **TASK-170** | **Xây dựng Module gửi Email thông báo hóa đơn và Nhắc nợ (Mock/SMTP)**<br>`ModuleGuiEmailThongBaoVaNhacNo_phamson` | Phạm Văn Sơn (BE) | Thông báo & Tối ưu<br>(WBS 5.1) | 19/10/2026 | 20/10/2026 | 3 | 7h | Module gửi email với Nodemailer / Mock Logger | ✅ Đã hoàn thành |
| **TASK-171** | **Xây dựng Model AuditLog lưu vết lịch sử: userId, action, entity, details, ip**<br>`ThietKeModelAuditLog_phamson` | Phạm Văn Sơn (BE) | Audit & Bảo mật<br>(WBS 5.1) | 20/10/2026 | 21/10/2026 | 2 | 4h | Model models/AuditLog.js chuẩn xác | ✅ Đã hoàn thành |
| **TASK-172** | **Xây dựng API Lấy lịch sử nhật ký Audit Log GET /api/audit (tối đa 100 dòng)**<br>`API_LayLichSuAuditLog_phamson` | Phạm Văn Sơn (BE) | Audit & Bảo mật<br>(WBS 5.1) | 21/10/2026 | 21/10/2026 | 2 | 4h | Endpoint GET /api/audit hỗ trợ phân trang | ✅ Đã hoàn thành |
| **TASK-173** | **Tích hợp ghi vết Audit Log tự động cho các hành động Login, Khách hàng, Deal, Hóa đơn, Nợ**<br>`TichHopGhiLogMoiHanhDong_phamson` | Phạm Văn Sơn (BE) | Audit & Bảo mật<br>(WBS 5.1) | 21/10/2026 | 22/10/2026 | 3 | 6h | Tự động tạo record audit khi thực thi controller | ✅ Đã hoàn thành |
| **TASK-174** | **Xây dựng API Cổng tra cứu cho doanh nghiệp B2B theo mã số thuế và mã bảo mật**<br>`API_ClientPortalTraCuuNo_phamson` | Phạm Văn Sơn (BE) | Khách hàng B2B<br>(WBS 5.1) | 22/10/2026 | 23/10/2026 | 2 | 5h | Endpoint tra cứu dữ liệu hóa đơn riêng biệt | ✅ Đã hoàn thành |
| **TASK-175** | **Áp dụng Parameterized Query chống SQL Injection tuyệt đối qua Sequelize**<br>`ChongSQLInjectionQuaSequelize_phamson` | Phạm Văn Sơn (BE) | Bảo mật<br>(WBS 5.2) | 23/10/2026 | 24/10/2026 | 2 | 4h | Mã nguồn backend an toàn 100% trước SQLi | ✅ Đã hoàn thành |
| **TASK-176** | **Viết Dockerfile và docker-compose.yml đóng gói ứng dụng phục vụ Deploy Staging**<br>`DongGoiUngDungDockerCompose_phamson` | Phạm Văn Sơn (BE) | DevOps & Staging<br>(WBS 5.2) | 24/10/2026 | 25/10/2026 | 2 | 5h | File Dockerfile và docker-compose.yml chạy một lệnh | ✅ Đã hoàn thành |
| **TASK-177** | **Xây dựng Giao diện Trang Nhật ký Audit Log audit.html chuyên nghiệp**<br>`ThietKeGiaoDienBangAuditLogUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.1) | 19/10/2026 | 20/10/2026 | 3 | 6h | Trang public/audit.html có filter và badges | ✅ Đã hoàn thành |
| **TASK-178** | **Thiết kế huy hiệu màu sắc cho các hành động Audit Log (Tạo, Sửa, Xóa, Nhắc nợ)**<br>`HienThiBadgeHanhDongAuditLog_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.1) | 20/10/2026 | 21/10/2026 | 2 | 4h | Badges sắc nét phân biệt thao tác người dùng | ✅ Đã hoàn thành |
| **TASK-179** | **Xây dựng Giao diện Cổng tra cứu riêng cho Khách hàng portal.html**<br>`ThietKeGiaoDienClientPortal_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.1) | 21/10/2026 | 22/10/2026 | 2 | 5h | Trang portal tra cứu hóa đơn không cần đăng nhập | ✅ Đã hoàn thành |
| **TASK-180** | **Tối ưu hóa hiệu ứng tương tác Micro-interactions và thông báo Toast trên UI**<br>`ToiUuHieuUngToastVaMicroInteractions_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.2) | 22/10/2026 | 23/10/2026 | 2 | 4h | Hiệu ứng chuyển trang mượt và thông báo Toast đẹp mắt | ✅ Đã hoàn thành |
| **TASK-181** | **Kiểm thử khả năng tương thích hiển thị trên các trình duyệt Chrome, Edge, Firefox**<br>`KiemTraTuongThichTrinhDuyetWeb_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.3) | 23/10/2026 | 24/10/2026 | 2 | 4h | Giao diện hiển thị chuẩn xác trên cả 3 trình duyệt | ✅ Đã hoàn thành |
| **TASK-182** | **Tối ưu hóa dung lượng CSS, JS và font chữ giảm thời gian tải trang dưới 1 giây**<br>`ToiUuDungLuongFrontendAsset_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.2) | 24/10/2026 | 24/10/2026 | 1 | 3h | Trang tải nhanh đạt điểm Google Lighthouse cao | ✅ Đã hoàn thành |
| **TASK-183** | **Chụp ảnh màn hình các phân hệ giao diện phục vụ tài liệu User Manual**<br>`ChupAnhManHinhGiaoDienUserManual_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.4) | 25/10/2026 | 25/10/2026 | 1 | 3h | Bộ ảnh chụp chất lượng cao các màn hình hệ thống | ✅ Đã hoàn thành |
| **TASK-184** | **Viết bộ kiểm thử tự động Ghi nhật ký thao tác Audit Log đầy đủ trường thông tin**<br>`BoKiemThuTuDong_AuditLog_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.3) | 19/10/2026 | 20/10/2026 | 2 | 4h | Test suite kiểm tra API /api/audit | ✅ Đã hoàn thành |
| **TASK-185** | **Xây dựng kịch bản kiểm thử tự động toàn trình End-to-End từ Deal đến Thu nợ**<br>`KiemThuTuDongToanTrinhE2E_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.3) | 21/10/2026 | 22/10/2026 | 3 | 7h | Test E2E bao phủ toàn bộ luồng nghiệp vụ chính | ✅ Đã hoàn thành |
| **TASK-186** | **Kiểm thử bảo mật API: Không lộ mật khẩu hash, kiểm tra quyền RBAC mọi endpoint**<br>`KiemThuBaoMatAPI_RBAC_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.3) | 22/10/2026 | 23/10/2026 | 2 | 4h | Báo cáo Security Assessment API an toàn | ✅ Đã hoàn thành |
| **TASK-187** | **Thực hiện phân tích Pareto nguyên nhân trễ hạn công nợ và rủi ro phần mềm**<br>`PhanTichParetoRuiRoVaNguyenNhanNo_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.3) | 23/10/2026 | 24/10/2026 | 2 | 5h | File HuynhNguyenVinhPhuc_Pareto.xlsx hoàn chỉnh | ✅ Đã hoàn thành |
| **TASK-188** | **Thiết lập script sao lưu và phục hồi CSDL tự động (Backup & Restore script)**<br>`ThietLapScriptBackupRestoreDB_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 5.2) | 24/10/2026 | 25/10/2026 | 2 | 4h | Script sao lưu tự động CSDL SQLite/PostgreSQL | ✅ Đã hoàn thành |
| **TASK-189** | **Cấu hình lệnh npm test chạy toàn bộ test suite và đo Code Coverage đạt 85%**<br>`CauHinhLenhNpmTestToanBo_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.3) | 25/10/2026 | 25/10/2026 | 1 | 3h | Lệnh npm test chạy pass 100% 7 bộ test suites | ✅ Đã hoàn thành |

---

### 🗓️ TUẦN 7 (Nghiệm thu & Báo cáo)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-190** | **Soạn thảo Báo cáo tổng kết dự án Project Closing Report theo chuẩn PMBOK**<br>`SoanThaoBaoCaoProjectClosing_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 3 | 6h | Tài liệu Project Closing Report hoàn chỉnh | ✅ Đã hoàn thành |
| **TASK-191** | **Lập bảng đối chiếu 4 mục tiêu SMART ban đầu với kết quả thực tế đạt được**<br>`DoiChieuMucTieuSMARTThucTe_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Bảng nghiệm thu 4/4 mục tiêu SMART đạt 100% | ✅ Đã hoàn thành |
| **TASK-192** | **Hoàn thiện tài liệu Báo cáo Đồ án Quản lý dự án QLDA_Nhom10_Lab.docx**<br>`HoanThienBaoCaoQLDA_Docx_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 3 | 8h | File QLDA_Nhom10_Lab.docx đầy đủ các chương | ✅ Đã hoàn thành |
| **TASK-193** | **Vẽ biểu đồ Gantt Chart tiến độ thực tế 4 Sprint trên Microsoft Excel**<br>`VeBieuDoGanttChartTienDoExcel_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 5h | Biểu đồ Gantt Chart tiến độ 7 tuần | ✅ Đã hoàn thành |
| **TASK-194** | **Tổng hợp Slide thuyết trình bảo vệ đồ án kết thúc học phần Nhóm 10**<br>`TongHopSlideBaoCaoBaoVeDoAn_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 6h | Slide thuyết trình PowerPoint/Canva chuyên nghiệp | ✅ Đã hoàn thành |
| **TASK-195** | **Biên soạn Cẩm nang Hướng dẫn sử dụng phần mềm User Manual chi tiết**<br>`BienSoanUserManualChiTiet_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 3 | 8h | Tài liệu User Manual có hình ảnh minh họa | ✅ Đã hoàn thành |
| **TASK-196** | **Soạn tài liệu hướng dẫn nghiệp vụ chuyên biệt cho Kế toán và Recruiter**<br>`SoanHuongDanNghiepVuKeToanRecruiter_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Cẩm nang hướng dẫn thao tác theo từng vai trò | ✅ Đã hoàn thành |
| **TASK-197** | **Cập nhật Product Backlog giai đoạn 2 cho các tính năng mở rộng tương lai**<br>`CapNhatBacklogChoGiaiDoanPhatTrien2_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Backlog giai đoạn 2 (Cổng thanh toán, Mobile) | ✅ Đã hoàn thành |
| **TASK-198** | **Tham gia diễn tập thuyết trình và demo kịch bản nghiệp vụ trực tiếp**<br>`DienTapThuyetTrinhDemoNghiepVu_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 3h | Kịch bản demo mượt mà không lỗi | ✅ Đã hoàn thành |
| **TASK-199** | **Kiểm tra rà soát Clean Code và tối ưu hóa toàn bộ controllers/routes**<br>`KiemTraCleanCodeBackend_phamson` | Phạm Văn Sơn (BE) | Kiến trúc & CSDL<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Mã nguồn sạch đẹp, đầy đủ chú thích | ✅ Đã hoàn thành |
| **TASK-200** | **Xuất bản bộ tài liệu API Documentation và Postman Collection kiểm thử**<br>`XuatBanTaiLieuAPIPostmanCollection_phamson` | Phạm Văn Sơn (BE) | Tài liệu kỹ thuật<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | File Postman Collection kèm môi trường mẫu | ✅ Đã hoàn thành |
| **TASK-201** | **Cập nhật hoàn chỉnh tài liệu hướng dẫn cài đặt và chạy trong README.md**<br>`CapNhatTaiLieuHuongDanReadme_phamson` | Phạm Văn Sơn (BE) | Tài liệu kỹ thuật<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 3h | File README.md hướng dẫn rõ ràng từ A-Z | ✅ Đã hoàn thành |
| **TASK-202** | **Tạo bản build triển khai production sẵn sàng chạy độc lập**<br>`TaoBanBuildProductionSanSang_phamson` | Phạm Văn Sơn (BE) | DevOps & Staging<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Gói release phần mềm v1.0.0 | ✅ Đã hoàn thành |
| **TASK-203** | **Trực kỹ thuật và hỗ trợ giải trình kiến trúc backend trong buổi bảo vệ**<br>`TrucKyThuatBaoVeBackend_phamson` | Phạm Văn Sơn (BE) | Bảo vệ đồ án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 3h | Sẵn sàng trả lời các câu hỏi kỹ thuật của hội đồng | ✅ Đã hoàn thành |
| **TASK-204** | **Kiểm tra toàn bộ liên kết điều hướng và tính đồng nhất giao diện 5 trang web**<br>`KiemTraLienKetDieuHuongDongNhat_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Hệ thống liên kết mượt mà không gãy link 404 | ✅ Đã hoàn thành |
| **TASK-205** | **Tinh chỉnh thông báo lỗi và trải nghiệm người dùng cuối thân thiện**<br>`TinhChinhThongBaoLoiNguoiDung_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 3h | Các thông báo lỗi bằng tiếng Việt rõ ràng, dễ hiểu | ✅ Đã hoàn thành |
| **TASK-206** | **Hỗ trợ chuẩn bị hình ảnh minh họa chất lượng cao cho Slide bảo vệ**<br>`HoTroHinhAnhSlideBaoVe_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 2h | Bộ asset hình ảnh đồ họa chất lượng sắc nét | ✅ Đã hoàn thành |
| **TASK-207** | **Thực hiện demo trực tiếp các luồng giao diện người dùng trước hội đồng**<br>`DemoGiaoDienTrucTiepHoiDong_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Bảo vệ đồ án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 3h | Phần trình diễn demo giao diện ấn tượng | ✅ Đã hoàn thành |
| **TASK-208** | **Chạy lần cuối toàn bộ test suite npm test đảm bảo 100% test pass**<br>`ChayFinalTestSuiteNpmTest_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 3h | Biên bản xác nhận 100% test case xanh lá | ✅ Đã hoàn thành |
| **TASK-209** | **Kiểm tra tính toàn vẹn dữ liệu CSDL sau các kịch bản demo kiểm thử**<br>`KiemTraToanVenCSDLSauDemo_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiến trúc & CSDL<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 3h | CSDL sạch, không có dữ liệu rác, quan hệ toàn vẹn | ✅ Đã hoàn thành |
| **TASK-210** | **Hoàn thiện bảng phân tích Pareto kiểm soát chất lượng đồ án**<br>`HoanThienBangPhanTichParetoDocx_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Biểu đồ Pareto kèm nhận xét và đề xuất cải tiến | ✅ Đã hoàn thành |
| **TASK-211** | **Đóng gói toàn bộ tài liệu Test Case, Test Log và Test Summary Report**<br>`DongGoiBoTaiLieuKiemThuQA_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Bộ hồ sơ QA & Testing hoàn chỉnh | ✅ Đã hoàn thành |
| **TASK-212** | **Hỗ trợ trả lời các câu hỏi về CSDL và quy trình đảm bảo chất lượng QA**<br>`TraLoiCauHoiCSDLVaQA_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Bảo vệ đồ án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 1 | 3h | Giải trình xuất sắc phần CSDL và Testing | ✅ Đã hoàn thành |

---

### 🗓️ TUẦN 6 (Sprint 4)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-213** | **Xây dựng cơ chế đổi mật khẩu cá nhân cho nhân viên PUT /api/auth/change-password**<br>`API_DoiMatKhauNguoiDung_phamson` | Phạm Văn Sơn (BE) | Xác thực RBAC<br>(WBS 5.1) | 22/10/2026 | 23/10/2026 | 2 | 4h | Endpoint đổi mật khẩu an toàn | ✅ Đã hoàn thành |
| **TASK-214** | **Xây dựng chức năng khóa / mở khóa tài khoản người dùng PUT /api/auth/users/:id/toggle**<br>`API_KhoaMoKhoaTaiKhoan_phamson` | Phạm Văn Sơn (BE) | Xác thực RBAC<br>(WBS 5.1) | 23/10/2026 | 24/10/2026 | 2 | 4h | Endpoint quản lý trạng thái tài khoản | ✅ Đã hoàn thành |
| **TASK-215** | **Tạo Modal Cập nhật thông tin Doanh nghiệp B2B và hạn mức công nợ Credit Limit**<br>`ThietKeModalChinhSuaKhachHangUI_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.1) | 22/10/2026 | 23/10/2026 | 2 | 4h | Modal cập nhật khách hàng đầy đủ | ✅ Đã hoàn thành |
| **TASK-216** | **Thêm Bộ lọc thời gian (Tháng này, Quý này, Năm nay) cho trang Dashboard dữ liệu**<br>`BoLocDashboardTheoThangQuyNam_nguyenhoangphuoc` | Nguyễn Hoàng Phước (FE) | Giao diện FE<br>(WBS 5.1) | 23/10/2026 | 24/10/2026 | 2 | 4h | Dropdown chọn thời gian tương tác realtime | ✅ Đã hoàn thành |
| **TASK-217** | **Đặc tả nghiệp vụ quản lý hạn mức công nợ Credit Limit và cảnh báo vượt hạn mức**<br>`DacTaQuanLyHanMucCongNo_nguyenxuandoan` | Nguyễn Xuân Đoàn (BA) | Nghiệp vụ BA<br>(WBS 5.1) | 21/10/2026 | 22/10/2026 | 2 | 4h | Tài liệu đặc tả hạn mức công nợ | ✅ Đã hoàn thành |
| **TASK-218** | **Xây dựng kịch bản kiểm thử tính năng cảnh báo khi khách hàng vượt hạn mức nợ**<br>`KiemThuCanhBaoVuotHanMucNo_huynhnguyenvinhphuc` | Huỳnh Nguyễn Vĩnh Phúc (DB/QA) | Kiểm thử QA<br>(WBS 5.3) | 23/10/2026 | 24/10/2026 | 2 | 4h | Test suite kiểm tra điều kiện Credit Limit | ✅ Đã hoàn thành |

---

### 🗓️ TUẦN 7 (Nghiệm thu & Báo cáo)

| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **TASK-219** | **Soạn thảo tài liệu Phân tích ma trận đánh giá năng lực nhóm và hiệu suất làm việc**<br>`PhanTichDanhGiaNangLucNhom_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Báo cáo đánh giá năng suất 5 thành viên | ✅ Đã hoàn thành |
| **TASK-220** | **Tổng hợp toàn bộ source code, cơ sở dữ liệu và tài liệu lên GitHub repository chính thức**<br>`TongHopSourceCodeTaiLieuLenGitHub_nguyenhuuphuc` | Nguyễn Hữu Phúc (PM) | Quản lý dự án<br>(WBS 5.4) | 26/10/2026 | 26/10/2026 | 2 | 4h | Repository GitHub chuẩn chỉnh, đầy đủ release tag | ✅ Đã hoàn thành |


---

## 🚀 HƯỚNG DẪN MỞ RỘNG VÀ THÊM TASK SAU NÀY (CHO TASK 221 TRỞ ĐI)
Hệ thống được thiết kế theo cấu trúc mở chuẩn Scrum/PMBOK. Khi có yêu cầu phát sinh hoặc mở rộng giai đoạn 2, nhóm tiến hành thêm task mới theo đúng template sau:

```markdown
| TASK-XXX | Tên Công Việc Chi Tiết<br>`TenTask_tenthanhvien` | Tên Thành Viên (Role) | Phân Hệ (WBS) | dd/mm/yyyy | dd/mm/yyyy | SP | Giờ | Deliverable bàn giao | Trạng thái |
```

**Các phân hệ mở rộng tiềm năng cho Giai đoạn 2:**
1. **Module Cổng thanh toán trực tuyến (Payment Gateway):** Tích hợp cổng VNPay / VietQR tự động gạch nợ hóa đơn khi khách hàng quét mã QR.
2. **Module Mobile App (React Native / Flutter):** Ứng dụng di động dành cho Recruiter theo dõi hoa hồng và Kế toán duyệt thanh toán.
3. **Module Phân tích AI Dự đoán Nợ Xấu (AI Predictive Debt Analytics):** Ứng dụng học máy dự báo xác suất trễ hạn thanh toán của khách hàng B2B dựa trên lịch sử giao dịch.

---
*Tài liệu được khởi tạo và lưu trữ chính thức tại kho mã nguồn dự án: `QLDA_NHOM10_GODDY`.*
