from threading import Thread
import subprocess
import datetime
import random as rand
import pygame
import math
from math import pi
import time
import maritestinggrounds
# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 650,650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Click and Drag Rectangle")

# Clock for controlling frame rate
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
#GAME CHARACTERS
# 0 = NEUTRAL
# 1 = FIRST ATTACK KICK
# 2 = SECOND ATTACK PUNCH
# 3 = DUCK

mario_poses = ["MarioNeutral.png","MarioFireball.png","MarioKick_Punch.png"]
luigi_poses = ["LuigiNeutral.png","LuigiKick.png","LuigiDuck.png"]
peach_poses = ["PeachNeutral.png","PeachPunch.png","PeachGold.png","PeachDuck.png"]
daisyposes = ["DaisyNeutral.png","DaisyKick.png","DaisyPunch.png"]
rosalinaposes = ["RosalineNeutral.png","RosalinaKick.png","RosalinaPunch.png","RosalineDuck.png"]
raccoon_poses = ["RaccoonNeutral.png","RaccoonKick.png","RaccoonPunch.png"]
other_poses = ["OtherNeutral.png","OtherKick.png","OtherPunch.png","OtherDuck.png"]
yoshi_poses = ["YoshiNeutral.png","YoshiKick.png","YoshiPunch.png","YoshiStare.png"]
toad_poses = ["ToadNeutral.png","ToadKick","ToadPunch"]
koopa_poses =["KoopaNeutral.png","KoopaKick.png","KoppaPunch.png"]
shy_poses = ["ShyNeutral.png","ShyKick.png","ShyPunch.png"]
lakitu_poses = ["LakituNeutral.png","LakituAtk.png","LakituSuper.png"]
toaddette_poses = ["ToddetteNeutral.png","ToaddetteKick.png","ToaddettePunch.png","ToaddetteLost.png"]
kingposes = ["BooNeutral.png","BooKick.png","BooPunch.png","BooLost.png","BooBaby.png"]
poseslist = [mario_poses,luigi_poses,peach_poses,daisyposes,rosalinaposes,raccoon_poses,other_poses,yoshi_poses,toad_poses,koopa_poses,shy_poses,lakitu_poses,toaddette_poses,kingposes]
class player():
    def __init__(self,health):
        self.health=health


mimage = pygame.image.load("marios.png")
bgscene = pygame.image.load("randobg.png")
scene1=True
scene2 = False
square_selector_x=125
square_selector_y=245
running = True
enterpress=False
player_choice_char = "Mario"
CPU_LISTERX = [125,182,239,296,353,410,467]
CPU_LISTERY=[245,325]
chartoplist=["Mario","Luigi","Princess Peach","Princess Daisy","Princess Rosalina","Raccoon Mario","Otro Princess"]
charbotlist=["Yoshi","Toad","Koopa","Shy Guy","Lakitu","Toaddette","King Boo"]
CPU_choice_char ="None"
CPU_choice_char2 ="None"

CPU_COUNTER=0
CPU_selector_x=125
CPU_selector_y=245
CPU_selector_x2=125
CPU_selector_y2=245
def cpcounter():
    global CPU_COUNTER
    global CPU_selector_x
    global CPU_selector_y
    global CPU_selector_x2
    global CPU_selector_y2
    while CPU_COUNTER<100:
        time.sleep(0.41)
        CPU_COUNTER+=1
        CPU_selector_x = CPU_LISTERX[rand.randint(0,6)]
        CPU_selector_y = CPU_LISTERY[rand.randint(0,1)]
        CPU_selector_x2 = CPU_LISTERX[rand.randint(0,6)]
        CPU_selector_y2 = CPU_LISTERY[rand.randint(0,1)]
def timerforscenes():
    time.sleep(2.5)
    global scene1
    global scene2
    scene1=False
    scene2 = True



