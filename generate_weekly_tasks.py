# -*- coding: utf-8 -*-
"""
Script tạo file Kế hoạch phân chia task theo tuần cho Đồ án Nhóm 10 GOODY
Bám sát BRD/SRS v5, Product Backlog xlsx, và Tài liệu WBS & Phân quyền nhóm 10
Xuất ra 2 định dạng:
1. KE_HOACH_PHAN_CHIA_TASK_THEO_TUAN.md
2. KE_HOACH_PHAN_CHIA_TASK_THEO_TUAN.xlsx
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

tasks = []

def add_task(week, sprint, tid, name, commit, assignee, module, wbs, start, end, sp, hours, deliverable, status):
    tasks.append({
        'week': week,
        'sprint': sprint,
        'tid': tid,
        'name': name,
        'commit': commit,
        'assignee': assignee,
        'module': module,
        'wbs': wbs,
        'start': start,
        'end': end,
        'sp': sp,
        'hours': hours,
        'deliverable': deliverable,
        'status': status
    })

# ==============================================================================
# TUẦN 1: 14/09/2026 - 20/09/2026 (Khởi tạo dự án, Khảo sát, BRD/SRS, Thiết kế CSDL & Khung Kiến trúc)
# ==============================================================================
# PM: Nguyễn Hữu Phúc (6 tasks)
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-001", "Soạn thảo Tuyên bố dự án (Project Charter) theo chuẩn PMBOK", "KhoiTaoProjectCharter_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1.1", "14/09/2026", "14/09/2026", 3, 8, "Văn bản Project Charter 8 mục hoàn chỉnh", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-002", "Xác lập 4 mục tiêu SMART về thời gian, chi phí, phạm vi và chất lượng", "XacLapMucTieuSMART_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1.1", "14/09/2026", "14/09/2026", 2, 4, "Bảng mục tiêu SMART và chỉ số đo lường", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-003", "Phân rã cấu trúc công việc WBS 3 cấp tuân thủ quy tắc 100% và 8/80", "PhanRaWBS3Cap_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1.3", "15/09/2026", "15/09/2026", 3, 8, "Sơ đồ và bảng WBS 6 gói công việc", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-004", "Thiết lập ma trận phân công trách nhiệm RACI cho 5 thành viên", "ThietLapMaTranRACI_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1.3", "15/09/2026", "15/09/2026", 2, 4, "Bảng ma trận RACI dự án Nhóm 10", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-005", "Dự toán ngân sách tổng thể 45 triệu và kế hoạch dự phòng 10%", "DuToanNganSachDuAn_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1.3", "15/09/2026", "15/09/2026", 2, 6, "Bảng dự toán chi phí theo WBS", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-006", "Tổ chức họp Kickoff dự án và phê duyệt Kế hoạch cơ sở (Milestone 1)", "HopKickoffPheDuyetKeHoach_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1.4", "15/09/2026", "15/09/2026", 1, 3, "Biên bản họp Kickoff và ký duyệt Kế hoạch", "Đã hoàn thành")

# BA: Nguyễn Xuân Đoàn (6 tasks)
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-007", "Khảo sát quy trình chốt deal và thu hồi công nợ doanh nghiệp Headhunt", "KhaoSatQuyTrinhHeadhunt_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 1.2", "14/09/2026", "14/09/2026", 3, 8, "Báo cáo khảo sát thực trạng nghiệp vụ", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-008", "Soạn thảo tài liệu đặc tả yêu cầu nghiệp vụ BRD & SRS v4.0", "SoanThaoBRD_SRS_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 1.2", "14/09/2026", "15/09/2026", 5, 12, "Tài liệu BRD-SRS v4.0 đầy đủ 12 mục", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-009", "Xác định danh mục Business Rules BR-01 đến BR-07 cốt lõi", "XacDinhBusinessRules_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 1.2", "15/09/2026", "15/09/2026", 2, 4, "Bảng 7 quy tắc nghiệp vụ hệ thống", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-010", "Viết User Stories US-01 đến US-04 cho Module Auth, B2B và Tuyển dụng", "VietUserStoriesGiaiDoan1_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 2.1", "16/09/2026", "17/09/2026", 3, 6, "Tài liệu User Stories và Acceptance Criteria", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-011", "Xây dựng Product Backlog ban đầu trên Excel (PB-01 đến PB-14)", "XayDungProductBacklogExcel_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 1.2", "16/09/2026", "17/09/2026", 3, 6, "File GOODY_Product_Backlog.xlsx", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-012", "Định nghĩa tiêu chuẩn hoàn thành Definition of Done (DoD) cho User Story", "DinhNghiaTieuChuanDoD_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 2.1", "17/09/2026", "18/09/2026", 2, 4, "Bộ tiêu chí DoD kiểm thử chấp nhận", "Đã hoàn thành")

# BE: Phạm Văn Sơn (6 tasks)
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-013", "Khởi tạo repository Git và cấu trúc thư mục Node.js Express MVC chuẩn", "KhoiTaoCauTrucThuMucDuAn_phamson", "Phạm Văn Sơn (BE)", "Kiến trúc & CSDL", "WBS 2.2", "16/09/2026", "16/09/2026", 2, 4, "Cấu trúc thư mục controllers, models, routes", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-014", "Cấu hình Sequelize ORM kết nối CSDL SQLite portable và Supabase", "KetNoiCoSoDuLieuSequelize_phamson", "Phạm Văn Sơn (BE)", "Kiến trúc & CSDL", "WBS 2.2", "16/09/2026", "17/09/2026", 3, 6, "File config/database.js hoạt động mượt mà", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-015", "Cấu hình CORS, Express JSON Parser và URL-encoded parser", "CauHinhCorsVaExpressParser_phamson", "Phạm Văn Sơn (BE)", "Kiến trúc & CSDL", "WBS 2.2", "17/09/2026", "17/09/2026", 1, 2, "Middleware parser tích hợp trong server.js", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-016", "Cấu hình phục vụ Static Assets thư mục public cho Web Dashboard", "CauHinhPhucVuStaticAssetsPublic_phamson", "Phạm Văn Sơn (BE)", "Kiến trúc & CSDL", "WBS 2.2", "17/09/2026", "18/09/2026", 1, 2, "Route express.static cho public folder", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-017", "Thiết lập cấu hình biến môi trường an toàn với file .env", "ThietLapBienMoiTruongDotenv_phamson", "Phạm Văn Sơn (BE)", "Kiến trúc & CSDL", "WBS 2.2", "18/09/2026", "18/09/2026", 1, 2, "File .env và .env.example mẫu", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-018", "Xây dựng middleware xử lý lỗi tập trung Error Handling và format JSON chuẩn", "XayDungMiddlewareErrorHandler_phamson", "Phạm Văn Sơn (BE)", "Kiến trúc & CSDL", "WBS 2.2", "18/09/2026", "19/09/2026", 2, 4, "Middleware errorHandler trả format { success, error }", "Đã hoàn thành")

# FE: Nguyễn Hoàng Phước (6 tasks)
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-019", "Phác thảo Wireframe Prototype UI hệ thống trên Figma", "ThietKeWireframeFigmaUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.1", "16/09/2026", "17/09/2026", 3, 8, "Bản thiết kế Figma các màn hình cốt lõi", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-020", "Xây dựng Design System, biến CSS Token và bảng màu Slate/Indigo hiện đại", "XayDungDesignSystemCssToken_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.1", "17/09/2026", "18/09/2026", 2, 6, "File public/css/style.css định nghĩa biến chuẩn", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-021", "Dựng khung bố cục giao diện dùng chung Layout: Sidebar + Top Header", "DungKhungBoCucSidebarHeader_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "18/09/2026", "19/09/2026", 2, 6, "Khung Sidebar có nav link và badge thông báo", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-022", "Tạo trang khung Dashboard dữ liệu skeleton index.html", "TaoTrangDashboardSkeleton_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "19/09/2026", "19/09/2026", 2, 4, "Giao diện khung ban đầu public/index.html", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-023", "Tạo trang khung Quản lý Khách hàng skeleton clients.html", "TaoTrangKhachHangSkeleton_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "19/09/2026", "20/09/2026", 2, 4, "Giao diện khung ban đầu public/clients.html", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-024", "Tích hợp icon thư viện Lucide / FontAwesome và Google Font Inter", "TichHopFontVaIcons_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.1", "20/09/2026", "20/09/2026", 1, 2, "Giao diện hiển thị font chữ Inter sắc nét", "Đã hoàn thành")

# QA/DB: Huỳnh Nguyễn Vĩnh Phúc (6 tasks)
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-025", "Thiết kế Sơ đồ quan hệ thực thể ERD 8 bảng dữ liệu quan hệ", "ThietKeSoDoQuanHeERD_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "16/09/2026", "17/09/2026", 3, 8, "File ERD_QLDA_NHOM10_GODDY.drawio", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-026", "Viết script DDL database_supabase_postgres.sql và database_sqlserver.sql", "VietScriptDDLPostgresSqlserver_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "17/09/2026", "17/09/2026", 3, 6, "Script SQL khởi tạo bảng, khóa chính, khóa ngoại", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-027", "Xây dựng Model User (username, email, password, role, isActive)", "ThietKeModelUser_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.2", "17/09/2026", "18/09/2026", 2, 4, "File models/User.js hoàn chỉnh", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-028", "Xây dựng Model Client (companyName, taxCode, netDays, contactPerson)", "ThietKeModelClient_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.2", "18/09/2026", "18/09/2026", 2, 4, "File models/Client.js đầy đủ trường", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-029", "Viết script tự động nạp dữ liệu mẫu seed data doanh nghiệp công nghệ", "VietScriptNapDuLieuMauEnterprise_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.2", "18/09/2026", "19/09/2026", 2, 4, "Seed script nạp sẵn FPT, VNG, Shopee, Viettel", "Đã hoàn thành")
add_task("Tuần 1", "Khởi tạo & Sprint 1", "TASK-030", "Cài đặt framework kiểm thử tự động Jest/Supertest và viết test kết nối CSDL", "CaiDatTestingJestKiemTraDB_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 2.4", "19/09/2026", "20/09/2026", 2, 4, "Bộ test tests/unit.test.js kiểm tra đồng bộ CSDL", "Đã hoàn thành")

# ==============================================================================
# TUẦN 2: 21/09/2026 - 27/09/2026 (Hoàn tất Sprint 1: Auth RBAC, B2B Clients, Tuyển dụng & Deal Placement)
# ==============================================================================
# PM: Nguyễn Hữu Phúc (6 tasks)
add_task("Tuần 2", "Sprint 1", "TASK-031", "Điều phối phiên họp Sprint 1 Planning và gán Story Points PB-01 -> PB-04", "DieuPhoiHopSprint1Planning_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1", "21/09/2026", "21/09/2026", 2, 4, "Kế hoạch Sprint 1 Backlog và phân chia công việc", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-032", "Theo dõi tiến độ commit git hàng ngày theo cú pháp TenTask_tenthanhvien", "TheoDoiTienDoCommitHangNgay_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1", "21/09/2026", "25/09/2026", 2, 6, "Bảng theo dõi số lượng commit của từng thành viên", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-033", "Rà soát rủi ro xung đột dữ liệu giữa Client và Deal Placement", "RaSoatRuiRoXungDotDuLieu_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1", "22/09/2026", "23/09/2026", 2, 4, "Ghi nhận Risk Log và biện pháp giảm thiểu", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-034", "Kiểm tra chất lượng mã nguồn tuân thủ coding convention nhóm", "KiemTraChatLuongCodeSprint1_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1", "24/09/2026", "25/09/2026", 2, 4, "Báo cáo Code Review Sprint 1", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-035", "Tổ chức họp Sprint 1 Review nghiệm thu tính năng Khách hàng & Tuyển dụng", "HopSprint1ReviewNghiemThu_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 2.4", "26/09/2026", "26/09/2026", 2, 4, "Biên bản nghiệm thu hoàn thành 18 Story Points", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-036", "Tổ chức họp Sprint 1 Retrospective rút kinh nghiệm quy trình phối hợp", "HopSprint1Retrospective_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 2.4", "26/09/2026", "27/09/2026", 1, 3, "Bảng đúc kết bài học What went well / Need improvement", "Đã hoàn thành")

# BA: Nguyễn Xuân Đoàn (6 tasks)
add_task("Tuần 2", "Sprint 1", "TASK-037", "Đặc tả chi tiết các yêu cầu chức năng FR-AUTH-01 đến 06 cho phân hệ RBAC", "DacTaChiTietFR_AUTH_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 2.1", "21/09/2026", "21/09/2026", 2, 4, "Tài liệu đặc tả FR-AUTH 3 vai trò", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-038", "Đặc tả chi tiết các yêu cầu chức năng FR-CUS-01 đến 07 cho Khách hàng B2B", "DacTaChiTietFR_CUS_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 2.1", "21/09/2026", "22/09/2026", 2, 4, "Tài liệu đặc tả nghiệp vụ Client B2B", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-039", "Đặc tả chi tiết các yêu cầu chức năng FR-REC-01 đến 07 cho Tuyển dụng & Deal", "DacTaChiTietFR_REC_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 2.1", "22/09/2026", "23/09/2026", 3, 6, "Tài liệu đặc tả Job, Candidate & Placement", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-040", "Xác định công thức tính phí hoa hồng Headhunt và quy tắc bảo hành 60 ngày", "XacDinhCongThucPhiVaBaoHanh_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 2.1", "23/09/2026", "23/09/2026", 2, 4, "Công thức serviceFee và warrantyEndDate", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-041", "Xây dựng kịch bản kiểm thử chấp nhận UAT cho phân hệ Khách hàng B2B", "XayDungKichBanUAT_Client_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 2.4", "24/09/2026", "25/09/2026", 2, 4, "Kịch bản UAT-01 kiểm tra Client và MST", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-042", "Thực hiện nghiệm thu chấp nhận người dùng UAT cho chốt Deal Placement", "NghiemThuUAT_DealPlacement_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 2.4", "25/09/2026", "26/09/2026", 2, 4, "Biên bản nghiệm thu UAT-02 Deal Placement", "Đã hoàn thành")

# BE: Phạm Văn Sơn (7 tasks)
add_task("Tuần 2", "Sprint 1", "TASK-043", "Cài đặt thư viện bcryptjs và viết hàm băm mật khẩu độ muối 10 rounds", "VietHamMaHoaMatKhauBcrypt_phamson", "Phạm Văn Sơn (BE)", "Xác thực RBAC", "WBS 2.2", "21/09/2026", "21/09/2026", 2, 4, "Hàm hashPassword và comparePassword", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-044", "Viết API Đăng nhập hệ thống POST /api/auth/login cấp JWT token 7 ngày", "API_DangNhapHeThong_phamson", "Phạm Văn Sơn (BE)", "Xác thực RBAC", "WBS 2.2", "21/09/2026", "22/09/2026", 3, 6, "Endpoint POST /api/auth/login hoàn chỉnh", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-045", "Viết Middleware verifyToken và requireRole phân quyền 3 cấp Admin/Kế toán/Recruiter", "MiddlewarePhanQuyenTheoVaiTro_phamson", "Phạm Văn Sơn (BE)", "Xác thực RBAC", "WBS 2.2", "22/09/2026", "22/09/2026", 3, 6, "Middleware middlewares/auth.js", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-046", "Viết API Đăng ký tài khoản POST /api/auth/register chặn trùng username", "API_DangKyNhanVienMoi_phamson", "Phạm Văn Sơn (BE)", "Xác thực RBAC", "WBS 2.2", "22/09/2026", "23/09/2026", 2, 4, "Endpoint POST /api/auth/register", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-047", "Xây dựng trọn bộ API CRUD Khách hàng B2B /api/clients kèm validate MST", "API_QuanLyKhachHangB2B_phamson", "Phạm Văn Sơn (BE)", "Khách hàng B2B", "WBS 2.2", "23/09/2026", "24/09/2026", 3, 8, "Routes routes/clients.js đầy đủ GET, POST, PUT, DELETE", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-048", "Xây dựng API Quản lý Vị trí tuyển dụng Job và Hồ sơ Ứng viên Candidate", "API_QuanLyJobVaCandidate_phamson", "Phạm Văn Sơn (BE)", "Tuyển dụng", "WBS 2.2", "24/09/2026", "25/09/2026", 3, 6, "Routes Job và Candidate trong routes/recruitment.js", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-049", "Xây dựng API Chốt Deal Tuyển dụng POST /api/recruitment/placements", "API_GhiNhanDealTuyenDungMoi_phamson", "Phạm Văn Sơn (BE)", "Tuyển dụng", "WBS 2.2", "25/09/2026", "26/09/2026", 3, 8, "Endpoint POST /api/recruitment/placements tự tính fee", "Đã hoàn thành")

# FE: Nguyễn Hoàng Phước (7 tasks)
add_task("Tuần 2", "Sprint 1", "TASK-050", "Thiết kế màn hình Đăng nhập login.html lưu trữ JWT vào localStorage", "ThietKeGiaoDienDangNhap_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "21/09/2026", "21/09/2026", 2, 5, "Trang public/login.html thẩm mỹ, có validate", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-051", "Cơ chế phân quyền giao diện: Tự động ẩn/hiện menu theo vai trò người dùng", "PhanQuyenGiaoDienTheoRole_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "22/09/2026", "22/09/2026", 2, 4, "Script phân quyền UI theo role Admin/Kế toán", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-052", "Xây dựng Bảng danh sách Khách hàng B2B clients.html kèm ô tìm kiếm realtime", "ThietKeBangDanhSachKhachHangUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "23/09/2026", "23/09/2026", 3, 6, "Bảng hiển thị đối tác, số thuế, Net days", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-053", "Thiết kế Modal Thêm mới Đối tác Doanh nghiệp kèm kiểm tra dữ liệu đầu vào", "ThietKeModalThemKhachHangMoiUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "23/09/2026", "24/09/2026", 2, 5, "Modal popup nhập MST, Tên công ty, Email", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-054", "Xây dựng chức năng Xuất danh sách khách hàng ra file CSV", "XuatDanhSachKhachHangRaCSV_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "24/09/2026", "24/09/2026", 2, 4, "Nút Export CSV xuất file client_list.csv", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-055", "Xây dựng Bảng danh sách Deal Tuyển dụng và Huy hiệu trạng thái bảo hành", "ThietKeBangDanhSachDealUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "25/09/2026", "25/09/2026", 2, 5, "Bảng Placement với badge thời hạn bảo hành", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-056", "Thiết kế Modal Chốt Deal: Tự động tải Job theo Khách hàng và ước tính phí", "ThietKeModalChotDealPlacementUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 2.3", "25/09/2026", "26/09/2026", 3, 6, "Modal chốt deal tính nhanh phí hoa hồng", "Đã hoàn thành")

# QA/DB: Huỳnh Nguyễn Vĩnh Phúc (6 tasks)
add_task("Tuần 2", "Sprint 1", "TASK-057", "Xây dựng Model Job và Model Candidate với ràng buộc khóa ngoại ClientId", "ThietKeModelJobVaCandidate_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "21/09/2026", "22/09/2026", 2, 5, "Files models/Job.js và models/Candidate.js", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-058", "Xây dựng Model Placement ghi nhận thỏa thuận tuyển dụng và quan hệ dữ liệu", "ThietKeModelPlacement_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "22/09/2026", "22/09/2026", 2, 4, "File models/Placement.js cấu hình quan hệ", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-059", "Viết bộ kiểm thử tự động xác thực Đăng nhập/Đăng ký và cấp Token JWT", "BoKiemThuTuDong_AuthJWT_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 2.4", "23/09/2026", "24/09/2026", 2, 4, "Test suite cho /api/auth pass 100%", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-060", "Viết bộ kiểm thử tự động Thêm khách hàng, chặn trùng MST và xóa an toàn", "BoKiemThuTuDong_ThemKhachHang_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 2.4", "24/09/2026", "25/09/2026", 2, 4, "Test suite cho Client MST validation", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-061", "Viết bộ kiểm thử tự động Chốt Deal Placement và tính ngày hết hạn bảo hành", "BoKiemThuTuDong_ChotDealPlacement_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 2.4", "25/09/2026", "26/09/2026", 2, 4, "Test suite cho Placement fee và warranty", "Đã hoàn thành")
add_task("Tuần 2", "Sprint 1", "TASK-062", "Đo lường độ bao phủ kiểm thử Code Coverage Sprint 1 đạt trên 80%", "DoLuongCodeCoverageSprint1_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 2.4", "26/09/2026", "27/09/2026", 1, 3, "Báo cáo Jest Coverage Report Sprint 1", "Đã hoàn thành")

# ==============================================================================
# TUẦN 3: 28/09/2026 - 04/10/2026 (Sprint 2 - Phần 1: Hóa đơn Invoicing, Thuế VAT 8%, Mẫu in PDF & Thanh toán)
# ==============================================================================
# PM: Nguyễn Hữu Phúc (6 tasks)
add_task("Tuần 3", "Sprint 2", "TASK-063", "Khởi động Sprint 2: Phân công hạng mục Hóa đơn Invoicing & Thu hồi công nợ", "KhoiDongSprint2_Invoicing_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3", "28/09/2026", "28/09/2026", 2, 4, "Bảng phân công Sprint 2 WBS 3.1 & 3.2", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-064", "Theo dõi ngân sách chi phí Sprint 2 (kế hoạch 9.000.000 VNĐ)", "TheoDoiNganSachChiPhiSprint2_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3", "28/09/2026", "02/10/2026", 2, 4, "Bảng theo dõi dòng tiền và chi phí thực tế", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-065", "Kiểm soát thay đổi phạm vi Scope Creep trong logic tự sinh mã hóa đơn", "KiemSoatThayDoiScopeInvoicing_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3", "29/09/2026", "30/09/2026", 2, 4, "Tài liệu Scope Baseline cập nhật", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-066", "Tổ chức họp giao ban Daily Standup giải quyết vướng mắc xuất file PDF", "HopDailyGiaiQuyetXuatPDF_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3", "30/09/2026", "01/10/2026", 1, 3, "Biên bản gỡ nút thắt in hóa đơn PDF", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-067", "Kiểm tra mốc tiến độ Milestone 2: Hoàn tất phân hệ Hóa đơn Invoicing", "KiemTraMilestone2HoaDon_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3.1", "02/10/2026", "03/10/2026", 2, 4, "Biên bản nghiệm thu Milestone 2", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-068", "Đánh giá tiến độ hoàn thành các task của 5 thành viên qua git commit", "DanhGiaTienDoCommitTuan3_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3", "03/10/2026", "04/10/2026", 1, 3, "Báo cáo kiểm soát tiến độ Tuần 3", "Đã hoàn thành")

# BA: Nguyễn Xuân Đoàn (6 tasks)
add_task("Tuần 3", "Sprint 2", "TASK-069", "Đặc tả yêu cầu chức năng FR-INV-01 đến 09 cho phân hệ Hóa đơn", "DacTaChiTietFR_INV_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.1", "28/09/2026", "28/09/2026", 2, 4, "Tài liệu đặc tả phát hành hóa đơn VAT", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-070", "Quy định định dạng sinh mã hóa đơn tự động duy nhất INV-YYYY-XXXX", "QuyDinhMaHoaDonTuDong_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.1", "28/09/2026", "29/09/2026", 2, 3, "Quy tắc sinh số hóa đơn chuẩn kế toán", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-071", "Đặc tả công thức tính thuế GTGT 8% và tính Ngày đến hạn dueDate theo Net Days", "DacTaCongThucVATVaDueDate_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.1", "29/09/2026", "29/09/2026", 2, 4, "Công thức vatAmount và dueDate", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-072", "Đặc tả yêu cầu mẫu in hóa đơn GTGT tiêu chuẩn điện tử và xuất PDF", "DacTaMauInHoaDonDienTu_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.1", "30/09/2026", "01/10/2026", 2, 4, "Đặc tả bố cục hóa đơn A4 chuẩn", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-073", "Đặc tả quy trình thanh toán từng đợt FR-PAY và trừ dần nợ remainingAmount", "DacTaQuyTrinhThanhToanFR_PAY_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.2", "01/10/2026", "02/10/2026", 2, 4, "Quy tắc đổi trạng thái Sent/Partial/Paid", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-074", "Xây dựng kịch bản kiểm thử nghiệp vụ cho quy trình xuất hóa đơn từ Deal", "KichBanKiemThuHoaDonTuDeal_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.1", "02/10/2026", "03/10/2026", 2, 4, "Bộ Test Scenario UAT Invoicing", "Đã hoàn thành")

# BE: Phạm Văn Sơn (7 tasks)
add_task("Tuần 3", "Sprint 2", "TASK-075", "Viết API Lấy danh sách hóa đơn GET /api/invoices kèm thông tin Client và Placement", "API_LayDanhSachHoaDon_phamson", "Phạm Văn Sơn (BE)", "Hóa đơn & Invoicing", "WBS 3.1", "28/09/2026", "28/09/2026", 2, 5, "Endpoint GET /api/invoices với include models", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-076", "Xây dựng thuật toán sinh mã hóa đơn tự động duy nhất INV-YYYY-XXXX", "HamSinhMaHoaDonTuDong_phamson", "Phạm Văn Sơn (BE)", "Hóa đơn & Invoicing", "WBS 3.1", "28/09/2026", "29/09/2026", 2, 4, "Hàm generateInvoiceNumber đảm bảo tính tuần tự", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-077", "Xây dựng hàm tính thuế VAT 8% (vatAmount) và tổng tiền thanh toán (totalAmount)", "HamTinhTienThueVAT8PhanTram_phamson", "Phạm Văn Sơn (BE)", "Hóa đơn & Invoicing", "WBS 3.1", "29/09/2026", "29/09/2026", 2, 4, "Logic tính thuế VAT chuẩn xác không làm tròn sai", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-078", "Viết logic tính ngày đến hạn dueDate = issueDate + client.netDays", "TuDongGanHanThanhToanTheoNetDays_phamson", "Phạm Văn Sơn (BE)", "Hóa đơn & Invoicing", "WBS 3.1", "29/09/2026", "30/09/2026", 2, 4, "Tính hạn thanh toán theo Net 15/30/45/60", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-079", "Viết API Phát hành hóa đơn từ Placement POST /api/invoices/from-placement", "API_PhatHanhHoaDonTuDealPlacement_phamson", "Phạm Văn Sơn (BE)", "Hóa đơn & Invoicing", "WBS 3.1", "30/09/2026", "01/10/2026", 3, 8, "Endpoint tạo hóa đơn tự động từ deal", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-080", "Thêm kiểm tra an toàn: Chặn phát hành nhiều hóa đơn cho cùng 1 deal placement", "ChanPhatHanhTrungHoaDonChoCung1Deal_phamson", "Phạm Văn Sơn (BE)", "Hóa đơn & Invoicing", "WBS 3.1", "01/10/2026", "02/10/2026", 2, 4, "Ràng buộc 1:1 bảo đảm không tạo trùng lặp", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-081", "Viết API Hủy hóa đơn PUT /api/invoices/:id/cancel (chặn hủy nếu đã thanh toán)", "API_HuyHoaDonDichVu_phamson", "Phạm Văn Sơn (BE)", "Hóa đơn & Invoicing", "WBS 3.1", "02/10/2026", "03/10/2026", 2, 4, "Endpoint hủy hóa đơn kèm kiểm tra paidAmount", "Đã hoàn thành")

# FE: Nguyễn Hoàng Phước (7 tasks)
add_task("Tuần 3", "Sprint 2", "TASK-082", "Xây dựng Giao diện Bảng quản lý hóa đơn invoices.html chuyên nghiệp", "ThietKeBangDanhSachHoaDonUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.1", "28/09/2026", "29/09/2026", 3, 7, "Giao diện public/invoices.html hiển thị tiền tệ VNĐ", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-083", "Thiết kế Huy hiệu trạng thái hóa đơn Sent (Lam), Partial (Cam), Paid (Lục), Overdue (Đỏ)", "HienThiHuyHieuTrangThaiHoaDon_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.1", "29/09/2026", "30/09/2026", 2, 4, "Badges màu sắc trực quan theo chuẩn UI", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-084", "Thiết kế Modal xem chi tiết hóa đơn theo mẫu Hóa đơn GTGT chuẩn doanh nghiệp", "ThietKeModalXemChiTietHoaDonUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.1", "30/09/2026", "01/10/2026", 3, 6, "Modal hiển thị đầy đủ MST bên bán, mua, chữ ký", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-085", "Viết CSS @media print tối ưu hóa hiển thị khi in ấn khổ giấy A4", "MauInHoaDonDienTuStandard_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.1", "01/10/2026", "01/10/2026", 2, 4, "Bố cục in chuẩn trang, ẩn thanh điều hướng", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-086", "Tích hợp tính năng In trực tiếp và Xuất PDF hóa đơn bằng window.print()", "ChucNangInHoaDonVaXuatPDF_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.1", "01/10/2026", "02/10/2026", 2, 4, "Nút In Hóa Đơn / Lưu PDF hoạt động mượt mà", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-087", "Thêm Bộ lọc hóa đơn theo trạng thái (Tất cả, Đã gửi, Trả 1 phần, Hoàn tất, Quá hạn)", "BoLocHoaDonTheoTrangThaiUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.1", "02/10/2026", "03/10/2026", 2, 4, "Dropdown lọc dữ liệu hóa đơn realtime", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-088", "Xây dựng chức năng Xuất toàn bộ danh sách hóa đơn ra file CSV", "XuatDanhSachHoaDonRaCSV_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.1", "03/10/2026", "03/10/2026", 2, 3, "Nút Export CSV xuất file invoices_list.csv", "Đã hoàn thành")

# QA/DB: Huỳnh Nguyễn Vĩnh Phúc (6 tasks)
add_task("Tuần 3", "Sprint 2", "TASK-089", "Xây dựng Model Invoice (invoiceNo, totalAmount, paidAmount, remainingAmount, status)", "ThietKeModelInvoice_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "28/09/2026", "29/09/2026", 2, 5, "File models/Invoice.js chuẩn trường dữ liệu", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-090", "Cấu hình quan hệ Placement 1 - 1 Invoice trong Sequelize ORM", "ThietLapQuanHePlacementVaInvoice_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "29/09/2026", "29/09/2026", 2, 4, "Ràng buộc foreign key PlacementId trong Invoice", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-091", "Viết bộ kiểm thử tự động Tính thuế VAT 8% và Tổng tiền hóa đơn", "BoKiemThuTuDong_PhatHanhHoaDon_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 3.4", "30/09/2026", "01/10/2026", 2, 4, "Test suite kiểm tra công thức VAT toán học", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-092", "Viết bộ kiểm thử tự động Chặn phát hành trùng hóa đơn trên cùng 1 deal", "BoKiemThuTuDong_ChanTrungHoaDon_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 3.4", "01/10/2026", "02/10/2026", 2, 4, "Test case trả lỗi 400 khi tạo hóa đơn lần 2", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-093", "Cập nhật seed data mẫu với các hóa đơn thực tế phát hành cho FPT, VNG, Shopee", "CapNhatSeedDataHoaDonMau_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.2", "02/10/2026", "03/10/2026", 2, 4, "Seed 6 hóa đơn với đầy đủ trạng thái khác nhau", "Đã hoàn thành")
add_task("Tuần 3", "Sprint 2", "TASK-094", "Kiểm tra tính toàn vẹn dữ liệu giữa Placement.fee và Invoice.subtotal", "KiemTraToanVenDuLieuFeeVaSubtotal_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 3.4", "03/10/2026", "04/10/2026", 1, 3, "Test case đối soát khớp số tiền 100%", "Đã hoàn thành")

# ==============================================================================
# TUẦN 4: 05/10/2026 - 11/10/2026 (Sprint 2 - Phần 2 & Khởi động Sprint 3: Tuổi nợ Aging, Nhắc nợ, Nghiệm thu Sprint 2)
# ==============================================================================
# PM: Nguyễn Hữu Phúc (6 tasks)
add_task("Tuần 4", "Sprint 2 & 3", "TASK-095", "Điều phối nghiệm thu các hạng mục công nợ & tuổi nợ WBS 3.3 và 3.4", "DieuPhoiNghiemThuCongNoAging_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3", "05/10/2026", "06/10/2026", 2, 4, "Biên bản rà soát phân hệ Tuổi nợ", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-096", "Tổ chức họp Sprint 2 Review và đánh giá đạt 18 Story Points cam kết", "HopSprint2ReviewNghiemThu_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3.4", "07/10/2026", "07/10/2026", 2, 4, "Biên bản nghiệm thu hoàn tất Sprint 2", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-097", "Tổ chức họp Sprint 2 Retrospective nâng cao hiệu suất xử lý logic thanh toán", "HopSprint2Retrospective_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 3.4", "07/10/2026", "08/10/2026", 1, 3, "Báo cáo cải tiến quy trình kỹ thuật", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-098", "Khởi động Sprint 3: Phân công xây dựng Dashboard KPI và Báo cáo trực quan", "KhoiDongSprint3_Dashboard_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 4", "08/10/2026", "08/10/2026", 2, 4, "Kế hoạch Sprint 3 Backlog (PB-10, 11, 14)", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-099", "Cập nhật đường găng Critical Path và phân tích độ trễ Slack của dự án", "CapNhatDuongGangCriticalPath_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1", "09/10/2026", "10/10/2026", 2, 5, "Bảng tính toán ES, EF, LS, LF, Slack", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-100", "Đánh giá các chỉ số giá trị thu được EVM (PV, EV, AC, SPI, CPI) giữa kỳ", "DanhGiaChiSoEVMGiuaKy_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 1", "10/10/2026", "11/10/2026", 2, 5, "Báo cáo phân tích hiệu suất tài chính EVM", "Đã hoàn thành")

# BA: Nguyễn Xuân Đoàn (6 tasks)
add_task("Tuần 4", "Sprint 2 & 3", "TASK-101", "Đặc tả yêu cầu chức năng FR-AGE-01 đến 05 cho phân tích tuổi nợ 3 bucket", "DacTaChiTietFR_AGE_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.3", "05/10/2026", "05/10/2026", 2, 4, "Tài liệu đặc tả 3 xô tuổi nợ (1-30, 31-60, >60)", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-102", "Đặc tả chức năng gửi thông báo nhắc nợ khách hàng FR-REM-01 & 02", "DacTaThongBaoNhacNoFR_REM_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.3", "05/10/2026", "06/10/2026", 2, 4, "Đặc tả mẫu lời nhắc nợ và tần suất gửi", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-103", "Viết User Stories US-08 (Thanh toán), US-09 (Aging), US-10 (Nhắc nợ)", "VietUserStoriesGiaiDoan2_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.3", "06/10/2026", "07/10/2026", 2, 5, "Bộ User Stories & Acceptance Criteria chi tiết", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-104", "Khảo sát và đặc tả các chỉ số KPI cần hiển thị trên Dashboard tuyển dụng", "DacTaKPIDashboardTuyenDung_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 4.1", "08/10/2026", "09/10/2026", 2, 4, "Tài liệu đặc tả FR-DASH-01 đến 07", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-105", "Đặc tả thuật toán gom doanh thu thực tế theo 12 tháng từ các đợt thanh toán", "DacTaDoanhThu12Thang_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 4.1", "09/10/2026", "10/10/2026", 2, 4, "Quy tắc thống kê doanh thu theo thời gian", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-106", "Thực hiện nghiệm thu chấp nhận UAT cho quy trình thanh toán và phân loại tuổi nợ", "NghiemThuUAT_ThanhToanVaAging_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 3.4", "10/10/2026", "11/10/2026", 2, 4, "Biên bản nghiệm thu UAT-03 Công nợ Aging", "Đã hoàn thành")

# BE: Phạm Văn Sơn (7 tasks)
add_task("Tuần 4", "Sprint 2 & 3", "TASK-107", "Xây dựng API Thu tiền thanh toán nợ POST /api/debt/payment", "API_GhiNhanThanhToanCongNo_phamson", "Phạm Văn Sơn (BE)", "Công nợ & Aging", "WBS 3.2", "05/10/2026", "05/10/2026", 3, 7, "Endpoint POST /api/debt/payment lưu bảng Payment", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-108", "Kiểm tra chặt chẽ số tiền thanh toán: Bắt buộc > 0 và không vượt remainingAmount", "ValidateSoTienTraKhongVuotQuaNo_phamson", "Phạm Văn Sơn (BE)", "Công nợ & Aging", "WBS 3.2", "05/10/2026", "06/10/2026", 2, 4, "Chặn overpayment trả về mã lỗi 400", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-109", "Cập nhật trừ dần nợ: paidAmount += pay, remainingAmount -= pay và đổi trạng thái", "TuDongTruDanDuNoHoaDon_phamson", "Phạm Văn Sơn (BE)", "Công nợ & Aging", "WBS 3.2", "06/10/2026", "06/10/2026", 2, 5, "Logic tự chuyển trạng thái Paid hoặc Partial", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-110", "Xây dựng API Tổng hợp công nợ và phân loại tuổi nợ GET /api/debt/overview", "API_BaoCaoTongHopCongNo_phamson", "Phạm Văn Sơn (BE)", "Công nợ & Aging", "WBS 3.3", "06/10/2026", "07/10/2026", 3, 8, "Endpoint GET /api/debt/overview trả 3 xô tuổi nợ", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-111", "Thuật toán tính số ngày quá hạn và phân nhóm tự động 1-30, 31-60, >60 ngày", "PhanTichTuoiNo3XoTuDong_phamson", "Phạm Văn Sơn (BE)", "Công nợ & Aging", "WBS 3.3", "07/10/2026", "07/10/2026", 2, 5, "Logic so khớp dueDate với ngày hiện tại", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-112", "Viết API Gửi thông báo nhắc nợ POST /api/debt/remind ghi nhận thời điểm nhắc", "API_GuiThongBaoNhacNo_phamson", "Phạm Văn Sơn (BE)", "Công nợ & Aging", "WBS 3.3", "08/10/2026", "09/10/2026", 2, 4, "Endpoint nhắc nợ kèm ghi nhận Audit Log", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-113", "Bắt đầu xây dựng API Thống kê KPI Dashboard GET /api/dashboard/stats", "API_LaySoLieuTongHopDashboard_phamson", "Phạm Văn Sơn (BE)", "Dashboard", "WBS 4.1", "09/10/2026", "11/10/2026", 3, 7, "Khung API thống kê số liệu tổng hợp ban đầu", "Đã hoàn thành")

# FE: Nguyễn Hoàng Phước (7 tasks)
add_task("Tuần 4", "Sprint 2 & 3", "TASK-114", "Thiết kế Giao diện Quản lý Công nợ debt.html đồng bộ hệ thống", "ThietKeGiaoDienQuanLyCongNoUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.3", "05/10/2026", "05/10/2026", 3, 6, "Trang public/debt.html trực quan, hiện đại", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-115", "Thiết kế 3 Thẻ chỉ số Tuổi nợ Aging: 1-30 ngày (Vàng), 31-60 (Cam), >60 (Đỏ)", "ThietKe3CardTuoiNoAgingUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.3", "05/10/2026", "06/10/2026", 2, 4, "3 card hiển thị tổng số tiền và số lượng hóa đơn", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-116", "Xây dựng Bảng chi tiết hóa đơn nợ hiển thị số ngày quá hạn và phân loại màu", "ThietKeBangChiTietCongNoUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.3", "06/10/2026", "07/10/2026", 3, 6, "Bảng danh sách chi tiết các khoản nợ quá hạn", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-117", "Thiết kế Modal Thu tiền nợ: Hiển thị số nợ còn lại và nhập số tiền thanh toán", "ThietKeModalThuTienTraNoUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.2", "07/10/2026", "07/10/2026", 2, 5, "Modal popup thu nợ hỗ trợ chuyển khoản/tiền mặt", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-118", "Tích hợp Nút Nhắc nợ trực tiếp trên từng dòng và gửi thông báo Toast", "NutNhacNoTuDongTrenTungDong_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.3", "08/10/2026", "08/10/2026", 2, 4, "Nút thao tác nhắc nợ có loading spinner", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-119", "Xây dựng chức năng Xuất báo cáo Tuổi nợ Aging Report ra file CSV", "XuatBaoCaoTuoiNoRaCSV_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 3.3", "09/10/2026", "09/10/2026", 2, 3, "Nút Export Aging CSV xuất aging_report.csv", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-120", "Chuẩn bị khung giao diện hiển thị 4 Card KPI và 2 biểu đồ cho Dashboard", "ChuanBiKhungDashboardKPI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 4.2", "10/10/2026", "11/10/2026", 2, 5, "Layout khung cho Chart.js trên index.html", "Đã hoàn thành")

# QA/DB: Huỳnh Nguyễn Vĩnh Phúc (6 tasks)
add_task("Tuần 4", "Sprint 2 & 3", "TASK-121", "Xây dựng Model Payment (amount, paymentDate, paymentMethod, referenceNo)", "ThietKeModelPayment_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "05/10/2026", "05/10/2026", 2, 4, "File models/Payment.js hoàn chỉnh", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-122", "Cấu hình quan hệ Invoice 1 - N Payment trong Sequelize ORM", "ThietLapQuanHeInvoiceVaPayment_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "05/10/2026", "06/10/2026", 2, 4, "Ràng buộc InvoiceId trong bảng Payments", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-123", "Viết bộ kiểm thử tự động Thanh toán trừ dần nợ và chống trả vượt quá số nợ", "BoKiemThuTuDong_ThanhToanTruNo_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 3.4", "06/10/2026", "07/10/2026", 2, 5, "Test suite cho Payment và remainingAmount", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-124", "Viết bộ kiểm thử tự động Thuật toán phân loại Tuổi nợ Aging chính xác", "BoKiemThuTuDong_PhanTichTuoiNo_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 3.4", "07/10/2026", "08/10/2026", 2, 5, "Test suite xác minh 3 bucket 1-30, 31-60, >60", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-125", "Tạo chỉ mục Database Indexes tối ưu tốc độ truy vấn cho dueDate và status", "TaoIndexToiUuTruyVanDueDate_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 2.1", "09/10/2026", "10/10/2026", 2, 4, "Migration script tạo index tăng tốc query nợ", "Đã hoàn thành")
add_task("Tuần 4", "Sprint 2 & 3", "TASK-126", "Lập báo cáo kiểm thử Acceptance Criteria Sprint 2 gửi Trưởng nhóm PM", "BaoCaoKiemThuSprint2_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 3.4", "10/10/2026", "11/10/2026", 1, 3, "Báo cáo QA Sprint 2 đạt 100% test case pass", "Đã hoàn thành")

# ==============================================================================
# TUẦN 5: 12/10/2026 - 18/10/2026 (Sprint 3 hoàn thiện: Dashboard KPI, Biểu đồ Doanh thu 12 tháng, Cơ cấu ngành, Top 5 Debtors)
# ==============================================================================
# PM: Nguyễn Hữu Phúc (6 tasks)
add_task("Tuần 5", "Sprint 3", "TASK-127", "Điều phối tiến độ Sprint 3 Dashboard & Báo cáo theo kế hoạch WBS 4", "DieuPhoiTienDoSprint3Dashboard_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 4", "12/10/2026", "12/10/2026", 2, 4, "Bảng theo dõi công việc Sprint 3 chi tiết", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-128", "Kiểm soát rủi ro không đồng nhất số liệu giữa Dashboard và Hóa đơn", "KiemSoatRuiRoDongNhatDuLieu_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 4", "13/10/2026", "14/10/2026", 2, 4, "Biện pháp đối soát số liệu CSDL tập trung", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-129", "Theo dõi ngân sách chi phí Sprint 3 (kế hoạch 9.000.000 VNĐ)", "TheoDoiChiPhiSprint3_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 4", "14/10/2026", "15/10/2026", 1, 3, "Bảng theo dõi chi phí nhân sự WBS 4.1 - 4.4", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-130", "Tổ chức họp Sprint 3 Review nghiệm thu Dashboard và tính năng xuất dữ liệu", "HopSprint3ReviewNghiemThu_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 4.4", "17/10/2026", "17/10/2026", 2, 4, "Biên bản nghiệm thu hoàn tất 13 Story Points", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-131", "Tổ chức họp Sprint 3 Retrospective đánh giá hiệu năng đồ họa biểu đồ", "HopSprint3Retrospective_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 4.4", "17/10/2026", "18/10/2026", 1, 3, "Bảng đúc kết kinh nghiệm tối ưu Chart.js", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-132", "Chuẩn bị kế hoạch Sprint 4: Thông báo Email, Tối ưu & Đóng gói Staging", "ChuanBiKeHoachSprint4_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5", "18/10/2026", "18/10/2026", 2, 4, "Kế hoạch Sprint 4 Backlog và nhân lực", "Đã hoàn thành")

# BA: Nguyễn Xuân Đoàn (6 tasks)
add_task("Tuần 5", "Sprint 3", "TASK-133", "Đặc tả các công thức tính tỷ lệ tài chính: Tỷ lệ thu hồi & Tỷ lệ nợ xấu quá hạn", "DacTaCongThucTyLeTaiChinh_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 4.1", "12/10/2026", "12/10/2026", 2, 4, "Công thức Collection Rate và Overdue Rate", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-134", "Đặc tả thuật toán xếp hạng Top 5 doanh nghiệp nợ nhiều nhất cần đòi", "DacTaXepHangTop5Debtors_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 4.1", "13/10/2026", "13/10/2026", 2, 3, "Tiêu chí xếp hạng nợ theo số tiền còn lại", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-135", "Đặc tả cơ cấu ngành nghề doanh nghiệp (IT, Fintech, E-commerce, Viễn thông)", "DacTaCoCauNganhNgheKhachHang_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 4.1", "13/10/2026", "14/10/2026", 2, 4, "Phân loại nhóm ngành phục vụ biểu đồ tròn", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-136", "Viết User Story US-11 cho Dashboard Quản trị và Giám đốc điều hành", "VietUserStoryUS11Dashboard_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 4.1", "14/10/2026", "15/10/2026", 2, 4, "User Story US-11 kèm Acceptance Criteria", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-137", "Xây dựng kịch bản kiểm thử chấp nhận UAT cho Dashboard và Biểu đồ thống kê", "KichBanUAT_DashboardBieuDo_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 4.4", "15/10/2026", "16/10/2026", 2, 4, "Bộ kịch bản UAT-04 kiểm tra số liệu Dashboard", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-138", "Thực hiện nghiệm thu tính nhất quán số liệu giữa Dashboard và Hóa đơn", "NghiemThuNhatQuanSoLieuDashboard_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 4.4", "16/10/2026", "17/10/2026", 2, 4, "Biên bản nghiệm thu số liệu khớp 100%", "Đã hoàn thành")

# BE: Phạm Văn Sơn (7 tasks)
add_task("Tuần 5", "Sprint 3", "TASK-139", "Viết hàm tính Tổng doanh thu đã thu thực tế từ CSDL", "TongHopTongDoanhThuDaThu_phamson", "Phạm Văn Sơn (BE)", "Dashboard", "WBS 4.1", "12/10/2026", "12/10/2026", 2, 4, "Truy vấn aggregate sum(paidAmount)", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-140", "Viết hàm tính Tổng công nợ phải thu AR và Tổng nợ quá hạn", "TongHopTongCongNoPhaiThuAR_phamson", "Phạm Văn Sơn (BE)", "Dashboard", "WBS 4.1", "12/10/2026", "13/10/2026", 2, 4, "Truy vấn aggregate sum(remainingAmount)", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-141", "Viết hàm đếm tổng số vị trí đã tuyển dụng thành công Placement", "DemSoDealTuyenDungThanhCong_phamson", "Phạm Văn Sơn (BE)", "Dashboard", "WBS 4.1", "13/10/2026", "13/10/2026", 1, 3, "Truy vấn đếm tổng số deal placement", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-142", "Viết hàm tính Tỷ lệ thu hồi nợ (%) và Tỷ lệ nợ quá hạn (%)", "TinhTyLeThuHoiVaNoQuaHan_phamson", "Phạm Văn Sơn (BE)", "Dashboard", "WBS 4.1", "13/10/2026", "14/10/2026", 2, 4, "Logic tính toán tỷ lệ tài chính chính xác", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-143", "Xây dựng logic gom nhóm và tính doanh thu thực tế theo 12 tháng từ bảng Payment", "TinhDoanhThuThucTeTheo12Thang_phamson", "Phạm Văn Sơn (BE)", "Dashboard", "WBS 4.1", "14/10/2026", "15/10/2026", 3, 7, "Mảng doanh thu 12 tháng trả về cho biểu đồ", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-144", "Xây dựng logic phân tích tỷ lệ khách hàng theo ngành nghề (IT, Viễn thông...)", "ThongKeCoCauKhachHangTheoNganh_phamson", "Phạm Văn Sơn (BE)", "Dashboard", "WBS 4.1", "15/10/2026", "16/10/2026", 2, 5, "Mảng tỷ lệ phần trăm các ngành nghề", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-145", "Xây dựng logic lọc và trả về Top 5 doanh nghiệp nợ nhiều nhất", "Top5DoanhNghiepNoNhieuNhat_phamson", "Phạm Văn Sơn (BE)", "Dashboard", "WBS 4.1", "16/10/2026", "16/10/2026", 2, 4, "Mảng Top 5 đối tác nợ lớn nhất kèm chi tiết", "Đã hoàn thành")

# FE: Nguyễn Hoàng Phước (7 tasks)
add_task("Tuần 5", "Sprint 3", "TASK-146", "Thiết kế 4 Thẻ KPI Dashboard với hiệu ứng gradient và icon hiện đại", "ThietKe4CardKPIDashboardUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 4.2", "12/10/2026", "13/10/2026", 2, 5, "4 card KPI: Đã thu, Tổng nợ, Quá hạn, Placements", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-147", "Thiết kế 2 Thanh tiến trình hiển thị Tỷ lệ thu hồi nợ và Tỷ lệ nợ quá hạn", "ThietKe2TheTyLeThuHoiVaNoXau_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 4.2", "13/10/2026", "14/10/2026", 2, 4, "Progress bar có nhãn % và màu cảnh báo", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-148", "Tích hợp thư viện Chart.js vẽ Biểu đồ đường Doanh thu 12 tháng mượt mà", "VeBieuDoDuongDoanhThuTheoThang_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 4.2", "14/10/2026", "15/10/2026", 3, 7, "Line Chart doanh thu có tooltip hiển thị tiền tệ", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-149", "Vẽ Biểu đồ tròn Doughnut Chart thể hiện Cơ cấu ngành nghề đối tác", "VeBieuDoTronCoCauNganhNghe_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 4.2", "15/10/2026", "15/10/2026", 2, 5, "Doughnut Chart phối màu theo Palette chuẩn", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-150", "Thiết kế Bảng Top 5 Con Nợ lớn nhất kèm nút xem chi tiết nhanh", "ThietKeBangTop5DebtorsTrenDashboard_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 4.2", "15/10/2026", "16/10/2026", 2, 4, "Bảng Top Debtors với số tiền format VNĐ", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-151", "Tạo Nút Làm mới Dữ liệu Dashboard với hiệu ứng xoay loading mượt", "NutLamMoiDuLieuDashboard_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 4.2", "16/10/2026", "16/10/2026", 1, 3, "Nút Refresh gọi lại API và cập nhật chart", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-152", "Tối ưu hóa hiển thị giao diện Dashboard Responsive trên màn hình di động", "ToiUuGiaoDienDashboardResponsive_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 4.2", "16/10/2026", "17/10/2026", 2, 5, "Layout tự động co giãn đẹp mắt trên Mobile/Tablet", "Đã hoàn thành")

# QA/DB: Huỳnh Nguyễn Vĩnh Phúc (5 tasks)
add_task("Tuần 5", "Sprint 3", "TASK-153", "Viết bộ kiểm thử tự động kiểm tra tính toán số liệu thống kê Dashboard", "BoKiemThuTuDong_DashboardStats_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 4.4", "12/10/2026", "13/10/2026", 2, 5, "Test suite kiểm tra API /api/dashboard/stats", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-154", "Kiểm thử đối soát mảng doanh thu 12 tháng khớp 100% các bản ghi Payment", "KiemThuDoiSoatDoanhThu12Thang_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 4.4", "14/10/2026", "15/10/2026", 2, 4, "Test case đối soát tổng doanh thu từng tháng", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-155", "Kiểm thử đối chiếu danh sách Top 5 Debtors khớp với hóa đơn quá hạn", "KiemThuTop5DebtorsKhopHoaDon_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 4.4", "15/10/2026", "16/10/2026", 2, 4, "Test case kiểm tra thứ tự sắp xếp nợ giảm dần", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-156", "Đo lường thời gian phản hồi API Dashboard đảm bảo tải dưới 500ms", "DoLuongThoiGianPhanHoiDashboard_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 4.4", "16/10/2026", "17/10/2026", 1, 3, "Báo cáo Performance Test API Dashboard", "Đã hoàn thành")
add_task("Tuần 5", "Sprint 3", "TASK-157", "Tổng hợp Báo cáo kiểm thử Sprint 3 bàn giao cho Trưởng nhóm", "TongHopBaoCaoKiemThuSprint3_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 4.4", "17/10/2026", "18/10/2026", 1, 3, "Báo cáo chất lượng Sprint 3 hoàn chỉnh", "Đã hoàn thành")

# ==============================================================================
# TUẦN 6: 19/10/2026 - 25/10/2026 (Sprint 4: Email nhắc nợ Mock/SMTP, Audit Log đầy đủ, Client Portal, Tối ưu & Staging)
# ==============================================================================
# PM: Nguyễn Hữu Phúc (6 tasks)
add_task("Tuần 6", "Sprint 4", "TASK-158", "Khởi động Sprint 4 hoàn tất dự án theo kế hoạch WBS 5", "KhoiDongSprint4_HoanTatDuAn_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5", "19/10/2026", "19/10/2026", 2, 4, "Kế hoạch Sprint 4 chi tiết và phân công nhân sự", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-159", "Theo dõi ngân sách chi phí Sprint 4 (kế hoạch 7.500.000 VNĐ)", "TheoDoiChiPhiSprint4_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5", "19/10/2026", "22/10/2026", 2, 4, "Bảng theo dõi chi phí nhân sự WBS 5.1 - 5.4", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-160", "Giám sát tích hợp hệ thống tổng thể và chuẩn bị môi trường Staging Demo", "GiamSatTichHopVaStagingDemo_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.2", "21/10/2026", "23/10/2026", 2, 5, "Môi trường Staging sẵn sàng demo cho giảng viên", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-161", "Rà soát ma trận rủi ro cập nhật và kiểm tra quỹ dự phòng 4.5 triệu VNĐ", "RaSoatMaTranRuiRoCapNhat_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 6", "23/10/2026", "24/10/2026", 2, 4, "Sổ đăng ký rủi ro Risk Register cập nhật lần cuối", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-162", "Tổ chức họp bàn giao sản phẩm kỹ thuật trước buổi nghiệm thu chính thức", "HopBanGiaoSanPhamKyThuat_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "24/10/2026", "25/10/2026", 1, 3, "Biên bản bàn giao sản phẩm giữa các thành viên", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-163", "Tổng kết đánh giá hiệu quả phối hợp và mức độ hoàn thành nhiệm vụ Sprint 4", "TongKetDanhGiaSprint4_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "25/10/2026", "25/10/2026", 1, 3, "Báo cáo nghiệm thu hoàn thành 5 Story Points Sprint 4", "Đã hoàn thành")

# BA: Nguyễn Xuân Đoàn (6 tasks)
add_task("Tuần 6", "Sprint 4", "TASK-164", "Đặc tả mẫu nội dung email thông báo phát hành hóa đơn và email nhắc nợ", "DacTaMauEmailThongBaoVaNhacNo_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.1", "19/10/2026", "20/10/2026", 2, 4, "Nội dung template email chuyên nghiệp", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-165", "Đặc tả phân hệ Cổng thông tin Khách hàng (Client Portal) tra cứu riêng", "DacTaPhanHeClientPortal_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.1", "20/10/2026", "21/10/2026", 2, 5, "Tài liệu đặc tả FR-PORTAL-01 & 02", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-166", "Đặc tả danh mục các hành động nghiệp vụ bắt buộc phải ghi vết Audit Log", "DacTaHanhDongBatBuocAuditLog_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.1", "21/10/2026", "22/10/2026", 2, 4, "Bảng ma trận hành động và phân hệ Audit Log", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-167", "Cập nhật và hoàn thiện tài liệu Đặc tả BRD & SRS v5.0 chính thức", "HoanThienBRD_SRS_v5_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.4", "22/10/2026", "23/10/2026", 3, 8, "File BRD-SRS_GOODY_QLHDCN_CHUC_NANG_THEO_SOURCE_v5.docx", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-168", "Xây dựng kịch bản kiểm thử chấp nhận người dùng UAT toàn diện hệ thống", "XayDungKichBanUATToanDien_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.3", "23/10/2026", "24/10/2026", 3, 6, "Bộ tài liệu UAT đầy đủ từ Auth -> Deal -> Hóa đơn -> Nợ", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-169", "Hỗ trợ người dùng thử nghiệm và ghi nhận phản hồi đóng góp (Feedback Log)", "HoTroNguoiDungThuNghiemFeedback_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.3", "24/10/2026", "25/10/2026", 2, 4, "Bảng tổng hợp ý kiến người dùng và đề xuất", "Đã hoàn thành")

# BE: Phạm Văn Sơn (7 tasks)
add_task("Tuần 6", "Sprint 4", "TASK-170", "Xây dựng Module gửi Email thông báo hóa đơn và Nhắc nợ (Mock/SMTP)", "ModuleGuiEmailThongBaoVaNhacNo_phamson", "Phạm Văn Sơn (BE)", "Thông báo & Tối ưu", "WBS 5.1", "19/10/2026", "20/10/2026", 3, 7, "Module gửi email với Nodemailer / Mock Logger", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-171", "Xây dựng Model AuditLog lưu vết lịch sử: userId, action, entity, details, ip", "ThietKeModelAuditLog_phamson", "Phạm Văn Sơn (BE)", "Audit & Bảo mật", "WBS 5.1", "20/10/2026", "21/10/2026", 2, 4, "Model models/AuditLog.js chuẩn xác", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-172", "Xây dựng API Lấy lịch sử nhật ký Audit Log GET /api/audit (tối đa 100 dòng)", "API_LayLichSuAuditLog_phamson", "Phạm Văn Sơn (BE)", "Audit & Bảo mật", "WBS 5.1", "21/10/2026", "21/10/2026", 2, 4, "Endpoint GET /api/audit hỗ trợ phân trang", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-173", "Tích hợp ghi vết Audit Log tự động cho các hành động Login, Khách hàng, Deal, Hóa đơn, Nợ", "TichHopGhiLogMoiHanhDong_phamson", "Phạm Văn Sơn (BE)", "Audit & Bảo mật", "WBS 5.1", "21/10/2026", "22/10/2026", 3, 6, "Tự động tạo record audit khi thực thi controller", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-174", "Xây dựng API Cổng tra cứu cho doanh nghiệp B2B theo mã số thuế và mã bảo mật", "API_ClientPortalTraCuuNo_phamson", "Phạm Văn Sơn (BE)", "Khách hàng B2B", "WBS 5.1", "22/10/2026", "23/10/2026", 2, 5, "Endpoint tra cứu dữ liệu hóa đơn riêng biệt", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-175", "Áp dụng Parameterized Query chống SQL Injection tuyệt đối qua Sequelize", "ChongSQLInjectionQuaSequelize_phamson", "Phạm Văn Sơn (BE)", "Bảo mật", "WBS 5.2", "23/10/2026", "24/10/2026", 2, 4, "Mã nguồn backend an toàn 100% trước SQLi", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-176", "Viết Dockerfile và docker-compose.yml đóng gói ứng dụng phục vụ Deploy Staging", "DongGoiUngDungDockerCompose_phamson", "Phạm Văn Sơn (BE)", "DevOps & Staging", "WBS 5.2", "24/10/2026", "25/10/2026", 2, 5, "File Dockerfile và docker-compose.yml chạy một lệnh", "Đã hoàn thành")

# FE: Nguyễn Hoàng Phước (7 tasks)
add_task("Tuần 6", "Sprint 4", "TASK-177", "Xây dựng Giao diện Trang Nhật ký Audit Log audit.html chuyên nghiệp", "ThietKeGiaoDienBangAuditLogUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.1", "19/10/2026", "20/10/2026", 3, 6, "Trang public/audit.html có filter và badges", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-178", "Thiết kế huy hiệu màu sắc cho các hành động Audit Log (Tạo, Sửa, Xóa, Nhắc nợ)", "HienThiBadgeHanhDongAuditLog_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.1", "20/10/2026", "21/10/2026", 2, 4, "Badges sắc nét phân biệt thao tác người dùng", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-179", "Xây dựng Giao diện Cổng tra cứu riêng cho Khách hàng portal.html", "ThietKeGiaoDienClientPortal_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.1", "21/10/2026", "22/10/2026", 2, 5, "Trang portal tra cứu hóa đơn không cần đăng nhập", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-180", "Tối ưu hóa hiệu ứng tương tác Micro-interactions và thông báo Toast trên UI", "ToiUuHieuUngToastVaMicroInteractions_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.2", "22/10/2026", "23/10/2026", 2, 4, "Hiệu ứng chuyển trang mượt và thông báo Toast đẹp mắt", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-181", "Kiểm thử khả năng tương thích hiển thị trên các trình duyệt Chrome, Edge, Firefox", "KiemTraTuongThichTrinhDuyetWeb_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.3", "23/10/2026", "24/10/2026", 2, 4, "Giao diện hiển thị chuẩn xác trên cả 3 trình duyệt", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-182", "Tối ưu hóa dung lượng CSS, JS và font chữ giảm thời gian tải trang dưới 1 giây", "ToiUuDungLuongFrontendAsset_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.2", "24/10/2026", "24/10/2026", 1, 3, "Trang tải nhanh đạt điểm Google Lighthouse cao", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-183", "Chụp ảnh màn hình các phân hệ giao diện phục vụ tài liệu User Manual", "ChupAnhManHinhGiaoDienUserManual_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.4", "25/10/2026", "25/10/2026", 1, 3, "Bộ ảnh chụp chất lượng cao các màn hình hệ thống", "Đã hoàn thành")

# QA/DB: Huỳnh Nguyễn Vĩnh Phúc (6 tasks)
add_task("Tuần 6", "Sprint 4", "TASK-184", "Viết bộ kiểm thử tự động Ghi nhật ký thao tác Audit Log đầy đủ trường thông tin", "BoKiemThuTuDong_AuditLog_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.3", "19/10/2026", "20/10/2026", 2, 4, "Test suite kiểm tra API /api/audit", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-185", "Xây dựng kịch bản kiểm thử tự động toàn trình End-to-End từ Deal đến Thu nợ", "KiemThuTuDongToanTrinhE2E_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.3", "21/10/2026", "22/10/2026", 3, 7, "Test E2E bao phủ toàn bộ luồng nghiệp vụ chính", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-186", "Kiểm thử bảo mật API: Không lộ mật khẩu hash, kiểm tra quyền RBAC mọi endpoint", "KiemThuBaoMatAPI_RBAC_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.3", "22/10/2026", "23/10/2026", 2, 4, "Báo cáo Security Assessment API an toàn", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-187", "Thực hiện phân tích Pareto nguyên nhân trễ hạn công nợ và rủi ro phần mềm", "PhanTichParetoRuiRoVaNguyenNhanNo_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.3", "23/10/2026", "24/10/2026", 2, 5, "File HuynhNguyenVinhPhuc_Pareto.xlsx hoàn chỉnh", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-188", "Thiết lập script sao lưu và phục hồi CSDL tự động (Backup & Restore script)", "ThietLapScriptBackupRestoreDB_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 5.2", "24/10/2026", "25/10/2026", 2, 4, "Script sao lưu tự động CSDL SQLite/PostgreSQL", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-189", "Cấu hình lệnh npm test chạy toàn bộ test suite và đo Code Coverage đạt 85%", "CauHinhLenhNpmTestToanBo_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.3", "25/10/2026", "25/10/2026", 1, 3, "Lệnh npm test chạy pass 100% 7 bộ test suites", "Đã hoàn thành")

# ==============================================================================
# TUẦN 7: 26/10/2026 (Nghiệm thu, Đóng gói dự án, User Manual, Báo cáo PMBOK & Bảo vệ Đồ án)
# ==============================================================================
# PM: Nguyễn Hữu Phúc (5 tasks)
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-190", "Soạn thảo Báo cáo tổng kết dự án Project Closing Report theo chuẩn PMBOK", "SoanThaoBaoCaoProjectClosing_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "26/10/2026", "26/10/2026", 3, 6, "Tài liệu Project Closing Report hoàn chỉnh", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-191", "Lập bảng đối chiếu 4 mục tiêu SMART ban đầu với kết quả thực tế đạt được", "DoiChieuMucTieuSMARTThucTe_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Bảng nghiệm thu 4/4 mục tiêu SMART đạt 100%", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-192", "Hoàn thiện tài liệu Báo cáo Đồ án Quản lý dự án QLDA_Nhom10_Lab.docx", "HoanThienBaoCaoQLDA_Docx_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "26/10/2026", "26/10/2026", 3, 8, "File QLDA_Nhom10_Lab.docx đầy đủ các chương", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-193", "Vẽ biểu đồ Gantt Chart tiến độ thực tế 4 Sprint trên Microsoft Excel", "VeBieuDoGanttChartTienDoExcel_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 5, "Biểu đồ Gantt Chart tiến độ 7 tuần", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-194", "Tổng hợp Slide thuyết trình bảo vệ đồ án kết thúc học phần Nhóm 10", "TongHopSlideBaoCaoBaoVeDoAn_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 6, "Slide thuyết trình PowerPoint/Canva chuyên nghiệp", "Đã hoàn thành")

# BA: Nguyễn Xuân Đoàn (4 tasks)
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-195", "Biên soạn Cẩm nang Hướng dẫn sử dụng phần mềm User Manual chi tiết", "BienSoanUserManualChiTiet_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.4", "26/10/2026", "26/10/2026", 3, 8, "Tài liệu User Manual có hình ảnh minh họa", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-196", "Soạn tài liệu hướng dẫn nghiệp vụ chuyên biệt cho Kế toán và Recruiter", "SoanHuongDanNghiepVuKeToanRecruiter_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Cẩm nang hướng dẫn thao tác theo từng vai trò", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-197", "Cập nhật Product Backlog giai đoạn 2 cho các tính năng mở rộng tương lai", "CapNhatBacklogChoGiaiDoanPhatTrien2_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Backlog giai đoạn 2 (Cổng thanh toán, Mobile)", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-198", "Tham gia diễn tập thuyết trình và demo kịch bản nghiệp vụ trực tiếp", "DienTapThuyetTrinhDemoNghiepVu_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 3, "Kịch bản demo mượt mà không lỗi", "Đã hoàn thành")

# BE: Phạm Văn Sơn (5 tasks)
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-199", "Kiểm tra rà soát Clean Code và tối ưu hóa toàn bộ controllers/routes", "KiemTraCleanCodeBackend_phamson", "Phạm Văn Sơn (BE)", "Kiến trúc & CSDL", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Mã nguồn sạch đẹp, đầy đủ chú thích", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-200", "Xuất bản bộ tài liệu API Documentation và Postman Collection kiểm thử", "XuatBanTaiLieuAPIPostmanCollection_phamson", "Phạm Văn Sơn (BE)", "Tài liệu kỹ thuật", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "File Postman Collection kèm môi trường mẫu", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-201", "Cập nhật hoàn chỉnh tài liệu hướng dẫn cài đặt và chạy trong README.md", "CapNhatTaiLieuHuongDanReadme_phamson", "Phạm Văn Sơn (BE)", "Tài liệu kỹ thuật", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 3, "File README.md hướng dẫn rõ ràng từ A-Z", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-202", "Tạo bản build triển khai production sẵn sàng chạy độc lập", "TaoBanBuildProductionSanSang_phamson", "Phạm Văn Sơn (BE)", "DevOps & Staging", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Gói release phần mềm v1.0.0", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-203", "Trực kỹ thuật và hỗ trợ giải trình kiến trúc backend trong buổi bảo vệ", "TrucKyThuatBaoVeBackend_phamson", "Phạm Văn Sơn (BE)", "Bảo vệ đồ án", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 3, "Sẵn sàng trả lời các câu hỏi kỹ thuật của hội đồng", "Đã hoàn thành")

# FE: Nguyễn Hoàng Phước (4 tasks)
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-204", "Kiểm tra toàn bộ liên kết điều hướng và tính đồng nhất giao diện 5 trang web", "KiemTraLienKetDieuHuongDongNhat_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Hệ thống liên kết mượt mà không gãy link 404", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-205", "Tinh chỉnh thông báo lỗi và trải nghiệm người dùng cuối thân thiện", "TinhChinhThongBaoLoiNguoiDung_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 3, "Các thông báo lỗi bằng tiếng Việt rõ ràng, dễ hiểu", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-206", "Hỗ trợ chuẩn bị hình ảnh minh họa chất lượng cao cho Slide bảo vệ", "HoTroHinhAnhSlideBaoVe_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 2, "Bộ asset hình ảnh đồ họa chất lượng sắc nét", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-207", "Thực hiện demo trực tiếp các luồng giao diện người dùng trước hội đồng", "DemoGiaoDienTrucTiepHoiDong_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Bảo vệ đồ án", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 3, "Phần trình diễn demo giao diện ấn tượng", "Đã hoàn thành")

# QA/DB: Huỳnh Nguyễn Vĩnh Phúc (5 tasks)
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-208", "Chạy lần cuối toàn bộ test suite npm test đảm bảo 100% test pass", "ChayFinalTestSuiteNpmTest_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 3, "Biên bản xác nhận 100% test case xanh lá", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-209", "Kiểm tra tính toàn vẹn dữ liệu CSDL sau các kịch bản demo kiểm thử", "KiemTraToanVenCSDLSauDemo_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiến trúc & CSDL", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 3, "CSDL sạch, không có dữ liệu rác, quan hệ toàn vẹn", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-210", "Hoàn thiện bảng phân tích Pareto kiểm soát chất lượng đồ án", "HoanThienBangPhanTichParetoDocx_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Biểu đồ Pareto kèm nhận xét và đề xuất cải tiến", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-211", "Đóng gói toàn bộ tài liệu Test Case, Test Log và Test Summary Report", "DongGoiBoTaiLieuKiemThuQA_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Bộ hồ sơ QA & Testing hoàn chỉnh", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-212", "Hỗ trợ trả lời các câu hỏi về CSDL và quy trình đảm bảo chất lượng QA", "TraLoiCauHoiCSDLVaQA_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Bảo vệ đồ án", "WBS 5.4", "26/10/2026", "26/10/2026", 1, 3, "Giải trình xuất sắc phần CSDL và Testing", "Đã hoàn thành")

# ==============================================================================
# BỔ SUNG CÁC TASK MỞ RỘNG (GIAI ĐOẠN HOÀN THIỆN NÂNG CAO - TASK 213 ĐẾN TASK 220)
# Giúp tổng số task đạt 220 tasks (Vượt mốc ít nhất 200 task và có thể mở rộng tiếp)
# ==============================================================================
add_task("Tuần 6", "Sprint 4", "TASK-213", "Xây dựng cơ chế đổi mật khẩu cá nhân cho nhân viên PUT /api/auth/change-password", "API_DoiMatKhauNguoiDung_phamson", "Phạm Văn Sơn (BE)", "Xác thực RBAC", "WBS 5.1", "22/10/2026", "23/10/2026", 2, 4, "Endpoint đổi mật khẩu an toàn", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-214", "Xây dựng chức năng khóa / mở khóa tài khoản người dùng PUT /api/auth/users/:id/toggle", "API_KhoaMoKhoaTaiKhoan_phamson", "Phạm Văn Sơn (BE)", "Xác thực RBAC", "WBS 5.1", "23/10/2026", "24/10/2026", 2, 4, "Endpoint quản lý trạng thái tài khoản", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-215", "Tạo Modal Cập nhật thông tin Doanh nghiệp B2B và hạn mức công nợ Credit Limit", "ThietKeModalChinhSuaKhachHangUI_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.1", "22/10/2026", "23/10/2026", 2, 4, "Modal cập nhật khách hàng đầy đủ", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-216", "Thêm Bộ lọc thời gian (Tháng này, Quý này, Năm nay) cho trang Dashboard dữ liệu", "BoLocDashboardTheoThangQuyNam_nguyenhoangphuoc", "Nguyễn Hoàng Phước (FE)", "Giao diện FE", "WBS 5.1", "23/10/2026", "24/10/2026", 2, 4, "Dropdown chọn thời gian tương tác realtime", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-217", "Đặc tả nghiệp vụ quản lý hạn mức công nợ Credit Limit và cảnh báo vượt hạn mức", "DacTaQuanLyHanMucCongNo_nguyenxuandoan", "Nguyễn Xuân Đoàn (BA)", "Nghiệp vụ BA", "WBS 5.1", "21/10/2026", "22/10/2026", 2, 4, "Tài liệu đặc tả hạn mức công nợ", "Đã hoàn thành")
add_task("Tuần 6", "Sprint 4", "TASK-218", "Xây dựng kịch bản kiểm thử tính năng cảnh báo khi khách hàng vượt hạn mức nợ", "KiemThuCanhBaoVuotHanMucNo_huynhnguyenvinhphuc", "Huỳnh Nguyễn Vĩnh Phúc (DB/QA)", "Kiểm thử QA", "WBS 5.3", "23/10/2026", "24/10/2026", 2, 4, "Test suite kiểm tra điều kiện Credit Limit", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-219", "Soạn thảo tài liệu Phân tích ma trận đánh giá năng lực nhóm và hiệu suất làm việc", "PhanTichDanhGiaNangLucNhom_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Báo cáo đánh giá năng suất 5 thành viên", "Đã hoàn thành")
add_task("Tuần 7", "Nghiệm thu & Báo cáo", "TASK-220", "Tổng hợp toàn bộ source code, cơ sở dữ liệu và tài liệu lên GitHub repository chính thức", "TongHopSourceCodeTaiLieuLenGitHub_nguyenhuuphuc", "Nguyễn Hữu Phúc (PM)", "Quản lý dự án", "WBS 5.4", "26/10/2026", "26/10/2026", 2, 4, "Repository GitHub chuẩn chỉnh, đầy đủ release tag", "Đã hoàn thành")

print(f"Tổng số task đã tạo: {len(tasks)}")

# Thống kê theo tuần
week_counts = {}
for t in tasks:
    w = t['week']
    week_counts[w] = week_counts.get(w, 0) + 1

print("\n--- PHÂN BỔ TASK THEO TUẦN ---")
for w, c in week_counts.items():
    print(f"{w}: {c} tasks")

# Thống kê theo thành viên
assignee_counts = {}
for t in tasks:
    a = t['assignee']
    assignee_counts[a] = assignee_counts.get(a, 0) + 1

print("\n--- PHÂN BỔ TASK THEO THÀNH VIÊN ---")
for a, c in assignee_counts.items():
    print(f"{a}: {c} tasks")

# Thống kê theo trạng thái
status_counts = {}
for t in tasks:
    s = t['status']
    status_counts[s] = status_counts.get(s, 0) + 1

print("\n--- PHÂN BỔ TASK THEO TRẠNG THÁI ---")
for s, c in status_counts.items():
    print(f"{s}: {c} tasks")

# ==============================================================================
# XUẤT RA FILE MARKDOWN
# ==============================================================================
md_content = """# KẾ HOẠCH PHÂN CHIA CHI TIẾT 220 TASK THEO 7 TUẦN DỰ ÁN QLDA - NHÓM 10
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

