import math
from PIL import Image

img = Image.new('RGB', (255, 255))
# img = Image.new('RGB', (2550, 2550))
pixels = img.load()

width, height = img.size

for y in range(height):
    for x in range(width):
        r = math.floor(255 / height * y)
        g = math.floor(255 / width * x)
        b = r
        pixels[x, y] = (r, g, b)

img.show()
