import pygame, time, sys
from pygame.locals import *
import random

class game:
    def __init__(self):
        self.width=900
        self.height=520
        self.reset=True
        self.active = False
        self.end = False
        
        self.input_text=''
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
        self.open_img = pygame.image.load('type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.width,self.height))
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Flash Type')
    
    def write(self, screen, message, y ,font_size, color):
        font = pygame.font.SysFont(None, font_size)
        text = font.render(message, 1,color)
        text_rect = text.get_rect(center=(self.width/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()
    
    def write_heading(self, screen, message, y ,font_size, color):
        font = pygame.font.SysFont("monospace", font_size)
        text = font.render(message, 1,color)
        text_rect = text.get_rect(center=(self.width/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()
        
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

    def get_sentence(self):
        f = open(random.choice(self.books), encoding='utf-8-sig').read()
        text = self.prepare_text(f)
        
        new = []
        l = []
        i = 0
        new = list(map(str, text.split()))
        while i < 10:
            l += [random.choice(new)]
            i += 1
        l = ' '.join(l) 
        return l
    
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
    
    def mode(self,array):
        most = max(list(map(array.count, array)))
        
        return list(set(filter(lambda x: array.count(x) == most, array)))
            
    def show_results(self, screen):
        self.accuracy = sum(self.accuracy) / len(self.accuracy)
            
        # alculate words per minute
        self.wpm = len(self.typed_chars)/(5 * self.total_time / 60)
        self.end = True
        # print(self.total_time)
        if len(self.errorList) > 0:
            freqError = self.mode(self.errorList)[0]
            if freqError == ' ':
                freqError = 'space'
        else:
            freqError = None
        self.results = f'''Most frequent Error: {freqError}      Accuracy: {round(self.accuracy,2)}%      WPM: {round(self.wpm)}'''
        # draw icon image
        self.time_img = pygame.image.load('icon.png')
        self.time_img = pygame.transform.scale(self.time_img, (150,150))
            
        screen.blit(self.time_img, (self.width/2-75,self.height-140))
        self.write(screen,"Reset", self.height - 70, 26, (100,100,100))
        # print(self.results)
        pygame.display.update()
            
    def main(self):
        self.reset_game()
        self.running=True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0), (50,250,800,50))
            # format: pygame.draw.rect(screen, color, (x,y,width,height), thickness)
            pygame.draw.rect(self.screen,self.theme_color, (50,250,800,50), 2)
            # update the text of user input
            self.write(self.screen, self.input_text, 274, 27,(255,255,255))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # position of input box
                    if(x>=50 and x<=800 and y>=250 and y<=300):
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
                                self.write(self.screen, self.results,350, 28, self.display_color)
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
        time.sleep(2.5)
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
        subhead = "- a typing speed test -"
        self.write_heading(self.screen, message, 80, 80,self.theme_color)
        self.write_heading(self.screen, subhead, 140, 22,self.theme_color)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,800,50), 2)
        # draw the sentence string
        self.write(self.screen, self.word,220, 35,self.text_color)
        pygame.display.update()
        
    def new_round(self):
        self.input_text=''
        self.word = ''
        self.start_time = 0
        self.word = self.get_sentence()
        
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        
        message = "Flash Type"
        subhead = "- a typing speed test -"
        self.write_heading(self.screen, message, 80, 80,self.theme_color)
        self.write_heading(self.screen, subhead, 140, 22,self.theme_color)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,800,50), 2)
        # draw the sentence string
        self.write(self.screen, self.word,220, 35,self.text_color)
        pygame.display.update()
        
game().main()
    
    
    
    
    
    
    
    
