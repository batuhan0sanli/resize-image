import cv2


sizes = [64, 128, 256, 512, 1024]

img = cv2.imread('original.jpg')

def resize(img, size):
    resizedImg = cv2.resize(img, (size, size))
    cv2.imwrite(f'{size}x{size}.jpg', resizedImg)

for size in sizes:

    resize(img, size)