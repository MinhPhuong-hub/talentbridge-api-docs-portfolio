# Xử lý lỗi

TalentBridge sử dụng cấu trúc JSON nhất quán cho các response lỗi.

Content type của response lỗi:

```http
Content-Type: application/problem+json
```

Ví dụ:

<!-- doc-test: response GET /jobs/{jobId} 404 -->
```json
{
  "type": "https://api.talentbridge.example/problems/not-found",
  "title": "Resource not found",
  "status": 404,
  "detail": "The requested resource could not be found.",
  "instance": "/jobs/job_unknown"
}
```

## Các trường trong response lỗi

| Trường | Mô tả |
|---|---|
| `type` | URI xác định loại lỗi. |
| `title` | Tóm tắt ngắn gọn, dễ hiểu về lỗi. |
| `status` | Mã trạng thái HTTP. |
| `detail` | Giải thích lỗi cụ thể trong lần request này. |
| `instance` | Xác định request hoặc tài nguyên liên quan đến lỗi. |

## Các mã trạng thái thường gặp

### 400 Bad Request

Request hợp lệ về mặt cú pháp HTTP nhưng chứa dữ liệu đầu vào không hợp lệ theo quy tắc API.

Ví dụ:

- Thiếu trường bắt buộc.
- Giá trị không thuộc danh sách `enum` cho phép.
- Chuỗi vượt quá độ dài quy định.

Kiểm tra trường `detail`, sửa request rồi gửi lại.

### 401 Unauthorized

Thiếu thông tin xác thực hoặc thông tin xác thực không hợp lệ. Hãy lấy access token hợp lệ trước khi thử lại.

### 403 Forbidden

Xác thực thành công nhưng người gọi không có quyền thực hiện thao tác. Chỉnh sửa request body thường không giải quyết được lỗi này; cần kiểm tra vai trò người dùng hoặc quyền đối với tài nguyên.

### 404 Not Found

Không tìm thấy tài nguyên được yêu cầu. Kiểm tra lại mã định danh tài nguyên trước khi gửi lại request.

### 409 Conflict

Request xung đột với trạng thái hiện tại của hệ thống. Ví dụ, API trả về `409` khi cùng một ứng viên gửi hồ sơ ứng tuyển lần thứ hai cho cùng một việc làm.

[← Mục lục tiếng Việt](README.md) · [English](../en/errors.md)


---

**Điều hướng:** [Mục lục tiếng Việt](README.md) · [English version](../en/errors.md)

## Xử lý lỗi ở phía client

Dùng HTTP status để phân loại cách xử lý và `type` để nhận diện loại sự cố trong hợp đồng được mô tả. Không dùng `detail` làm mã lỗi ổn định để lập trình. Với `409` khi nộp ứng tuyển, không tự động gửi lại request giống hệt. Case study chưa xác định retry interval, request ID hay hợp đồng idempotency key.

**Lưu ý Prism:** `Prefer: code=409` chỉ tạo response mô phỏng, không xác minh thuật toán phát hiện ứng tuyển trùng.
