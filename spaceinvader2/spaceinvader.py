import platform
platform.architecture()
from pygame import *
import sys

SCREEN 	= display.set_mode((800,600))

class SpaceInvaders(object):
    def __init__(self):
        print("init ...")
        mixer.pre_init(44100, -16, 1,512)
        init()
        self.caption = display.set_caption("Space Invader")
        self.background = image.load('images/background.jpg').convert()
        self.screen = SCREEN
        self.mainScreen = True
        self.startGame = False
        self.gameOver = False

    ## check for keyboard input 
    def check_input(self):
        self.keys = key.get_pressed()
        for e in event.get():
            if e.type == QUIT:
                sys.exit()

    ## create game menu
    def create_main_menu(self):
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYUP:
                print("key up")
                self.startGame = True
                self.mainScreen = False

    def main(self):
        print("init ...")
        while True:
            if self.mainScreen:
                print("main screen...")
                self.create_main_menu()
            elif self.startGame:
                print("start game ...")
                sys.exit()
            elif self.gameOver :
                print("game over ...")