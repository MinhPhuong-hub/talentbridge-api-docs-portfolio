# Bắt đầu sử dụng API

Tài liệu này hướng dẫn cách gửi request đầu tiên đến TalentBridge API.

## Base URL

Ví dụ môi trường production:

`https://api.talentbridge.example/v1`

Trong project portfolio này, bạn có thể chạy mock server trên máy mà
không cần backend thật.

## Chạy mock API

Từ thư mục gốc của repository:

```bash
npx @stoplight/prism-cli mock openapi.yaml
```

Mock API sẽ chạy tại:

`http://127.0.0.1:4010`

## Lấy danh sách việc làm

```bash
curl \
  -H "Prefer: example=normal" \
  http://127.0.0.1:4010/jobs
```

Response mẫu:

```json
{
  "items": [
    {
      "id": "job_123",
      "title": "Backend Developer",
      "description": "Build and maintain recruitment platform APIs.",
      "location": "Ho Chi Minh City",
      "recruiterId": "user_901",
      "createdAt": "2026-10-20T10:00:00Z"
    }
  ],
  "nextCursor": "cursor_abc123"
}
```

## Phân trang

Dùng query parameter `limit` để giới hạn số lượng việc làm được trả về.

```bash
curl "http://127.0.0.1:4010/jobs?limit=10"
```

Nếu `nextCursor` có giá trị, hãy truyền nguyên giá trị đó vào request
tiếp theo:

```bash
curl \
  "http://127.0.0.1:4010/jobs?limit=10&cursor=cursor_abc123"
```

Cursor là một giá trị opaque. Client không nên tự phân tích hoặc chỉnh
sửa giá trị này.

## Request cần xác thực

Các endpoint được bảo vệ yêu cầu bearer access token:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```


---

**Điều hướng:** [Mục lục tiếng Việt](README.md) · [English version](../en/getting-started.md)
