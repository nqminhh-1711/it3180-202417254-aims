### Mục đích
- Mô tả mục đích của Pull Request (tính năng mới, sửa lỗi, tái cấu trúc hoặc cập nhật tài liệu).

### Thay đổi
- Liệt kê các tệp đã thay đổi và tóm tắt nội dung chỉnh sửa:
  - `aims/`: Cập nhật logic xử lý (cart.py, dvd.py, search.py).
  - `main.py`: Cập nhật chương trình điều khiển và hiển thị kết quả.
  - Các tệp cấu hình hoặc tài liệu liên quan.

### Kiểm thử
- Chạy chương trình chính để kiểm tra luồng thực thi:
  `python main.py`
  (Kết quả đối chiếu: Total cost: 63.89 $)
- Chạy toàn bộ kiểm thử đơn vị tự động:
  `python -m unittest discover -s tests -v`

### Checklist
- [ ] Đã chạy thử mã nguồn cục bộ, không có lỗi runtime/cú pháp
- [ ] Tuân thủ quy ước đặt tên commit (Conventional Commits: feat, fix, refactor, docs, chore)
- [ ] Đã đồng bộ mã mới nhất từ master trước khi tạo PR
- [ ] Đã kiểm tra lại tab Files changed, không có tệp rác (__pycache__, tệp tạm)