while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT and scene1==True and enterpress==False:
                square_selector_x+=57
                if square_selector_x>=467:
                    square_selector_x=467
            if event.key==pygame.K_LEFT and scene1==True and enterpress==False:
                square_selector_x-=57
                if square_selector_x<=125:
                    square_selector_x=125
            if event.key==pygame.K_DOWN and scene1==True and enterpress==False:
                square_selector_y+=80
                if square_selector_y >= 325:
                    square_selector_y = 325
            if event.key==pygame.K_UP and scene1==True and enterpress==False:
                square_selector_y-=80
                if square_selector_y <= 245:
                    square_selector_y = 245
            if event.key==pygame.K_RETURN and scene1==True:
                enterpress=True
    screen.fill(BLACK)

    if scene1==True:
        screen.blit(mimage,(125,245))
        
        pygame.draw.rect(screen, BLUE, (square_selector_x,square_selector_y,60,80),3)  #Selecter rect Player
        #print(square_selector_y)
        #print(square_selector_x)

        instructions = font.render("Press Enter to confirm selection", True, WHITE)  # Text, anti-aliasing, color
        screen.blit(instructions, (145, 50))

        if square_selector_y == 245:
            player_choice_char = chartoplist[CPU_LISTERX.index(square_selector_x)]
        elif square_selector_y == 325:
            player_choice_char = charbotlist[CPU_LISTERX.index(square_selector_x)]
        player_chara = font.render(f"Your Choice Is: {player_choice_char}",True,WHITE)
        screen.blit(player_chara, (125, 450))
        Cpu_chara = font.render(f"CPU Choice Is: {CPU_choice_char}",True,WHITE)
        screen.blit(Cpu_chara, (125, 500))
        Cpu_chara2 = font.render(f"CPU Choice Is: {CPU_choice_char2}",True,WHITE)
        screen.blit(Cpu_chara2, (125, 550))

        if enterpress == True and scene1 == True:
            pygame.draw.rect(screen, RED, (CPU_selector_x,CPU_selector_y,60,80),3)  #Selecter rect Player
            pygame.draw.rect(screen, BLACK, (CPU_selector_x2,CPU_selector_y2,60,80),3)  #Selecter rect Player
            if CPU_selector_y == 245:
                CPU_choice_char = chartoplist[CPU_LISTERX.index(CPU_selector_x)]
            elif CPU_selector_y == 325:
                CPU_choice_char = charbotlist[CPU_LISTERX.index(CPU_selector_x)]
            if CPU_selector_y2 == 245:
                CPU_choice_char2 = chartoplist[CPU_LISTERX.index(CPU_selector_x2)]
            elif CPU_selector_y2 == 325:
                CPU_choice_char2 = charbotlist[CPU_LISTERX.index(CPU_selector_x2)]


            t1 = Thread(target=cpcounter)
            t1.start()
            if CPU_COUNTER >=170:
                t2=Thread(target=timerforscenes)
                t2.start()


    if scene2 == True:
        screen.blit(bgscene,(0,0))
        if square_selector_y == 245:
            pygame.draw.rect(screen, BLUE, (100,100,100,100),3)  #Selecter rect Player
            playercharacterloading = poseslist[CPU_LISTERX.index(square_selector_x)][0]
            characteraccimage = pygame.image.load(playercharacterloading)
            charactersaccimage = pygame.transform.scale(characteraccimage,(100,100))
        elif square_selector_y == 325:
            pygame.draw.rect(screen, BLUE, (100,100,100,100),3)  #Selecter rect Player
            playercharacterloading = poseslist[CPU_LISTERX.index(square_selector_x)+7][0]
            characteraccimage = pygame.image.load(playercharacterloading)
            charactersaccimage = pygame.transform.scale(characteraccimage,(100,100))

        screen.blit(charactersaccimage,(150,350))
        if CPU_selector_y == 245:
            CPUcharacterloading = poseslist[CPU_LISTERX.index(CPU_selector_x)][0]
            CPUcharacteraccimage = pygame.image.load(CPUcharacterloading)
            CPUcharactersaccimage = pygame.transform.scale(CPUcharacteraccimage,(100,100))
            CPUCHARSFIMAGE = pygame.transform.flip(CPUcharactersaccimage,True,False)

        elif CPU_selector_y == 325:
            CPUcharacterloading = poseslist[CPU_LISTERX.index(CPU_selector_x)+7][0]
            CPUcharacteraccimage = pygame.image.load(CPUcharacterloading)
            CPUcharactersaccimage = pygame.transform.scale(CPUcharacteraccimage,(100,100))
            CPUCHARSFIMAGE = pygame.transform.flip(CPUcharactersaccimage,True,False)
        screen.blit(CPUCHARSFIMAGE,(350,350))




    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()