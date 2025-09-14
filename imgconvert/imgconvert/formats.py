# imgconvert/formats.py

# Top formats for image conversion (declared)
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
    "SVG": "Scalable Vector Graphics (vector)",
    "PDF": "Portable Document Format",
    "PPM": "Portable Pixmap Format",
    "PGM": "Portable Graymap Format",
    "RAW": "RAW image format"
}

def list_formats():
    return list(SUPPORTED_FORMATS.keys())