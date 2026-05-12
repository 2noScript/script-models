# Script Models

Registry chứa các bộ prompt/model cho **Script Pro**.

**👉 Tải models về:** Dùng đường dẫn `plugin.json` bên dưới trong tool/extension của bạn:

```
https://raw.githubusercontent.com/2noScript/script-models/main/plugin.json
```

## Cấu trúc thư mục

```
script-models/
├── plugin.json              # 🔸 File chủ đạo — load vào tool để nhận danh sách models
├── core/
│   └── wildlife/            # Model: Wildlife & Science Creators
│       ├── icon.png         # Icon 128×128 PNG (tự động tạo)
│       ├── SCRIPT WRITER.md
│       ├── THUMBNAIL GENERATOR.md
│       ├── VIDEO IDEA GENERATOR.md
│       └── VISUAL & IMAGE PROMPT MAKER.md
└── helper/                  # Công cụ hỗ trợ (Python)
    ├── convert.py           # Xử lý icon tự động
    ├── pyproject.toml
    ├── uv.lock
    └── README.md
```

## plugin.json — Registry Format

File này định nghĩa metadata của nhà cung cấp và danh sách các model hiện có.

```json
{
  "metadata": {
    "providerName": "2noScript",
    "providerLink": "https://github.com/2noScript",
    "providerAvatar": "https://github.com/2noScript.png",
    "description": "Gen Script Pro",
    "version": "1",
    "remotePath": "https://raw.githubusercontent.com/2noScript/script-models/main/core",
    "localPath": ""
  },
  "models": [
    {
      "name": "Wildlife & Science Creators",
      "author": "2noScript",
      "path": "wildlife",
      "version": "1",
      "description": "Ready-to-Use Prompts for Wildlife & Science Creators",
      "tags": ["Youtube"],
      "script": {
        "idea": "VIDEO IDEA GENERATOR.md",
        "script": "SCRIPT WRITER.md",
        "thumbnail": "THUMBNAIL GENERATOR.md",
        "visuals": "VISUAL & IMAGE PROMPT MAKER.md"
      }
    }
  ]
}
```

### Giải thích các trường:
- **metadata**: Thông tin chung về registry.
  - `remotePath`: Đường dẫn gốc để tải các file script.
- **models**: Danh sách các bộ prompt.
  - `path`: Tên thư mục con trong `core/`.
  - `script`: Ánh xạ các file Markdown tương ứng với từng bước trong workflow.

## Cấu trúc Script Files (`.md`)

Mỗi file Markdown chứa prompt hệ thống (system prompt) cho một bước cụ thể:

- **VIDEO IDEA GENERATOR.md** — Tạo ý tưởng video.
- **SCRIPT WRITER.md** — Viết kịch bản chi tiết.
- **THUMBNAIL GENERATOR.md** — Tạo mô tả/ý tưởng thumbnail.
- **VISUAL & IMAGE PROMPT MAKER.md** — Tạo prompt cho AI tạo hình ảnh.

## helper/ — Công cụ Icon

Dùng để tự động chuẩn hoá icon cho tất cả models bằng Python.

### Cách sử dụng

1. Đảm bảo đã cài đặt `uv` hoặc `pip`.
2. Chạy lệnh:
```bash
cd helper
uv run python convert.py
```

Công cụ sẽ tự động tìm ảnh đầu tiên trong mỗi thư mục model, resize về **128x128**, chuyển sang định dạng **PNG** và đổi tên thành `icon.png`.

## Thêm Model mới

1. **Tạo thư mục**: `mkdir core/<model-name>`
2. **Thêm script**: Tạo các file `.md` với nội dung prompt.
3. **Thêm ảnh**: Bỏ 1 file ảnh bất kỳ vào thư mục để làm icon.
4. **Chuẩn hoá icon**: Chạy `helper/convert.py`.
5. **Cập nhật registry**: Thêm entry mới vào mảng `models` trong `plugin.json`.