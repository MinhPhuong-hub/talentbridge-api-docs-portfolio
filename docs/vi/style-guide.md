# Quy chuẩn viết tài liệu TalentBridge bằng tiếng Việt

## Độc giả mục tiêu

Nhà phát triển đang tích hợp ứng dụng với TalentBridge API.

## Văn phong

Viết trực tiếp, ngắn gọn, hướng tới thao tác người đọc cần thực hiện.

**Nên viết:**

> Gửi nguyên giá trị cursor nhận được từ request trước.

**Tránh viết:**

> Người dùng có thể cân nhắc việc sử dụng giá trị cursor đã được hệ thống trả về trước đó.

## Thuật ngữ

Dùng nhất quán các thuật ngữ sau:

| Thuật ngữ kỹ thuật | Cách diễn đạt tiếng Việt |
|---|---|
| job | việc làm / tin tuyển dụng (tùy ngữ cảnh) |
| candidate | ứng viên |
| recruiter | nhà tuyển dụng |
| application | hồ sơ ứng tuyển |
| access token | access token |
| request body | request body / phần thân request |
| endpoint | endpoint |
| response | response / phản hồi |
| cursor | cursor (giá trị phân trang) |

Không thay đổi tên property, path, header, mã HTTP hoặc giá trị `enum` trong code và ví dụ.

## Quy tắc HTTP

Viết phương thức HTTP bằng chữ in hoa: `GET`, `POST`, `PATCH`, `DELETE`.

Khi nhắc đến một mã lỗi lần đầu, ghi đủ mã và tên: `404 Not Found`. Các lần sau có thể dùng `404`.

## Tên tham số và thuộc tính

Tên phải khớp chính xác với API contract: dùng `candidateId`, không đổi thành `candidate_id`.

## Ví dụ kỹ thuật

Ví dụ phải:

- Phù hợp với schema OpenAPI hiện hành.
- Sử dụng dữ liệu giả lập, không chứa thông tin bí mật production.
- Dùng `YOUR_ACCESS_TOKEN` thay cho thông tin xác thực thật.
- Có thể chạy được nếu được giới thiệu là ví dụ có thể thực thi.

## Viết tài liệu lỗi

Không chỉ ghi mã HTTP; phải giải thích nguyên nhân, cách xác định vấn đề và hành động khắc phục.

## Quy tắc biên dịch Anh–Việt

- Giữ nguyên `nextCursor`, `candidateId`, `/jobs`, `Authorization` và các định danh kỹ thuật khác.
- Giữ nguyên nội dung JSON và shell command khi chúng được dùng làm ví dụ kiểm thử chung.
- Dịch phần giải thích theo ngữ cảnh của nhà phát triển; không dịch máy móc từng từ.
- Mỗi khi API contract thay đổi, kiểm tra cả tài liệu tiếng Anh lẫn tiếng Việt.

[← Mục lục tiếng Việt](README.md) · [English style guide](../style-guide.md)


## Quy tắc dùng từ `Job`

- Dùng **“việc làm”** khi nói về cơ hội việc làm từ góc nhìn ứng viên.
- Dùng **“tin tuyển dụng”** khi nói về tin đăng do nhà tuyển dụng tạo hoặc quản lý.
- Giữ nguyên **`Job`** khi nói về resource hoặc schema của API.
- Không dịch định danh kỹ thuật như `jobId`, `recruiterId`, `nextCursor` và các giá trị enum.
