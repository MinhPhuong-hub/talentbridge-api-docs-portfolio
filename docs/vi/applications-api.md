# Applications API — Hồ sơ ứng tuyển

Tài liệu này mô tả **hợp đồng API giả lập** của TalentBridge. Lệnh ví dụ sử dụng [Prism mock cục bộ](getting-started.md), không phải backend thật. Prism không chứng minh việc kiểm tra token, phân quyền, chống nộp trùng hoặc chuyển trạng thái.

## Nộp hồ sơ

`POST /jobs/{jobId}/applications` · Bearer token · Vai trò ứng viên (quy tắc giả định)

| Đầu vào | Vị trí | Bắt buộc | Ràng buộc |
|---|---|---|---|
| `jobId` | Path | Có | Mã công việc |
| `coverLetter` | JSON body | Không | Chuỗi tối đa 1.000 ký tự |

Không gửi `candidateId` hoặc `status`. Theo **quy tắc giả định** của case study, server lấy candidate từ token và khởi tạo `status` là `pending`.

```bash
curl -i -X POST 'http://127.0.0.1:4010/jobs/job_123/applications' \
  -H 'Authorization: Bearer demo-token' \
  -H 'Content-Type: application/json' \
  -d '{"coverLetter":"I have experience documenting HTTP APIs."}'
```

**201 Created** — Response ví dụ:

<!-- doc-test: response POST /jobs/{jobId}/applications 201 -->
```json
{"id":"app_456","jobId":"job_123","candidateId":"user_321","status":"pending","coverLetter":"I have experience documenting HTTP APIs.","createdAt":"2026-10-24T13:00:00Z"}
```

**Lỗi:** `400` body không hợp lệ; `401` token thiếu/không hợp lệ; `403` không có quyền; `404` không tìm thấy job; `409` nộp trùng cho cùng cặp ứng viên–job (quy tắc giả định). Khi nhận `409`, không tự động gửi lại cùng request. Xem [Xử lý lỗi](errors.md).

## Xem danh sách hồ sơ của một công việc

`GET /jobs/{jobId}/applications` · Bearer token · Recruiter sở hữu job (quy tắc giả định)

```bash
curl -i 'http://127.0.0.1:4010/jobs/job_123/applications' \
  -H 'Authorization: Bearer demo-token'
```

**200 OK** trả về `items` là mảng các `Application`. Nếu job tồn tại nhưng chưa có hồ sơ, kết quả là `{"items":[]}`, **không phải** `404`. Các lỗi: `401`, `403`, `404` (job không tồn tại).

## Cập nhật trạng thái hồ sơ

`PATCH /applications/{applicationId}` · Bearer token · Recruiter được phân quyền

```bash
curl -i -X PATCH 'http://127.0.0.1:4010/applications/app_456' \
  -H 'Authorization: Bearer demo-token' \
  -H 'Content-Type: application/json' \
  -d '{"status":"accepted"}'
```

Body bắt buộc có `status`, nhận `accepted` hoặc `rejected`. **200 OK** trả về `Application`. Các lỗi đã mô tả: `400`, `401`, `403`, `404`.

**Khoảng trống hợp đồng:** Schema chỉ giới hạn **trạng thái đích**, chưa xác định trạng thái nguồn hợp lệ, cập nhật lặp lại, recruiter nào có quyền, hay xử lý cập nhật đồng thời. Không tự suy diễn các quy tắc này từ enum. Xem [sổ quyết định API](contract-decision-record.md). Prism không kiểm chứng được hành vi nghiệp vụ.

## Các trường trong response

`Application` chứa `id`, `jobId`, `candidateId`, `status`, `createdAt` và `coverLetter` tùy chọn. Trạng thái trả về: `pending`, `accepted`, `rejected`; request PATCH chỉ nhận `accepted`, `rejected`.

---

[Mục lục](README.md) · [English](../en/applications-api.md)
