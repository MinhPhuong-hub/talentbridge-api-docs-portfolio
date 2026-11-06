# Ví dụ chạy với Prism (tiếng Việt)

**[English](README.md) | Tiếng Việt**

Các script minh họa request đến **Prism mock server** chạy tại máy, được tạo từ `openapi.yaml`. Chúng **không kiểm chứng** backend production, xác thực thật, phân quyền thật, lưu trữ dữ liệu hoặc quy tắc nghiệp vụ. Phản hồi mô phỏng `403`/`404` không chứng minh chức năng phân quyền hay tìm kiếm tài nguyên đã được triển khai.

## Khởi động Prism

Từ thư mục gốc repository:

```powershell
npx.cmd @stoplight/prism-cli mock openapi.yaml
```

Giữ server chạy và mở terminal khác để thử request.

## Chạy các script Bash

Trong Git Bash hoặc WSL (không chạy trực tiếp `.sh` trong PowerShell):

```bash
bash examples/list-jobs.sh
bash examples/list-jobs-empty.sh
bash examples/create-job.sh
bash examples/simulate-forbidden.sh
bash examples/simulate-not-found.sh
```

## Ví dụ PowerShell

```powershell
curl.exe -H "Prefer: example=empty" http://127.0.0.1:4010/jobs
curl.exe -i -H "Prefer: code=404" http://127.0.0.1:4010/jobs/job_unknown
```

Header `Prefer` chỉ chọn ví dụ hoặc HTTP status mô phỏng; không kiểm chứng logic server thực tế.
