from PIL import Image
image = Image.open("idol.jpg")  # ganti ke gambar yang diinginkan
image = image.resize((120, 120))  
image = image.convert("RGB") 
width, height = image.size
pixels = image.load()
colors = [[None for _ in range(width)] for _ in range(height)]
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        colors[y][x] = "#" + format(r, "02x") + format(g, "02x") + format(b, "02x")
print(colors)
