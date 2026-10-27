# Tài liệu API tuyển dụng TalentBridge

**Ngôn ngữ:** [English](README.md) | **Tiếng Việt**

> Portfolio mô phỏng thể hiện năng lực viết tài liệu API, OpenAPI, trải nghiệm nhà phát triển, docs-as-code, biên soạn tài liệu song ngữ và quản lý thay đổi API.

**TalentBridge là nền tảng tuyển dụng giả lập được xây dựng cho mục đích portfolio; đây không phải sản phẩm thương mại đang vận hành.**

## Điểm nổi bật của portfolio

Portfolio tài liệu API minh họa OpenAPI, docs-as-code, ví dụ chạy được, biên soạn kỹ thuật song ngữ và quản lý thay đổi API.

| Tài liệu | Năng lực minh họa |
|---|---|
| [`openapi.yaml`](openapi.yaml) | Đặc tả API theo hợp đồng |
| [Ghi chú rà soát API](docs/vi/api-review-notes.md) | Nhận diện điểm mơ hồ và giả định trong portfolio |
| [Jobs API](docs/vi/jobs-api.md) | Tài liệu tham chiếu cho developer |
| [Xử lý lỗi](docs/vi/errors.md) | HTTP status và hướng xử lý |
| [Release notes](docs/vi/release-notes/v1.1.0.md) | Truyền đạt thay đổi |
| [Migration guide](docs/vi/migration-v1-to-v2.md) | Kịch bản breaking change giả lập |
| [Quy chuẩn viết](docs/vi/style-guide.md) | Nhất quán biên tập |
| [Ví dụ chạy được](examples/README.md) | Minh họa contract/mock tại máy |
| [Tiếng Việt](docs/vi/README.md) / [English](docs/en/README.md) | Tài liệu song ngữ |

## Giới thiệu

Repository minh họa quy trình tiếp nhận API contract, làm rõ yêu cầu, viết tài liệu cho nhà phát triển tích hợp, kiểm tra ví dụ và quản lý phiên bản tài liệu.

Các nội dung chính:

- Đặc tả API bằng OpenAPI 3.0.3
- Tài liệu tham chiếu API và hướng dẫn tích hợp
- Ví dụ `curl` có thể chạy với mock server
- Xác thực và phân quyền
- Xử lý lỗi nhất quán
- Ghi chú rà soát API và làm rõ yêu cầu
- Quản lý phiên bản, hướng dẫn migration và release notes
- Tài liệu kỹ thuật tiếng Anh và tiếng Việt
- Quy trình docs-as-code sử dụng Git và Pull Request

## Phạm vi API

TalentBridge phục vụ hai nhóm người dùng:

- **Ứng viên (candidate):** tìm việc và gửi hồ sơ ứng tuyển.
- **Nhà tuyển dụng (recruiter):** tạo tin tuyển dụng và xem xét hồ sơ ứng tuyển.

Hai tài nguyên chính là `Job` và `Application`.

## Tổng quan endpoint

| Phương thức | Endpoint | Chức năng |
|---|---|---|
| `GET` | `/jobs` | Lấy danh sách việc làm |
| `POST` | `/jobs` | Tạo tin tuyển dụng |
| `GET` | `/jobs/{jobId}` | Lấy thông tin một việc làm |
| `POST` | `/jobs/{jobId}/applications` | Nộp hồ sơ ứng tuyển |
| `GET` | `/jobs/{jobId}/applications` | Lấy danh sách hồ sơ của một việc làm |
| `PATCH` | `/applications/{applicationId}` | Cập nhật trạng thái hồ sơ |

## Chạy mock API trên máy

Bạn có thể thử API mà không cần xây dựng backend. Từ thư mục gốc repository, chạy:

```bash
npx @stoplight/prism-cli mock openapi.yaml
```

Mock server chạy tại `http://127.0.0.1:4010`.

Ví dụ lấy danh sách việc làm:

```bash
curl -H "Prefer: example=normal" http://127.0.0.1:4010/jobs
```

*Lưu ý:* Prism mô phỏng phản hồi dựa trên OpenAPI; không thay thế backend thật và không chứng minh việc kiểm tra phân quyền thực tế.

**Giới hạn mock server:** Prism sinh phản hồi dựa trên `openapi.yaml`; đây không phải backend production và không xác minh xác thực thực tế, phân quyền, lưu trữ dữ liệu, thực thi quy tắc nghiệp vụ hay tích hợp dịch vụ.

## Tài liệu tiếng Việt

- [Mục lục tài liệu tiếng Việt](docs/vi/README.md)
- [Bắt đầu sử dụng](docs/vi/getting-started.md)
- [Xác thực và phân quyền](docs/vi/authentication.md)
- [Jobs API](docs/vi/jobs-api.md)
- [Xử lý lỗi](docs/vi/errors.md)
- [Ghi chú rà soát API](docs/vi/api-review-notes.md)
- [Hướng dẫn chuyển từ v1 sang v2](docs/vi/migration-v1-to-v2.md)
- [Release notes v1.1.0](docs/vi/release-notes/v1.1.0.md)
- [Quy chuẩn biên soạn tài liệu](docs/vi/style-guide.md)

Tài liệu tiếng Anh: [English documentation](docs/en/getting-started.md).

## Quản lý thay đổi

Các thay đổi API được theo dõi qua [CHANGELOG.md](CHANGELOG.md), release notes, hướng dẫn migration và quy trình review bằng Pull Request. Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết quy trình đóng góp.

## Kỹ năng được minh họa

**Viết tài liệu API:** Chuyển đặc tả OpenAPI thành tài liệu dễ sử dụng cho nhà phát triển.

**Làm rõ yêu cầu:** Nhận diện điểm mơ hồ và đặt câu hỏi với kỹ sư hoặc BA trước khi công bố hành vi API.

**Developer experience:** Viết ví dụ request/response, hướng dẫn xác thực, xử lý lỗi và tích hợp.

**Docs-as-code:** Duy trì tài liệu qua Git, branch và Pull Request.

**Quản lý thay đổi:** Phân biệt thay đổi tương thích và breaking change, viết release notes và migration guide.

**Biên soạn song ngữ:** Duy trì hai phiên bản Anh–Việt nhất quán về định danh và hành vi kỹ thuật.
