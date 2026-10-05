# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as ET

# Đảm bảo mã hóa UTF-8 cho console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Từ điển ánh xạ cột sang Tiếng Việt chuẩn hóa cho CSDL GODDY Recruit
COLUMN_TRANSLATIONS = {
    # Users
    ("tbl_users", "tbl_users_col_0"): ('<b style="color:#dc2626;">[PK]</b> id <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã người dùng)</b>'),
    ("tbl_users", "tbl_users_col_1"): ('<b style="color:#059669;">[UK]</b> username <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Tên đăng nhập)</b>'),
    ("tbl_users", "tbl_users_col_2"): ('<b style="color:#059669;">[UK]</b> email <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Thư điện tử)</b>'),
    ("tbl_users", "tbl_users_col_3"): ('password <span style="color:#64748b; font-size:11px;">: NVARCHAR(255)</span> &nbsp;<b>(Mật khẩu băm Bcrypt)</b>'),
    ("tbl_users", "tbl_users_col_4"): ('fullName <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Họ và tên hiển thị)</b>'),
    ("tbl_users", "tbl_users_col_5"): ('role <span style="color:#64748b; font-size:11px;">: NVARCHAR(20)</span> &nbsp;<b>(Vai trò: admin/accountant/recruiter)</b>'),
    ("tbl_users", "tbl_users_col_6"): ('avatar <span style="color:#64748b; font-size:11px;">: NVARCHAR(MAX)</span> &nbsp;<b>(Ảnh đại diện)</b>'),
    ("tbl_users", "tbl_users_col_7"): ('isActive <span style="color:#64748b; font-size:11px;">: BIT</span> &nbsp;<b>(Trạng thái: Hoạt động/Khóa)</b>'),
    ("tbl_users", "tbl_users_col_8"): ('createdAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm tạo tài khoản)</b>'),
    ("tbl_users", "tbl_users_col_9"): ('updatedAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm cập nhật)</b>'),

    # AuditLogs
    ("tbl_audit", "tbl_audit_col_0"): ('<b style="color:#dc2626;">[PK]</b> id <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã bản ghi nhật ký)</b>'),
    ("tbl_audit", "tbl_audit_col_1"): ('<b style="color:#2563eb;">[FK]</b> userId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã người thực hiện)</b>'),
    ("tbl_audit", "tbl_audit_col_2"): ('action <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Hành động thao tác)</b>'),
    ("tbl_audit", "tbl_audit_col_3"): ('module <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Phân hệ tác động)</b>'),
    ("tbl_audit", "tbl_audit_col_4"): ('details <span style="color:#64748b; font-size:11px;">: NVARCHAR(MAX)</span> &nbsp;<b>(Nội dung chi tiết thay đổi)</b>'),
    ("tbl_audit", "tbl_audit_col_5"): ('createdAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm ghi nhận log)</b>'),
    ("tbl_audit", "tbl_audit_col_6"): ('updatedAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm cập nhật log)</b>'),

    # Candidates
    ("tbl_candidates", "tbl_candidates_col_0"): ('<b style="color:#dc2626;">[PK]</b> id <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã hồ sơ ứng viên)</b>'),
    ("tbl_candidates", "tbl_candidates_col_1"): ('fullName <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Họ tên ứng viên)</b>'),
    ("tbl_candidates", "tbl_candidates_col_2"): ('<b style="color:#059669;">[UK]</b> email <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Email liên hệ ứng viên)</b>'),
    ("tbl_candidates", "tbl_candidates_col_3"): ('phone <span style="color:#64748b; font-size:11px;">: NVARCHAR(20)</span> &nbsp;<b>(Số điện thoại ứng viên)</b>'),
    ("tbl_candidates", "tbl_candidates_col_4"): ('currentPosition <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Vị trí chuyên môn hiện tại)</b>'),
    ("tbl_candidates", "tbl_candidates_col_5"): ('status <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Trạng thái: Sẵn sàng/Đã tuyển)</b>'),
    ("tbl_candidates", "tbl_candidates_col_6"): ('createdAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Ngày tiếp nhận hồ sơ)</b>'),
    ("tbl_candidates", "tbl_candidates_col_7"): ('updatedAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm cập nhật)</b>'),

    # Clients
    ("tbl_clients", "tbl_clients_col_0"): ('<b style="color:#dc2626;">[PK]</b> id <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã khách hàng B2B)</b>'),
    ("tbl_clients", "tbl_clients_col_1"): ('companyName <span style="color:#64748b; font-size:11px;">: NVARCHAR(200)</span> &nbsp;<b>(Tên công ty / Doanh nghiệp)</b>'),
    ("tbl_clients", "tbl_clients_col_2"): ('<b style="color:#059669;">[UK]</b> taxCode <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Mã số thuế doanh nghiệp)</b>'),
    ("tbl_clients", "tbl_clients_col_3"): ('address <span style="color:#64748b; font-size:11px;">: NVARCHAR(255)</span> &nbsp;<b>(Địa chỉ trụ sở công ty)</b>'),
    ("tbl_clients", "tbl_clients_col_4"): ('contactPerson <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Người đại diện liên hệ)</b>'),
    ("tbl_clients", "tbl_clients_col_5"): ('contactEmail <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Email liên hệ làm việc)</b>'),
    ("tbl_clients", "tbl_clients_col_6"): ('contactPhone <span style="color:#64748b; font-size:11px;">: NVARCHAR(20)</span> &nbsp;<b>(Số điện thoại liên hệ)</b>'),
    ("tbl_clients", "tbl_clients_col_7"): ('paymentTermDays <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Hạn nợ Net Days: 15/30/45 ngày)</b>'),
    ("tbl_clients", "tbl_clients_col_8"): ('status <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Trạng thái: Hoạt động/Tạm dừng)</b>'),
    ("tbl_clients", "tbl_clients_col_9"): ('createdAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Ngày ký kết hợp tác)</b>'),
    ("tbl_clients", "tbl_clients_col_10"): ('updatedAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm cập nhật)</b>'),

    # Jobs
    ("tbl_jobs", "tbl_jobs_col_0"): ('<b style="color:#dc2626;">[PK]</b> id <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã vị trí tuyển dụng)</b>'),
    ("tbl_jobs", "tbl_jobs_col_1"): ('<b style="color:#2563eb;">[FK]</b> clientId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã công ty đặt hàng)</b>'),
    ("tbl_jobs", "tbl_jobs_col_2"): ('title <span style="color:#64748b; font-size:11px;">: NVARCHAR(150)</span> &nbsp;<b>(Chức danh cần tuyển: Dev/BA/PM)</b>'),
    ("tbl_jobs", "tbl_jobs_col_3"): ('department <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Phòng ban / Khối chuyên môn)</b>'),
    ("tbl_jobs", "tbl_jobs_col_4"): ('salaryRange <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Khung lương thỏa thuận)</b>'),
    ("tbl_jobs", "tbl_jobs_col_5"): ('feeRatePercent <span style="color:#64748b; font-size:11px;">: FLOAT</span> &nbsp;<b>(Tỷ lệ phí dịch vụ: 15% - 25%)</b>'),
    ("tbl_jobs", "tbl_jobs_col_6"): ('status <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Trạng thái: Đang tuyển/Đã đóng)</b>'),
    ("tbl_jobs", "tbl_jobs_col_7"): ('createdAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Ngày đăng yêu cầu tuyển)</b>'),
    ("tbl_jobs", "tbl_jobs_col_8"): ('updatedAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm cập nhật)</b>'),

    # Placements
    ("tbl_placements", "tbl_placements_col_0"): ('<b style="color:#dc2626;">[PK]</b> id <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã hợp đồng Deal)</b>'),
    ("tbl_placements", "tbl_placements_col_1"): ('<b style="color:#2563eb;">[FK]</b> jobId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã vị trí tuyển dụng)</b>'),
    ("tbl_placements", "tbl_placements_col_2"): ('<b style="color:#2563eb;">[FK]</b> candidateId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã ứng viên trúng tuyển)</b>'),
    ("tbl_placements", "tbl_placements_col_3"): ('<b style="color:#2563eb;">[FK]</b> clientId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã doanh nghiệp tiếp nhận)</b>'),
    ("tbl_placements", "tbl_placements_col_4"): ('<b style="color:#2563eb;">[FK]</b> recruiterId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã chuyên viên phụ trách Deal)</b>'),
    ("tbl_placements", "tbl_placements_col_5"): ('officialSalary <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Mức lương chính thức VNĐ)</b>'),
    ("tbl_placements", "tbl_placements_col_6"): ('serviceFee <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Phí dịch vụ Headhunt VNĐ)</b>'),
    ("tbl_placements", "tbl_placements_col_7"): ('onboardDate <span style="color:#64748b; font-size:11px;">: DATE</span> &nbsp;<b>(Ngày ứng viên bắt đầu đi làm)</b>'),
    ("tbl_placements", "tbl_placements_col_8"): ('warrantyDays <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Thời hạn bảo hành: 60 ngày)</b>'),
    ("tbl_placements", "tbl_placements_col_9"): ('warrantyEndDate <span style="color:#64748b; font-size:11px;">: DATE</span> &nbsp;<b>(Ngày kết thúc bảo hành)</b>'),
    ("tbl_placements", "tbl_placements_col_10"): ('status <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Trạng thái: Bảo hành/Hoàn tất)</b>'),
    ("tbl_placements", "tbl_placements_col_11"): ('createdAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Ngày ký thỏa thuận Deal)</b>'),
    ("tbl_placements", "tbl_placements_col_12"): ('updatedAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm cập nhật)</b>'),

    # Invoices
    ("tbl_invoices", "tbl_invoices_col_0"): ('<b style="color:#dc2626;">[PK]</b> id <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã định danh hóa đơn)</b>'),
    ("tbl_invoices", "tbl_invoices_col_1"): ('<b style="color:#059669;">[UK]</b> invoiceCode <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Số hóa đơn: HD-2026-...)</b>'),
    ("tbl_invoices", "tbl_invoices_col_2"): ('<b style="color:#2563eb;">[FK]</b> clientId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã khách hàng thanh toán)</b>'),
    ("tbl_invoices", "tbl_invoices_col_3"): ('<b style="color:#2563eb;">[FK]</b> placementId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã hợp đồng tuyển dụng tương ứng)</b>'),
    ("tbl_invoices", "tbl_invoices_col_4"): ('subtotal <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Tiền dịch vụ trước thuế)</b>'),
    ("tbl_invoices", "tbl_invoices_col_5"): ('vatRate <span style="color:#64748b; font-size:11px;">: FLOAT</span> &nbsp;<b>(Thuế suất VAT: 0.08 = 8%)</b>'),
    ("tbl_invoices", "tbl_invoices_col_6"): ('vatAmount <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Tiền thuế GTGT = 8% subtotal)</b>'),
    ("tbl_invoices", "tbl_invoices_col_7"): ('totalAmount <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Tổng tiền phải trả sau thuế)</b>'),
    ("tbl_invoices", "tbl_invoices_col_8"): ('paidAmount <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Số tiền khách đã thanh toán)</b>'),
    ("tbl_invoices", "tbl_invoices_col_9"): ('remainingAmount <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Số tiền công nợ còn lại)</b>'),
    ("tbl_invoices", "tbl_invoices_col_10"): ('issueDate <span style="color:#64748b; font-size:11px;">: DATE</span> &nbsp;<b>(Ngày phát hành hóa đơn)</b>'),
    ("tbl_invoices", "tbl_invoices_col_11"): ('dueDate <span style="color:#64748b; font-size:11px;">: DATE</span> &nbsp;<b>(Hạn chót thanh toán công nợ)</b>'),
    ("tbl_invoices", "tbl_invoices_col_12"): ('status <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Trạng thái: Chưa thanh toán/Trả 1 phần/Quá hạn/Hoàn tất)</b>'),
    ("tbl_invoices", "tbl_invoices_col_13"): ('createdAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Ngày xuất hóa đơn)</b>'),
    ("tbl_invoices", "tbl_invoices_col_14"): ('updatedAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm cập nhật)</b>'),

    # Payments
    ("tbl_payments", "tbl_payments_col_0"): ('<b style="color:#dc2626;">[PK]</b> id <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã phiếu thu tiền)</b>'),
    ("tbl_payments", "tbl_payments_col_1"): ('<b style="color:#2563eb;">[FK]</b> invoiceId <span style="color:#64748b; font-size:11px;">: INT</span> &nbsp;<b>(Mã hóa đơn được thanh toán)</b>'),
    ("tbl_payments", "tbl_payments_col_2"): ('amount <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Số tiền thu nợ thực tế)</b>'),
    ("tbl_payments", "tbl_payments_col_3"): ('paymentDate <span style="color:#64748b; font-size:11px;">: DATE</span> &nbsp;<b>(Ngày khách chuyển khoản)</b>'),
    ("tbl_payments", "tbl_payments_col_4"): ('paymentMethod <span style="color:#64748b; font-size:11px;">: NVARCHAR(50)</span> &nbsp;<b>(Hình thức: Chuyển khoản/Tiền mặt)</b>'),
    ("tbl_payments", "tbl_payments_col_5"): ('referenceCode <span style="color:#64748b; font-size:11px;">: NVARCHAR(100)</span> &nbsp;<b>(Mã giao dịch ngân hàng / UNC)</b>'),
    ("tbl_payments", "tbl_payments_col_6"): ('notes <span style="color:#64748b; font-size:11px;">: NVARCHAR(MAX)</span> &nbsp;<b>(Ghi chú phiếu thu nợ)</b>'),
    ("tbl_payments", "tbl_payments_col_7"): ('createdAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm ghi nhận thu nợ)</b>'),
    ("tbl_payments", "tbl_payments_col_8"): ('updatedAt <span style="color:#64748b; font-size:11px;">: DATETIME2</span> &nbsp;<b>(Thời điểm cập nhật)</b>'),
}

