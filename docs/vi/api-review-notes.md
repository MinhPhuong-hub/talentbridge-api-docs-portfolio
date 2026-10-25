# Rà soát API và làm rõ yêu cầu

Tài liệu này ghi lại những câu hỏi phát sinh khi chuyển yêu cầu sản phẩm thành tài liệu API dành cho nhà phát triển.

Mục tiêu là minh họa cách làm rõ hành vi API trước khi công bố thành thông tin chính thức. Các quyết định bên dưới thuộc **tình huống giả lập của portfolio**, không phải biên bản trao đổi với đội kỹ thuật có thật.

## 1. Nguồn gốc của `recruiterId`

**Điểm chưa rõ ban đầu**

Model `Job` chứa `recruiterId`, nhưng yêu cầu tạo tin tuyển dụng không nói rõ client có phải gửi trường này hay không.

**Câu hỏi cho engineering**

`recruiterId` do client cung cấp hay được lấy từ người dùng đã xác thực?

**Hành vi đã chốt trong tình huống giả lập**

Server lấy `recruiterId` từ nhà tuyển dụng đã xác thực.

**Ảnh hưởng đến tài liệu**

`recruiterId` xuất hiện trong response `Job`, nhưng không xuất hiện trong `CreateJobRequest`.

---

## 2. Trạng thái hồ sơ mới

**Câu hỏi:** Ứng viên có thể tự chỉ định trạng thái khi nộp hồ sơ không?

**Hành vi đã chốt:** Không. Hồ sơ mới luôn có trạng thái `pending`. Chỉ nhà tuyển dụng có quyền mới có thể thay đổi trạng thái sau đó.

---

## 3. Nộp hồ sơ trùng lặp

**Câu hỏi:** Điều gì xảy ra khi một ứng viên ứng tuyển hai lần vào cùng một việc làm?

**Hành vi đã chốt:** API trả về `409 Conflict`. Quy tắc này được ghi trong OpenAPI và tài liệu xử lý lỗi.

---

## 4. Quyền xem danh sách hồ sơ

**Câu hỏi:** Mọi nhà tuyển dụng đều có thể xem hồ sơ ứng tuyển của mọi tin tuyển dụng hay không?

**Hành vi đã chốt:** Không. Chỉ nhà tuyển dụng sở hữu tin tuyển dụng mới có quyền xem danh sách hồ sơ. Người dùng đã xác thực nhưng không có quyền sẽ nhận `403 Forbidden`.

---

## 5. Cursor phân trang

**Câu hỏi:** Client có thể giải mã cursor hoặc tự tạo cursor không?

**Hành vi đã chốt:** Không. Cursor là giá trị opaque; client phải dùng nguyên giá trị API trả về.

---

## 6. Chuyển trạng thái hồ sơ

**Câu hỏi:** Nhà tuyển dụng có thể gửi giá trị nào khi xử lý hồ sơ đang ở trạng thái `pending`?

**Hành vi đã chốt:** Endpoint cập nhật chấp nhận `accepted` hoặc `rejected`. Ứng viên không thể tự thay đổi trạng thái hồ sơ.

---

## Nguyên tắc viết tài liệu

Khi hành vi API chưa rõ, người viết tài liệu không nên tự đặt ra quy tắc. Cần xác định điểm mơ hồ, hỏi kỹ sư hoặc người phụ trách nghiệp vụ, ghi lại quyết định và cập nhật đồng bộ API contract cùng tài liệu.

[← Mục lục tiếng Việt](README.md) · [English](../en/api-review-notes.md)
