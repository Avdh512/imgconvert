# imgconvert/backends/raster.py
from .common import decode_bytes_to_image, encode_image_to_fake_bytes

# READERS: functions that accept a path and return an Image dict
def read_png(path: str):
    return _generic_read(path, expected_fmt="PNG")

def read_jpg(path: str):
    return _generic_read(path, expected_fmt="JPG")

def read_jpeg(path: str):
    return _generic_read(path, expected_fmt="JPEG")

def read_bmp(path: str):
    return _generic_read(path, expected_fmt="BMP")

def read_gif(path: str):
    return _generic_read(path, expected_fmt="GIF")

def read_tiff(path: str):
    return _generic_read(path, expected_fmt="TIFF")

def read_webp(path: str):
    return _generic_read(path, expected_fmt="WEBP")

# WRITERS: write image dict to path; return number of bytes written
def write_png(image: dict, path: str):
    return _generic_write(image, path, "PNG")

def write_jpg(image: dict, path: str):
    return _generic_write(image, path, "JPG")

def write_jpeg(image: dict, path: str):
    return _generic_write(image, path, "JPEG")

def write_bmp(image: dict, path: str):
    return _generic_write(image, path, "BMP")

def write_gif(image: dict, path: str):
    return _generic_write(image, path, "GIF")

def write_tiff(image: dict, path: str):
    return _generic_write(image, path, "TIFF")

def write_webp(image: dict, path: str):
    return _generic_write(image, path, "WEBP")


# Generic helpers used in this module
def _generic_read(path: str, expected_fmt: str):
    """
    Try to decode our fake-formatted file first; otherwise fall back to generic decode.
    """
    try:
        with open(path, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        raise

    # If the file was previously written by this package, parse header:
    if data.startswith(b"IMGCONV:FORMAT:" + expected_fmt.encode("utf-8")):
        # simple parsing: header up to blank line
        parts = data.split(b"\n\n", 1)
        header = parts[0].decode("utf-8", errors="ignore")
        payload = parts[1] if len(parts) > 1 else b""
        # parse width/height (robust)
        w = 1; h = 1
        for line in header.splitlines():
            if line.startswith("WIDTH:"):
                try:
                    w = int(line.split(":", 1)[1])
                except:
                    pass
            if line.startswith("HEIGHT:"):
                try:
                    h = int(line.split(":", 1)[1])
                except:
                    pass
        return {"width": w, "height": h, "mode": "RGB", "pixels": payload[:w*h*3], "metadata": {"source": expected_fmt, "fake_header": True}}
    # else fallback generic decode
    return decode_bytes_to_image(data)

def _generic_write(image: dict, path: str, fmt: str):
    payload = encode_image_to_fake_bytes(image, fmt)
    with open(path, "wb") as f:
        f.write(payload)
    return len(payload)


# registry dictionaries used by the package importer
READERS = {
    "PNG": read_png,
    "JPG": read_jpg,
    "JPEG": read_jpeg,
    "BMP": read_bmp,
    "GIF": read_gif,
    "TIFF": read_tiff,
    "WEBP": read_webp,
}

WRITERS = {
    "PNG": write_png,
    "JPG": write_jpg,
    "JPEG": write_jpeg,
    "BMP": write_bmp,
    "GIF": write_gif,
    "TIFF": write_tiff,
    "WEBP": write_webp,
}
