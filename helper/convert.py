from PIL import Image
import os

IMAGE_EXTENSIONS = frozenset({
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".tiff", ".tif",
    ".ico", ".svg", ".avif", ".heic", ".heif", ".jp2", ".j2k", ".pcx",
    ".ppm", ".pgm", ".pbm", ".xbm", ".xpm",
})


def _find_first_image(folder):
    try:
        entries = sorted(os.listdir(folder))
    except OSError:
        return None
    for name in entries:
        ext = os.path.splitext(name)[1].lower()
        if ext not in IMAGE_EXTENSIONS:
            continue
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue
        try:
            with Image.open(path) as img:
                img.verify()
            return path
        except Exception:
            continue
    return None


def convert_first_images_to_icons():
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for name in sorted(os.listdir(parent)):
        subdir = os.path.join(parent, name)
        if not os.path.isdir(subdir) or name == "helper" or name.startswith("."):
            continue

        first = _find_first_image(subdir)
        if first is None:
            continue

        with Image.open(first) as img:
            should_resize = img.size != (128, 128)
            should_convert = img.format != "PNG"
            should_rename = os.path.basename(first) != "icon.png"

            if not (should_resize or should_convert or should_rename):
                print(f"⏭️  {name}/icon.png — already correct")
                continue

            if should_resize:
                img = img.resize((128,128), Image.LANCZOS)

            dst = os.path.join(subdir, "icon.png")
            if first != dst:
                os.remove(first)
                print(f"🗑️  removed {os.path.relpath(first, parent)}")

            img.save(dst, "PNG")
            print(f"✅ {name}/icon.png ({img.size[0]}x{img.size[1]}, PNG)")


def convert_all_to_png(input_folder, size=None):
    output_folder = os.path.join(input_folder, "converted")
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)

        if not os.path.isfile(input_path):
            continue

        try:
            with Image.open(input_path) as img:
                if size:
                    img = img.resize(size, Image.LANCZOS)

                base_name, _ = os.path.splitext(file_name)
                output_path = os.path.join(output_folder, f"{base_name}.png")

                img.save(output_path, "PNG")
                print(f"✅ {file_name} → {output_path} (size={img.size})")
        except Exception as e:
            print(f"⚠️ {file_name}: {e}")

    print(f"\n🎉 done: {output_folder}")


if __name__ == "__main__":
    convert_first_images_to_icons() 
