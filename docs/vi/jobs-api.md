# Jobs API

Jobs API cho phép client tìm kiếm cơ hội việc làm và cho phép nhà tuyển dụng tạo tin tuyển dụng mới.

## Lấy danh sách việc làm

`GET /jobs`

Trả về danh sách việc làm hiện có.

### Query parameters

| Tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|---|---|
| `location` | string | Không | Lọc việc làm theo địa điểm. |
| `limit` | integer | Không | Số kết quả tối đa; từ 1 đến 100; mặc định là 20. |
| `cursor` | string | Không | Cursor không thể tự giải mã, dùng để lấy trang tiếp theo. |
| `sort` | string | Không | Thứ tự sắp xếp; mặc định `createdAt:desc`. |

Các giá trị `sort` được hỗ trợ:

```text
createdAt:desc
createdAt:asc
title:asc
title:desc
```

### Request mẫu

```bash
curl \
  "https://api.talentbridge.example/v1/jobs?location=Remote&limit=20"
```

### Response `200`

```json
{
  "items": [
    {
      "id": "job_124",
      "title": "Technical Writer",
      "description": "Create developer documentation and API guides.",
      "location": "Remote",
      "recruiterId": "user_902",
      "createdAt": "2026-10-21T08:30:00Z"
    }
  ],
  "nextCursor": null
}
```

---

## Tạo tin tuyển dụng

`POST /jobs`

Tạo một tin tuyển dụng mới. Người gọi phải được xác thực với vai trò `recruiter`.

API lấy `recruiterId` từ danh tính người dùng đã xác thực. Client **không** gửi trường này trong request body.

### Request body

| Trường | Kiểu dữ liệu | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `title` | string | Có | Từ 3 đến 100 ký tự |
| `description` | string | Có | Từ 20 đến 5.000 ký tự |
| `location` | string | Có | Từ 2 đến 100 ký tự |

### Request mẫu

```bash
curl -X POST \
  https://api.talentbridge.example/v1/jobs \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Backend Developer",
    "description": "Build and maintain recruitment platform APIs.",
    "location": "Ho Chi Minh City"
  }'
```

### Response `201`

```json
{
  "id": "job_123",
  "title": "Backend Developer",
  "description": "Build and maintain recruitment platform APIs.",
  "location": "Ho Chi Minh City",
  "recruiterId": "user_901",
  "createdAt": "2026-10-24T12:00:00Z"
}
```

### Các lỗi có thể gặp

| Mã HTTP | Ý nghĩa |
|---|---|
| `400` | Request body không hợp lệ. |
| `401` | Thiếu thông tin xác thực hoặc thông tin xác thực không hợp lệ. |
| `403` | Người dùng đã xác thực không có quyền tạo tin tuyển dụng. |

Xem [Xử lý lỗi](errors.md) để biết cấu trúc response lỗi dùng chung.

> Tên miền `api.talentbridge.example` chỉ là ví dụ; để chạy thử hãy dùng mock server tại `http://127.0.0.1:4010`.

[← Mục lục tiếng Việt](README.md) · [English](../en/jobs-api.md)


---

**Điều hướng:** [Mục lục tiếng Việt](README.md) · [English version](../en/jobs-api.md)
