# -*- coding: utf-8 -*-
"""
Script xuất Kế hoạch phân chia 220 Task theo 7 tuần ra file Word (.docx) chuyên nghiệp
Dự án: Phần Mềm Quản Lý Hóa Đơn / Công Nợ Tuyển Dụng (GODDY Recruit) - Nhóm 10 HUTECH
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

import generate_weekly_tasks

tasks = generate_weekly_tasks.tasks

doc = docx.Document()

# ==============================================================================
# CẤU HÌNH TRANG VĂN BẢN (PAGE SETUP)
# Khổ giấy A4, Lề: Top 2cm, Bottom 2cm, Left 1.8cm, Right 1.8cm
# ==============================================================================
section = doc.sections[0]
section.page_width = Inches(8.27)   # A4 Width: 21.0 cm
section.page_height = Inches(11.69) # A4 Height: 29.7 cm
section.top_margin = Inches(0.75)   # ~1.9 cm
section.bottom_margin = Inches(0.75)
section.left_margin = Inches(0.65)  # ~1.65 cm (đủ rộng cho bảng 8 cột)
section.right_margin = Inches(0.65)

# Cấu hình Header và Footer
footer = section.footer
f_p = footer.paragraphs[0]
f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
f_run = f_p.add_run("Dự Án QLDA Nhóm 10 - GODDY Recruit | 220 Tasks Kế Hoạch 7 Tuần")
f_run.font.name = "Calibri"
f_run.font.size = Pt(8.5)
f_run.font.italic = True
f_run.font.color.rgb = RGBColor(148, 163, 184)

# ==============================================================================
# HÀM TIỆN ÍCH ĐỊNH DẠNG BẢNG & TEXT (XML HELPERS)
# ==============================================================================
def set_cell_background(cell, hex_color):
    """Đặt màu nền cho cell trong bảng"""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    """Đặt khoảng cách đệm (padding) trong ô tính bằng dxa (1 pt = 20 dxa)"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1"):
    """Thiết lập đường viền mỏng thanh lịch cho bảng"""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def make_row_header_repeat(row):
    """Lặp lại hàng tiêu đề khi bảng tràn sang trang mới"""
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

def prevent_row_split(row):
    """Ngăn hàng bị cắt ngang giữa 2 trang"""
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

# ==============================================================================
# 1. TIÊU ĐỀ DỰ ÁN & THÔNG TIN HỌC PHẦN
# ==============================================================================
p_univ = doc.add_paragraph()
p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_univ.paragraph_format.space_after = Pt(2)
r_u1 = p_univ.add_run("TRƯỜNG ĐẠI HỌC CÔNG NGHỆ TP. HỒ CHÍ MINH (HUTECH)\n")
r_u1.font.name = "Calibri"
r_u1.font.size = Pt(11)
r_u1.font.bold = True
r_u1.font.color.rgb = RGBColor(30, 41, 59)

r_u2 = p_univ.add_run("KHOA CÔNG NGHỆ THÔNG TIN — BỘ MÔN KỸ THUẬT PHẦN MỀM & QLDA")
r_u2.font.name = "Calibri"
r_u2.font.size = Pt(10)
r_u2.font.color.rgb = RGBColor(100, 116, 139)

p_div = doc.add_paragraph()
p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_div.paragraph_format.space_after = Pt(12)
r_div = p_div.add_run("━━━━ ❖ ━━━━")
r_div.font.color.rgb = RGBColor(2, 132, 199)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(4)
r_title = p_title.add_run("KẾ HOẠCH PHÂN CHIA CHI TIẾT 220 TASK THEO 7 TUẦN")
r_title.font.name = "Calibri"
r_title.font.size = Pt(18)
r_title.font.bold = True
r_title.font.color.rgb = RGBColor(30, 58, 138) # Navy

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(16)
r_sub = p_sub.add_run("Đề tài: Phần Mềm Quản Lý Hóa Đơn / Công Nợ Tích Hợp Dashboard Dữ Liệu Tuyển Dụng (GODDY Recruit)\n"
                      "GVHD: ThS. Nguyễn Hữu Trung | Nhóm 10 — Lớp: 23DTHC3\n"
                      "Thời gian: 14/09/2026 – 26/10/2026 (7 Tuần / 4 Sprints) | Ngân sách: 45.000.000 VNĐ | Dự phòng rủi ro 10%: 4.500.000 VNĐ")
