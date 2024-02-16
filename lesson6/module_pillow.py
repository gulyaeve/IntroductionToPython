from PIL import Image, ImageFilter
import numpy as np


if __name__ == '__main__':
    my_image = Image.open("1.png")
    my_image.load()
    print(my_image.size)
    print(my_image.format)
    print(my_image.mode)

    my_image_filtered = my_image.filter(ImageFilter.BLUR)
    # my_image.show()
    # my_image_filtered.show()
    my_image_filtered.save("1_f.png")

    size = (128, 128)
    # my_image.thumbnail(size)
    my_image_resized = my_image.resize(size)
    # my_image_resized.show()
    my_image_resized = my_image_resized.filter(ImageFilter.CONTOUR)
    my_image_resized.show()
    my_image_resized.save("1_s.webp")
    my_image_resized = my_image_resized.convert("RGB")
    my_image_resized.save("1_s.jpg", "JPEG", optimize=True, quality=10)

    my_image_numpy = np.array(my_image_resized)
    print(my_image_numpy)

