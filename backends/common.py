# imgconvert/backends/common.py
import math

def decode_bytes_to_image(data: bytes):
    """
    Generic decode from arbitrary bytes to an internal Image dict.
    This is used when a real parser is not available.
    The function deterministically creates width/height and pixel bytes
    from input data so conversions are repeatable.
    Returns: dict with keys: width, height, mode, pixels (bytes), metadata
    """
    n = len(data)
    # assume RGB 3 bytes per pixel
    pixels_count = max(1, n // 3)
    width = int(math.sqrt(pixels_count))
    if width == 0:
        width = 1
    height = (pixels_count + width - 1) // width
    needed = width * height * 3

    # build pixel bytes by repeating input bytes deterministically
    pixel_bytes = bytearray(needed)
    if n == 0:
        # default grey
        for i in range(needed):
            pixel_bytes[i] = 128
    else:
        for i in range(needed):
            pixel_bytes[i] = data[i % n]

    return {
        "width": width,
        "height": height,
        "mode": "RGB",
        "pixels": bytes(pixel_bytes),
        "metadata": {
            "inferred_from_bytes": True,
            "orig_len": n
        }
    }

def encode_image_to_fake_bytes(image: dict, fmt: str):
    """
    Create a deterministic, human-readably prefixed binary for a given format.
    This is NOT a real encoder: it writes a simple ASCII header then raw pixels.
    Returns bytes to write into file.
    """
    header = (
        f"IMGCONV:FORMAT:{fmt}\n"
        f"WIDTH:{image['width']}\n"
        f"HEIGHT:{image['height']}\n"
        f"MODE:{image.get('mode','RGB')}\n"
        f"METADATA:{image.get('metadata',{})}\n"
        f"\n"
    ).encode("utf-8")
    payload = image["pixels"]
    return header + payload
