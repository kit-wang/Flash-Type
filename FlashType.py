import pygame, time, sys
from pygame.locals import *
import random

class game:
    def __init__(self):
        self.width = 900
        self.height = 520
        self.reset = True
        self.active = False
        self.end = False
        
        self.input_line=''
        self.word = ''
        self.lines = ''
        self.typed_chars = ''
        self.start_time = 0
        self.total_time = 0
        self.wpm = 0
        
        
        self.accuracy = []
        self.errorList = []
        self.books = ['alice.txt', 'frankenstein.txt', 'dubliners.txt']
        
        # rgb color codes for text
        self.theme_color = (251,210,215)
        self.text_color = (220,208,255)
        self.display_color = (252,76,78)
        
        pygame.init()
        
        # loading the landing and background imgs
        self.load_img = pygame.image.load('loading-page.png')
        self.load_img = pygame.transform.scale(self.load_img, (self.width,self.height))
        self.background = pygame.image.load('background.jpg')
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Flash Type')
    
    # method for writing a line of text on screen
    def write(self, screen, message, ycor ,font_size, color):
        font = pygame.font.SysFont(None, font_size)
        text = font.render(message, 1, color)
        text_rect = text.get_rect(center=(self.width/2, ycor))
        screen.blit(text, text_rect)
        pygame.display.update()
        
    # methtod for different font text on screen
    def write_heading(self, screen, message, y ,font_size, color):
        font = pygame.font.SysFont("monospace", font_size)
        text = font.render(message, 1,color)
        text_rect = text.get_rect(center=(self.width/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()
        
    # prepares raw book text
    def prepare_text(self, book):
        t = str(book)
        start = t.find('***') + 3
        d = t[start:]
        start1 = d.find('***') + 3
        end = d.find('*** END OF THE PROJECT')
        t = d[start1:end]
        
        s = t.split()
        s = ' '.join(s)
        final = ""
        
        for letter in s:
            if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z') or letter == " ":
                final += letter
        return final
    
    # generates a sentence from prepared text
    def get_sentence(self):
        f = open(random.choice(self.books), encoding='utf-8-sig').read()
        text = self.prepare_text(f)
        
        new = []
        l = []
        i = 0
        new = list(map(str, text.split()))
        while i < 8:
            l += [random.choice(new)]
            i += 1
        l = ' '.join(l) 
        return l
    
    # computes accuracy at the end of each round
    def calculate_accuracy(self, screen):
        if(not self.end):
            round_percent = 0
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_line[i] == c:
                        count += 1
                    else:
                        self.errorList.append( c )
                except:
                    pass
            round_percent = count * 100 / len(self.word)
            self.accuracy.append(round_percent)
    
    # calculates the mode from a list
    def mode(self,array):
        most = max(list(map(array.count, array)))
        
        return list(set(filter(lambda x: array.count(x) == most, array)))
            
    # display results
    def display_results(self, screen):
        self.accuracy = sum(self.accuracy) / len(self.accuracy)
            
        # compute words per minute
        self.wpm = len(self.typed_chars)/(4.7 * self.total_time / 60)
        self.end = True
        # print(self.total_time)
        # determines mode of errorList
        if len(self.errorList) > 0:
            freqError = self.mode(self.errorList)[0]
            # case with space
            if freqError == ' ':
                freqError = 'space'
        else:
            # no error case
            freqError = None
        self.results = f'''Most frequent Error: {freqError}      Accuracy: {round(self.accuracy,2)}%      WPM: {round(self.wpm)}'''
        # load keyboard icon for reset
        self.time_img = pygame.image.load('icon.png')
        self.time_img = pygame.transform.scale(self.time_img, (160,160))
            
        screen.blit(self.time_img, (self.width/2 - 80,self.height - 170))
        self.write(screen,"RESET", self.height - 60, 25, (255,255,255))
        # print(self.results)
        pygame.display.update()
            
    # main method for running of the program
    def main(self):
        self.reset_game()
        self.running=True
        
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0), (50,250,800,50))
            # format: pygame.draw.rect(screen, color, (x,y,width,height), thickness)
            pygame.draw.rect(self.screen,self.theme_color, (50,250,800,50), 2)
            # update the user's input text
            self.write(self.screen, self.input_line, 274, 28,(255,255,255))
            pygame.display.update()
            
            for event in pygame.event.get():
                # three general possible events
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # range of the input box
                    if(x >= 50 and x <= 800 and y >= 250 and y <= 300):
                        self.active = True
                        self.input_line = ''
                        self.start_time = time.time()
                     # range of reset box
                    if(x >= 300 and x <= 520 and y >= 395 and self.end):
                        self.reset_game()
                        x,y = pygame.mouse.get_pos()
                        
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        # this checks for an enter key & loads new line
                        if event.key == pygame.K_RETURN:
                            # print(self.input_line)
                            self.typed_chars += self.input_line
                            self.lines += self.word
                            self.total_time += time.time() - self.start_time
                            self.calculate_accuracy(self.screen)
                            # ends the round after ~60 secs
                            if self.total_time >= 60:
                                self.display_results(self.screen)
                                print(self.results)
                                self.write(self.screen, self.results, 350, 30, self.display_color)
                                self.end = True
                            # initiates new round
                            else:
                                self.new_round()
                                self.active = True
                                self.input_line = ''
                                self.start_time = time.time()
                        # accounts for if user deletes a char
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_line = self.input_line[:-1]
                        else:
                            try:
                                self.input_line += event.unicode
                            except:
                                pass
            
            pygame.display.update()
        # conducted in ticks
        clock.tick(60)
    
    def reset_game(self):
        self.screen.blit(self.load_img, (0,0))
        pygame.display.update()
        
        time.sleep(2.5)
        self.reset=False
        self.end = False
        self.input_line=''
        self.word = ''
        self.start_time = 0
        self.total_time = 0
        self.wpm = 0
        self.accuracy = []
        
        # gets random sentence
        self.word = self.get_sentence()
        if (not self.word):
            self.reset_game()
        #writing heading
        self.screen.fill((0,0,0))
        self.screen.blit(self.background,(0,0))
        message = "Flash Type"
        subhead = "- a typing speed test -"
        self.write_heading(self.screen, message, 80, 80,self.theme_color)
        self.write_heading(self.screen, subhead, 140, 22,self.theme_color)
        # draws the input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,800,50), 2)
        # writes the line of sentence string
        self.write(self.screen, self.word,220, 35,self.text_color)
        pygame.display.update()
        
    def new_round(self):
        self.input_line=''
        self.word = ''
        self.start_time = 0
        self.word = self.get_sentence()
        
        self.screen.fill((0,0,0))
        self.screen.blit(self.background,(0,0))
        
        message = "Flash Type"
        subhead = "- a typing speed test -"
        self.write_heading(self.screen, message, 80, 80,self.theme_color)
        self.write_heading(self.screen, subhead, 140, 22,self.theme_color)
        # draw the input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,800,50), 2)
        # draw the sentence string
        self.write(self.screen, self.word,220, 35,self.text_color)
        pygame.display.update()
        
game().main()
    
    
    
    
    
    
    
    
