import pygame
import random
x=pygame.init()
screen_x=600
gamewindow=pygame.display.set_mode((screen_x,screen_x))
pygame.display.set_caption("snake game")
def gameloop():
 exit_g=False
 game_o=False
 s_x=45
 s_y=55
 velocity_x=0
 velocity_y=0
 clock=pygame.time.Clock()
 white=(255,255,255)
 red=(255,0,0)
 black=(0,0,0)
 snake_size=30

 fps=30
 food_x=random.randint(20,screen_x-20)
 food_y=random.randint(20,screen_x+20)
 score=0
 font=pygame.font.SysFont(None,55)
 def textscreen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[int(x),int(y)])

 def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
         pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
 snk_list=[]
 snk_length=1
 while not exit_g:
    if game_o:
        gamewindow.fill(white)
        textscreen("game over!! ",red,screen_x/2-200,screen_x/2-200)
        textscreen("score:"+str(score*10),red,screen_x/2-200,screen_x/2-150)
        textscreen("press enter to restart",red,100,screen_x/2-100)
        for event in pygame.event.get():
         if event.type==pygame.QUIT:
            exit_g=True
         if event.type==pygame.KEYDOWN:
               if  event.key==pygame.K_RETURN:
                  gameloop()
    else:
     for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_g=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                   velocity_x=5
                   velocity_y=0
            if event.key==pygame.K_DOWN:
                velocity_x=0
                velocity_y=5
            if event.key==pygame.K_LEFT:
                velocity_x=-5
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_x=0
                velocity_y=-5
     s_x=s_x + velocity_x
     s_y=s_y + velocity_y
     if abs(s_x-food_x)<20 and abs(s_y-food_y)<20:
        score+=10
        food_x=random.randint(20,screen_x-20)
        food_y=random.randint(20,screen_x-20)
        snk_length+=5
            

     gamewindow.fill(black)
     pygame.draw.rect(gamewindow,white,[food_x,food_y,snake_size,snake_size])
     textscreen("score:"+str(score*10),red,50,10)
     head=[]
     head.append(s_x)
     head.append(s_y)
     snk_list.append(head)
     if len(snk_list)>snk_length:
        del snk_list[0]
     
     if head in snk_list[:-1]:
         game_o=True
     if(s_x<0 or s_x>screen_x or s_y<0 or s_y>screen_x):
        game_o=True
     
     plot_snake(gamewindow,red,snk_list,snake_size) 
    pygame.display.update()
    clock.tick(fps)
 pygame.quit()
 quit()
gameloop()
