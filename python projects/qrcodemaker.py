import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

typeofqr = input("Would you like to encode or decode a qrcode: ")

if typeofqr.lower() == "encode":

    data = input("What would you like to turn into a qrcode: ")

    img = qrcode.make(data)
    Qrcodename = input("What would you like to name the saved qrcode: ")
    img.save(Qrcodename+".png")

elif typeofqr.lower() == "decode":
    ToDecode = input("What qrcode you like decode: ")
    result = decode(Image.open(ToDecode))
    print(result)
