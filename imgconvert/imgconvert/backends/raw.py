# imgconvert/backends/raw.py
from .common import decode_bytes_to_image, encode_image_to_fake_bytes

def read_raw(path: str):
    with open(path, "rb") as f:
        data = f.read()
    return decode_bytes_to_image(data)

def write_raw(image: dict, path: str):
    payload = encode_image_to_fake_bytes(image, "RAW")
    with open(path, "wb") as f:
        f.write(payload)
    return len(payload)

# HEIF and AVIF are stubbed to the same generic handlers for now
def read_heif(path: str):
    with open(path, "rb") as f:
        data = f.read()
    return decode_bytes_to_image(data)

def write_heif(image: dict, path: str):
    payload = encode_image_to_fake_bytes(image, "HEIF")
    with open(path, "wb") as f:
        f.write(payload)
    return len(payload)

def read_avif(path: str):
    with open(path, "rb") as f:
        data = f.read()
    return decode_bytes_to_image(data)

def write_avif(image: dict, path: str):
    payload = encode_image_to_fake_bytes(image, "AVIF")
    with open(path, "wb") as f:
        f.write(payload)
    return len(payload)

READERS = {
    "RAW": read_raw,
    "HEIF": read_heif,
    "AVIF": read_avif,
}

WRITERS = {
    "RAW": write_raw,
    "HEIF": write_heif,
    "AVIF": write_avif
}
