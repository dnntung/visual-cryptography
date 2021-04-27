from PIL import Image
import sys

cShare = Image.open("cShare.jpg")
mShare = Image.open("mShare.jpg")
yShare = Image.open("yShare.jpg")

decryptedImage = Image.new('CMYK', cShare.size)

for x in range(0,cShare.size[0],2):
    for y in range(0,cShare.size[1],2):

    	#Get the tone of the top right square of each pixel
    	#in each shares
        C = cShare.getpixel((x+1, y))[0]
        M = mShare.getpixel((x+1, y))[1]
        Y = yShare.getpixel((x+1, y))[2]

        #Return back the tones to each pixel in the decryted image
        decryptedImage.putpixel((x, y), (C,M,Y,0))
        decryptedImage.putpixel((x+1, y), (C,M,Y,0))
        decryptedImage.putpixel((x, y+1), (C,M,Y,0))
        decryptedImage.putpixel((x+1, y+1), (C,M,Y,0))

decryptedImage.save("decryptedImage.jpg")
