from PIL import Image
import cv2
import numpy as np

def showImage(title, img):
    while True:
        cv2.imshow(title, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def showImages(titles, imgs):
    while True:
        if len(titles) != len(imgs):
            titles = [str(x) for x in range(len(imgs))]
        for title, img in zip(titles, imgs):
            cv2.imshow(title, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def cv2pil(img):
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

def pil2cv(img):
    return np.array(img)[:, :, ::-1].copy()

def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

def getCenter(x1, y1, x2, y2):
    return ((x1 + x2) // 2, (y1 + y2) //2)

def drawPath(img, path, color):
    for i in range(len(path)-1):
        img = cv2.line(img, path[i].center, path[i+1].center, color, 2)
    return img

def timeit(func):
    from time import time
    def tf(*args, **kwargs):
        start = time()
        rv = func(*args, **kwargs)
        print(f'{func.__name__}: required time: {(time() - start) * 1000}ms')
        return rv
    return tf
        
