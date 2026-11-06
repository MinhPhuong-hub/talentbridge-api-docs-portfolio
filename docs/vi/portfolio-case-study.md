# Case study: tài liệu API tuyển dụng giả lập

**Vai trò mô phỏng:** Technical Writer / API Documentation.

**Phạm vi:** Đặc tả OpenAPI 3.0.3; tài liệu tích hợp; ví dụ request/response; release notes; quản lý thuật ngữ; rà soát điểm chưa rõ trong API contract.

**Công bố giới hạn:** TalentBridge là dự án giả lập. Không có backend production, hệ thống xác thực thật, người dùng thật hoặc dữ liệu đo lường thật. Prism mô phỏng phản hồi dựa trên đặc tả, không thực hiện logic nghiệp vụ.

## Vấn đề cần giải quyết

Chỉ liệt kê endpoint chưa đủ để tích hợp. Người đọc cần hiểu quyền truy cập, phạm vi sở hữu dữ liệu, các chuyển trạng thái hợp lệ, cách phân biệt lỗi và điều kiện thử lại request.

## Cách tiếp cận

1. Tổ chức tài liệu theo nhiệm vụ người đọc.
2. Đối chiếu trường dữ liệu, mã trạng thái và ví dụ với OpenAPI.
3. Ghi lại câu hỏi chưa được xác nhận; không trình bày giả định như hành vi đã triển khai.
4. Phân biệt URL minh họa, mock server và production.
5. Kiểm tra Markdown, đường dẫn tài liệu và các thay đổi trước khi publish.

## Ví dụ tư duy chất vấn

Câu “Recruiter được thay đổi trạng thái hồ sơ” chưa xác định recruiter nào, hồ sơ của job nào, chuyển từ trạng thái nào sang trạng thái nào, và gọi lặp có cho cùng kết quả hay không. Đây là những quyết định phải làm rõ trước khi viết tài liệu mang tính quy phạm.

## Những gì portfolio chứng minh

- Có khả năng cấu trúc tài liệu và đặc tả API giả lập.
- Nhận diện điểm mơ hồ và ghi lại câu hỏi kỹ thuật/nghiệp vụ cần giải quyết.
- Phân biệt giới hạn của mock với hành vi backend thật.

**Không phải bằng chứng** đã phỏng vấn developer thực, bảo đảm bảo mật thực tế, quản lý hệ thống production hoặc giảm số ticket hỗ trợ khách hàng.
