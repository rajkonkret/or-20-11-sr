from PIL import Image, ImageDraw

email = "rajkonkret660@gmail.com"

img = Image.new('RGB', (200, 600), color=(73, 109, 137))

d = ImageDraw.Draw(img)
d.text((10, 10), email, fill=(255, 255, 0))

img.save('email.png')
