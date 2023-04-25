import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0,0,200))
pygame.display.set_caption("Esimene aken")


lill4=pygame.Rect(300,50,100,100)
pygame.draw.ellipse(ekraani_pind,(250,250,250),lill4)
lill3=pygame.Rect(400,60,100,100)
pygame.draw.ellipse(ekraani_pind,(250,250,250),lill3)
lill2=pygame.Rect(440,150,100,100)
pygame.draw.ellipse(ekraani_pind,(250,250,250),lill2)
ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0,255,0),ristkülik)
jaig=pygame.Rect(310,200,30,200)
pygame.draw.rect(ekraani_pind,(50,205,0),jaig)
lill=pygame.Rect(200,100,280,200)
pygame.draw.ellipse(ekraani_pind,(255,0,255),lill)
kaka1=pygame.Rect(400,140,50,50)
pygame.draw.rect(ekraani_pind,(100,200,23),kaka1)
kaka2=pygame.Rect(240,140,50,50)
pygame.draw.rect(ekraani_pind,(100,200,23),kaka2)

pilt=pygame.image.load("snail.png")
ekraani_pind.blit(pilt,(300,50))

font=pygame.font.SysFont("Broadway",40)
sõnad="Tere tulemast!"
värv=[200,200,200]
teksti_lisamine=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisamine,(150,30))


pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: #функцмя для кнопки "выход" (крест)
        break
pygame.quit()


#--------
import pygame, random
pygame.init()

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Surface")
screen.fill(lBlue)
clock = pygame.time.Clock()
posX, posY = 0, 0
speedX, speedY = 3, 4

player = pygame.Rect(posX, posY, 120, 120)
playerImage = pygame.image.load("22.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

enemies = []
for i in range(5):
    enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0,screenY - 100), 60, 73))
enemyImage = pygame.image.load("666.png")
enemyImage = pygame.transform.scale(enemyImage, [enemies[0].width, enemies[0].height])

enemyCounter = 0
totalEnemies = 20
score = 0

gameover = False
while not gameover:
    clock.tick(60)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    player = pygame.Rect(posX, posY, 120, 140)
    screen.blit(playerImage,player)

    posX += speedX
    posY += speedY

    if posX > screenX-playerImage.get_rect().width or posX <0:
        speedX = -speedX

    if posY > screenY-playerImage.get_rect().width or posY <0:
        speedY = -speedY
    enemyCounter += 1
    if enemyCounter >= totalEnemies:
        enemyCounter = 0
        enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1

    for enemy in enemies:
        screen.blit(enemyImage, enemy)

    pygame.display.flip()
    screen.fill(blue)

    print(score)
    if score == 20:
        gameover = True
pygame.quit()
