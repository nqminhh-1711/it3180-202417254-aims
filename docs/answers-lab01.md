# Trả lời câu hỏi thảo luận - Lab 01

### 1. Vì sao dùng `git mv` thay vì xóa rồi tạo tệp mới?
- `git mv` đổi tên/di chuyển tệp và đưa ngay thay đổi vào staging, Git ghi nhận đây là **rename** chứ không phải "xóa + thêm".
- Nhờ đó lịch sử của tệp được giữ liên tục: `git log --follow -- aims/cart.py` vẫn xem được các commit trước khi tệp nằm ở thư mục gốc, `git blame` vẫn chỉ đúng tác giả từng dòng.
- Trên Pull Request, tab *Files changed* hiển thị *renamed*, reviewer dễ thấy đây là refactor thuần túy, không đổi nội dung.
- (Về kỹ thuật Git phát hiện rename dựa trên độ giống nội dung, nên nếu vừa di chuyển vừa sửa nhiều thì có thể mất dấu; vì vậy di chuyển và sửa import được tách thành 2 commit riêng.)

### 2. `release/lab01` có phải là baseline không?
- **Có.** Baseline là một phiên bản cấu hình đã được thống nhất, được định danh rõ ràng và chỉ được thay đổi qua quy trình kiểm soát.
- `release/lab01` được tạo từ `master` sau khi PR #1 đã được review và merge, đánh dấu đúng trạng thái bài nộp Lab 01 (cùng mã băm với `origin/master` lúc tạo).
- Tuy nhiên nhánh vẫn có thể di chuyển (khi hotfix), nên ở Lab 04 baseline này được cố định thêm bằng annotated tag `v0.1.0` - tag không bao giờ di chuyển.

### 3. Vì sao không commit thẳng lên `master` dù làm một mình?
- Tuân thủ quy trình kiểm soát thay đổi: mọi thay đổi đều đi qua nhánh riêng + Pull Request, tạo dấu vết (mục đích, thay đổi, cách kiểm thử) để truy vết sau này.
- `master` luôn ở trạng thái ổn định, chạy được; thay đổi dở dang nằm ở nhánh riêng, có thể bỏ đi mà không ảnh hưởng `master`.
- Tạo thói quen đúng trước khi làm nhóm và trước khi bật branch protection / CI (Lab 02, Lab 05): PR là điểm để review và chạy test tự động.
- Dễ hoàn tác: cả thay đổi gói trong một merge commit, có thể `git revert -m 1` khi cần.
