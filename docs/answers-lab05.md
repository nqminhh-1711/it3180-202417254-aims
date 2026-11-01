# Trả lời câu hỏi thảo luận - Lab 05

### 1. So sánh cách xử lý hotfix giữa các mô hình

| Mô hình | Hotfix tạo từ | Đưa về | Phù hợp |
| :--- | :--- | :--- | :--- |
| **Release Flow (học phần)** | `release/*` | `release/*` + `master` | Nộp bài theo tuần, duy trì nhiều bản song song |
| **Release Flow (Microsoft)** | `master` (*upstream first*) | `cherry-pick` → `release/*` | Sản phẩm quy mô lớn, phát hành theo sprint |
| **GitFlow** | `main` | `main` + `develop` | Phát hành định kỳ, nhiều môi trường kiểm thử |
| **GitHub Flow** | `main` | `main` (deploy ngay) | Ứng dụng web, chỉ có một phiên bản duy nhất chạy thực tế |

---

### 2. Ưu, nhược điểm của upstream first so với release first

#### A. Upstream first (Sửa trên `master` trước rồi cherry-pick về `release/*`):
- **Ưu điểm:**
  - Loại bỏ hoàn toàn nguy cơ quên đưa bản vá về `master` (ngăn chặn lỗi tái diễn (*regression*) ở các bản phát hành trong tương lai).
  - Bản sửa lỗi được kiểm thử ngay trên nền mã nguồn mới nhất.
- **Nhược điểm:**
  - Nếu nhánh `master` đã có nhiều thay đổi kiến trúc hoặc tính năng mới chưa ổn định, việc cherry-pick bản vá ngược về nhánh release cũ (*backport*) có thể gặp nhiều xung đột và đòi hỏi chỉnh sửa lại mã nguồn.
  - Tốc độ vá lỗi trên bản release có thể bị chậm lại do quy trình kiểm duyệt trên `master`.

#### B. Release first (Sửa trên `release/*` trước rồi lan truyền về `master`):
- **Ưu điểm:**
  - Ưu tiên xử lý nhanh nhất sự cố cho khách hàng/người dùng đang chạy bản release cụ thể mà không bị chi phối bởi các thay đổi đang dở dang trên `master`.
- **Nhược điểm:**
  - Nếu thiếu kỷ luật hoặc công cụ tự động hóa kiểm toán, lập trình viên rất dễ quên lan truyền bản sửa về `master` hoặc các nhánh release song song khác.

---

### 3. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
Nếu quên đưa bản sửa sang `release/lab05`, các lệnh sau ở Phần F sẽ lập tức phát hiện:
1. **Lệnh đối chiếu commit tương đương `git cherry`:**
   ```bash
   git cherry -v origin/release/lab05 origin/release/lab04
   ```
   Lệnh sẽ hiển thị dấu `+` trước commit sửa lỗi `fix: make search_by_title case-insensitive`, báo hiệu rằng bản sửa trên `release/lab04` chưa có bản tương đương tương ứng trên `release/lab05`.
2. **Vòng lặp kiểm tra hành vi thực tế (Functional verification loop):**
   ```bash
   for ref in v1.0.1 v1.1.0 master; do
       git switch --detach -q $ref; printf "%-8s " $ref
       python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; print(len(search_by_title([D('The Lion King')], 'lion')))"
   done
   ```
   Kết quả kỳ vọng cho cả 3 phiên bản là `1`. Nếu quên lan truyền sang `release/lab05`, tại `v1.1.0` sẽ in ra `0` (hoặc rỗng) do tìm kiếm vẫn phân biệt hoa thường, làm lộ ngay lỗi chưa được vá.
