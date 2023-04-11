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