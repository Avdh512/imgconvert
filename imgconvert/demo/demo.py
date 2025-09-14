#!/usr/bin/env python3

import os
import sys
from pathlib import Path

# Import the installed package
try:
    from imgconvert import convert, list_supported_formats
except ImportError:
    print("❌ Error: imgconvert package not installed.")
    print("Run: pip install -e . (from the main project directory)")
    sys.exit(1)

def create_output_folder():
    """Create output folder for converted files"""
    output_dir = Path(__file__).parent / "converted_files"
    output_dir.mkdir(exist_ok=True)
    return output_dir

def run_demo():
    print("🖼️  ImgConvert Demo")
    print("=" * 60)
    
    # Show supported formats
    formats = list_supported_formats()
    print(f"📋 Supported formats ({len(formats)}): {', '.join(formats)}")
    print()
    
    # Get paths
    demo_dir = Path(__file__).parent
    input_path = demo_dir / "Example.jpg"
    output_dir = create_output_folder()
    
    # Check if example image exists
    if not input_path.exists():
        print(f"❌ Error: Example image not found at {input_path}")
        print("Please ensure 'Example.jpg' exists in the demo folder.")
        print()
        print("You can:")
        print("1. Copy any JPG image to the demo folder")
        print("2. Rename it to 'Example.jpg'")
        return
    
    print(f"📁 Input image: {input_path.name}")
    print(f"📏 Input size: {input_path.stat().st_size:,} bytes")
    print(f"💾 Output folder: {output_dir.name}/")
    print()
    
    # List of conversions to perform
    conversions = [
        ("PNG", "Portable Network Graphics", "🔷"),
        ("BMP", "Windows Bitmap", "🟦"), 
        ("GIF", "Graphics Interchange Format", "🎬"),
        ("TIFF", "Tagged Image File Format", "📄"),
        ("WEBP", "WebP Format", "🌐"),
        ("PPM", "Portable Pixmap", "🔴"),
        ("PGM", "Portable Graymap", "⚫"),
        ("SVG", "Scalable Vector Graphics", "📐"),
        ("ICO", "Windows Icon", "🖼️")
    ]
    
    successful_conversions = 0
    failed_conversions = []
    
    print("🔄 Converting JPG to various formats...")
    print("-" * 60)
    
    for dst_format, description, icon in conversions:
        try:
            # Create output filename in the converted_files folder
            output_filename = f"converted_example.{dst_format.lower()}"
            output_path = output_dir / output_filename
            
            # Perform conversion
            result = convert(
                input_path=str(input_path),
                output_path=str(output_path),
                src_format="JPG",
                dst_format=dst_format
            )
            
            # Check if file was created and get its size
            if output_path.exists():
                file_size = output_path.stat().st_size
                successful_conversions += 1
                
                print(f"{icon} JPG → {dst_format:4s}: {description}")
                print(f"   📄 File: {output_filename}")
                print(f"   📏 Size: {file_size:,} bytes")
                print(f"   📐 Dims: {result.get('width', 'N/A')}×{result.get('height', 'N/A')}")
            else:
                print(f"❌ JPG → {dst_format}: Failed - output file not created")
                failed_conversions.append(dst_format)
                
        except Exception as e:
            print(f"❌ JPG → {dst_format}: Error - {str(e)}")
            failed_conversions.append(dst_format)
        
        print()
    
    # Summary
    print("=" * 60)
    print(f"📊 CONVERSION SUMMARY")
    print(f"✅ Successful: {successful_conversions}/{len(conversions)}")
    if failed_conversions:
        print(f"❌ Failed: {', '.join(failed_conversions)}")
    
    if successful_conversions > 0:
        print(f"📁 All converted files saved in: {output_dir}")
        
        # List all created files
        created_files = list(output_dir.glob("converted_example.*"))
        if created_files:
            print(f"📋 Created files:")
            for file_path in sorted(created_files):
                size = file_path.stat().st_size
                print(f"   • {file_path.name} ({size:,} bytes)")

def clean_output_files():
    """Clean up generated output files"""
    output_dir = Path(__file__).parent / "converted_files"
    
    if not output_dir.exists():
        print("🧹 No output folder found to clean")
        return
    
    deleted_files = []
    for file_path in output_dir.glob("converted_example.*"):
        if file_path.is_file():
            file_path.unlink()
            deleted_files.append(file_path.name)
    
    if deleted_files:
        print(f"🧹 Cleaned up {len(deleted_files)} files:")
        for filename in deleted_files:
            print(f"   • {filename}")
        
        # Remove folder if empty
        try:
            if not any(output_dir.iterdir()):
                output_dir.rmdir()
                print(f"📁 Removed empty folder: {output_dir.name}")
        except:
            pass
    else:
        print("🧹 No files found to clean up")

def show_help():
    """Show help information"""
    print("🖼️  ImgConvert Demo Help")
    print("=" * 40)
    print("Usage:")
    print("  python demo.py           - Run conversion demo")
    print("  python demo.py clean     - Clean up output files") 
    print("  python demo.py help      - Show this help")
    print()
    print("Requirements:")
    print("  • Example.jpg file in the same folder as demo.py")
    print("  • imgconvert package installed (pip install -e .)")
    print()
    print("Output:")
    print("  • Converted files will be saved in 'output/converted_files/' folder")
    print("  • Original Example.jpg will not be modified")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "clean":
            clean_output_files()
        elif command in ["help", "-h", "--help"]:
            show_help()
        else:
            print(f"Unknown command: {command}")
            print("Use 'python demo.py help' for usage information")
    else:
        run_demo()
        print()
        print("💡 Tips:")
        print("   • Run 'python demo.py clean' to remove converted files")
        print("   • Run 'python demo.py help' for more options")