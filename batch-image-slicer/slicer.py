from pathlib import Path
from PIL import Image


def load_clean_rgba(image_path: Path) -> Image.Image:
    with Image.open(image_path) as img:
        # Converting to RGBA and creating a new image strips EXIF metadata
        rgba = img.convert("RGBA")
        clean_img = Image.new("RGBA", rgba.size)
        clean_img.paste(rgba, (0, 0))
        return clean_img