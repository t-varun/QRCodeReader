from pyzbar.pyzbar import decode
from PIL import Image

text = decode(Image.open('Sateesh.png'))
text = text[0].data.decode('UTF-8')
print(text)
