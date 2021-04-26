from PIL import Image
import random
import sys

inputImage = Image.open("test_image.jpg")

cMono = Image.new("CMYK", [dimension for dimension in inputImage.size])
mMono = Image.new("CMYK", [dimension for dimension in inputImage.size])
yMono = Image.new("CMYK", [dimension for dimension in inputImage.size])

for x in range(0, inputImage.size[0], 1):
    for y in range(0, inputImage.size[1], 1):
        imagePixel = inputImage.getpixel((x, y))

        cMono.putpixel((x, y),(imagePixel[0],0,0,0))
        mMono.putpixel((x, y),(0,imagePixel[1],0,0))
        yMono.putpixel((x, y),(0,0,imagePixel[2],0))

cMono = cMono.convert('1')
mMono = mMono.convert('1')
yMono = yMono.convert('1')

cHf = Image.new("CMYK", [d for d in cMono.size])
mHf = Image.new("CMYK", [d for d in mMono.size])
yHf = Image.new("CMYK", [d for d in yMono.size])

for x in range(0, inputImage.size[0]):
    for y in range(0, inputImage.size[1]):
        if cMono.getpixel((x, y)) == 255:
            cHf.putpixel((x, y),(255,0,0,0))
        else:
            cHf.putpixel((x, y),(0,0,0,0))

        if mMono.getpixel((x, y)) == 255:
            mHf.putpixel((x, y),(0,255,0,0))
        else:
            mHf.putpixel((x, y),(0,0,0,0))

        if yMono.getpixel((x, y)) == 255:
            yHf.putpixel((x, y),(0,0,255,0))
        else:
            yHf.putpixel((x, y),(0,0,0,0))


cHf.save('cHf.jpg')
mHf.save('mHf.jpg')
yHf.save('yHf.jpg')