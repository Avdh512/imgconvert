# imgconvert/backends/misc.py
from .common import decode_bytes_to_image, encode_image_to_fake_bytes

def read_ico(path: str):
    with open(path, "rb") as f:
        data = f.read()
    return decode_bytes_to_image(data)

def write_ico(image: dict, path: str):
    # produce a tiny fake ICO header + pixels
    header = b"ICONFAKE\n"
    payload = encode_image_to_fake_bytes(image, "ICO")
    with open(path, "wb") as f:
        f.write(header + payload)
    return len(header + payload)

READERS = {
    "ICO": read_ico
}
WRITERS = {
    "ICO": write_ico
}
