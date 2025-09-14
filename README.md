
# 🖼️ ImgConvert

A lightweight Python package for image format conversion supporting 15+ popular formats. Built with a modular backend system for easy extensibility.

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-prototype-orange)

## ✨ Features

* 🔄  **Multi-format support** : Convert between 15+ image formats
* 🧩  **Modular design** : Extensible backend system
* 📦  **Zero dependencies** : Works out of the box
* 🎯  **Simple API** : Easy to use and integrate
* 🖥️  **Cross-platform** : Works on Windows, macOS, and Linux
* 📚  **Well documented** : Clear examples and API reference

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
https://github.com/Avdh512/imgconvert
cd imgconvert

# Install the package in development mode
pip install -e .
```

### Basic Usage

```python
from imgconvert import convert, list_supported_formats

# List all supported formats
formats = list_supported_formats()
print(f"Supported formats: {formats}")

# Convert an image
result = convert(
    input_path="photo.jpg",
    output_path="photo.png", 
    src_format="JPG",
    dst_format="PNG"
)

# Check conversion results
print(f"✅ Converted successfully!")
print(f"📏 Output size: {result['file_size']} bytes")
print(f"📐 Dimensions: {result['width']}×{result['height']}")
```

## 🎯 Interactive Demo

Try the built-in demo to see all formats in action:

```bash
# Navigate to demo folder
cd demo

# Run the interactive demo
python demo.py

# Clean up generated files
python demo.py clean

# Show help
python demo.py help
```

**Demo Features:**

* 🖼️ Converts a sample image to 9 different formats
* 📁 Creates organized output in `demo/output/converted_files/`
* 📊 Shows detailed conversion statistics
* 🧹 Easy cleanup with built-in clean command

## 📋 Supported Formats

| Format             | Extension           | Description                  | Status          |
| ------------------ | ------------------- | ---------------------------- | --------------- |
| **PNG**      | `.png`            | Portable Network Graphics    | ✅ Full Support |
| **JPG/JPEG** | `.jpg`,`.jpeg`  | JPEG images                  | ✅ Full Support |
| **GIF**      | `.gif`            | Graphics Interchange Format  | ✅ Full Support |
| **TIFF**     | `.tiff`           | Tagged Image File Format     | ✅ Full Support |
| **BMP**      | `.bmp`            | Windows Bitmap               | ✅ Full Support |
| **WEBP**     | `.webp`           | Google WebP format           | ✅ Full Support |
| **ICO**      | `.ico`            | Windows Icon format          | ✅ Full Support |
| **SVG**      | `.svg`            | Scalable Vector Graphics     | ✅ Full Support |
| **PPM**      | `.ppm`            | Portable Pixmap Format       | ✅ Full Support |
| **PGM**      | `.pgm`            | Portable Graymap Format      | ✅ Full Support |
| **RAW**      | `.raw`            | RAW image format             | ⚠️ Prototype  |
| **HEIF**     | `.heif`,`.heic` | High Efficiency Image Format | ⚠️ Prototype  |
| **AVIF**     | `.avif`           | AV1 Image Format             | ⚠️ Prototype  |
| **PDF**      | `.pdf`            | Portable Document Format     | ⚠️ Prototype  |

> **Note** : Formats marked as "Prototype" use stub implementations. For production use, integrate with specialized libraries.

## 📚 API Reference

### `convert(input_path, output_path, src_format, dst_format)`

Convert an image from one format to another.

**Parameters:**

* `input_path` (str): Path to the input image file
* `output_path` (str): Path where the converted image will be saved
* `src_format` (str): Source format (e.g., "JPG", "PNG")
* `dst_format` (str): Target format (e.g., "PNG", "WEBP")

**Returns:**

* `dict`: Conversion metadata with the following keys:
  * `output_path`: Path to the converted file
  * `dst_format`: Destination format used
  * `width`: Image width in pixels
  * `height`: Image height in pixels
  * `file_size`: Output file size in bytes
  * `bytes_written`: Number of bytes written
  * `metadata`: Additional format-specific metadata

**Example:**

```python
result = convert("input.jpg", "output.png", "JPG", "PNG")
# Returns: {
#     'output_path': 'output.png',
#     'dst_format': 'PNG', 
#     'width': 1920,
#     'height': 1080,
#     'file_size': 234567,
#     'bytes_written': 234567,
#     'metadata': {...}
# }
```

### `list_supported_formats()`

Get a list of all supported image formats.

**Returns:**

* `list[str]`: List of supported format strings

**Example:**

```python
formats = list_supported_formats()
print(formats)
# Output: ['PNG', 'JPG', 'JPEG', 'GIF', 'TIFF', 'BMP', 'WEBP', 'ICO', 'HEIF', 'AVIF', 'SVG', 'PDF', 'PPM', 'PGM', 'RAW']
```

## 🏗️ Architecture

### Project Structure

```
imgconvert/
├── imgconvert/              # Main package
│   ├── __init__.py         # Package entry point
│   ├── converter.py        # Core conversion logic
│   ├── formats.py          # Supported format definitions
│   └── backends/           # Format-specific handlers
│       ├── __init__.py     # Backend registry
│       ├── common.py       # Shared utilities
│       ├── raster.py       # Raster formats (PNG, JPG, BMP, etc.)
│       ├── vector.py       # Vector formats (SVG, PDF)
│       ├── raw.py          # RAW and modern formats (HEIF, AVIF)
│       └── misc.py         # Miscellaneous formats (ICO)
├── demo/                   # Demo and examples
│   ├── demo.py            # Interactive demo script
│   └── Example.jpg        # Sample image for testing
├── setup.py               # Package configuration
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT license
└── README.md             # This documentation
```

### Backend System

The package uses a modular backend system:

* **Readers** : Convert file formats to internal image representation
* **Writers** : Convert internal representation to file formats
* **Common** : Shared utilities for format handling
* **Extensible** : Easy to add new format support

## 🛠️ Development

### For Production Use

This is a prototype implementation. For production applications, consider integrating with:

* **[Pillow (PIL)](https://pillow.readthedocs.io/)** - Standard image processing library
* **[OpenCV](https://opencv.org/)** - Computer vision and advanced image processing
* **[imageio](https://imageio.readthedocs.io/)** - Multi-format image I/O
* **[rawpy](https://github.com/letmaik/rawpy)** - RAW camera format support
* **[Wand](http://docs.wand-py.org/)** - ImageMagick binding for Python

### Adding New Formats

1. **Define the format** in `imgconvert/formats.py`
2. **Create reader/writer** functions in appropriate backend module
3. **Register functions** in the backend's `READERS` and `WRITERS` dictionaries
4. **Test** with the demo script

Example:

```python
# In backends/raster.py
def read_new_format(path: str):
    # Implementation here
    pass

