# Trả lời câu hỏi thảo luận - Lab 02

### 1. Vì sao phải đồng bộ master trước khi gửi PR?
- Giúp nhánh cập nhật các thay đổi mới nhất từ master.
- Giúp phát hiện và giải quyết xung đột (conflict) sớm ngay tại máy local trước khi gửi PR lên master.

### 2. Khi nào không được rebase?
- Không được rebase trên các nhánh dùng chung (master, release/*) hoặc các commit đã được push công khai cho người khác dùng, vì rebase sẽ viết lại lịch sử (đổi SHA) gây xáo trộn.

### 3. feature/* khác topic/* ra sao?
- feature/*: Dùng để xây dựng các chức năng nghiệp vụ của hệ thống (in giỏ hàng, tìm kiếm).
- topic/*: Dùng cho các nội dung ngắn hạn ngoài tính năng nghiệp vụ (tài liệu, cấu hình, template).

---

## Ghi chú tự kiểm toán (bổ sung sau khi nộp)

### a. Review PR `feature/cart-print` (PR #3)
- Bài làm **một mình**, không có partner nên branch protection đặt `Require approvals = 0` (theo slide "Làm một mình"); vẫn bắt buộc đi qua PR. Do tác giả không thể tự approve / request changes trên GitHub, PR không có bản ghi review.
- Các commit `feat: add print_cart to Cart` và `feat: handle empty cart in print_cart` (sửa theo review) đã bị gộp chung vào một commit `c2e1158 feat: show cart details in demo program`. Lịch sử đã push và merge nên không viết lại; về sau mỗi bước được tách commit riêng.

### b. Sai sót branching policy ở `release/lab02`
- Khi PR #5 (`topic/use-case-diagram`, rebase and merge) có xung đột với bản `docs/use-case.md` khác, xung đột đã bị giải quyết **trực tiếp trên `release/lab02`** (commit `616dcf0`, `cc99d68`) thay vì trên nhánh topic, và `topic/answers-lab02` lại được tạo từ `release/lab02` rồi merge vào `master` (PR #6) — tức là release đã bị đưa ngược vào master.
- Điều này vi phạm 2 quy tắc: "không commit trực tiếp lên `release/*`" và "`release/*` không bao giờ merge ngược vào master".
- Không sửa bằng cách viết lại lịch sử vì `release/lab02` và tag `v0.2.0` đã chia sẻ (tag đã chia sẻ thì không xóa, không di chuyển). Nội dung `use-case.md` trên master là đúng; từ Lab 03 trở đi mọi `release/labXX` đều được tạo từ `master` và nhánh answers đều tạo từ `master`.
