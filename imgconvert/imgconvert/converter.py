# imgconvert/converter.py
import os
from .formats import SUPPORTED_FORMATS
from .backends import READERS, WRITERS
from .backends.common import decode_bytes_to_image

def list_supported_formats():
    return list(SUPPORTED_FORMATS.keys())

def _ensure_format(fmt: str):
    if not fmt:
        raise ValueError("Format string must be provided (e.g., 'PNG', 'JPG').")
    return fmt.upper()

def convert(input_path: str, output_path: str, src_format: str, dst_format: str):
    """
    Convert input_path (using explicit src_format string) to output_path (dst_format string).
    Returns a dict with metadata including final file size.
    """
    src = _ensure_format(src_format)
    dst = _ensure_format(dst_format)

    if src not in SUPPORTED_FORMATS:
        raise ValueError(f"Source format '{src}' not declared in SUPPORTED_FORMATS.")
    if dst not in SUPPORTED_FORMATS:
        raise ValueError(f"Destination format '{dst}' not declared in SUPPORTED_FORMATS.")

    # choose reader (if backend exists), else fallback to generic decode from bytes
    reader = READERS.get(src)
    if reader:
        image = reader(input_path)
    else:
        # fallback generic decoder
        with open(input_path, "rb") as f:
            data = f.read()
        image = decode_bytes_to_image(data)
        image.setdefault("metadata", {})["claimed_src_format"] = src

    # choose writer
    writer = WRITERS.get(dst)
    if not writer:
        raise NotImplementedError(f"No writer implemented for destination format: {dst}")

    bytes_written = writer(image, output_path)
    file_size = os.path.getsize(output_path) if os.path.exists(output_path) else bytes_written

    return {
        "output_path": output_path,
        "dst_format": dst,
        "width": image.get("width"),
        "height": image.get("height"),
        "bytes_written": bytes_written,
        "file_size": file_size,
        "metadata": image.get("metadata", {})
    }
