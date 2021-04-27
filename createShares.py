from PIL import Image
import random
import sys

cHf = Image.open("cHf.jpg")
cHf = cHf.convert('CMYK')

mHf = Image.open("mHf.jpg")
mHf = mHf.convert('CMYK')

yHf = Image.open("yhf.jpg")
yHf = yHf.convert('CMYK')

#Create images with each pixel is multiplied
#into 4 small squares
cShare = Image.new("CMYK", [dimension * 2 for dimension in cHf.size])
mShare = Image.new("CMYK", [dimension * 2 for dimension in mHf.size])
yShare = Image.new("CMYK", [dimension * 2 for dimension in yHf.size])



for x in range(0, cHf.size[0]):
    for y in range(0, cHf.size[1]):


        pixel = cHf.getpixel((x, y)) #(C,M,Y,K)

        #If the selected pixel located in the halftone image has the cyan tone,
        #the top right and the bottom left square of the share's pixel 
        #will have the cyan tone, and the rest squares will have the white tone
        if pixel[0]+pixel[1]+pixel[2] == 0:
            cShare.putpixel((x * 2, y * 2), (255,0,0,0))
            cShare.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
            cShare.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
            cShare.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))


        #Otherwise, the opposite rule will be applied to the share's pixel
        else:
            cShare.putpixel((x * 2, y * 2), (0,0,0,0))
            cShare.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
            cShare.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
            cShare.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

        pixel = mHf.getpixel((x, y))


        #Repeat the same task for the rest halftone images
        if pixel[0]+pixel[1]+pixel[2] == 0:
            mShare.putpixel((x * 2, y * 2), (0,255,0,0))
            mShare.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
            mShare.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
            mShare.putpixel((x * 2 + 1, y * 2 + 1), (0,255,0,0))

        else:
            mShare.putpixel((x * 2, y * 2), (0,0,0,0))
            mShare.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
            mShare.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
            mShare.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

        pixel = yHf.getpixel((x, y))

        if pixel[0]+pixel[1]+pixel[2] == 0:
            yShare.putpixel((x * 2, y * 2), (0,0,255,0))
            yShare.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
            yShare.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
            yShare.putpixel((x * 2 + 1, y * 2 + 1), (0,0,255,0))

        else:
            yShare.putpixel((x * 2, y * 2), (0,0,0,0))
            yShare.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
            yShare.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
            yShare.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

cShare.save('cShare.jpg')
mShare.save('mShare.jpg')
yShare.save('yShare.jpg')
