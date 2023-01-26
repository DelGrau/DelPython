from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Codigos/Python/qrcodes/qrcode.png')

result = decode(img)

print (result)