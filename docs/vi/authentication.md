# Xác thực và phân quyền

TalentBridge sử dụng bearer access token cho các thao tác API được bảo vệ.

Gửi token trong header `Authorization`:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Ví dụ:

```bash
curl -X POST \
  http://127.0.0.1:4010/jobs \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Backend Developer",
    "description": "Build and maintain recruitment platform APIs.",
    "location": "Ho Chi Minh City"
  }'
```

## Lỗi xác thực và phân quyền

### 401 Unauthorized

Response `401` cho biết request chưa được xác thực thành công. Nguyên nhân thường gặp:

- Không gửi access token.
- Token không hợp lệ.
- Token đã hết hạn.

### 403 Forbidden

Response `403` cho biết người gọi đã được xác thực nhưng không có quyền thực hiện thao tác.

Ví dụ: ứng viên không thể tạo tin tuyển dụng vì thao tác này yêu cầu vai trò `recruiter`.

**Authentication** trả lời câu hỏi: *Bạn là ai?*

**Authorization** trả lời câu hỏi: *Bạn có được phép thực hiện thao tác này không?*

> **Lưu ý về mock:** Token minh họa và Prism mock server không chứng minh việc xác thực hay phân quyền thật. Quy tắc phân quyền ở đây là hành vi được mô tả trong API contract giả lập.

[← Mục lục tiếng Việt](README.md) · [English](../en/authentication.md)


---

**Điều hướng:** [Mục lục tiếng Việt](README.md) · [English version](../en/authentication.md)
