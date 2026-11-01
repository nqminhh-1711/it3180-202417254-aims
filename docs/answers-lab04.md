# Trả lời câu hỏi thảo luận - Lab 04

### 1. Vì sao release/* không bao giờ merge ngược vào master?
- **Nguyên tắc "master là chân lý" (Single Source of Truth):** Trong Release Flow, mọi tính năng mới và chuẩn bị phát hành đã được hoàn thiện trên `master` trước khi rẽ nhánh `release/*`. Nhánh `release/*` chỉ đóng vai trò đóng băng (*freeze*) baseline để phục vụ phát hành và làm dòng bảo trì (*maintenance stream*) cho phiên bản đó.
- **Tránh xung đột và ô nhiễm lịch sử:** Việc merge cả nhánh `release/*` ngược về `master` có thể gây xung đột không đáng có (ví dụ: xung đột số phiên bản, đè hoặc cuốn theo các thay đổi đặc thù của môi trường phát hành). Nếu có sửa lỗi khẩn cấp (*hotfix*) trên `release/*`, bản sửa lỗi đó sẽ được đưa về `master` thông qua `cherry-pick` (hoặc PR riêng) chứ không gộp toàn bộ nhánh release vào master.

### 2. So sánh Release Flow với GitFlow
- **Cấu trúc nhánh chính:**
  - *GitFlow:* Sử dụng 2 nhánh vĩnh viễn là `main/master` (chỉ chứa bản phát hành) và `develop` (nhánh tích hợp chính). Các nhánh `feature` rẽ từ `develop`, `release` rẽ từ `develop` rồi merge vào cả `main` và `develop`, `hotfix` rẽ từ `main` rồi merge vào cả `main` và `develop`.
  - *Release Flow:* Sử dụng duy nhất 1 nhánh chính là `master` (mô hình *Trunk-based*). Các nhánh `feature/*`, `bugfix/*` rẽ từ `master` và merge ngay về `master`. Nhánh `release/*` rẽ từ `master` khi phát hành và không merge ngược lại.
- **Độ phức tạp và nguy cơ xung đột:**
  - *GitFlow:* Cấu trúc phân nhánh phức tạp, nhánh sống dài (*long-lived branches*), dễ dẫn đến tình trạng "merge hell" khi phải đồng bộ giữa release, develop và master.
  - *Release Flow:* Tinh gọn, áp dụng nguyên tắc nhánh sống ngắn (*short-lived branches*), tích hợp liên tục (CI), rất phù hợp với quy trình phát triển và triển khai nhanh hiện đại (như thực tiễn của Microsoft Azure DevOps).

### 3. Vì sao lên 1.0.0 mà không phải 0.4.0?
- **Quy ước Semantic Versioning (SemVer):** Các phiên bản `0.y.z` đại diện cho giai đoạn phát triển ban đầu (*initial development*), phần mềm chưa hoàn thiện và API có thể thay đổi bất cứ lúc nào mà không đảm bảo tính tương thích ngược.
- **Cột mốc Release chính thức (Production-ready / GA):** Phiên bản `1.0.0` đánh dấu baseline ổn định đầu tiên của sản phẩm khi đã có đầy đủ các tính năng cơ bản hoàn chỉnh (quản lý giỏ hàng, in ấn, tìm kiếm, tính chiết khấu), có bộ kiểm thử tự động (*unit tests*) và tài liệu theo dõi thay đổi (*CHANGELOG*).
- **Cam kết chất lượng:** Chuyển sang `1.0.0` là lời tuyên bố về độ ổn định của phần mềm và bắt đầu áp dụng nghiêm ngặt các quy tắc SemVer cho các bản tiếp theo (tăng MAJOR khi phá vỡ tương thích, MINOR khi thêm tính năng mới, PATCH khi vá lỗi).