def write_new_format(image: dict, path: str):
    # Implementation here
    pass

READERS["NEW_FORMAT"] = read_new_format
WRITERS["NEW_FORMAT"] = write_new_format
```

### Running Tests

```bash
# Test basic functionality
python -c "from imgconvert import convert, list_supported_formats; print('✅ Import successful')"

# Test with demo
cd demo
python demo.py

# Test conversion
python -c "
from imgconvert import convert
result = convert('demo/Example.jpg', 'test.png', 'JPG', 'PNG')
print('✅ Conversion successful:', result['file_size'], 'bytes')
"
```

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
3. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
4. **Make** your changes
5. **Test** your changes with the demo
6. **Commit** your changes (`git commit -m 'Add amazing feature'`)
7. **Push** to the branch (`git push origin feature/amazing-feature`)
8. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/imgconvert.git
cd imgconvert

# Install in development mode
pip install -e .

# Make changes and test
cd demo
python demo.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://claude.ai/chat/LICENSE) file for details.

## 🙏 Acknowledgments

* Built as a learning project for Python packaging and image processing
* Inspired by the need for a simple, dependency-free image converter
* Thanks to the Python packaging community for excellent documentation

## 📞 Support

If you encounter any issues or have questions:

1. **Check the demo** : Run `python demo.py` to verify installation
2. **Read the docs** : This README covers most use cases
3. **Open an issue** : Use GitHub issues for bug reports
4. **Start a discussion** : Use GitHub discussions for questions

## 🔄 Version History

* **v0.1.0** (Current): Initial release with 15 format support and demo

---

**Happy Converting! 🎉**

*Made with ❤️ for the Python community*
