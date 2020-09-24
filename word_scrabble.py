import cv2
from tesserocr import PyTessBaseAPI, PSM
from scrabble import ScrabbleSolver
from utils import showImages, showImage, cv2pil
from const import RED, BLUE, BLACK, GREEN, IMG_PATH, WINDOW_LOC
from models import Letter, Board
from screen_capture import getGameImage
import mouse_controller as mc
from time import time


def getWhiteBoxLocations(img, preview=False):
    if type(img) == type(''):
        img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    # area_thresh = 0
    min_area = 0.95*180*29
    max_area = 1.05*180*35
    result = img.copy()
    boxLocations = []
    boxes = []
    for c in contours:
        area = cv2.contourArea(c)
        if area >= min_area <= max_area:
            x, y, w, h = cv2.boundingRect(c)
            # print(x, y, x + w, y + h)
            x, y, w, h = x - 5, y - 5, w + 7, h + 7
            # print(x, y, x + w, y + h)
            cv2.rectangle(result, (x, y), (x + w, y + h), RED, 2)
            boxLocations.append((x, y, x + w, y + h)) # top, left, bottom, right
            boxes.append(img[y : y + h, x : x + w])
            # cv2.drawContours(result, [c], -1, RED, 3)
    if preview:
        showImages(['main', 'gray', 'thresh', 'result'], [img, gray, thresh, result])
    return boxes, boxLocations

def preprocessBlock(box):    
    cropped = box[20:-20, 20:-20]
    print(f'Uncropped: {box.shape}, Cropped: {cropped.shape}')
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_OTSU)[1]
    cropped = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)    
    # showImages(['cropped', 'uncropped', 'threshold'], [cropped, box, thresh])
    return cv2pil(cropped)

def getLetters(letterBoxes, boxLocations):
    letters = []
    with PyTessBaseAPI(psm=PSM.SINGLE_CHAR, lang='eng') as api:
        for box, location in zip(letterBoxes, boxLocations):
            img = preprocessBlock(box)
            api.SetImage(img)
            text = api.GetUTF8Text()
            letters.append(Letter(text, location))
    return letters

def getGameBoard(img, save=False):
    import sys
    import os
    path = f'images/{time()}'
    os.makedirs(path)
    boxes, boxLocations = getWhiteBoxLocations(img)
    if save:
        cv2.imwrite(f'{path}/current_board.jpg', img)
        for i, box in enumerate(boxes):
            cv2.imwrite(f'{path}/{i}.jpg', box)
    letters = getLetters(boxes, boxLocations)
    print("Identified Letters:")
    for letter in letters:
        print(letter.__repr__())
    board = Board(letters)
    if save:
        centerDrawn = drawCenters(img, board)
        cv2.imwrite(f'{path}/centers.jpg', centerDrawn)
    return board

def drawCenters(img, board):
    image = img.copy()
    for letter in board.letters:
        image = cv2.circle(image, letter.center, 3, RED, 2)
    return image

def wreckIt():
    # capture the game screen
    img = getGameImage()
    # img = cv2.imread('images/sample_board.jpg')

    # get gameBoard
    board = getGameBoard(img, save=True)
    
    # get valid words with path
    ss = ScrabbleSolver()
    paths = ss.validateByLocation(board, ss.getValidWords(board.letters))

    start = time()
    for path in paths:
        print(f'Making word: {path}')
        mc.imitateMoveX(paths[path], *WINDOW_LOC['top_left'])
        if time() - start >= 75:
            break

if __name__ == '__main__':
    wreckIt()
    # boxes, boxLocations = getWhiteBoxLocations(IMG_PATH)
    # letters = getLetters(boxes, boxLocations)
    # for letter in letters: print(letter)
    # board = Board(letters)
    # print(str(board))
    # import pickle
    # with open('sample_board.dat', 'wb') as file:
    #     pickle.dump(board, file)
    # solver = ScrabbleSolver()
    # lettersList = [x.character for x in letters]
    # print(f'Number words: {len(solver.getValidWords(lettersList))}')
