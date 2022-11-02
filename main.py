import pygame,random
from pygame.locals import *

#Valor aleatorio da maça
def on_grid_random():
    x=random.randint(0,590)
    y=random.randint(0,590)
    return (x//10*10,y//10*10)

def collision(c1,c2):
    return (c1[0]==c2[0]) and (c1[1]==c2[1])

#Limite de tela
def off_limits(pos):
    if 0<= pos[0]<WINDOW_SIZE[0] and 0<=pos[1]<WINDOW_SIZE[1]:
        return False
    else:
        return True

#Restarta o jogo
def restart_game():
    global snake
    global apple_pos
    global my_direction
    global pontos
    snake = [(200, 200), (210, 200), (220, 200)]
    my_direction=LEFT
    apple_pos = on_grid_random()
    pontos=0

pause=False

#pausa o jogo
def pausar():
    pause=True
    while pause:
     clock.tick(10)

     for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
          if event.key == K_SPACE:
             global run
             pause=False
             run=True
    pygame.display.update()

#game over
def game_over(pontos):
    white = (255, 255, 255)
    display_surface = pygame.display.set_mode((WINDOW_SIZE))
    pygame.display.set_caption('Snake')
    text = fonte2.render((f"GAME OVER"), True, white)
    display_surface.blit(text,(400,150))
    text2 = fonte.render((f"Sua pontuação: {pontos}"), True, white)
    display_surface.blit(text2, (400, 350))
    pygame.display.update()
    pygame.time.wait(4000)
    restart_game()

clock2=pygame.time.Clock()

menu=True
while menu:
 pygame.init()
 WINDOW_SIZE2=(1360,768)
 screen3=pygame.display.set_mode((WINDOW_SIZE2))
 pygame.display.set_caption("Snake")
 clock2.tick(20)
 fonte3 = pygame.font.SysFont("arial", 50, bold=True, italic=True)
 text3 = fonte3.render((f"Pressione J para jogar."), True,(255,255,255))
 screen3.blit(text3,(400,350))
 for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_j:
                menu=False
                run=True

 pygame.display.update()

UP=0
RIGHT=1
DOWN=2
LEFT=3

pygame.init()
WINDOW_SIZE=(1360,768)
screen=pygame.display.set_mode((WINDOW_SIZE))
pygame.display.set_caption("Snake")

snake=[(200,200),(210,200),(220,200)]
snake_skin=pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos=on_grid_random()
apple=pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction=LEFT
clock=pygame.time.Clock()

pontos=0
fonte=pygame.font.SysFont("arial",40,bold=True,italic=True)
fonte2=pygame.font.SysFont("arial",70,bold=True,italic=True)

run=True
while run:

    clock.tick(20)

    mensagem=f"PONTOS:{pontos}"
    texto_formatado=fonte.render(mensagem,True,(255,255,255))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_s:
                pygame.quit()
                quit()
            if event.key == K_SPACE:
               pausar()

    if event.type==KEYDOWN:
        if event.key==K_UP:
            my_direction = UP
        if event.key==K_DOWN:
            my_direction = DOWN
        if event.key==K_LEFT:
            my_direction = LEFT
        if event.key==K_RIGHT:
            my_direction = RIGHT

    if collision(snake[0],apple_pos):
        apple_pos=on_grid_random()
        snake.append((0,0))
        pontos += 1

    if my_direction == UP:
        snake[0]=(snake[0][0],snake[0][1]-10)
    if my_direction == DOWN:
        snake[0]=(snake[0][0],snake[0][1]+10)
    if my_direction == RIGHT:
        snake[0]=(snake[0][0]+10,snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0]-10, snake[0][1])

    for i in range(len(snake)-1,0,-1):
        if collision(snake[0],snake[i]):
            game_over(pontos)
        snake[i]=(snake[i-1][0],snake[i-1][1])

    if off_limits(snake[0]):
        game_over(pontos)

    screen.fill((0,0,0))
    screen.blit(apple,apple_pos)
    screen.blit(texto_formatado,(1100,80))

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()