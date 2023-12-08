import qrcode

features= qrcode.QRCode(version=1, box_size=30,border=2)
features.add_data("https://www.youtube.com/")
features.make(fit=True)

genrate_image= features.make_image(fill_color="blue", back_color="white")
genrate_image.save('image3.png')