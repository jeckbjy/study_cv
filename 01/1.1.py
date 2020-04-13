#!/usr/bin/python3

from PIL import Image
import os


def createGray(img):
    img = img.convert('L')
    img.save('output/empire_gray.jpg')
    return


def createThumbnail(img):
    img.thumbnail([128, 128])
    img.save('output/empire_thumbnail.jpg')
    return


def createCrop(img):
    box = [100, 100, 400, 400]
    region = img.crop(box)
    region = region.transpose(Image.ROTATE_180)
    img.paste(region, box)
    img.save('output/empire_crop.jpg')
    return


def createResize(img):
    img = img.resize([128, 128])
    img.save('output/empire_resize.jpg')
    return


def createRotate(img):
    img = img.rotate(45)
    img.save('output/empire_rotate.jpg')
    return


if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    img = Image.open('images/empire.jpg')
    createGray(img)
    createThumbnail(img)
    createCrop(img)
    createResize(img)
    createRotate(img)