TABLE_TITLE_TRANSLATIONS = {
    "tbl_users": "<b>NGƯỜI DÙNG & TÀI KHOẢN (Users)</b>",
    "tbl_audit": "<b>NHẬT KÝ THAO TÁC (AuditLogs)</b>",
    "tbl_candidates": "<b>HỒ SƠ ỨNG VIÊN (Candidates)</b>",
    "tbl_clients": "<b>KHÁCH HÀNG DOANH NGHIỆP (Clients)</b>",
    "tbl_jobs": "<b>VỊ TRÍ TUYỂN DỤNG (Jobs)</b>",
    "tbl_placements": "<b>HỢP ĐỒNG TUYỂN DỤNG & DEAL (Placements)</b>",
    "tbl_invoices": "<b>HÓA ĐƠN & CÔNG NỢ VAT 8% (Invoices)</b>",
    "tbl_payments": "<b>LỊCH SỬ THU HỒI CÔNG NỢ (Payments)</b>",
}

RELATION_TRANSLATIONS = {
    "rel_users_audit": "1 - N (Thực hiện thao tác)",
    "rel_users_placements": "1 - N (Chuyên viên chốt Deal)",
    "rel_clients_jobs": "1 - N (Đặt hàng tuyển dụng)",
    "rel_clients_placements": "1 - N (Tiếp nhận nhân sự)",
    "rel_clients_invoices": "1 - N (Chịu trách nhiệm công nợ)",
    "rel_jobs_placements": "1 - N (Tuyển dụng khớp vị trí)",
    "rel_candidates_placements": "1 - N (Ứng viên nhận việc Onboard)",
    "rel_placements_invoices": "1 - 1 (Xuất hóa đơn dịch vụ)",
    "rel_invoices_payments": "1 - N (Thu nợ thanh toán từng đợt)",
}

