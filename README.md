# Script Models

Registry chứa các bộ prompt/model cho **Script Pro**. Mỗi model là một thư mục con trong `core/` với cấu trúc thống nhất.

## Cấu trúc

```
script-models/
├── plugin.json              # Registry — danh sách tất cả models
├── core/
│   └── wildlife/            # Model: Wildlife & Science Creators
│       ├── manifest.json    # Metadata + mapping script files
│       ├── icon.png         # Icon 128×128 PNG
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

## plugin.json — Registry

Khai báo tất cả models. Cấu trúc mỗi entry:

```json
{
  "name": "Tên hiển thị",
  "author": "2noScript",
  "path": "https://raw.githubusercontent.com/2noScript/script-models/main/core/<model>/manifest.json",
  "version": 1,
  "icon": "https://raw.githubusercontent.com/2noScript/script-models/main/core/<model>/icon.png",
  "description": "Mô tả ngắn",
  "tags": ["Youtube"]
}
```

## Cấu trúc một model

Mỗi model là một thư mục con trong `core/` (ví dụ: `core/wildlife/`).

### manifest.json

```json
{
  "metadata": {
    "name": "<model>",
    "author": "2noScript",
    "version": 1,
    "description": "..."
  },
  "script": {
    "idea": "<file>.md",
    "script": "<file>.md",
    "thumbnail": "<file>.md",
    "visuals": "<file>.md"
  }
}
```

### Script files (`.md`)

Mỗi file Markdown chứa prompt cho một bước trong quy trình sản xuất nội dung:

- **SCRIPT WRITER.md** — viết kịch bản
- **THUMBNAIL GENERATOR.md** — tạo thumbnail
- **VIDEO IDEA GENERATOR.md** — ý tưởng video
- **VISUAL & IMAGE PROMPT MAKER.md** — tạo prompt hình ảnh

### icon.png

Icon đại diện cho model, chuẩn **128×128 PNG**.

## helper/ — Công cụ icon

Dùng để tự động chuẩn hoá icon cho tất cả models.

### convert_first_images_to_icons()

Tự động tìm file ảnh đầu tiên (sort alphabet) trong mỗi thư mục con của `script-models/` (trừ `helper/` và thư mục ẩn) và chuẩn hoá thành `icon.png`:

- Kích thước → `(128, 128)` nếu chưa đúng
- Định dạng → PNG nếu chưa phải PNG
- Tên → `icon.png` nếu chưa đúng tên

Nếu ảnh đã đúng cả 3 điều kiện → bỏ qua.

### convert_all_to_png(input_folder, size=None)

Convert hàng loạt ảnh trong folder sang PNG, lưu vào thư mục `converted/`.

### Sử dụng

```bash
cd helper
uv run python convert.py
```

Yêu cầu: Python ≥ 3.12, Pillow.

## Thêm model mới

1. Tạo thư mục: `mkdir core/<model>`
2. Tạo `manifest.json` và các file `.md`
3. Thêm ảnh vào thư mục (bất kỳ định dạng/kích thước nào)
4. Chạy `uv run python convert.py` để tự động tạo `icon.png` chuẩn
5. Thêm entry vào `plugin.json`
