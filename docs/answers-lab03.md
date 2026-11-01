# Trả lời câu hỏi thảo luận - Lab 03

### 1. Merge base là gì?
- **Định nghĩa:** Merge base là commit tổ tiên chung gần nhất (*best common ancestor*) giữa hai nhánh (hoặc hai commit) được chỉ định trong Git.
- **Vai trò:** Khi thực hiện hợp nhất 3 phía (*3-way merge*), Git sử dụng merge base làm điểm quy chiếu gốc. Git so sánh sự khác biệt từ merge base đến nhánh hiện tại (HEAD) và từ merge base đến nhánh cần gộp để xác định những thay đổi cần tích hợp hoặc phát hiện xung đột (*conflict*).
- **Lệnh kiểm tra:** `git merge-base <branchA> <branchB>`.

### 2. Vì sao master/release/* phải dùng revert thay vì reset?
- **Bảo toàn lịch sử chung (Không viết lại lịch sử):** Nhánh `master` và các nhánh `release/*` là nhánh dùng chung công khai, làm baseline cho mọi thành viên trong dự án. Lệnh `git reset` dời con trỏ nhánh và viết lại lịch sử commit, đòi hỏi phải dùng `git push --force` (thường bị cấm bởi *branch protection*). Việc ép viết lại lịch sử trên nhánh chung sẽ phá vỡ cây lịch sử của những người khác và gây lỗi nghiêm trọng khi cộng tác.
- **Tạo commit đảo ngược an toàn (*Forward-only history*):** `git revert` không xóa commit cũ mà tạo ra một commit mới có nội dung đảo ngược hoàn toàn thay đổi của commit/merge commit trước đó. Nhờ vậy, lịch sử vẫn tiến về phía trước, giữ nguyên tính toàn vẹn và cung cấp dấu vết kiểm toán (*audit trail*) rõ ràng trong quy trình SCM.
