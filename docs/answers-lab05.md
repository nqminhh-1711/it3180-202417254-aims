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
   Kết quả kỳ vọng cho cả 3 phiên bản là `1`. Nếu quên lan truyền sang `release/lab05` (và mã có lỗi thật), tại `v1.1.0` sẽ in ra `0`, làm lộ ngay lỗi chưa được vá.
3. **Truy vết bằng commit message:** `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` chỉ ra 1 bản thay vì 2.

---

## Ghi chú tự kiểm toán (bổ sung sau khi nộp)

### a. Lỗi ở Phần B không tái hiện được trên mã của tôi
- `search_by_title` viết ở Lab 02 đã dùng `keyword.lower() in item.title.lower()`, tức là **đã không phân biệt hoa thường** ngay từ `v1.0.0` (`git show v1.0.0:aims/search.py`). Vì vậy bước tái hiện in ra `['The Lion King']` chứ không phải `[]`.
- Commit `4bff8bb` vì thế chỉ đổi tên biến `item` → `dvd` và **bổ sung regression test** `tests/test_search.py`; giá trị thực của hotfix là test này, bảo đảm hành vi không phân biệt hoa thường được kiểm thử trên cả 3 dòng phiên bản. Quy trình hotfix (nhánh từ `release/lab04`, tách commit sửa / commit nâng phiên bản, `cherry-pick -x`, tag `v1.0.1`, `v1.1.0`) vẫn thực hiện đầy đủ.
- Hệ quả: vòng lặp kiểm tra ở Phần F in `1` cho cả 3 phiên bản kể cả khi quên lan truyền, nên với repo này nó không phải bằng chứng; bằng chứng là `git log --grep` và `git tag --contains`.

### b. `git cherry` hiện dấu `+` cho commit fix
- `git cherry -v origin/master origin/release/lab04` in `+` cho cả `fix:` lẫn `chore: bump version`, khác với kỳ vọng `-` của slide.
- Nguyên nhân: `git cherry` so sánh *patch-id*; trên `master`/`release/lab05` tệp `aims/search.py` có thêm `search_by_category` và khác dòng cuối tệp (`\ No newline at end of file`), nên ngữ cảnh diff khác → patch-id khác dù nội dung sửa giống nhau.
- Việc lan truyền được xác nhận bằng:
  ```bash
  git log --all --oneline --grep "cherry picked from commit 4bff8bb"   # e118118 (master), ca32759 (release/lab05)
  git tag --contains 4bff8bb                                         # v1.0.1
  ```
