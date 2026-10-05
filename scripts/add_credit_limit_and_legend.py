# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as ET

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def enhance_erd(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    graph_model = root.find('diagram').find('mxGraphModel').find('root')

    # 1. Thêm creditLimit vào tbl_clients nếu chưa có
    tbl_clients = None
    for cell in graph_model.findall('mxCell'):
        if cell.get('id') == 'tbl_clients':
            tbl_clients = cell
            break

    existing_col_ids = [cell.get('id') for cell in graph_model.findall('mxCell')]
    if 'tbl_clients_col_creditLimit' not in existing_col_ids and tbl_clients is not None:
        # Tăng chiều cao của tbl_clients từ 296 lên 320
        geo = tbl_clients.find('mxGeometry')
        if geo is not None:
            geo.set('height', '320')

        # Tạo cell mới cho creditLimit
        new_col = ET.Element('mxCell', {
            'id': 'tbl_clients_col_creditLimit',
            'parent': 'tbl_clients',
            'style': 'text;strokeColor=none;fillColor=#ffffff;align=left;verticalAlign=middle;spacingLeft=10;spacingRight=8;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontColor=#0f172a;fontSize=12;',
            'value': 'creditLimit <span style="color:#64748b; font-size:11px;">: DECIMAL(15,2)</span> &nbsp;<b>(Hạn mức nợ tối đa VNĐ)</b>',
            'vertex': '1'
        })
        new_geo = ET.Element('mxGeometry', {
            'height': '24',
            'width': '380',
            'y': '224',
            'as': 'geometry'
        })
        new_col.append(new_geo)

        # Đẩy các dòng bên dưới xuống (status, createdAt, updatedAt)
        for cell in graph_model.findall('mxCell'):
            if cell.get('parent') == 'tbl_clients':
                cid = cell.get('id', '')
                cgeo = cell.find('mxGeometry')
                if cgeo is not None:
                    if cid == 'tbl_clients_col_8': # status
                        cgeo.set('y', '248')
                        cell.set('style', cell.get('style', '').replace('fillColor=#ffffff', 'fillColor=#f1f5f9'))
                    elif cid == 'tbl_clients_col_9': # createdAt
                        cgeo.set('y', '272')
                        cell.set('style', cell.get('style', '').replace('fillColor=#f1f5f9', 'fillColor=#ffffff'))
                    elif cid == 'tbl_clients_col_10': # updatedAt
                        cgeo.set('y', '296')
                        cell.set('style', cell.get('style', '').replace('fillColor=#ffffff', 'fillColor=#f1f5f9'))

        # Chèn new_col vào graph_model
        graph_model.append(new_col)
        print("Đã thêm thuộc tính creditLimit vào bảng Khách hàng B2B.")

    # 2. Thêm hộp Chú giải Bảng (Legend) nếu chưa có
    if 'legend_box' not in existing_col_ids:
        legend_cell = ET.Element('mxCell', {
            'id': 'legend_box',
            'parent': '1',
            'style': 'rounded=1;whiteSpace=wrap;html=1;fillColor=#f8fafc;strokeColor=#0284c7;strokeWidth=2;shadow=1;align=left;spacingLeft=12;verticalAlign=top;fontSize=12;fontColor=#0f172a;',
            'value': '&lt;b style=&quot;color:#0369a1; font-size:14px;&quot;&gt;📌 BẢNG CHÚ GIẢI THỰC THỂ QUAN HỆ (ERD LEGEND)&lt;/b&gt;&lt;br&gt;&lt;br&gt;' +
                     '&lt;b style=&quot;color:#dc2626;&quot;&gt;[PK]&lt;/b&gt; Primary Key: Khóa chính (Định danh duy nhất, NOT NULL)&lt;br&gt;' +
                     '&lt;b style=&quot;color:#2563eb;&quot;&gt;[FK]&lt;/b&gt; Foreign Key: Khóa ngoại (Ràng buộc toàn vẹn tham chiếu)&lt;br&gt;' +
                     '&lt;b style=&quot;color:#059669;&quot;&gt;[UK]&lt;/b&gt; Unique Key: Khóa duy nhất (Chống trùng lặp dữ liệu)&lt;br&gt;&lt;br&gt;' +
                     '&lt;b&gt;1 - 1&lt;/b&gt; : Quan hệ Một - Một (Một Deal xuất duy nhất một Hóa đơn VAT)&lt;br&gt;' +
                     '&lt;b&gt;1 - N&lt;/b&gt; : Quan hệ Một - Nhiều (Một Khách hàng có nhiều Deal / Hóa đơn)&lt;br&gt;&lt;br&gt;' +
                     '&lt;span style=&quot;color:#475569; font-size:11px;&quot;&gt;🎓 &lt;b&gt;Thiết kế &amp;amp; Quản trị CSDL:&lt;/b&gt; Huỳnh Nguyễn Vĩnh Phúc (MSSV: 2380614923 - DBA &amp;amp; QA)&lt;/span&gt;',
            'vertex': '1'
        })
        legend_geo = ET.Element('mxGeometry', {
            'x': '1170',
            'y': '-190',
            'width': '480',
            'height': '170',
            'as': 'geometry'
        })
        legend_cell.append(legend_geo)
        graph_model.append(legend_cell)
        print("Đã thêm Bảng chú giải ERD Legend chuẩn đồ án.")

    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print(f"Cập nhật hoàn tất: {filepath}")

if __name__ == '__main__':
    enhance_erd('ERD_QLDA_NHOM10_GODDY.drawio')
    try:
        enhance_erd(r'C:\Users\phuco\.gemini\antigravity-ide\brain\323f00f0-15d6-4822-9929-38126dd7cf0b\scratch\repo_sv5\ERD_QLDA_NHOM10_GODDY.drawio')
    except Exception as e:
        print("Bỏ qua:", e)
