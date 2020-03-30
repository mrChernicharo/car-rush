import os
import pygame
from pygame import image
from random import randint


BLACK = (0, 0, 0)
WHITE = (255,255,255)

pygame.init()

x = 365
y = 300
velocidade = 10

screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

bg_y = -400

count = 0
life = 100

#coordenadas dos bots 
pos_x = 490 #polícia
pos_x_a = 370 # carrinho verde
pos_x_b = 150 #ambulancia
pos_x_c = 250 #pickup

pos_y = 700
pos_y_a = 800
pos_y_b = 1000
pos_y_c = 900

velocidade_bots = 14

timer = 0
tempo_segundo = 0

fonte = pygame.font.SysFont('arial black', 30 ) #procurar fonte no sistema sysFont('fonte', tamanho)
fonte_grd = pygame.font.SysFont('arial black', 50, bold=True, italic=False)

texto = fonte.render('Tempo | 0  ' , True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (60, 50)

texto2 = fonte.render('Carro | 100  ' , True, (255,255,255), (0,0,0))
pos_texto2 = texto2.get_rect()
pos_texto2.center = (65, 90)


game_over = fonte_grd.render(' FIM DE JOGO ' , True, (255,255,255), (0,0,0))
pos_texto3 = game_over.get_rect()
pos_texto3.center = (400, 200)

pygame.display.set_caption('Car Rush')

fundo = pygame.image.load('fundo.jpg')
carro = pygame.image.load('carrinho_amarelo3.png')

#carregando outros carrinhos

policia = pygame.image.load('carrinho_police.png')
carrinho_verde = pygame.image.load('carrinho_verde.png')
ambulancia = pygame.image.load('ambulancia.png')
pickup = pygame.image.load('carrinho_pickup.png')



#surface = pygame.Surface((100, 100))
clock = pygame.time.Clock()

running = True

while running:
    bg_y +=18
    pygame.time.delay(10)
    
    for event in pygame.event.get(): 
        if life <= 0:
            pygame.time.delay(3000)
            pygame.quit()
        if event.type == pygame.QUIT: 
            running = False

    comandos = pygame.key.get_pressed()
    if (comandos[pygame.K_UP] | comandos[pygame.K_w]) and y >= -70 :
        y -= velocidade
    if comandos[pygame.K_DOWN] | comandos[pygame.K_s] and y <= 530 :
        y += velocidade
    if comandos[pygame.K_RIGHT] | comandos[pygame.K_d] and x <= 490:
        x += velocidade
    if comandos[pygame.K_LEFT] | comandos[pygame.K_a] and x >= 120:
        x -= velocidade            
    
    
    # detecção de colisões

    #carro de polícia
    if (x + 65 > pos_x and y + 130 > pos_y and y < pos_y +130):
        print(('colisão com a polícia! {0}').format(count) )
        count += 1 
        if life > 0:
            life -= 3

    #carrinho verde
    if (x + 65 > pos_x_a and x < pos_x_a + 65 and y + 130 > pos_y_a and y < pos_y_a +130):
        print(('colisão com o carro verde! {0}').format(count) )
        count += 1 
        if life > 0:
            life -= 2       
    
    #ambulância
    if (x < pos_x_b + 65 and y + 130 > pos_y_b and y < pos_y_b + 130):        
        print(('colisão com a ambulância! {0}').format(count) )
        count += 1    
        if life > 0: 
            life -= 4

    #pickup
    if (x + 65 > pos_x_c and x < pos_x_c + 65 and y + 130 > pos_y_c and y < pos_y_c + 130): 
        print(('colisão com a pickup! {0}').format(count) )
        count += 1
        if life > 0:   
            life -= 2  


    pos_y -= velocidade_bots  #policia
    pos_y_a -= velocidade_bots + 2  #carrinho verde   
    pos_y_b -= velocidade_bots - 1   #ambulancia
    pos_y_c -= velocidade_bots + 3   #pickup   
       

    if (pos_y <= -820):
        pos_y = randint(700, 1400)
    if (pos_y_a <= -820):
        pos_y_a = randint(700, 1800)
    if (pos_y_b <= -820):
        pos_y_b = randint(700, 1000) 
    if (pos_y_c <= -820):
        pos_y_c = randint(1500, 2200)        

    if (timer < 30):  
        timer += 1 
    else:
        tempo_segundo += 1
        texto = fonte.render('Tempo | ' + str(tempo_segundo) +' ', True, (255,255,255), (0,0,0))
        timer = 0

    texto2 = fonte.render('Carro | ' + str(life) + ' ' , True, (255,255,255), (0,0,0))
    


    #screen.fill(BLACK)
    if bg_y >= 0:
        bg_y = -340

    screen.blit(fundo,(0, bg_y))
    screen.blit(carro, (x,y))
    screen.blit(policia, (pos_x, pos_y))
    screen.blit(carrinho_verde, (pos_x_a, pos_y_a))
    screen.blit(ambulancia, (pos_x_b , pos_y_b))
    screen.blit(pickup, (pos_x_c , pos_y_c))
    screen.blit(texto, pos_texto)
    screen.blit(texto2, pos_texto2) 

    print(pos_y_a)
    print(pos_y)

    if (life <= 0):
        screen.blit(game_over, pos_texto3) 
      

    #pygame.draw.circle(screen, (0, 255, 0), (x, y), 30)
    pygame.display.update()
 

pygame.quit()
