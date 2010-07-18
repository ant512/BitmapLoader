import bitmaploader

# Load a bitmap
bmp = bitmaploader.Bitmap("./logo.bmp")

# Print the bitmap's properties
bmp.output()
print("")

# Print the colours of all pixels
for x in range(0, bmp.width):
	for y in range(0, bmp.height):
		print(bmp.get_pixel_color(x, y))
	print("")
		
# Print the red component of the pixel 0, 0
print(bmp.get_pixel_red(0, 0))