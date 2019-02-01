import pygame
from alienobj import *
import threading

pygame.init()

count = 0
displayWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption('Alien invaders')
clock = pygame.time.Clock()

shuttle = pygame.image.load('transport.png')

running = True

player = playershut()

t = 0.0

bullslw = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullsfst = pygame.sprite.Group()

def alienspawn():

        al = alien()
        aliens.add(al)
        if running == True:
            threading.Timer(5.0,alienspawn).start()

alienspawn()

def countdown():

    for al in aliens:

        if al.timer == 1:
            al.timer = 0
            aliens.remove(al)
            del al
        else:
            al.timer = al.timer - 1
    if running == True:
            threading.Timer(1.0,countdown).start()

countdown()

while running:

    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == 276:
                count = count - 5
            elif event.key == 275:
                count = count + 5
            elif event.key == pygame.K_x:
                running = False
            elif event.key == pygame.K_g:

                bull = bulletfst(340 + count,425)
                bullslw.add(bull)

            elif event.key == pygame.K_h:

                bull = bulletslw(325 + count,425)
                bullsfst.add(bull)

    for bull in bullslw:
        bull.move()

    for bull in bullsfst:
        bull.move()

    slwcollisional = pygame.sprite.groupcollide(aliens,bullslw,False,False)
    slwcollisionbull = pygame.sprite.groupcollide(aliens,bullslw,True,True)

    for al in slwcollisional:
        al.timer = 0
        del al

    for bull in slwcollisionbull:
        del bull

    fstcollisional = pygame.sprite.groupcollide(aliens,bullsfst,False,False)
    fstcollisionbull = pygame.sprite.groupcollide(aliens,bullsfst,False,True)

    for al in fstcollisional:
        al.timer = al.timer + 5

    for bull in fstcollisionbull:
        del bull

    bullslw.draw(displayWindow)
    bullsfst.draw(displayWindow)
    aliens.draw(displayWindow)
    pygame.display.update()

    pressmv = pygame.key.get_pressed()

    if pressmv[pygame.K_LEFT]:
        count = count - 5
    elif pressmv[pygame.K_RIGHT]:
        count = count + 5

    if count <= -340:
        count = -340
    elif count >= 365:
        count = 365

    displayWindow.fill((0,0,255))
    displayWindow.blit(player.shuttle, (325 + count,450))
    clock.tick(60)

pygame.quit()
quit()
