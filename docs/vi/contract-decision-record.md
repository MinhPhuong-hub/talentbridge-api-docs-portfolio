# Sổ quyết định và câu hỏi về API contract

> **Dự án giả lập.** Đây là các câu hỏi mà Technical Writer phải đưa cho Developer hoặc Business Specialist; không phải biên bản họp thực tế hoặc xác nhận từ backend.

| Chủ đề | Hành vi được mô tả trong case study | Điều cần xác minh khi triển khai thật |
|---|---|---|
| `recruiterId` | Lấy từ người dùng xác thực | Quy tắc ánh xạ người dùng, tổ chức/tenant |
| `candidateId` | Lấy từ người dùng xác thực | Ai có thể ứng tuyển thay người khác? |
| Hồ sơ trùng (TB-005) | **Đã chấp thuận trong hợp đồng giả lập v1.1:** cùng ứng viên nộp lại vào cùng job nhận `409 Conflict`; không phải bằng chứng backend thật | **Chưa quyết định:** hồ sơ đã rút, race condition, idempotency/retry và cách thực thi uniqueness |
| Quyền xem hồ sơ | Recruiter sở hữu job | Truy cập trong tổ chức, `403`/`404` |
| Cursor | Giá trị mờ đục (`opaque`) | Hết hạn, ràng buộc bộ lọc, thứ tự |
| PATCH status | Chỉ nhận `accepted`, `rejected` | Ma trận chuyển trạng thái, cập nhật lặp |
| PATCH authorization | “Authorized recruiter” | Quyền theo sở hữu, tenant và vai trò |
| Lỗi API | `application/problem+json` | Mã lỗi ổn định, correlation ID |

**Nguyên tắc:** Không ghi một giả định là “đã xác nhận”. Nếu Developer chưa trả lời, đặt trạng thái `Open` và tránh khẳng định hành vi ngoài những gì spec mô tả.

[English decision record](../en/contract-decision-record.md) · [Mục lục](README.md)
