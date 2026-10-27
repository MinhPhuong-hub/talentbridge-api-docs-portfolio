# Chuyển đổi từ API v1 sang v2

Tài liệu này minh họa cách thông báo các **breaking change** cho nhà phát triển đang tích hợp API.

> Đây là kịch bản migration giả lập. File `openapi.yaml` trong repository hiện mô tả API v1.1.0, không phải một API v2 đã triển khai.

## Bảng tóm tắt breaking change

| Thay đổi | v1 | v2 giả định | Hành động của client |
|---|---|---|---|
| Trường chủ sở hữu tin tuyển dụng | `recruiterId` | `ownerId` | Cập nhật tham chiếu trường và kiểu dữ liệu |
| Trạng thái ứng tuyển | `pending`, `accepted`, `rejected` | `pending`, `approved`, `declined` | Cập nhật điều kiện, ánh xạ và kiểm thử |

## Tổng quan

Phiên bản v2 đưa ra hai thay đổi không tương thích ngược:

1. Đổi tên trường `recruiterId` thành `ownerId`.
2. Đổi tên các giá trị trạng thái của hồ sơ ứng tuyển.

Client sử dụng các trường này phải cập nhật trước khi chuyển sang v2.

## Đổi `recruiterId` thành `ownerId`

### v1

```json
{
  "id": "job_123",
  "recruiterId": "user_901"
}
```

### v2

```json
{
  "id": "job_123",
  "ownerId": "user_901"
}
```

### Thay đổi cần thực hiện ở client

Thay đoạn code:

```javascript
job.recruiterId
```

bằng:

```javascript
job.ownerId
```

Đây là breaking change vì client phụ thuộc vào `recruiterId` sẽ không còn nhận được trường đó trong response v2.

---

## Thay đổi giá trị trạng thái hồ sơ

Phiên bản v1 sử dụng:

```text
pending
accepted
rejected
```

Phiên bản v2 sử dụng:

```text
pending
approved
declined
```

Cần cập nhật các phép so sánh, ánh xạ hiển thị, ánh xạ cơ sở dữ liệu và logic validation phụ thuộc vào giá trị cũ.

Ví dụ:

```javascript
if (application.status === "accepted") {
  // v1
}
```

được đổi thành:

```javascript
if (application.status === "approved") {
  // v2
}
```

## Checklist migration

Trước khi chuyển traffic production sang v2:

- [ ] Cập nhật kiểu dữ liệu API được sinh tự động hoặc tự viết.
- [ ] Cập nhật các vị trí tham chiếu tên trường.
- [ ] Cập nhật ánh xạ trạng thái.
- [ ] Cập nhật automated tests.
- [ ] Kiểm tra response v2 trong môi trường staging.
- [ ] Triển khai các thay đổi ở client.
- [ ] Chuyển tích hợp sang base URL của v2.

[← Mục lục tiếng Việt](README.md) · [English](../en/migration-v1-to-v2.md)


---

**Điều hướng:** [Mục lục tiếng Việt](README.md) · [English version](../en/migration-v1-to-v2.md)