def process_file(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    # Mở rộng chiều rộng các bảng để chữ tiếng Việt hiển thị đẹp, rõ ràng không bị che khuất
    table_widths = {
        "tbl_users": 360,
        "tbl_audit": 350,
        "tbl_candidates": 350,
        "tbl_clients": 380,
        "tbl_jobs": 370,
        "tbl_placements": 400,
        "tbl_invoices": 400,
        "tbl_payments": 370,
    }

    for cell in root.iter('mxCell'):
        cid = cell.get('id', '')
        parent = cell.get('parent', '')

        # Đổi tiêu đề bảng
        if cid in TABLE_TITLE_TRANSLATIONS:
            cell.set('value', TABLE_TITLE_TRANSLATIONS[cid])
            # Tăng chiều rộng swimlane
            geo = cell.find('mxGeometry')
            if geo is not None and cid in table_widths:
                geo.set('width', str(table_widths[cid]))

        # Đổi tên và chú thích cột
        key = (parent, cid)
        if key in COLUMN_TRANSLATIONS:
            cell.set('value', COLUMN_TRANSLATIONS[key])
            geo = cell.find('mxGeometry')
            if geo is not None and parent in table_widths:
                geo.set('width', str(table_widths[parent]))

        # Đổi nhãn quan hệ (Edge)
        if cid in RELATION_TRANSLATIONS:
            cell.set('value', RELATION_TRANSLATIONS[cid])

    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print(f"Đã Việt hóa thành công sơ đồ ERD: {filepath}")

if __name__ == '__main__':
    process_file('ERD_QLDA_NHOM10_GODDY.drawio')
    try:
        process_file(r'C:\Users\phuco\.gemini\antigravity-ide\brain\323f00f0-15d6-4822-9929-38126dd7cf0b\scratch\repo_sv5\ERD_QLDA_NHOM10_GODDY.drawio')
    except Exception as e:
        print("Bỏ qua đường dẫn scratch nếu không tồn tại:", e)
