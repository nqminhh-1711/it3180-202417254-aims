# Nhật ký thay đổi (CHANGELOG)

Tất cả các thay đổi đáng chú ý của dự án sẽ được ghi nhận tại tệp này.

Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
và dự án này tuân thủ chuẩn [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-02
### Added
- Thêm phương thức `Cart.sort_by_title()` và `Cart.sort_by_cost()` để sắp xếp các đĩa trong giỏ hàng.
- Thêm hàm `search_by_category()` trong `aims.search` để tìm kiếm DVD theo thể loại.

## [1.0.1] - 2026-11-02
### Fixed
- Sửa lỗi tìm kiếm phân biệt hoa thường trong `search_by_title` (Fixes #20).

## [1.0.0] - 2026-11-01
### Added
- Thêm phương thức `Cart.print_cart()` hiển thị danh sách các đĩa đã đặt và tổng chi phí.
- Thêm hàm `search_by_title()` trong `aims.search` phục vụ tìm kiếm đĩa DVD theo từ khóa.
- Thêm phương thức `Cart.total_cost_with_discount()` tính tổng tiền giỏ hàng khi áp dụng phần trăm giảm giá.
- Tích hợp kiểm thử tự động với `unittest discover`.
- Bổ sung mẫu Pull Request (`pull_request_template.md`) và các tài liệu hướng dẫn.

### Fixed
- Từ chối thêm đĩa vào giỏ hàng khi vượt quá giới hạn `MAX_NUMBERS_ORDERED` (20 đĩa) (#7).
- Kiểm tra tính hợp lệ của phần trăm giảm giá trong khoảng từ 0 đến 100 trong `total_cost_with_discount`.