"""

current_week = ""
for t in tasks:
    if t['week'] != current_week:
        current_week = t['week']
        md_content += f"\n---\n\n### 🗓️ {current_week.upper()} ({t['sprint']})\n\n"
        md_content += "| Mã Task | Tên Công Việc & Quy Ước Commit | Người Phụ Trách | Phân Hệ / WBS | Bắt Đầu | Kết Thúc | SP | Giờ | Kết Quả Bàn Giao (Deliverable) | Trạng Thái |\n"
        md_content += "|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---:|\n"
    
    status_icon = "✅ " if t['status'] == "Đã hoàn thành" else ("🔄 " if t['status'] == "Đang thực hiện" else "⏳ ")
    md_content += f"| **{t['tid']}** | **{t['name']}**<br>`{t['commit']}` | {t['assignee']} | {t['module']}<br>({t['wbs']}) | {t['start']} | {t['end']} | {t['sp']} | {t['hours']}h | {t['deliverable']} | {status_icon}{t['status']} |\n"

md_content += """

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
"""

with open(r'c:\Users\phuco\QLDA_NHOM10_GODDY\KE_HOACH_PHAN_CHIA_TASK_THEO_TUAN.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Đã xuất file KE_HOACH_PHAN_CHIA_TASK_THEO_TUAN.md thành công!")

# ==============================================================================
# XUẤT RA FILE EXCEL (.xlsx) CHUYÊN NGHIỆP
# ==============================================================================
wb = openpyxl.Workbook()

# Sheet 1: Dashboard Thống kê
ws_dash = wb.active
ws_dash.title = "Dashboard Tổng Quan"

# Sheet 2: Danh sách 220 Task
ws_tasks = wb.create_sheet(title="Danh Sách 220 Task Chi Tiết")

# Sheet 3: Phân Bổ Thành Viên
ws_members = wb.create_sheet(title="Phân Công Thành Viên")

# Sheet 4: Tiến Độ 7 Tuần
ws_weeks = wb.create_sheet(title="Kế Hoạch 7 Tuần & Sprints")

# Styles
font_title = Font(name="Calibri", size=16, bold=True, color="1E293B")
font_subtitle = Font(name="Calibri", size=11, italic=True, color="64748B")
font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
font_bold = Font(name="Calibri", size=11, bold=True, color="1E293B")
font_normal = Font(name="Calibri", size=10, color="000000")

fill_header = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid") # Dark blue
fill_week_header = PatternFill(start_color="0284C7", end_color="0284C7", fill_type="solid") # Light blue
fill_accent = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
fill_done = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid") # Green
fill_progress = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Yellow
fill_todo = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid") # Gray

thin_border = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)

# ----------------- SHEET 2: DANH SÁCH 220 TASK -----------------
headers = [
    "STT", "Tuần", "Sprint / Giai Đoạn", "Mã Task", "Tên Công Việc Chi Tiết", 
    "Quy Ước Git Commit", "Người Phụ Trách", "Phân Hệ Nghiệp Vụ", "Hạng Mục WBS", 
    "Ngày Bắt Đầu", "Ngày Kết Thúc", "Story Points", "Giờ Công (h)", "Kết Quả Bàn Giao (Deliverable)", "Trạng Thái"
]

ws_tasks.row_dimensions[1].height = 28
for col_idx, h in enumerate(headers, 1):
    cell = ws_tasks.cell(row=1, column=col_idx, value=h)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border

for idx, t in enumerate(tasks, 1):
    row_num = idx + 1
    ws_tasks.row_dimensions[row_num].height = 22
    row_vals = [
        idx, t['week'], t['sprint'], t['tid'], t['name'],
        t['commit'], t['assignee'], t['module'], t['wbs'],
        t['start'], t['end'], t['sp'], t['hours'], t['deliverable'], t['status']
    ]
    for col_idx, val in enumerate(row_vals, 1):
        cell = ws_tasks.cell(row=row_num, column=col_idx, value=val)
        cell.font = font_normal
        cell.border = thin_border
        if col_idx in [1, 2, 4, 9, 10, 11, 12, 13]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx == 15:
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if val == "Đã hoàn thành":
                cell.fill = fill_done
            elif val == "Đang thực hiện":
                cell.fill = fill_progress
            else:
                cell.fill = fill_todo
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

ws_tasks.auto_filter.ref = f"A1:O{len(tasks)+1}"

# Auto width sheet 2
for col in ws_tasks.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws_tasks.column_dimensions[col_letter].width = min(max(max_len + 3, 11), 45)

# ----------------- SHEET 1: DASHBOARD TỔNG QUAN -----------------
ws_dash.row_dimensions[1].height = 30
ws_dash.cell(row=1, column=1, value="BÁO CÁO TỔNG QUAN TIẾN ĐỘ 220 TASK - DỰ ÁN NHÓM 10 GOODY").font = font_title
ws_dash.cell(row=2, column=1, value="Hệ thống Quản lý Hóa đơn / Công nợ tích hợp Dashboard Tuyển dụng (GODDY Recruit)").font = font_subtitle

# Bảng tóm tắt chỉ số KPI
kpis = [
    ("Tổng số Task", len(tasks)),
    ("Tổng Story Points", sum(t['sp'] for t in tasks)),
    ("Tổng Giờ Công Ước Tính", f"{sum(t['hours'] for t in tasks)} giờ"),
    ("Thời Gian Thực Hiện", "7 Tuần (14/09 - 26/10/2026)"),
    ("Tổng Số Thành Viên", "5 Thành viên (Lớp 23DTHC3)"),
    ("Ngân Sách Dự Án", "45.000.000 VNĐ (+10% rủi ro)")
]

for idx, (k, v) in enumerate(kpis, 4):
    ws_dash.cell(row=idx, column=1, value=k).font = font_bold
    ws_dash.cell(row=idx, column=2, value=v).font = font_normal
    ws_dash.cell(row=idx, column=1).border = thin_border
    ws_dash.cell(row=idx, column=2).border = thin_border

# Bảng tiến độ theo trạng thái
ws_dash.cell(row=11, column=1, value="TIẾN ĐỘ THỰC HIỆN THEO TRẠNG THÁI").font = font_bold
ws_dash.cell(row=12, column=1, value="Trạng Thái").font = font_header
ws_dash.cell(row=12, column=1).fill = fill_header
ws_dash.cell(row=12, column=2, value="Số Lượng Task").font = font_header
ws_dash.cell(row=12, column=2).fill = fill_header
ws_dash.cell(row=12, column=3, value="Tỷ Lệ (%)").font = font_header
ws_dash.cell(row=12, column=3).fill = fill_header

r = 13
for s, c in status_counts.items():
    ws_dash.cell(row=r, column=1, value=s).font = font_normal
    ws_dash.cell(row=r, column=2, value=c).font = font_normal
    ws_dash.cell(row=r, column=3, value=f"{(c/len(tasks))*100:.1f}%").font = font_normal
    ws_dash.cell(row=r, column=1).border = thin_border
    ws_dash.cell(row=r, column=2).border = thin_border
    ws_dash.cell(row=r, column=3).border = thin_border
    r += 1

# Bảng thống kê theo tuần
ws_dash.cell(row=18, column=1, value="PHÂN BỔ SỐ LƯỢNG TASK THEO 7 TUẦN").font = font_bold
ws_dash.cell(row=19, column=1, value="Tuần").font = font_header
ws_dash.cell(row=19, column=1).fill = fill_week_header
ws_dash.cell(row=19, column=2, value="Số Task").font = font_header
ws_dash.cell(row=19, column=2).fill = fill_week_header
ws_dash.cell(row=19, column=3, value="Tỷ Lệ (%)").font = font_header
ws_dash.cell(row=19, column=3).fill = fill_week_header

r = 20
for w, c in week_counts.items():
    ws_dash.cell(row=r, column=1, value=w).font = font_normal
    ws_dash.cell(row=r, column=2, value=c).font = font_normal
    ws_dash.cell(row=r, column=3, value=f"{(c/len(tasks))*100:.1f}%").font = font_normal
    ws_dash.cell(row=r, column=1).border = thin_border
    ws_dash.cell(row=r, column=2).border = thin_border
    ws_dash.cell(row=r, column=3).border = thin_border
    r += 1

ws_dash.column_dimensions['A'].width = 35
ws_dash.column_dimensions['B'].width = 25
ws_dash.column_dimensions['C'].width = 18

# ----------------- SHEET 3: PHÂN BỔ THÀNH VIÊN -----------------
ws_members.cell(row=1, column=1, value="PHÂN BỔ TRÁCH NHIỆM & KHỐI LƯỢNG CÔNG VIỆC 5 THÀNH VIÊN").font = font_title
m_headers = ["Họ Tên Thành Viên", "MSSV", "Vai Trò Dự Án", "Số Lượng Task", "Tỷ Lệ Task (%)", "Story Points", "Giờ Công Ước Tính"]
for col_idx, h in enumerate(m_headers, 1):
    cell = ws_members.cell(row=3, column=col_idx, value=h)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = thin_border

member_details = [
    ("Nguyễn Hữu Phúc", "2380601740", "Project Manager (PM)"),
    ("Nguyễn Xuân Đoàn", "2380600510", "Business Analyst (BA)"),
    ("Phạm Văn Sơn", "2380601922", "Backend Developer (BE)"),
    ("Nguyễn Hoàng Phước", "2380601770", "Frontend Developer (FE)"),
    ("Huỳnh Nguyễn Vĩnh Phúc", "2380614923", "Tester & Database (DB/QA)")
]

for idx, (m_name, m_mssv, m_role) in enumerate(member_details, 4):
    m_tasks = [t for t in tasks if m_name in t['assignee']]
    c = len(m_tasks)
    sp = sum(t['sp'] for t in m_tasks)
    h = sum(t['hours'] for t in m_tasks)
    vals = [m_name, m_mssv, m_role, c, f"{(c/len(tasks))*100:.1f}%", sp, f"{h}h"]
    for col_idx, val in enumerate(vals, 1):
        cell = ws_members.cell(row=idx, column=col_idx, value=val)
        cell.font = font_normal
        cell.border = thin_border
        if col_idx in [2, 4, 5, 6, 7]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

for col in ws_members.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws_members.column_dimensions[col_letter].width = max(max_len + 4, 16)

# ----------------- SHEET 4: TIẾN ĐỘ 7 TUẦN -----------------
ws_weeks.cell(row=1, column=1, value="KẾ HOẠCH LỊCH TRÌNH 7 TUẦN & 4 SPRINT THEO CHUẨN PMBOK").font = font_title
w_headers = ["Tuần", "Khoảng Thời Gian", "Giai Đoạn / Sprint", "Trọng Tâm Nghiệp Vụ & Kỹ Thuật", "Số Lượng Task", "Mục Tiêu Deliverable"]
for col_idx, h in enumerate(w_headers, 1):
    cell = ws_weeks.cell(row=3, column=col_idx, value=h)
    cell.font = font_header
    cell.fill = fill_week_header
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = thin_border

week_plan_data = [
    ("Tuần 1", "14/09 – 20/09/2026", "Khởi tạo & Sprint 1", "Project Charter, WBS, BRD/SRS v4, ERD CSDL, Setup Express MVC, Wireframe Figma", 30, "Project Charter, ERD 8 bảng, CSDL khởi tạo, wireframe UI"),
    ("Tuần 2", "21/09 – 27/09/2026", "Sprint 1 (Hoàn tất)", "Auth JWT 3 vai trò, Khách hàng B2B, Job, Candidate, Deal Placement, Sprint 1 Review", 32, "Module Auth, Khách hàng B2B, Tuyển dụng chốt deal hoàn chỉnh"),
    ("Tuần 3", "28/09 – 04/10/2026", "Sprint 2 (Phần 1)", "Phát hành Hóa đơn Invoicing, Thuế VAT 8%, Net Days Due Date, Mẫu in PDF, Thanh toán", 32, "Module Hóa đơn phát hành tự động, in PDF chuẩn GTGT"),
    ("Tuần 4", "05/10 – 11/10/2026", "Sprint 2 (P.2) & Sprint 3", "Đối soát công nợ, Tuổi nợ Aging 3 xô (1-30, 31-60, >60), Nhắc nợ, Nghiệm thu Sprint 2", 30, "Module Công nợ, Aging Report, Nút nhắc nợ tự động"),
    ("Tuần 5", "12/10 – 18/10/2026", "Sprint 3 (Hoàn tất)", "Dashboard 4 KPI, Biểu đồ Chart.js doanh thu 12 tháng, Cơ cấu ngành, Top 5 Debtors", 31, "Dashboard phân tích tài chính & tuyển dụng trực quan tương tác"),
    ("Tuần 6", "19/10 – 25/10/2026", "Sprint 4", "Email nhắc nợ, Audit Log hoàn chỉnh, Client Portal, Tối ưu & Đóng gói Docker Staging", 38, "Hệ thống bảo mật, Audit Log đầy đủ, Staging sẵn sàng demo"),
    ("Tuần 7", "26/10/2026", "Nghiệm thu & Bảo vệ", "Đóng gói mã nguồn, User Manual, Báo cáo PMBOK, Gantt Chart, Slide bảo vệ đồ án", 27, "Hồ sơ nghiệm thu đồ án, Báo cáo Lab Word, Slide thuyết trình")
]

for idx, row_data in enumerate(week_plan_data, 4):
    for col_idx, val in enumerate(row_data, 1):
        cell = ws_weeks.cell(row=idx, column=col_idx, value=val)
        cell.font = font_normal
        cell.border = thin_border
        if col_idx in [1, 2, 3, 5]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center")

for col in ws_weeks.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws_weeks.column_dimensions[col_letter].width = max(max_len + 4, 18)

excel_path = r'c:\Users\phuco\QLDA_NHOM10_GODDY\KE_HOACH_PHAN_CHIA_TASK_THEO_TUAN.xlsx'
wb.save(excel_path)
print(f"Đã xuất file Excel thành công: {excel_path}")
