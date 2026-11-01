# Trả lời câu hỏi thảo luận - Lab 02

### 1. Vì sao phải đồng bộ master trước khi gửi PR?
- Giúp nhánh cập nhật các thay đổi mới nhất từ master.
- Giúp phát hiện và giải quyết xung đột (conflict) sớm ngay tại máy local trước khi gửi PR lên master.

### 2. Khi nào không được rebase?
- Không được rebase trên các nhánh dùng chung (master, release/*) hoặc các commit đã được push công khai cho người khác dùng, vì rebase sẽ viết lại lịch sử (đổi SHA) gây xáo trộn.

### 3. feature/* khác topic/* ra sao?
- feature/*: Dùng để xây dựng các chức năng nghiệp vụ của hệ thống (in giỏ hàng, tìm kiếm).
- topic/*: Dùng cho các nội dung ngắn hạn ngoài tính năng nghiệp vụ (tài liệu, cấu hình, template).