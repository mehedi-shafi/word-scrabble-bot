# I made a bot to play word scrabble.

# DISCLAIMER
Before going ahead, yes, I know this is cheating. No, I don't intend to play with it. I made it to put some of my knowledge into test.

## Introduction
I decided to make a bot to play scrabble for me(better than me!). 

I get the game's screenshot using pyscreenshot module. Then run very basic image processing algorithms to get the character blocks isolated. This allows me to know the positions of the characters. Also lets me clean up the image for better OCR result.

Then process the individual block a bit and run through tesseract ocr engine to get the letter of the block. With the letters detected I make up words from a dictionary word list with very naive method.

Then I decide the validity of the built up words using adjacency matrix built from the letters and positions of them. Also build the path to make the word in the board.

Finally mouse is controlled using pyautogui to emulate drag. And voila.

Demo:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ScsF-_AQCD8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

> I am sorry for the guy on otherside.

## Todo
- [x] Make words in word blitz word scrabble game.
- [ ] Identify multipliers and plan accordingly.
- [ ] Jumble words to make more human like.

## Requirements
* Python 3.8+
* [Tesseract](https://github.com/tesseract-ocr/tesseract)

## Instllation
* Clone the repository.
* Install tesseract.
* Create and activate virtual environment if you use one (recommended)
* Install the required packages. 
```bash
pip install -r requirements.txt
```
> Note: tesserocr sometimes fails with anaconda if tesseract is installed after conda configured. Make sure to refresh conda's system path.

## Usage
* Obviously you will need to play the game to test it. The game I used is a messenger based game called "Word Blitz".
* In the [const.py](const.py) file configure the game window location accordingly.
* When game starts run the [word_scrabble.py](word_scrabble.py) file.
```bash
python word_scrabble.py
```
* Almost all of the stuffs are hard coded for this game specifically. Please read through the code if you want to test on other similar game.