r_sub.font.name = "Calibri"
r_sub.font.size = Pt(10.5)
r_sub.font.italic = True
r_sub.font.color.rgb = RGBColor(71, 85, 105)

# ==============================================================================
# 2. PHẦN 1: THÀNH VIÊN VÀ MA TRẬN TRÁCH NHIỆM RACI
# ==============================================================================
h1 = doc.add_paragraph()
h1.paragraph_format.space_before = Pt(12)
h1.paragraph_format.space_after = Pt(6)
r_h1 = h1.add_run("1. DANH SÁCH 5 THÀNH VIÊN & MA TRẬN PHÂN VAI (RACI)")
r_h1.font.name = "Calibri"
r_h1.font.size = Pt(13)
r_h1.font.bold = True
r_h1.font.color.rgb = RGBColor(30, 58, 138)

t_members = doc.add_table(rows=6, cols=5)
t_members.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_members)

m_headers = ["Vai Trò Dự Án", "Họ Tên & MSSV", "Trọng Trách Chuyên Môn", "Thông Tin Liên Hệ", "Chữ Ký"]
m_widths = [Inches(1.4), Inches(1.8), Inches(2.3), Inches(1.8), Inches(0.7)]

hdr_cells = t_members.rows[0].cells
make_row_header_repeat(t_members.rows[0])
prevent_row_split(t_members.rows[0])
for idx, text in enumerate(m_headers):
    hdr_cells[idx].text = text
    set_cell_background(hdr_cells[idx], "1E3A8A")
    set_cell_margins(hdr_cells[idx], top=100, bottom=100, left=100, right=100)
    p = hdr_cells[idx].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

member_data = [
    ("Quản lý dự án\n(Project Manager)", "2380601740\nNguyễn Hữu Phúc", "Trưởng nhóm, lập kế hoạch WBS, kiểm soát tiến độ, quản lý rủi ro & báo cáo PMBOK", "039 4393 147\nnguyenhuuphuc22012005@gmail.com", "Phúc"),
    ("Phân tích nghiệp vụ\n(Business Analyst)", "2380600510\nNguyễn Xuân Đoàn", "Khảo sát nghiệp vụ hóa đơn/công nợ, đặc tả BRD/SRS v5, Product Backlog & UAT", "093 493 1506\nxuandoan755@gmail.com", "Đoàn"),
    ("Lập trình Backend\n(Backend Developer)", "2380601922\nPhạm Văn Sơn", "Node.js/Express REST API, Sequelize ORM, Auth/RBAC, Invoicing, Payment, Aging, Docker", "097 4208 705\nphamson333zzz@gmail.com", "Sơn"),
    ("Lập trình Frontend\n(Frontend Developer)", "2380601770\nNguyễn Hoàng Phước", "Wireframe Figma, HTML5/CSS3 Responsive, Web Dashboard, Invoices UI, Chart.js, PDF", "035 3090 168\nphuoc801901@gmail.com", "Phước"),
    ("Kiểm thử & Database\n(Tester & DB Admin)", "2380614923\nHuỳnh Nguyễn Vĩnh Phúc", "Quản trị PostgreSQL/Supabase & SQLite, ERD, Unit Test Jest, Integration Test, Pareto", "0337 482 995\nphuchh9999@gmail.com", "Phúc")
]

for r_idx, row_vals in enumerate(member_data, 1):
    row_cells = t_members.rows[r_idx].cells
    prevent_row_split(t_members.rows[r_idx])
    for c_idx, val in enumerate(row_vals):
        row_cells[c_idx].text = val
        set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=80, right=80)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1, 4]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.runs[0]
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        if r_idx % 2 == 0:
            set_cell_background(row_cells[c_idx], "F8FAFC")

for row in t_members.rows:
    for idx, width in enumerate(m_widths):
        row.cells[idx].width = width

