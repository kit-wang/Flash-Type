import pygame
from pygame.locals import *
import sys
import time
import random
import statistics

class game:
    def __init__(self):
        self.w=800
        self.h=520
        self.reset=True
        self.active = False
        self.input_text=''
        self.word = ''
        self.lines = ''
        self.typed_chars = ''
        self.start_time = 0
        self.total_time = 0
        self.accuracy = []
        self.wpm = 0
        self.end = False
        self.errorList = []
        # the following are colors for text
        self.theme_color = (255,213,200)
        self.text_color = (240,240,100)
        self.display_color = (255,70,70)
        pygame.init()
        self.open_img = pygame.image.load('type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w,self.h))
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.w, self.h))
        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Flash Type: a typing speed test')
        
    
    def draw_text(self, screen, message, y ,fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(message, 1,color)
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()
        
    def get_sentence(self):
        f = open('sentences.txt', encoding='utf-8-sig').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence
    
    def calculate_accuracy(self, screen):
        if(not self.end):
            round_percent = 0
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                    else:
                        self.errorList.append( c )
                except:
                    pass
            round_percent = count * 100 / len(self.word)
            self.accuracy.append(round_percent)
            
            
    def show_results(self, screen):
        self.accuracy = sum(self.accuracy) / len(self.accuracy)
            
        # alculate words per minute
        self.wpm = len(self.typed_chars)/(5 * self.total_time / 60)
        self.end = True
        # print(self.total_time)
        if len(self.errorList) > 0:
            freqError = statistics.mode(self.errorList)
        else:
            freqError = None
        self.results = f'Most frequent Error: {freqError} Accuracy: {round(self.accuracy)}% Wpm: {round(self.wpm)}'
        # draw icon image
        self.time_img = pygame.image.load('icon.png')
        self.time_img = pygame.transform.scale(self.time_img, (150,150))
            
        screen.blit(self.time_img, (self.w/2-75,self.h-140))
        self.draw_text(screen,"Reset", self.h - 70, 26, (100,100,100))
        print(self.results)
        pygame.display.update()
            
    def run(self):
        self.reset_game()
        self.running=True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0), (50,250,700,50))
            pygame.draw.rect(self.screen,self.theme_color, (50,250,700,50), 2)
            # update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26,(250,250,250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # position of input box
                    if(x>=50 and x<=700 and y>=250 and y<=300):
                        self.active = True
                        self.input_text = ''
                        self.start_time = time.time()
                     # position of reset box
                    if(x>=310 and x<=510 and y>=390 and self.end):
                        self.reset_game()
                        x,y = pygame.mouse.get_pos()
                        
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            #print(self.input_text)
                            self.typed_chars += self.input_text
                            self.lines += self.word
                            self.total_time += time.time() - self.start_time
                            self.calculate_accuracy(self.screen)
                            if self.total_time >= 60:
                                self.show_results(self.screen)
                                print(self.results)
                                self.draw_text(self.screen, self.results,350, 28, self.display_color)
                                self.end = True
                            else:
                                self.new_round()
                                self.active = True
                                self.input_text = ''
                                self.start_time = time.time()
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            
            pygame.display.update()
        clock.tick(60)
    
    def reset_game(self):
        self.screen.blit(self.open_img, (0,0))
        pygame.display.update()
        time.sleep(3)
        self.reset=False
        self.end = False
        self.input_text=''
        self.word = ''
        self.start_time = 0
        self.total_time = 0
        self.wpm = 0
        self.accuracy = []
        # Get random sentence
        self.word = self.get_sentence()
        if (not self.word):
            self.reset_game()
        #drawing heading
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        message = "Flash Type"
        subhead = "a fun typing speed analysis program"
        self.draw_text(self.screen, message, 80, 80,self.theme_color)
        self.draw_text(self.screen, subhead, 130, 28,self.theme_color)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,700,50), 2)
        # draw the sentence string
        self.draw_text(self.screen, self.word,200, 28,self.text_color)
        pygame.display.update()
        
    def new_round(self):
        self.input_text=''
        self.word = ''
        self.start_time = 0
        self.word = self.get_sentence()
        
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        
        message = "Flash Type"
        subhead = "a fun typing speed analysis program"
        self.draw_text(self.screen, message,80, 80,self.theme_color)
        self.draw_text(self.screen, subhead, 130, 28,self.theme_color)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,700,50), 2)
        # draw the sentence string
        self.draw_text(self.screen, self.word,200, 28,self.text_color)
        pygame.display.update()
        
game().run()
    
    
    
    
    
    
    
    
