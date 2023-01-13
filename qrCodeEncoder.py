import qrcode as qr

data = 'Beba agua'

qrc = qr.QRCode(version=2, box_size=50, border=1)
qrc.add_data(data)

qrc.make(fit=True)
img = qrc.make_image(fill_color = 'blue', back_color='white')

img.save('C:/Codigos/Python/qrcodes/qrcode3.png')

print ("QR-CODE GENERATED SUCCESSFULLY")