# Đoạn quy ước commit
p_commit = doc.add_paragraph()
p_commit.paragraph_format.space_before = Pt(8)
p_commit.paragraph_format.space_after = Pt(12)
r_com_title = p_commit.add_run("📌 Quy ước commit Git chuẩn dự án: ")
r_com_title.font.bold = True
r_com_title.font.color.rgb = RGBColor(30, 58, 138)
r_com_desc = p_commit.add_run(
    'Mỗi khi thành viên làm xong một task, tiến hành commit theo đúng cấu trúc: '
    'git commit -m "TenTask_tenthanhvien". Ví dụ: '
    'git commit -m "API_PhatHanhHoaDonTuDealPlacement_phamson". '
    'Trưởng nhóm kiểm tra số lượng commit hoàn thành bất cứ lúc nào qua lệnh PowerShell: '
    '(git log --grep="_phamson" --oneline | Measure-Object).Count'
)
r_com_desc.font.size = Pt(9.5)
r_com_desc.font.italic = True

# ==============================================================================
# 3. PHẦN 2: TỔNG HỢP TIẾN ĐỘ 7 TUẦN & 4 SPRINT
# ==============================================================================
h2 = doc.add_paragraph()
h2.paragraph_format.space_before = Pt(10)
h2.paragraph_format.space_after = Pt(6)
r_h2 = h2.add_run("2. BẢNG TỔNG HỢP TIẾN ĐỘ 7 TUẦN & 4 SPRINT (14/09 – 26/10/2026)")
r_h2.font.name = "Calibri"
r_h2.font.size = Pt(13)
r_h2.font.bold = True
r_h2.font.color.rgb = RGBColor(30, 58, 138)

t_weeks = doc.add_table(rows=8, cols=6)
t_weeks.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_weeks)

w_headers = ["Tuần", "Khoảng Thời Gian", "Giai Đoạn / Sprint", "Trọng Tâm Nghiệp Vụ & Kỹ Thuật", "Số Task", "Trạng Thái"]
w_widths = [Inches(1.0), Inches(1.4), Inches(1.3), Inches(3.0), Inches(0.8), Inches(1.1)]

w_hdr_cells = t_weeks.rows[0].cells
make_row_header_repeat(t_weeks.rows[0])
prevent_row_split(t_weeks.rows[0])
for idx, text in enumerate(w_headers):
    w_hdr_cells[idx].text = text
    set_cell_background(w_hdr_cells[idx], "0284C7") # Cyan blue
    set_cell_margins(w_hdr_cells[idx], top=100, bottom=100, left=80, right=80)
    p = w_hdr_cells[idx].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

week_summary_data = [
    ("Tuần 1", "14/09 – 20/09/2026", "Khởi tạo & Sprint 1", "Project Charter, WBS, BRD/SRS v4, ERD CSDL, Setup Express MVC, Wireframe Figma", "30 Tasks", "Đã hoàn thành"),
    ("Tuần 2", "21/09 – 27/09/2026", "Sprint 1 (Hoàn tất)", "Auth JWT 3 vai trò, Khách hàng B2B, Job, Candidate, Deal Placement, Sprint 1 Review", "32 Tasks", "Đã hoàn thành"),
    ("Tuần 3", "28/09 – 04/10/2026", "Sprint 2 (Phần 1)", "Phát hành Hóa đơn Invoicing, Thuế VAT 8%, Net Days Due Date, Mẫu in PDF, Thanh toán", "32 Tasks", "Đã hoàn thành"),
    ("Tuần 4", "05/10 – 11/10/2026", "Sprint 2 (P.2) & Sprint 3", "Đối soát công nợ, Tuổi nợ Aging 3 xô (1-30, 31-60, >60), Nhắc nợ, Nghiệm thu Sprint 2", "32 Tasks", "Đã hoàn thành"),
    ("Tuần 5", "12/10 – 18/10/2026", "Sprint 3 (Hoàn tất)", "Dashboard 4 KPI, Biểu đồ Chart.js doanh thu 12 tháng, Cơ cấu ngành, Top 5 Debtors", "31 Tasks", "Đã hoàn thành"),
    ("Tuần 6", "19/10 – 25/10/2026", "Sprint 4", "Email nhắc nợ, Audit Log hoàn chỉnh, Client Portal, Tối ưu & Đóng gói Docker Staging", "38 Tasks", "Đang thực hiện"),
    ("Tuần 7", "26/10/2026", "Nghiệm thu & Báo cáo", "Đóng gói mã nguồn, User Manual, Báo cáo PMBOK, Gantt Chart, Slide bảo vệ đồ án", "25 Tasks", "Kế hoạch")
]

