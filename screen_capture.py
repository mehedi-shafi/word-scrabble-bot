from const import WINDOW_LOC
import pyscreenshot as ImageGrab
from utils import pil2cv

def getGameImage():
    im = ImageGrab.grab(bbox=WINDOW_LOC['bbox'])
    return pil2cv(im)

if __name__ == '__main__':
    from utils import showImage
    img = getGameImage()
    showImage('', img)