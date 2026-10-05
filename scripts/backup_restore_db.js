/**
 * Script Sao Lưu & Phục Hồi CSDL Tự Động - Dự Án GODDY Recruit
 * Phụ trách: Huỳnh Nguyễn Vĩnh Phúc (Tester & Database Admin - SV5)
 * Hỗ trợ: Backup file SQLite, dump cấu trúc và phục hồi an toàn
 */

const fs = require('fs');
const path = require('path');

const DB_PATH = path.join(__dirname, '..', 'database.sqlite');
const BACKUP_DIR = path.join(__dirname, '..', 'backups');

// Đảm bảo thư mục backups tồn tại
if (!fs.existsSync(BACKUP_DIR)) {
  fs.mkdirSync(BACKUP_DIR, { recursive: true });
}

function getTimestamp() {
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  const hh = String(now.getHours()).padStart(2, '0');
  const min = String(now.getMinutes()).padStart(2, '0');
  const ss = String(now.getSeconds()).padStart(2, '0');
  return `${yyyy}${mm}${dd}_${hh}${min}${ss}`;
}

// 1. Sao lưu CSDL
function backupDatabase() {
  if (!fs.existsSync(DB_PATH)) {
    console.error(`[Lỗi] Không tìm thấy file CSDL tại: ${DB_PATH}`);
    return null;
  }

  const timestamp = getTimestamp();
  const backupFileName = `database_backup_${timestamp}.sqlite`;
  const backupFilePath = path.join(BACKUP_DIR, backupFileName);

  try {
    fs.copyFileSync(DB_PATH, backupFilePath);
    const stats = fs.statSync(backupFilePath);
    const sizeKB = (stats.size / 1024).toFixed(2);

    console.log('====================================================');
    console.log('     SAO LƯU CƠ SỞ DỮ LIỆU THÀNH CÔNG (BACKUP PASS) ');
    console.log('====================================================');
    console.log(` File gốc     : ${path.basename(DB_PATH)}`);
    console.log(` File sao lưu : ${backupFileName}`);
    console.log(` Vị trí       : ${BACKUP_DIR}`);
    console.log(` Kích thước   : ${sizeKB} KB`);
    console.log(` Thời gian    : ${new Date().toLocaleString('vi-VN')}`);
    console.log('====================================================\n');
    return backupFilePath;
  } catch (error) {
    console.error('[Lỗi sao lưu]:', error.message);
    return null;
  }
}

// 2. Danh sách các bản sao lưu
function listBackups() {
  console.log('====================================================');
  console.log('          DANH SÁCH BẢN SAO LƯU CSDL HIỆN CÓ        ');
  console.log('====================================================');

  const files = fs.readdirSync(BACKUP_DIR).filter(f => f.endsWith('.sqlite'));
  if (files.length === 0) {
    console.log('  (Chưa có bản sao lưu nào trong thư mục backups/)');
  } else {
    files.forEach((file, index) => {
      const stats = fs.statSync(path.join(BACKUP_DIR, file));
      const sizeKB = (stats.size / 1024).toFixed(2);
      console.log(`  ${index + 1}. ${file} (${sizeKB} KB - ${stats.mtime.toLocaleString('vi-VN')})`);
    });
  }
  console.log('====================================================\n');
  return files;
}

// 3. Phục hồi CSDL
function restoreDatabase(backupFileName) {
  if (!backupFileName) {
    // Tự động lấy bản mới nhất
    const files = fs.readdirSync(BACKUP_DIR).filter(f => f.endsWith('.sqlite'));
    if (files.length === 0) {
      console.error('[Lỗi] Không có bản sao lưu nào để phục hồi!');
      return false;
    }
    files.sort((a, b) => fs.statSync(path.join(BACKUP_DIR, b)).mtime - fs.statSync(path.join(BACKUP_DIR, a)).mtime);
    backupFileName = files[0];
  }

  const sourceBackup = path.join(BACKUP_DIR, backupFileName);
  if (!fs.existsSync(sourceBackup)) {
    console.error(`[Lỗi] Không tìm thấy bản sao lưu: ${sourceBackup}`);
    return false;
  }

  try {
    // Tạo bản backup snapshot trước khi ghi đè
    if (fs.existsSync(DB_PATH)) {
      const safetyBackup = path.join(BACKUP_DIR, `database_before_restore_${getTimestamp()}.sqlite`);
      fs.copyFileSync(DB_PATH, safetyBackup);
    }

    fs.copyFileSync(sourceBackup, DB_PATH);
    console.log('====================================================');
    console.log('    PHỤC HỒI CƠ SỞ DỮ LIỆU THÀNH CÔNG (RESTORE PASS)');
    console.log('====================================================');
    console.log(` Bản sao lưu nguồn : ${backupFileName}`);
    console.log(` CSDL mục tiêu     : ${path.basename(DB_PATH)}`);
    console.log(` Trạng thái        : Đã khôi phục nguyên vẹn 100%`);
    console.log('====================================================\n');
    return true;
  } catch (error) {
    console.error('[Lỗi phục hồi]:', error.message);
    return false;
  }
}

// Xử lý tham số dòng lệnh CLI
const command = process.argv[2] || 'backup';
const targetFile = process.argv[3];

if (command === 'backup') {
  backupDatabase();
} else if (command === 'list') {
  listBackups();
} else if (command === 'restore') {
  restoreDatabase(targetFile);
} else {
  console.log('Cách dùng:');
  console.log('  node scripts/backup_restore_db.js backup           # Tạo bản sao lưu mới');
  console.log('  node scripts/backup_restore_db.js list             # Xem danh sách bản sao lưu');
  console.log('  node scripts/backup_restore_db.js restore [file]   # Phục hồi CSDL từ bản sao lưu');
}

module.exports = { backupDatabase, listBackups, restoreDatabase };