for r_idx, row_vals in enumerate(week_summary_data, 1):
    row_cells = t_weeks.rows[r_idx].cells
    prevent_row_split(t_weeks.rows[r_idx])
    for c_idx, val in enumerate(row_vals):
        row_cells[c_idx].text = val
        set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=80, right=80)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1, 2, 4, 5]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.runs[0]
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        if c_idx == 5:
            if val == "Đã hoàn thành":
                set_cell_background(row_cells[c_idx], "DCFCE7") # Light Green
                r.font.bold = True
                r.font.color.rgb = RGBColor(22, 101, 52)
            elif val == "Đang thực hiện":
                set_cell_background(row_cells[c_idx], "FEF3C7") # Light Yellow
                r.font.bold = True
                r.font.color.rgb = RGBColor(146, 64, 14)
            else:
                set_cell_background(row_cells[c_idx], "F1F5F9") # Light Gray
                r.font.color.rgb = RGBColor(71, 85, 105)
        elif r_idx % 2 == 0:
            set_cell_background(row_cells[c_idx], "F8FAFC")

for row in t_weeks.rows:
    for idx, width in enumerate(w_widths):
        row.cells[idx].width = width

# ==============================================================================
# 4. PHẦN 3: PHÂN BỔ KHỐI LƯỢNG CHO 5 THÀNH VIÊN
# ==============================================================================
h3 = doc.add_paragraph()
h3.paragraph_format.space_before = Pt(14)
h3.paragraph_format.space_after = Pt(6)
r_h3 = h3.add_run("3. PHÂN BỔ KHỐI LƯỢNG CÔNG VIỆC CHO 5 THÀNH VIÊN (220 TASKS)")
r_h3.font.name = "Calibri"
r_h3.font.size = Pt(13)
r_h3.font.bold = True
r_h3.font.color.rgb = RGBColor(30, 58, 138)

t_alloc = doc.add_table(rows=6, cols=6)
t_alloc.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_alloc)

a_headers = ["Thành Viên", "Vai Trò Chính", "Số Task", "Tỷ Lệ (%)", "Story Points", "Giờ Công Ước Tính"]
a_widths = [Inches(1.8), Inches(2.2), Inches(1.0), Inches(1.1), Inches(1.3), Inches(1.5)]

a_hdr_cells = t_alloc.rows[0].cells
make_row_header_repeat(t_alloc.rows[0])
prevent_row_split(t_alloc.rows[0])
for idx, text in enumerate(a_headers):
    a_hdr_cells[idx].text = text
    set_cell_background(a_hdr_cells[idx], "1E3A8A")
    set_cell_margins(a_hdr_cells[idx], top=100, bottom=100, left=80, right=80)
    p = a_hdr_cells[idx].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

member_alloc_data = [
    ("Nguyễn Hữu Phúc", "Project Manager (PM) - Quản lý & Báo cáo", "43 Tasks", "19.5%", "88 SP", "165 Giờ"),
    ("Nguyễn Xuân Đoàn", "Business Analyst (BA) - Nghiệp vụ & UAT", "41 Tasks", "18.6%", "97 SP", "172 Giờ"),
    ("Phạm Văn Sơn", "Backend Developer (BE) - Node.js Express API", "48 Tasks", "21.8%", "118 SP", "210 Giờ"),
    ("Nguyễn Hoàng Phước", "Frontend Developer (FE) - Web UI & Chart.js", "47 Tasks", "21.4%", "105 SP", "195 Giờ"),
    ("Huỳnh Nguyễn Vĩnh Phúc", "Tester & DB Admin (DB/QA) - Test Suite & DB", "41 Tasks", "18.6%", "87 SP", "158 Giờ")
]

for r_idx, row_vals in enumerate(member_alloc_data, 1):
    row_cells = t_alloc.rows[r_idx].cells
    prevent_row_split(t_alloc.rows[r_idx])
    for c_idx, val in enumerate(row_vals):
        row_cells[c_idx].text = val
        set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=80, right=80)
        p = row_cells[c_idx].paragraphs[0]
        if c_idx in [0, 1]:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.runs[0]
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        if r_idx % 2 == 0:
            set_cell_background(row_cells[c_idx], "F8FAFC")

for row in t_alloc.rows:
    for idx, width in enumerate(a_widths):
        row.cells[idx].width = width

