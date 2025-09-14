import os
from imgconvert import convert, list_supported_formats

def run_demo():
    print("Supported formats:", list_supported_formats())

    base_dir = os.path.dirname(__file__)
    input_path = os.path.join(base_dir, "Example.jpg")

    # --- Convert Example.jpg into different formats ---

    out_png = os.path.join(base_dir, "out_from_jpg.png")
    res1 = convert(input_path, out_png, src_format="JPG", dst_format="PNG")
    print("JPG -> PNG:", res1, "size:", os.path.getsize(out_png))

    out_bmp = os.path.join(base_dir, "out_from_jpg.bmp")
    res2 = convert(input_path, out_bmp, src_format="JPG", dst_format="BMP")
    print("JPG -> BMP:", res2, "size:", os.path.getsize(out_bmp))

    out_gif = os.path.join(base_dir, "out_from_jpg.gif")
    res3 = convert(input_path, out_gif, src_format="JPG", dst_format="GIF")
    print("JPG -> GIF:", res3, "size:", os.path.getsize(out_gif))

    out_tiff = os.path.join(base_dir, "out_from_jpg.tiff")
    res4 = convert(input_path, out_tiff, src_format="JPG", dst_format="TIFF")
    print("JPG -> TIFF:", res4, "size:", os.path.getsize(out_tiff))

    out_webp = os.path.join(base_dir, "out_from_jpg.webp")
    res5 = convert(input_path, out_webp, src_format="JPG", dst_format="WEBP")
    print("JPG -> WEBP:", res5, "size:", os.path.getsize(out_webp))

    out_ppm = os.path.join(base_dir, "out_from_jpg.ppm")
    res6 = convert(input_path, out_ppm, src_format="JPG", dst_format="PPM")
    print("JPG -> PPM:", res6, "size:", os.path.getsize(out_ppm))

    out_pgm = os.path.join(base_dir, "out_from_jpg.pgm")
    res7 = convert(input_path, out_pgm, src_format="JPG", dst_format="PGM")
    print("JPG -> PGM:", res7, "size:", os.path.getsize(out_pgm))

    out_svg = os.path.join(base_dir, "out_from_jpg.svg")
    res8 = convert(input_path, out_svg, src_format="JPG", dst_format="SVG")
    print("JPG -> SVG:", res8, "size:", os.path.getsize(out_svg))

    out_ico = os.path.join(base_dir, "out_from_jpg.ico")
    res9 = convert(input_path, out_ico, src_format="JPG", dst_format="ICO")
    print("JPG -> ICO:", res9, "size:", os.path.getsize(out_ico))

if __name__ == "__main__":
    run_demo()
