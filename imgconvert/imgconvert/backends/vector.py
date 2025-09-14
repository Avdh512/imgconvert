# imgconvert/backends/vector.py
from .common import decode_bytes_to_image, encode_image_to_fake_bytes

def read_svg(path: str):
    """
    Read SVG as text and produce a small rasterized Image dict by sampling text bytes.
    (This is a stub: we don't parse SVG; just create an image from file bytes.)
    """
    with open(path, "rb") as f:
        data = f.read()
    return decode_bytes_to_image(data)

def write_svg(image: dict, path: str):
    """
    Create a simple SVG file that contains a solid rect with width/height from image.
    Not a real raster-to-vector conversion, but a useful placeholder.
    """
    w = image["width"]
    h = image["height"]
    # create a very tiny SVG with one rect and base64 pixel comment (not required)
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <rect width="{w}" height="{h}" style="fill:rgb(200,200,200)"/>
  <!-- IMGCONV:SVG METADATA width={w} height={h} -->
</svg>
"""
    data = svg.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return len(data)

def read_pdf(path: str):
    with open(path, "rb") as f:
        data = f.read()
    return decode_bytes_to_image(data)

def write_pdf(image: dict, path: str):
    """
    Create a very simple plaintext-ish PDF stub (not a valid PDF viewer file).
    This is a placeholder to show the plumbing.
    """
    content = f"%PDF-FAKE\n% IMGCONV PDF stub\nWidth:{image['width']}\nHeight:{image['height']}\n\n".encode("utf-8") + image["pixels"][:100]
    with open(path, "wb") as f:
        f.write(content)
    return len(content)

READERS = {
    "SVG": read_svg,
    "PDF": read_pdf,
}

WRITERS = {
    "SVG": write_svg,
    "PDF": write_pdf
}