# ==============================================================================
# 5. PHẦN 4: CHI TIẾT 220 TASK THEO TỪNG TUẦN (TUẦN 1 -> TUẦN 7)
# ==============================================================================
h4 = doc.add_paragraph()
h4.paragraph_format.space_before = Pt(16)
h4.paragraph_format.space_after = Pt(6)
r_h4 = h4.add_run("4. DANH SÁCH CHI TIẾT 220 TASK PHÂN BỔ THEO 7 TUẦN")
r_h4.font.name = "Calibri"
r_h4.font.size = Pt(14)
r_h4.font.bold = True
r_h4.font.color.rgb = RGBColor(30, 58, 138)

weeks_list = ["Tuần 1", "Tuần 2", "Tuần 3", "Tuần 4", "Tuần 5", "Tuần 6", "Tuần 7"]
week_meta = {
    "Tuần 1": ("Khởi tạo & Sprint 1 (14/09 – 20/09/2026)", "Thiết lập nền tảng dự án: Project Charter, WBS, BRD/SRS v4.0, ERD 8 bảng, Khung Express MVC & Wireframe Figma"),
    "Tuần 2": ("Sprint 1 Hoàn tất (21/09 – 27/09/2026)", "Hoàn thành Sprint 1: Xác thực JWT & RBAC 3 vai trò, Quản lý Khách hàng B2B, Job/Candidate, Deal Placement & Review 1"),
    "Tuần 3": ("Sprint 2 - Phần 1 (28/09 – 04/10/2026)", "Phát hành hóa đơn tự động từ Deal, công thức VAT 8%, Net Days Due Date, mẫu in PDF và ghi nhận thanh toán/phiếu thu"),
    "Tuần 4": ("Sprint 2 - Phần 2 & Khởi động Sprint 3 (05/10 – 11/10/2026)", "Đối soát công nợ, phân tích tuổi nợ Aging 3 xô (1-30, 31-60, >60 ngày), gửi thông báo nhắc nợ và khởi động API Dashboard"),
    "Tuần 5": ("Sprint 3 Hoàn tất (12/10 – 18/10/2026)", "Hoàn thiện Dashboard 4 thẻ KPI, Biểu đồ Chart.js doanh thu 12 tháng, Cơ cấu ngành, Bảng Top 5 Debtors và Xuất báo cáo CSV/PDF"),
    "Tuần 6": ("Sprint 4 Tối ưu & Staging (19/10 – 25/10/2026)", "Email nhắc nợ tự động, Module Audit Log hoàn chỉnh, Client Portal, Tối ưu hiệu năng, Bộ test tự động 100% & Docker Staging"),
    "Tuần 7": ("Nghiệm thu, Báo cáo & Bảo vệ Đồ án (26/10/2026)", "Đóng gói mã nguồn, User Manual, Báo cáo PMBOK tổng kết (QLDA_Nhom10_Lab.docx), Biểu đồ Gantt Chart & Slide thuyết trình")
}

task_col_headers = ["Mã Task", "Tên Công Việc & Quy Ước Commit Git", "Người Phụ Trách", "Phân Hệ / WBS", "Bắt Đầu - Kết Thúc", "SP/Giờ", "Kết Quả Bàn Giao", "Trạng Thái"]
task_col_widths = [Inches(0.85), Inches(2.2), Inches(1.3), Inches(1.1), Inches(1.0), Inches(0.65), Inches(1.2), Inches(0.85)]

