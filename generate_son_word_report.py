# -*- coding: utf-8 -*-
"""
Tạo tài liệu Word (.docx) chuyên nghiệp:
BẢNG ÁNH XẠ DANH MỤC 48 TASK VÀ FILE GIT COMMIT DÀNH CHO PHẠM VĂN SƠN (BACKEND DEVELOPER - SV4)
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

def build_son_word_document():
    doc = docx.Document()

    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)
        
        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run("QLDA Nhóm 10 - GODDY Recruit | 48 Task & File Git Phạm Văn Sơn (BE)")
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
    r_title = p_title.add_run("BẢNG ÁNH XẠ 48 TASK VÀ FILE GIT COMMIT LÊN GITHUB")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(15)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(30, 58, 138)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("Dự án: Phần Mềm Quản Lý Hóa Đơn / Công Nợ Tuyển Dụng (GODDY Recruit)\nGVHD: ThS. Nguyễn Hữu Trung | Đơn vị: Nhóm 10 - Lớp 23DTHC3")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10)
    r_sub.font.color.rgb = RGBColor(100, 116, 139)

    # THÔNG TIN THÀNH VIÊN PHẠM VĂN SƠN
    p_box = doc.add_paragraph()
    p_box.paragraph_format.space_after = Pt(10)
    r_box = p_box.add_run(
        "★ Họ và tên: PHẠM VĂN SƠN | MSSV: 2380601922\n"
        "★ Vai trò: Backend Developer (BE) - Sinh viên 4 (SV4)\n"
        "★ Trọng trách: Node.js Express MVC, RESTful API Auth/RBAC, Invoicing, Debt, Dashboard Stats, Docker Compose\n"
        "★ Khối lượng: 48 Tasks (118 Story Points - 21.8% toàn dự án)\n"
        "★ Quy ước đặt tên Git Commit: git commit -m \"TenTask_phamson\""
    )
    r_box.font.name = "Calibri"
    r_box.font.size = Pt(9.5)
    r_box.font.bold = True
    r_box.font.color.rgb = RGBColor(15, 23, 42)

    # TỔNG QUAN CÁC THƯ MỤC & FILE CỦA BACKEND
    p_ov = doc.add_paragraph()
    p_ov.paragraph_format.space_before = Pt(8)
    p_ov.paragraph_format.space_after = Pt(4)
    r_ov = p_ov.add_run("I. TỔNG HỢP CÁC FILE VÀ THƯ MỤC CẦN GIT CỦA PHẠM VĂN SƠN (SV4)")
    r_ov.font.name = "Calibri"
    r_ov.font.size = Pt(12)
    r_ov.font.bold = True
    r_ov.font.color.rgb = RGBColor(30, 58, 138)

    file_groups = [
        ("1. Khởi tạo & Cấu hình", "server.js, config/db.js, .env.example, package.json, package-lock.json", "Cấu hình Server Express, kết nối Sequelize ORM, CORS, Parser"),
        ("2. Xác thực & Phân quyền", "middlewares/authMiddleware.js, controllers/authController.js, routes/authRoutes.js", "Xác thực JWT token, Bcrypt băm mật khẩu, RBAC 3 cấp"),
        ("3. Khách hàng & Tuyển dụng", "controllers/clientController.js, routes/clientRoutes.js, controllers/recruitmentController.js, routes/recruitmentRoutes.js", "CRUD B2B Clients, Validate MST, CRUD Job/Candidate, Chốt Deal"),
        ("4. Hóa đơn Invoicing", "controllers/invoiceController.js, routes/invoiceRoutes.js", "Tạo HĐ từ deal, tính VAT 8%, Net Days Due Date, chặn trùng lặp, hủy HĐ"),
        ("5. Công nợ & Thanh toán", "controllers/debtController.js, routes/debtRoutes.js", "Ghi nhận thanh toán, trừ dần nợ, 3 xô tuổi nợ (1-30, 31-60, >60), nhắc nợ"),
        ("6. Dashboard & Thống kê", "controllers/dashboardController.js, routes/dashboardRoutes.js", "API 4 KPI, Biểu đồ doanh thu 12 tháng, Cơ cấu ngành, Top 5 Debtors"),
        ("7. Audit Log & An toàn CSDL", "models/AuditLog.js, controllers/auditController.js, routes/auditRoutes.js", "Ghi vết hành động người dùng, chống SQL Injection với Sequelize Op"),
        ("8. Đóng gói & Triển khai", "Dockerfile, docker-compose.yml, README.md", "Container hóa Docker, tài liệu README hướng dẫn chạy dự án")
    ]

    tbl_ov = doc.add_table(rows=1, cols=3)
    tbl_ov.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ov.autofit = False
    set_table_borders(tbl_ov)

    col_widths_ov = [Inches(1.8), Inches(2.7), Inches(2.5)]
    headers_ov = ["Phân Hệ Backend", "File Mã Nguồn Tương Ứng", "Chức Năng & Nghiệp Vụ Chính"]
    hdr_cells_ov = tbl_ov.rows[0].cells
    for i, title in enumerate(headers_ov):
        hdr_cells_ov[i].width = col_widths_ov[i]
        set_cell_background(hdr_cells_ov[i], "1E3A8A")
        set_cell_margins(hdr_cells_ov[i], top=100, bottom=100, left=80, right=80)
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
            set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
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

    # II. BẢNG CHI TIẾT 48 TASK CỦA PHẠM VĂN SƠN
    p_h2 = doc.add_paragraph()
    p_h2.paragraph_format.space_before = Pt(14)
    p_h2.paragraph_format.space_after = Pt(4)
    r_h2 = p_h2.add_run("II. BẢNG CHI TIẾT 48 TASK & LỆNH COMMIT GIT CỦA PHẠM VĂN SƠN")
    r_h2.font.name = "Calibri"
    r_h2.font.size = Pt(12)
    r_h2.font.bold = True
    r_h2.font.color.rgb = RGBColor(30, 58, 138)

    son_tasks_data = [
        # Tuần 1 (6 tasks)
        ("TASK-013", "Tuần 1", "Khởi tạo repo Git và cấu trúc thư mục Express MVC", "KhoiTaoCauTrucThuMucDuAn_phamson", "package.json, controllers/, routes/"),
        ("TASK-014", "Tuần 1", "Cấu hình Sequelize ORM kết nối SQLite & Supabase", "KetNoiCoSoDuLieuSequelize_phamson", "config/db.js"),
        ("TASK-015", "Tuần 1", "Cấu hình CORS, Express JSON Parser & URL-encoded", "CauHinhCorsVaExpressParser_phamson", "server.js"),
        ("TASK-016", "Tuần 1", "Cấu hình phục vụ Static Assets public cho Dashboard", "CauHinhPhucVuStaticAssetsPublic_phamson", "server.js"),
        ("TASK-017", "Tuần 1", "Thiết lập biến môi trường an toàn với file .env", "ThietLapBienMoiTruongDotenv_phamson", ".env, .env.example"),
        ("TASK-018", "Tuần 1", "Xây dựng middleware xử lý lỗi tập trung Error Handling", "XayDungMiddlewareErrorHandler_phamson", "server.js"),

        # Tuần 2 (7 tasks)
        ("TASK-043", "Tuần 2", "Cài bcryptjs và viết hàm băm mật khẩu 10 rounds", "VietHamMaHoaMatKhauBcrypt_phamson", "controllers/authController.js"),
        ("TASK-044", "Tuần 2", "API Đăng nhập hệ thống POST /api/auth/login cấp JWT", "API_DangNhapHeThong_phamson", "controllers/authController.js, routes/authRoutes.js"),
        ("TASK-045", "Tuần 2", "Middleware verifyToken và requireRole 3 cấp RBAC", "MiddlewarePhanQuyenTheoVaiTro_phamson", "middlewares/authMiddleware.js"),
        ("TASK-046", "Tuần 2", "API Đăng ký POST /api/auth/register chặn trùng username", "API_DangKyNhanVienMoi_phamson", "controllers/authController.js, routes/authRoutes.js"),
        ("TASK-047", "Tuần 2", "Trọn bộ API CRUD Khách hàng B2B kèm validate MST", "API_QuanLyKhachHangB2B_phamson", "controllers/clientController.js, routes/clientRoutes.js"),
        ("TASK-048", "Tuần 2", "API Quản lý Job vị trí và Ứng viên Candidate", "API_QuanLyJobVaCandidate_phamson", "controllers/recruitmentController.js, routes/recruitmentRoutes.js"),
        ("TASK-049", "Tuần 2", "API Chốt Deal Tuyển dụng POST /api/recruitment/placements", "API_GhiNhanDealTuyenDungMoi_phamson", "controllers/recruitmentController.js, routes/recruitmentRoutes.js"),

        # Tuần 3 (7 tasks)
        ("TASK-075", "Tuần 3", "API Danh sách hóa đơn GET /api/invoices kèm Client/Placement", "API_LayDanhSachHoaDon_phamson", "controllers/invoiceController.js, routes/invoiceRoutes.js"),
        ("TASK-076", "Tuần 3", "Thuật toán sinh mã hóa đơn tự động duy nhất INV-YYYY-XXXX", "HamSinhMaHoaDonTuDong_phamson", "controllers/invoiceController.js"),
        ("TASK-077", "Tuần 3", "Hàm tính thuế VAT 8% (vatAmount) và tổng tiền (totalAmount)", "HamTinhTienThueVAT8PhanTram_phamson", "controllers/invoiceController.js"),
        ("TASK-078", "Tuần 3", "Logic tính ngày đến hạn dueDate = issueDate + client.netDays", "TuDongGanHanThanhToanTheoNetDays_phamson", "controllers/invoiceController.js"),
        ("TASK-079", "Tuần 3", "API Phát hành HĐ từ Placement POST /api/invoices/from-placement", "API_PhatHanhHoaDonTuDealPlacement_phamson", "controllers/invoiceController.js, routes/invoiceRoutes.js"),
        ("TASK-080", "Tuần 3", "Ràng buộc bảo vệ: Chặn phát hành nhiều HĐ cho cùng 1 deal", "ChanPhatHanhTrungHoaDonChoCung1Deal_phamson", "controllers/invoiceController.js"),
        ("TASK-081", "Tuần 3", "API Hủy hóa đơn PUT /api/invoices/:id/cancel (chặn nếu đã trả)", "API_HuyHoaDonDichVu_phamson", "controllers/invoiceController.js, routes/invoiceRoutes.js"),

        # Tuần 4 (7 tasks)
        ("TASK-107", "Tuần 4", "API Thu tiền thanh toán nợ POST /api/debt/payment", "API_GhiNhanThanhToanCongNo_phamson", "controllers/debtController.js, routes/debtRoutes.js"),
        ("TASK-108", "Tuần 4", "Validate số tiền trả > 0 và không vượt quá remainingAmount", "ValidateSoTienTraKhongVuotQuaNo_phamson", "controllers/debtController.js"),
        ("TASK-109", "Tuần 4", "Cập nhật trừ dần nợ & tự động đổi trạng thái Paid/Partial", "TuDongTruDanDuNoHoaDon_phamson", "controllers/debtController.js"),
        ("TASK-110", "Tuần 4", "API Tổng hợp công nợ và phân loại tuổi nợ GET /api/debt/overview", "API_BaoCaoTongHopCongNo_phamson", "controllers/debtController.js, routes/debtRoutes.js"),
        ("TASK-111", "Tuần 4", "Thuật toán tính số ngày quá hạn và phân 3 xô (1-30, 31-60, >60)", "PhanTichTuoiNo3XoTuDong_phamson", "controllers/debtController.js"),
        ("TASK-112", "Tuần 4", "API Gửi thông báo nhắc nợ POST /api/debt/remind", "API_GuiThongBaoNhacNo_phamson", "controllers/debtController.js, routes/debtRoutes.js"),
        ("TASK-113", "Tuần 4", "Bắt đầu xây dựng API Thống kê KPI GET /api/dashboard/stats", "API_LaySoLieuTongHopDashboard_phamson", "controllers/dashboardController.js, routes/dashboardRoutes.js"),

        # Tuần 5 (7 tasks)
        ("TASK-139", "Tuần 5", "Hàm aggregate tính Tổng doanh thu đã thu thực tế từ CSDL", "TongHopTongDoanhThuDaThu_phamson", "controllers/dashboardController.js"),
        ("TASK-140", "Tuần 5", "Hàm aggregate tính Tổng công nợ phải thu AR & nợ quá hạn", "TongHopTongCongNoPhaiThuAR_phamson", "controllers/dashboardController.js"),
        ("TASK-141", "Tuần 5", "Hàm đếm tổng số vị trí đã tuyển dụng thành công Placement", "DemSoDealTuyenDungThanhCong_phamson", "controllers/dashboardController.js"),
        ("TASK-142", "Tuần 5", "Hàm tính Tỷ lệ thu hồi nợ (%) và Tỷ lệ nợ quá hạn (%)", "TinhTyLeThuHoiVaNoQuaHan_phamson", "controllers/dashboardController.js"),
        ("TASK-143", "Tuần 5", "Gom nhóm và tính doanh thu thực tế 12 tháng từ bảng Payment", "TinhDoanhThuThucTeTheo12Thang_phamson", "controllers/dashboardController.js"),
        ("TASK-144", "Tuần 5", "Logic phân tích tỷ lệ cơ cấu khách hàng theo ngành nghề", "ThongKeCoCauKhachHangTheoNganh_phamson", "controllers/dashboardController.js"),
        ("TASK-145", "Tuần 5", "Logic lọc và trả về danh sách Top 5 doanh nghiệp nợ nhiều nhất", "Top5DoanhNghiepNoNhieuNhat_phamson", "controllers/dashboardController.js"),

        # Tuần 6 (7 tasks)
        ("TASK-170", "Tuần 6", "Module gửi Email thông báo hóa đơn & Nhắc nợ (Mock/SMTP)", "ModuleGuiEmailThongBaoVaNhacNo_phamson", "controllers/debtController.js"),
        ("TASK-171", "Tuần 6", "Xây dựng Model AuditLog lưu vết lịch sử: user, action, ip", "ThietKeModelAuditLog_phamson", "models/AuditLog.js"),
        ("TASK-172", "Tuần 6", "API Lấy lịch sử nhật ký Audit Log GET /api/audit (tối đa 100)", "API_LayLichSuAuditLog_phamson", "controllers/auditController.js, routes/auditRoutes.js"),
        ("TASK-173", "Tuần 6", "Tích hợp ghi vết Audit Log tự động cho các hành động chính", "TichHopGhiLogMoiHanhDong_phamson", "controllers/authController.js, clientController.js, invoiceController.js"),
        ("TASK-174", "Tuần 6", "API Cổng tra cứu B2B theo mã số thuế và mã bảo mật", "API_ClientPortalTraCuuNo_phamson", "controllers/clientController.js, routes/clientRoutes.js"),
        ("TASK-175", "Tuần 6", "Áp dụng Parameterized Query chống SQL Injection tuyệt đối", "ChongSQLInjectionQuaSequelize_phamson", "controllers/ (toàn bộ truy vấn Sequelize)"),
        ("TASK-176", "Tuần 6", "Viết Dockerfile & docker-compose.yml đóng gói triển khai Staging", "DongGoiUngDungDockerCompose_phamson", "Dockerfile, docker-compose.yml"),

        # Tuần 7 (7 tasks)
        ("TASK-199", "Tuần 7", "Rà soát Clean Code và tối ưu hóa controllers/routes", "KiemTraCleanCodeBackend_phamson", "controllers/*.js, routes/*.js"),
        ("TASK-200", "Tuần 7", "Xuất bản tài liệu API Documentation & Postman Collection", "XuatBanTaiLieuAPIPostmanCollection_phamson", "docs/ (hoặc postman_collection.json)"),
        ("TASK-201", "Tuần 7", "Cập nhật hoàn chỉnh hướng dẫn cài đặt trong README.md", "CapNhatTaiLieuHuongDanReadme_phamson", "README.md"),
        ("TASK-202", "Tuần 7", "Tạo bản build triển khai production sẵn sàng chạy độc lập", "TaoBanBuildProductionSanSang_phamson", "package.json, server.js"),
        ("TASK-203", "Tuần 7", "Trực kỹ thuật và hỗ trợ giải trình kiến trúc backend bảo vệ", "TrucKyThuatBaoVeBackend_phamson", "Báo cáo bảo vệ đồ án"),
        ("TASK-213", "Tuần 7", "API Đổi mật khẩu cá nhân PUT /api/auth/change-password", "API_DoiMatKhauNguoiDung_phamson", "controllers/authController.js, routes/authRoutes.js"),
        ("TASK-214", "Tuần 7", "API Khóa / Mở khóa tài khoản PUT /api/auth/users/:id/toggle", "API_KhoaMoKhoaTaiKhoan_phamson", "controllers/authController.js, routes/authRoutes.js")
    ]

    tbl = doc.add_table(rows=1, cols=5)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_borders(tbl)

    col_widths = [Inches(1.0), Inches(0.8), Inches(2.2), Inches(1.8), Inches(1.2)]
    headers = ["Mã Task", "Tuần", "Tên Công Việc (WBS)", "Tên Git Commit Message", "File Cần Git Add"]
    hdr_cells = tbl.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], "1E3A8A")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=60, right=60)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.font.name = "Calibri"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (task_id, week, name, commit_msg, files) in enumerate(son_tasks_data):
        row = tbl.add_row()
        bg_col = "F8FAFC" if idx % 2 == 1 else "FFFFFF"
        for i, text in enumerate([task_id, week, name, commit_msg, files]):
            cell = row.cells[i]
            cell.width = col_widths[i]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            p = cell.paragraphs[0]
            run = p.add_run(text)
            run.font.name = "Calibri"
            run.font.size = Pt(8)
            if i == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run.font.bold = True
                run.font.color.rgb = RGBColor(30, 58, 138)
            elif i == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run.font.bold = True
                run.font.color.rgb = RGBColor(71, 85, 105)
            elif i == 3:
                run.font.bold = True
                run.font.color.rgb = RGBColor(2, 132, 199)
            elif i == 4:
                run.font.bold = True
                run.font.color.rgb = RGBColor(180, 83, 9)
            else:
                run.font.color.rgb = RGBColor(15, 23, 42)

    # III. QUY TRÌNH THỰC HIỆN LỆNH GIT
    p_h3 = doc.add_paragraph()
    p_h3.paragraph_format.space_before = Pt(14)
    p_h3.paragraph_format.space_after = Pt(4)
    r_h3 = p_h3.add_run("III. HƯỚNG DẪN QUY TRÌNH THỰC HIỆN LỆNH GIT ĐẨY TASK LÊN GITHUB")
    r_h3.font.name = "Calibri"
    r_h3.font.size = Pt(12)
    r_h3.font.bold = True
    r_h3.font.color.rgb = RGBColor(30, 58, 138)

    p_cmd = doc.add_paragraph()
    p_cmd.paragraph_format.space_after = Pt(8)
    r_cmd = p_cmd.add_run(
        "Mỗi khi hoàn thành một task, bạn Phạm Văn Sơn thực hiện chuỗi lệnh sau trong terminal:\n\n"
        "# 1. Tạo và chuyển sang nhánh tính năng của task (hoặc làm việc trên nhánh thành viên sv4-backend)\n"
        "git checkout -b feature/sv4/TASK-013\n\n"
        "# 2. Thêm file mã nguồn tương ứng vào Staging Area (chỉ add file thuộc task đó)\n"
        "git add controllers/authController.js routes/authRoutes.js\n\n"
        "# 3. Tiến hành commit với đúng tên quy ước\n"
        "git commit -m \"API_DangNhapHeThong_phamson\"\n\n"
        "# 4. Đẩy nhánh lên repository GitHub cá nhân hoặc repository nhóm\n"
        "git push origin feature/sv4/TASK-013\n\n"
        "# 5. Sau khi hoàn thành tuần/sprint, hợp nhất nhánh vào nhánh chính 'main':\n"
        "git checkout main\n"
        "git merge feature/sv4/TASK-013\n"
        "git push origin main"
    )
    r_cmd.font.name = "Consolas"
    r_cmd.font.size = Pt(8.5)
    r_cmd.font.color.rgb = RGBColor(30, 41, 59)

    out_path = r"c:\Users\phuco\QLDA_NHOM10_GODDY\DANH_SACH_TASK_VA_FILE_GIT_PHAM_VAN_SON.docx"
    doc.save(out_path)
    print(f"Đã lưu thành công tài liệu Word: {out_path}")

if __name__ == "__main__":
    build_son_word_document()
