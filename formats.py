# imgconvert/formats.py

# Top 10 famous formats for Prototype 1 (declared)
SUPPORTED_FORMATS = {
    "PNG": "Portable Network Graphics",
    "JPG": "JPEG image (JPG)",
    "JPEG": "JPEG image",
    "GIF": "Graphics Interchange Format",
    "TIFF": "Tagged Image File Format",
    "BMP": "Windows Bitmap",
    "WEBP": "WebP image",
    "ICO": "Windows Icon format",
    "HEIF": "High Efficiency Image File Format (HEIF/HEIC) - stubbed",
    "AVIF": "AV1 Image File Format (AVIF) - stubbed",
    "SVG": "Scalable Vector Graphics (vector)"
}

def list_formats():
    return list(SUPPORTED_FORMATS.keys())