for w_name in weeks_list:
    w_tasks = [t for t in tasks if t['week'] == w_name]
    sprint_title, sprint_goal = week_meta[w_name]
    
    # Heading từng tuần
    wp = doc.add_paragraph()
    wp.paragraph_format.space_before = Pt(14)
    wp.paragraph_format.space_after = Pt(2)
    r_wp = wp.add_run(f"🗓️ {w_name.upper()}: {sprint_title} ({len(w_tasks)} Tasks)")
    r_wp.font.name = "Calibri"
    r_wp.font.size = Pt(11.5)
    r_wp.font.bold = True
    r_wp.font.color.rgb = RGBColor(2, 132, 199) # Blue accent
    
    # Mục tiêu tuần
    wg = doc.add_paragraph()
    wg.paragraph_format.space_after = Pt(6)
    r_wg_lbl = wg.add_run("Mục tiêu trọng tâm: ")
    r_wg_lbl.font.bold = True
    r_wg_lbl.font.size = Pt(9)
    r_wg_lbl.font.color.rgb = RGBColor(71, 85, 105)
    r_wg = wg.add_run(sprint_goal)
    r_wg.font.size = Pt(9)
    r_wg.font.italic = True
    r_wg.font.color.rgb = RGBColor(71, 85, 105)
    
    # Bảng chi tiết task trong tuần
    table = doc.add_table(rows=len(w_tasks) + 1, cols=8)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    
    # Tiêu đề bảng
    hdr = table.rows[0]
    make_row_header_repeat(hdr)
    prevent_row_split(hdr)
    for c_idx, h_text in enumerate(task_col_headers):
        hdr.cells[c_idx].text = h_text
        set_cell_background(hdr.cells[c_idx], "1E3A8A")
        set_cell_margins(hdr.cells[c_idx], top=80, bottom=80, left=60, right=60)
        p = hdr.cells[c_idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.runs[0]
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
    
    # Điền dữ liệu từng task
    for t_idx, t in enumerate(w_tasks, 1):
        row = table.rows[t_idx]
        prevent_row_split(row)
        
        # Cột 1: Mã Task
        c0 = row.cells[0]
        c0.text = t['tid']
        c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c0.paragraphs[0].runs[0].font.bold = True
        c0.paragraphs[0].runs[0].font.size = Pt(8)
        
        # Cột 2: Tên công việc + Commit
        c1 = row.cells[1]
        c1.text = ""
        p1 = c1.paragraphs[0]
        r1_name = p1.add_run(t['name'] + "\n")
        r1_name.font.bold = True
        r1_name.font.size = Pt(8.5)
        r1_commit = p1.add_run(f"commit: {t['commit']}")
        r1_commit.font.size = Pt(7.5)
        r1_commit.font.italic = True
        r1_commit.font.color.rgb = RGBColor(100, 116, 139)
        
        # Cột 3: Người phụ trách
        c2 = row.cells[2]
        c2.text = t['assignee']
        c2.paragraphs[0].runs[0].font.size = Pt(8)
        
        # Cột 4: Phân hệ / WBS
        c3 = row.cells[3]
        c3.text = f"{t['module']}\n({t['wbs']})"
        c3.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c3.paragraphs[0].runs[0].font.size = Pt(7.5)
        
        # Cột 5: Bắt đầu - Kết thúc
        c4 = row.cells[4]
        # Hiển thị dd/mm
        s_date = t['start'].split('/')[0] + '/' + t['start'].split('/')[1]
        e_date = t['end'].split('/')[0] + '/' + t['end'].split('/')[1]
        c4.text = f"{s_date} – {e_date}"
        c4.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c4.paragraphs[0].runs[0].font.size = Pt(8)
        
        # Cột 6: SP / Giờ
        c5 = row.cells[5]
        c5.text = f"{t['sp']} SP\n({t['hours']}h)"
        c5.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c5.paragraphs[0].runs[0].font.size = Pt(7.5)
        
        # Cột 7: Deliverable
        c6 = row.cells[6]
        c6.text = t['deliverable']
        c6.paragraphs[0].runs[0].font.size = Pt(7.5)
        
        # Cột 8: Trạng thái
        c7 = row.cells[7]
        c7.text = t['status']
        c7.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        r7 = c7.paragraphs[0].runs[0]
        r7.font.size = Pt(7.5)
        r7.font.bold = True
        if t['status'] == "Đã hoàn thành":
            set_cell_background(c7, "DCFCE7") # Green
            r7.font.color.rgb = RGBColor(22, 101, 52)
        elif t['status'] == "Đang thực hiện":
            set_cell_background(c7, "FEF3C7") # Yellow
            r7.font.color.rgb = RGBColor(146, 64, 14)
        else:
            set_cell_background(c7, "F1F5F9") # Gray
            r7.font.color.rgb = RGBColor(71, 85, 105)
            
        # Padding & shading cho các ô
        for col_i in range(8):
            set_cell_margins(row.cells[col_i], top=60, bottom=60, left=50, right=50)
            if t_idx % 2 == 0 and col_i != 7:
                set_cell_background(row.cells[col_i], "F8FAFC")
                
    # Áp dụng độ rộng cột
    for row in table.rows:
        for idx, width in enumerate(task_col_widths):
            row.cells[idx].width = width

# ==============================================================================
# 6. PHẦN 5: HƯỚNG DẪN MỞ RỘNG VÀ THÊM TASK SAU NÀY (CHO TASK 221 TRỞ ĐI)
# ==============================================================================
h5 = doc.add_paragraph()
h5.paragraph_format.space_before = Pt(16)
h5.paragraph_format.space_after = Pt(6)
r_h5 = h5.add_run("5. HƯỚNG DẪN MỞ RỘNG VÀ THÊM TASK MỚI (TỪ TASK 221 TRỞ ĐI)")
r_h5.font.name = "Calibri"
r_h5.font.size = Pt(13)
r_h5.font.bold = True
r_h5.font.color.rgb = RGBColor(30, 58, 138)

p_exp = doc.add_paragraph()
p_exp.paragraph_format.space_after = Pt(8)
r_exp = p_exp.add_run(
    "Dự án được thiết kế theo cấu trúc mở chuẩn Scrum và PMBOK. Khi có yêu cầu phát sinh hoặc mở rộng giai đoạn 2, "
    "nhóm tiếp tục bổ sung task tuần tự theo mẫu chuẩn sau để đảm bảo tính đồng bộ mã nguồn và báo cáo:"
)
r_exp.font.size = Pt(9.5)

# Bảng mẫu thêm task mới
t_sample = doc.add_table(rows=2, cols=8)
t_sample.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(t_sample)

sample_hdr = t_sample.rows[0]
for idx, text in enumerate(task_col_headers):
    sample_hdr.cells[idx].text = text
    set_cell_background(sample_hdr.cells[idx], "0284C7")
    set_cell_margins(sample_hdr.cells[idx], top=80, bottom=80, left=60, right=60)
    p = sample_hdr.cells[idx].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(8.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

sample_row = t_sample.rows[1]
sample_vals = [
    "TASK-221",
    "Tích hợp cổng VietQR thanh toán tự động gạch nợ\ncommit: TichHopVietQRPayment_phamson",
    "Phạm Văn Sơn (BE)",
    "Cổng thanh toán\n(WBS 6.1)",
    "27/10 – 28/10",
    "3 SP\n(6h)",
    "API sinh mã VietQR và webhook callback",
    "Kế hoạch"
]

for idx, val in enumerate(sample_vals):
    sample_row.cells[idx].text = val
    set_cell_margins(sample_row.cells[idx], top=60, bottom=60, left=50, right=50)
    p = sample_row.cells[idx].paragraphs[0]
    if idx in [0, 3, 4, 5, 7]:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(8)
    if idx == 7:
        set_cell_background(sample_row.cells[idx], "F1F5F9")
        r.font.bold = True

for row in t_sample.rows:
    for idx, width in enumerate(task_col_widths):
        row.cells[idx].width = width

# Danh mục phân hệ mở rộng gợi ý
p_sug = doc.add_paragraph()
p_sug.paragraph_format.space_before = Pt(10)
p_sug.paragraph_format.space_after = Pt(4)
r_sug = p_sug.add_run("Các phân hệ đề xuất phát triển mở rộng trong Giai đoạn 2:")
r_sug.font.bold = True
r_sug.font.size = Pt(10)
r_sug.font.color.rgb = RGBColor(30, 58, 138)

suggestions = [
    "Module Cổng thanh toán trực tuyến VietQR / VNPay: Tự động gạch nợ hóa đơn khi khách hàng quét mã QR thanh toán thành công.",
    "Module Ứng dụng Di động (Mobile App React Native/Flutter): Cho phép Recruiter xem hoa hồng và Kế toán phê duyệt nhanh thanh toán.",
    "Module AI Dự đoán Rủi ro Nợ xấu (Predictive Debt Analytics): Sử dụng Machine Learning đánh giá xác suất chậm trả nợ của doanh nghiệp B2B."
]

for s in suggestions:
    p_item = doc.add_paragraph(style='List Bullet')
    p_item.paragraph_format.space_after = Pt(2)
    r_item = p_item.add_run(s)
    r_item.font.size = Pt(9)
    r_item.font.color.rgb = RGBColor(51, 65, 85)

# Lưu file
docx_path = r'c:\Users\phuco\QLDA_NHOM10_GODDY\KE_HOACH_PHAN_CHIA_TASK_THEO_TUAN.docx'
doc.save(docx_path)
print(f"Xuất file Word thành công tại: {docx_path}")
