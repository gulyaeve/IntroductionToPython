from PIL import Image


def watermark(input_image: str, watermark_image: str) -> str:
    base_image = Image.open(input_image)
    watermark = Image.open(watermark_image).convert("RGBA")

    transparent = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, (40, 100), watermark)

    if base_image.mode == 'RGB':
        transparent = transparent.convert('RGB')
    else:
        transparent = transparent.convert('P')

    transparent.save(f"watermarked.png")
    return f"watermarked.png"


if __name__ == '__main__':
    watermark("1.png", "2.png")
