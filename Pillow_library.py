# pip install PIL

from PIL import Image
img = Image.open("Boy.jpeg")
# img.show()
print(img.format, img.size, img.mode)
# resized = img.resize((546,546))
# resized.show()
# croping = img.crop((0,0,546,1000))
# croping.show()
# img.save("out.png")
# Rotating
# rotating= resized.rotate(90)
# resizing_2=rotating.resize((546,300))
# rotating.show()
# resizing_2.show()
# Fliping


