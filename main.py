import pygame
from  fighter import  Fighter
# import sys
# from pygame.locals import *


pygame.init()

# creating gamae windows
screen_width = 1000
screen_height =600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("himanshu's brawler")

clock = pygame.time.Clock()
fps =60
# color defined
yellow=(255,255,0)
red=(255,0,0)
white=(255,255,255)
black =(0,0,0)

# game varible
intro_count =3
last_update_time = pygame.time.get_ticks()
score =[0,0]
round_over =False
round_over_cooldown = 2000


# size of pic
warrior_size = 162
warrior_scale = 4
warrior_offset=[72,56]
warrior_data=[warrior_size,warrior_scale,warrior_offset]
wizard_size = 250
wizard_scale = 3
wizard_offset=[112,107]
wizard_data =[wizard_size,wizard_scale,wizard_offset]
#  load background images
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

# load main images
warrior_sheet =pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet =pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()


# game sound

mmusic = pygame.mixer.Sound("assets/audio/music.mp3")
magic = pygame.mixer.Sound("assets/audio/magic.wav")
sword = pygame.mixer.Sound("assets/audio/sword.wav")


# no. of steps in animation
warrior_animation_steps = [10,8,1,7,7,3,7]
wizard_animation_steps = [8,8,1,8,8,3,7]

# victory png
victory_img = pygame.image.load('assets/images/icons/victory.png').convert_alpha()

# define font
count_font = pygame.font.Font('assets/fonts/turok.ttf',80)
score_font = pygame.font.Font('assets/fonts/turok.ttf',30)

# drwning a imgaegs
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))


#  creating function for background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(screen_width,screen_height))
    screen.blit(scaled_bg,(0,0))

#  health bars
def draw_health_bar(health,x,y):
    ratio = health / 100
    pygame.draw.rect(screen,black,(x-2,y-2,404,34))
    pygame.draw.rect(screen,red,(x,y,400,30))
    pygame.draw.rect(screen,yellow,(x,y,400*ratio,30))

#      creating two instance for char
fighter_1 = Fighter(1,200,310,False,warrior_data,warrior_sheet,warrior_animation_steps,sword)
fighter_2 = Fighter(2,700,310,True,wizard_data,wizard_sheet,wizard_animation_steps,magic)



# game loop
run = True
while run:
    clock.tick(fps)

    # background loader
    draw_bg()
    # mmusic.play(-1,0,5000)
     # health bars

    draw_health_bar(fighter_1.health,20,20)
    draw_health_bar(fighter_2.health,580,20)
    draw_text("P1 : " + str(score[0]), score_font,red ,20,60)
    draw_text("P2 : " + str(score[1]), score_font,red ,580,60)

    if intro_count <=0:
        # move fighters
        fighter_1.move(screen_width, screen_height, screen, fighter_2,round_over,sword)
        fighter_2.move(screen_width, screen_height, screen, fighter_1,round_over,magic)
    else:
        draw_text(str(intro_count),count_font,black,screen_width/2,screen_height/3)
        if (pygame.time.get_ticks() - last_update_time >=1000):
            intro_count -= 1
            last_update_time = pygame.time.get_ticks()
            print(intro_count)



     # updating their action
    fighter_1.update()
    fighter_2.update()

     # two fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    if round_over == False:
        if fighter_1.alive ==False:
            score[1] +=1
            round_over =True
            round_over_time = pygame.time.get_ticks()

        elif fighter_2.alive ==False:
            score[0] +=1
            round_over =True
            round_over_time = pygame.time.get_ticks()
            # print(score)
    else:
        screen.blit(victory_img ,(320,150))
        # screen.blit(screen,"HIAMNSHU" ,(380,150))

        if pygame.time.get_ticks() - round_over_time >= round_over_cooldown:
            round_over =False
            intro_count = 3
            fighter_1 = Fighter(1, 200, 310, False, warrior_data, warrior_sheet, warrior_animation_steps,sword)
            fighter_2 = Fighter(2, 700, 310, True, wizard_data, wizard_sheet, wizard_animation_steps,magic)

    # event handles like quiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

# exiting the code
pygame.quit()
