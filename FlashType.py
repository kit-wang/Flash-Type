import time
from pprint import pprint
import random
import pygame
from pygame.locals import *
import sys

f = open('frank.txt', encoding="utf8")
text= f.read()

class game:
    def __init__(self):
        # self is an instance of the class
        self.h = 800
        self.w = 1300
        
        # ensuring to reset per round
        self.reset = True
        self.active = False
        
        # input_line == input_text
        self.word = ''
        self.input_line = ''
        self.accuracy = 0
        self.totalTime = 0
        # perhaps change this displaying format
        self.results = 'Time:{totalTime} Accuracy: {accuracy} % Words per minute: {speed} '
        
        self.speed = 0
        # end == end_game
        self.end_game = False
        
        # huh
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)
        
        # FINALLY!
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Flash Type')
        
    
    # typewriter effect rendering as input
    def typing(screen, self, color, message, ycor, font_size):
        # rendering font -- will play around w custom ones later
        lineFont = pygame.font.Font(None, font_size)
        renderedText = font.render(message, 1, color)
        
        # make the surrounding rect
        box = text.get_rect(center=(self.w / 2, ycor))
        
        # layering the text & the box
        screen.blit(renderedText, box)
        
        pygame.display.update()
        
    
    
    
    

    
    
    
    
    
    
    