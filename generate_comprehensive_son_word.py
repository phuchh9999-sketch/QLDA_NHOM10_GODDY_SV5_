# -*- coding: utf-8 -*-
"""
Tạo tài liệu Word (.docx) chuyên nghiệp:
TOÀN BỘ CÂU TRẢ LỜI VỀ NHỮNG TASK VÀ FILE CỦA PHẠM VĂN SƠN (BACKEND DEVELOPER - SV4)
Dự án: GODDY Recruit - Quản lý Hóa đơn / Công nợ Tuyển dụng (Nhóm 10 - HUTECH)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="1E3A8A"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_full_son_document():
    doc = docx.Document()

    # Cấu hình lề trang A4
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)
        
        # Header / Footer
        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run("QLDA Nhóm 10 - GODDY Recruit | 48 Task & File Git Phạm Văn Sơn (SV4)")
        f_run.font.name = "Calibri"
        f_run.font.size = Pt(8.5)
        f_run.font.italic = True
        f_run.font.color.rgb = RGBColor(148, 163, 184)

    # 1. TIÊU ĐỀ BÁO CÁO
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("TRƯỜNG ĐẠI HỌC CÔNG NGHỆ TP.HCM (HUTECH)\nKHOA CÔNG NGHỆ THÔNG TIN - BỘ MÔN CÔNG NGHỆ PHẦN MỀM")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(10)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(71, 85, 105)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("TỔNG HỢP DANH MỤC 48 TASK VÀ FILE GIT COMMIT")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(30, 58, 138)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("Dự án: Phần Mềm Quản Lý Hóa Đơn / Công Nợ Tích Hợp Dashboard Dữ Liệu Tuyển Dụng (GODDY Recruit)\nGVHD: ThS. Nguyễn Hữu Trung | Đơn vị: Nhóm 10 - Lớp 23DTHC3")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    # KHỐI THÔNG TIN THÀNH VIÊN
    p_info = doc.add_paragraph()
    p_info.paragraph_format.space_before = Pt(6)
    p_info.paragraph_format.space_after = Pt(10)
    r_info = p_info.add_run(
        "👤 THÔNG TIN THÀNH VIÊN:\n"
        "• Họ và tên: PHẠM VĂN SƠN\n"
        "• Mã số sinh viên (MSSV): 2380601922\n"
        "• Vai trò đảm nhiệm: Backend Developer (BE) - Sinh viên 4 (SV4)\n"
        "• Tài khoản GitHub: @phamson333zzz-sudo\n"
        "• Khối lượng công việc: 48 Tasks (118 Story Points – Chiếm 21.8% tổng thể dự án)\n"
        "• Quy ước đặt tên Git Commit: git commit -m \"TenTask_phamson\""
    )
    r_info.font.name = "Calibri"
    r_info.font.size = Pt(10)
    r_info.font.bold = True
    r_info.font.color.rgb = RGBColor(15, 23, 42)

    # I. CÁC THƯ MỤC & FILE MÃ NGUỒN BACKEND
    p_sec1 = doc.add_paragraph()
    p_sec1.paragraph_format.space_before = Pt(10)
    p_sec1.paragraph_format.space_after = Pt(4)
    r_sec1 = p_sec1.add_run("I. CÁC THƯ MỤC VÀ FILE MÃ NGUỒN THUỘC TRÁCH NHIỆM BACKEND (SV4)")
    r_sec1.font.name = "Calibri"
    r_sec1.font.size = Pt(12)
    r_sec1.font.bold = True
    r_sec1.font.color.rgb = RGBColor(30, 58, 138)

    file_groups = [
        ("1. Khởi tạo & Cấu hình Server", "server.js, config/db.js, .env.example, package.json", "Cấu hình Express MVC, kết nối Sequelize ORM (SQLite / Supabase), CORS, JSON Parser, Error Handler"),
        ("2. Xác thực & Phân quyền", "middlewares/authMiddleware.js, controllers/authController.js, routes/authRoutes.js", "Băm mật khẩu Bcrypt, Đăng nhập cấp JWT Token 7 ngày, Middleware phân quyền 3 cấp Admin / Kế toán / Recruiter"),
        ("3. Khách hàng Doanh nghiệp B2B", "controllers/clientController.js, routes/clientRoutes.js", "API CRUD Khách hàng Doanh nghiệp, Kiểm tra hợp lệ Mã Số Thuế (MST 10/13 số), Cổng Portal tra cứu"),
        ("4. Tuyển dụng & Chốt Deal", "controllers/recruitmentController.js, routes/recruitmentRoutes.js", "API CRUD Vị trí tuyển dụng (Job), Hồ sơ ứng viên (Candidate), Chốt deal Placement tự tính hoa hồng"),
        ("5. Hóa đơn Invoicing & Thuế VAT", "controllers/invoiceController.js, routes/invoiceRoutes.js", "Lấy danh sách HĐ, Sinh mã INV-YYYY-XXXX tuần tự, Tính VAT 8%, Tính Due Date theo Net Days, Chặn trùng Deal, Hủy HĐ"),
        ("6. Công nợ & Thanh toán", "controllers/debtController.js, routes/debtRoutes.js", "API Thu tiền nợ, Validate số tiền trả, Tự động trừ dần nợ & cập nhật trạng thái, Phân loại 3 xô tuổi nợ (1-30, 31-60, >60), Nhắc nợ"),
        ("7. Dashboard & Thống kê", "controllers/dashboardController.js, routes/dashboardRoutes.js", "API 4 KPI tổng hợp, Biểu đồ doanh thu 12 tháng từ bảng Payment, Cơ cấu ngành nghề, Top 5 doanh nghiệp nợ nhiều nhất"),
        ("8. Nhật ký hệ thống & Bảo mật", "models/AuditLog.js, controllers/auditController.js, routes/auditRoutes.js", "Ghi vết hành động (Audit Log), Tham số hóa truy vấn chống SQL Injection qua Sequelize Op"),
        ("9. Đóng gói & Triển khai", "Dockerfile, docker-compose.yml, README.md", "Đóng gói Container Docker, file docker-compose chạy 1 lệnh, viết tài liệu README hướng dẫn chạy dự án")
    ]

    tbl_ov = doc.add_table(rows=1, cols=3)
    tbl_ov.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ov.autofit = False
    set_table_borders(tbl_ov)

    col_widths_ov = [Inches(1.8), Inches(2.7), Inches(2.5)]
    headers_ov = ["Phân Hệ Backend", "File Cần Git Add", "Trách Nhiệm Kỹ Thuật"]
    hdr_cells_ov = tbl_ov.rows[0].cells
    for i, title in enumerate(headers_ov):
        hdr_cells_ov[i].width = col_widths_ov[i]
        set_cell_background(hdr_cells_ov[i], "1E3A8A")
        set_cell_margins(hdr_cells_ov[i], top=90, bottom=90, left=70, right=70)
        p = hdr_cells_ov[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.font.name = "Calibri"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (grp, files, desc) in enumerate(file_groups):
        row = tbl_ov.add_row()
        bg_col = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        for i, text in enumerate([grp, files, desc]):
            cell = row.cells[i]
            cell.width = col_widths_ov[i]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=60, bottom=60, left=70, right=70)
            p = cell.paragraphs[0]
            run = p.add_run(text)
            run.font.name = "Calibri"
            run.font.size = Pt(8.5)
            if i == 0:
                run.font.bold = True
                run.font.color.rgb = RGBColor(30, 58, 138)
            elif i == 1:
                run.font.bold = True
                run.font.color.rgb = RGBColor(180, 83, 9)
            else:
                run.font.color.rgb = RGBColor(51, 65, 85)

    # II. BẢNG PHÂN CHIA 48 TASK THEO TỪNG TUẦN (TUẦN 1 ĐẾN TUẦN 7)
    p_sec2 = doc.add_paragraph()
    p_sec2.paragraph_format.space_before = Pt(14)
    p_sec2.paragraph_format.space_after = Pt(4)
    r_sec2 = p_sec2.add_run("II. BẢNG PHÂN CHIA 48 TASK CHI TIẾT THEO TUẦN & FILE TƯƠNG ỨNG")
    r_sec2.font.name = "Calibri"
    r_sec2.font.size = Pt(12)
    r_sec2.font.bold = True
    r_sec2.font.color.rgb = RGBColor(30, 58, 138)

    weeks_data = [
        ("Tuần 1: Khởi tạo Kiến trúc & Server MVC (6 Tasks)", [
            ("TASK-013", "Khởi tạo repo Git và cấu trúc thư mục Express MVC", "KhoiTaoCauTrucThuMucDuAn_phamson", "package.json, controllers/, routes/"),
            ("TASK-014", "Cấu hình Sequelize kết nối CSDL SQLite & Supabase", "KetNoiCoSoDuLieuSequelize_phamson", "config/db.js"),
            ("TASK-015", "Cấu hình CORS, Express JSON Parser & URL-encoded", "CauHinhCorsVaExpressParser_phamson", "server.js"),
            ("TASK-016", "Cấu hình phục vụ Static Assets thư mục public", "CauHinhPhucVuStaticAssetsPublic_phamson", "server.js"),
            ("TASK-017", "Thiết lập biến môi trường an toàn với file .env", "ThietLapBienMoiTruongDotenv_phamson", ".env.example, .env"),
            ("TASK-018", "Xây dựng middleware xử lý lỗi tập trung Error Handler", "XayDungMiddlewareErrorHandler_phamson", "server.js")
        ]),
        ("Tuần 2: Xác thực RBAC, Khách Hàng & Tuyển Dụng (7 Tasks)", [
            ("TASK-043", "Cài đặt bcryptjs và viết hàm băm mật khẩu 10 rounds", "VietHamMaHoaMatKhauBcrypt_phamson", "controllers/authController.js"),
            ("TASK-044", "API Đăng nhập POST /api/auth/login cấp JWT token", "API_DangNhapHeThong_phamson", "controllers/authController.js, routes/authRoutes.js"),
            ("TASK-045", "Middleware verifyToken và requireRole phân quyền 3 cấp", "MiddlewarePhanQuyenTheoVaiTro_phamson", "middlewares/authMiddleware.js"),
            ("TASK-046", "API Đăng ký POST /api/auth/register chặn trùng username", "API_DangKyNhanVienMoi_phamson", "controllers/authController.js, routes/authRoutes.js"),
            ("TASK-047", "Trọn bộ API CRUD Khách hàng B2B kèm validate MST", "API_QuanLyKhachHangB2B_phamson", "controllers/clientController.js, routes/clientRoutes.js"),
            ("TASK-048", "API Quản lý vị trí Job và hồ sơ ứng viên Candidate", "API_QuanLyJobVaCandidate_phamson", "controllers/recruitmentController.js, routes/recruitmentRoutes.js"),
            ("TASK-049", "API Chốt Deal Tuyển dụng POST /api/recruitment/placements", "API_GhiNhanDealTuyenDungMoi_phamson", "controllers/recruitmentController.js, routes/recruitmentRoutes.js")
        ]),
        ("Tuần 3: Nghiệp Vụ Phát Hành Hóa Đơn Invoicing (7 Tasks)", [
            ("TASK-075", "API Danh sách hóa đơn GET /api/invoices kèm Client/Deal", "API_LayDanhSachHoaDon_phamson", "controllers/invoiceController.js, routes/invoiceRoutes.js"),
            ("TASK-076", "Thuật toán sinh mã hóa đơn tự động duy nhất INV-YYYY-XXXX", "HamSinhMaHoaDonTuDong_phamson", "controllers/invoiceController.js"),
            ("TASK-077", "Hàm tính thuế VAT 8% (vatAmount) và tổng tiền (totalAmount)", "HamTinhTienThueVAT8PhanTram_phamson", "controllers/invoiceController.js"),
            ("TASK-078", "Logic tính ngày đến hạn dueDate = issueDate + netDays", "TuDongGanHanThanhToanTheoNetDays_phamson", "controllers/invoiceController.js"),
            ("TASK-079", "API Phát hành HĐ từ Placement POST /api/invoices/from-placement", "API_PhatHanhHoaDonTuDealPlacement_phamson", "controllers/invoiceController.js, routes/invoiceRoutes.js"),
            ("TASK-080", "Chặn phát hành nhiều hóa đơn cho cùng 1 deal placement", "ChanPhatHanhTrungHoaDonChoCung1Deal_phamson", "controllers/invoiceController.js"),
            ("TASK-081", "API Hủy hóa đơn PUT /api/invoices/:id/cancel (chặn nếu đã trả)", "API_HuyHoaDonDichVu_phamson", "controllers/invoiceController.js, routes/invoiceRoutes.js")
        ]),
        ("Tuần 4: Quản Lý Thu Nợ & Phân Loại Tuổi Nợ Aging (7 Tasks)", [
            ("TASK-107", "API Thu tiền thanh toán nợ POST /api/debt/payment", "API_GhiNhanThanhToanCongNo_phamson", "controllers/debtController.js, routes/debtRoutes.js"),
            ("TASK-108", "Validate số tiền trả > 0 và không vượt quá remainingAmount", "ValidateSoTienTraKhongVuotQuaNo_phamson", "controllers/debtController.js"),
            ("TASK-109", "Tự động trừ dần nợ & cập nhật trạng thái Paid / Partial", "TuDongTruDanDuNoHoaDon_phamson", "controllers/debtController.js"),
            ("TASK-110", "API Tổng hợp công nợ và tuổi nợ GET /api/debt/overview", "API_BaoCaoTongHopCongNo_phamson", "controllers/debtController.js, routes/debtRoutes.js"),
            ("TASK-111", "Thuật toán phân loại 3 xô tuổi nợ (1-30, 31-60, >60 ngày)", "PhanTichTuoiNo3XoTuDong_phamson", "controllers/debtController.js"),
            ("TASK-112", "API Gửi thông báo nhắc nợ POST /api/debt/remind", "API_GuiThongBaoNhacNo_phamson", "controllers/debtController.js, routes/debtRoutes.js"),
            ("TASK-113", "Khởi tạo khung API Thống kê KPI GET /api/dashboard/stats", "API_LaySoLieuTongHopDashboard_phamson", "controllers/dashboardController.js, routes/dashboardRoutes.js")
        ]),
        ("Tuần 5: API Thống Kê & Phân Tích Dữ Liệu Dashboard (7 Tasks)", [
            ("TASK-139", "Viết hàm aggregate tính Tổng doanh thu đã thu thực tế", "TongHopTongDoanhThuDaThu_phamson", "controllers/dashboardController.js"),
            ("TASK-140", "Viết hàm aggregate tính Tổng nợ phải thu AR & nợ quá hạn", "TongHopTongCongNoPhaiThuAR_phamson", "controllers/dashboardController.js"),
            ("TASK-141", "Viết hàm đếm tổng số vị trí đã tuyển dụng thành công Deal", "DemSoDealTuyenDungThanhCong_phamson", "controllers/dashboardController.js"),
            ("TASK-142", "Viết hàm tính Tỷ lệ thu hồi nợ (%) và Tỷ lệ nợ quá hạn (%)", "TinhTyLeThuHoiVaNoQuaHan_phamson", "controllers/dashboardController.js"),
            ("TASK-143", "Gom nhóm và tính doanh thu thực tế 12 tháng từ Payment", "TinhDoanhThuThucTeTheo12Thang_phamson", "controllers/dashboardController.js"),
            ("TASK-144", "Logic phân tích tỷ lệ cơ cấu khách hàng theo ngành nghề", "ThongKeCoCauKhachHangTheoNganh_phamson", "controllers/dashboardController.js"),
            ("TASK-145", "Logic lọc và trả về danh sách Top 5 doanh nghiệp nợ nhiều nhất", "Top5DoanhNghiepNoNhieuNhat_phamson", "controllers/dashboardController.js")
        ]),
        ("Tuần 6: Email Nhắc Nợ, Audit Log & Docker Compose (7 Tasks)", [
            ("TASK-170", "Module gửi Email thông báo hóa đơn & Nhắc nợ (Mock/SMTP)", "ModuleGuiEmailThongBaoVaNhacNo_phamson", "controllers/debtController.js"),
            ("TASK-171", "Xây dựng Model AuditLog lưu vết: user, action, ip, details", "ThietKeModelAuditLog_phamson", "models/AuditLog.js"),
            ("TASK-172", "API Lấy lịch sử nhật ký Audit Log GET /api/audit (tối đa 100)", "API_LayLichSuAuditLog_phamson", "controllers/auditController.js, routes/auditRoutes.js"),
            ("TASK-173", "Tích hợp ghi vết Audit Log tự động cho toàn bộ actions", "TichHopGhiLogMoiHanhDong_phamson", "controllers/authController.js, clientController.js, invoiceController.js"),
            ("TASK-174", "API Cổng tra cứu B2B theo mã số thuế và mã bảo mật", "API_ClientPortalTraCuuNo_phamson", "controllers/clientController.js, routes/clientRoutes.js"),
            ("TASK-175", "Áp dụng Parameterized Query chống SQL Injection với Sequelize", "ChongSQLInjectionQuaSequelize_phamson", "controllers/*.js (các câu truy vấn)"),
            ("TASK-176", "Viết Dockerfile & docker-compose.yml đóng gói Staging", "DongGoiUngDungDockerCompose_phamson", "Dockerfile, docker-compose.yml")
        ]),
        ("Tuần 7: Tối Ưu Hóa, Đổi Mật Khẩu & Nghiệm Thu (7 Tasks)", [
            ("TASK-199", "Rà soát Clean Code và tối ưu hóa controllers / routes", "KiemTraCleanCodeBackend_phamson", "controllers/*.js, routes/*.js"),
            ("TASK-200", "Xuất bản tài liệu API Documentation & Postman Collection", "XuatBanTaiLieuAPIPostmanCollection_phamson", "docs/ hoặc file Postman"),
            ("TASK-201", "Cập nhật hoàn chỉnh hướng dẫn cài đặt trong README.md", "CapNhatTaiLieuHuongDanReadme_phamson", "README.md"),
            ("TASK-202", "Tạo bản build triển khai production sẵn sàng chạy độc lập", "TaoBanBuildProductionSanSang_phamson", "package.json, server.js"),
            ("TASK-203", "Trực kỹ thuật và hỗ trợ giải trình kiến trúc backend bảo vệ", "TrucKyThuatBaoVeBackend_phamson", "Slide & Tài liệu bảo vệ"),
            ("TASK-213", "API Đổi mật khẩu cá nhân PUT /api/auth/change-password", "API_DoiMatKhauNguoiDung_phamson", "controllers/authController.js, routes/authRoutes.js"),
            ("TASK-214", "API Khóa / Mở khóa tài khoản PUT /api/auth/users/:id/toggle", "API_KhoaMoKhoaTaiKhoan_phamson", "controllers/authController.js, routes/authRoutes.js")
        ])
    ]

    col_widths = [Inches(1.0), Inches(2.3), Inches(2.2), Inches(1.5)]
    headers = ["Mã Task", "Tên Công Việc (WBS)", "Tên Git Commit Message", "File Cần Git Add"]

    for week_title, tasks in weeks_data:
        p_w = doc.add_paragraph()
        p_w.paragraph_format.space_before = Pt(8)
        p_w.paragraph_format.space_after = Pt(2)
        r_w = p_w.add_run(f"★ {week_title}")
        r_w.font.name = "Calibri"
        r_w.font.size = Pt(11)
        r_w.font.bold = True
        r_w.font.color.rgb = RGBColor(14, 116, 144)

        tbl = doc.add_table(rows=1, cols=4)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        set_table_borders(tbl)

        hdr_cells = tbl.rows[0].cells
        for i, title in enumerate(headers):
            hdr_cells[i].width = col_widths[i]
            set_cell_background(hdr_cells[i], "1E3A8A")
            set_cell_margins(hdr_cells[i], top=80, bottom=80, left=60, right=60)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(title)
            run.font.name = "Calibri"
            run.font.size = Pt(8.5)
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 255, 255)

        for idx, (t_id, t_name, t_commit, t_file) in enumerate(tasks):
            row = tbl.add_row()
            bg_col = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
            for i, text in enumerate([t_id, t_name, t_commit, t_file]):
                cell = row.cells[i]
                cell.width = col_widths[i]
                set_cell_background(cell, bg_col)
                set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
                p = cell.paragraphs[0]
                run = p.add_run(text)
                run.font.name = "Calibri"
                run.font.size = Pt(8)
                if i == 0:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(30, 58, 138)
                elif i == 2:
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(2, 132, 199)
                elif i == 3:
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(180, 83, 9)
                else:
                    run.font.color.rgb = RGBColor(15, 23, 42)

    # III. HƯỚNG DẪN LỆNH GIT
    p_sec3 = doc.add_paragraph()
    p_sec3.paragraph_format.space_before = Pt(14)
    p_sec3.paragraph_format.space_after = Pt(4)
    r_sec3 = p_sec3.add_run("III. HƯỚNG DẪN QUY TRÌNH THỰC HIỆN LỆNH GIT CHO BẠN PHẠM VĂN SƠN")
    r_sec3.font.name = "Calibri"
    r_sec3.font.size = Pt(12)
    r_sec3.font.bold = True
    r_sec3.font.color.rgb = RGBColor(30, 58, 138)

    p_cmd_desc = doc.add_paragraph()
    r_cmd_desc = p_cmd_desc.add_run(
        "Mỗi khi hoàn thành một task, bạn Sơn mở terminal trong thư mục dự án và thực hiện tuần tự 4 lệnh sau:\n"
    )
    r_cmd_desc.font.name = "Calibri"
    r_cmd_desc.font.size = Pt(9.5)

    p_cmd = doc.add_paragraph()
    p_cmd.paragraph_format.space_after = Pt(8)
    r_cmd = p_cmd.add_run(
        "# Bước 1: Tạo và chuyển sang nhánh tính năng của task (hoặc làm trên nhánh sv4-backend)\n"
        "git checkout -b feature/sv4/TASK-044\n\n"
        "# Bước 2: Add chính xác các file mã nguồn của task đó (không add file thừa)\n"
        "git add controllers/authController.js routes/authRoutes.js\n\n"
        "# Bước 3: Commit đúng theo cú pháp quy định TenTask_phamson\n"
        "git commit -m \"API_DangNhapHeThong_phamson\"\n\n"
        "# Bước 4: Đẩy nhánh lên GitHub\n"
        "git push origin feature/sv4/TASK-044\n\n"
        "# Bước 5: Sau khi xong tuần hoặc sprint, hợp nhất nhánh vào nhánh chính 'main':\n"
        "git checkout main\n"
        "git merge feature/sv4/TASK-044\n"
        "git push origin main"
    )
    r_cmd.font.name = "Consolas"
    r_cmd.font.size = Pt(8.5)
    r_cmd.font.color.rgb = RGBColor(30, 41, 59)

    out_path = r"c:\Users\phuco\QLDA_NHOM10_GODDY\DANH_SACH_TASK_VA_FILE_GIT_PHAM_VAN_SON.docx"
    doc.save(out_path)
    print(f"Đã cập nhật hoàn chỉnh file Word: {out_path}")

if __name__ == "__main__":
    build_full_son_document()
