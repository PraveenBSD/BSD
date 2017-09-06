import pygame
import time
import random
pygame.init()
display_width=600
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
max=0


gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock=pygame.time.Clock()

carimg=pygame.image.load('car1.png')
bgimg=pygame.image.load('road.png')
policeimg=pygame.image.load('police.png')
crashimg=pygame.image.load('car2.png')

pygame.display.set_icon(carimg)

def things_dodged(count):
    font=pygame.font.SysFont(None,50)
    text=font.render("score: "+str(count),True,white)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
##    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
    gameDisplay.blit(policeimg,(thingx,thingy))

def background(y):
    gameDisplay.blit(bgimg,(0,y))

def boom(x,y):
    gameDisplay.blit(crashimg,(x,y))

def car(x,y):
    gameDisplay.blit(carimg,(x,y))

def text_objects(text, font):
    textSurface=font.render(text,True,(213,32,12))
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',75)
    TextSurf,TextRect= text_objects(text,largeText)
    TextRect.center= ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update() 
    time.sleep(4)

    game_loop()

def crash():
    message_display('you crashed!')

def game_loop():
    x=(display_width*0.45)
    y= (display_height*0.6)
    bgy=0

    x_chng=0

    thing_stx=random.randrange(0,display_width)
    thing_sty=-600
    thing_speed=4
    thing_width=120
    thing_height=264
    dodged=0
    
    
    gameExit=False
    while not gameExit:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_chng=-5
                if event.key==pygame.K_RIGHT:
                    x_chng=5    
                if event.key==pygame.K_UP:
                    thing_speed=14
            
            
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_chng=0
                if event.key==pygame.K_UP:
                    thing_speed=5


            
                
                
                    
                
                    

                    

        
        x+=x_chng    
        gameDisplay.fill((0,0,255))
        background(bgy)

        things(thing_stx,thing_sty,thing_width,thing_height,(100,255,100))
        thing_sty+=thing_speed
     
        car(x,y)

        things_dodged(dodged) 

        if x> display_width-120 or x<0:
             crash()

        if thing_sty>display_height :
            thing_sty=0-thing_height
            thing_stx=random.randrange(0,display_width)
            dodged+=1
            if(dodged>5):
                thing_speed=6
            if(dodged>10):
                thing_speed=10
            
##            thing_width+=(dodged*1.2)

        if y< thing_sty+thing_height:
            
            if (x >thing_stx and x<(thing_stx+thing_width)) or (x+120>thing_stx and x+119<thing_stx+thing_width):
                boom(x-290,y-145)
                crash()
                
     
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()  
quit()
