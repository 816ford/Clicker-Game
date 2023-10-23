import pygame
import sys


pygame.init()
main_clock = pygame.time.Clock()
height = 720
width = 1280
SCREEN = pygame.display.set_mode((width, height))
BG = pygame.image.load("background.jpg")
BG = pygame.transform.scale(BG, (width, height))
oj_button = pygame.image.load("Oj.png")



def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        pygame.display.set_caption("Main Menu")
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        MENU_TEXT = MENU_TEXT.render("Save Christmas!", True, "white")
        MENU_TEXT_RECT = MENU_TEXT.get_rect()
        MENU_TEXT_RECT.center = (width/2, 100)
        
        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)

        oj_button_rect = oj_button.get_rect()
        oj_button_rect.center = (width/2, height/2)
        SCREEN.blit(oj_button, oj_button_rect)

        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if oj_button_rect.collidepoint(MENU_MOUSE_POS):
                    play()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions()
                
        
        pygame.display.update()



        



def play():
    pygame.display.set_caption("Play")
    while True:
        SCREEN.fill("black")
        oj_button_rect = oj_button.get_rect()
        oj_button_rect.center = (width/2, height/2)
        SCREEN.blit(oj_button, oj_button_rect)
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if oj_button_rect.collidepoint(GAME_MOUSE_POS):
                    instructions()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions()
        
        
        pygame.display.update()

        

def instructions():
    
    pygame.display.set_caption("Instructions")
    while True:
        SCREEN.fill("black")
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
        pygame.display.update()
main_menu()
