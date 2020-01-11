import pygame
pygame.init()

win = pygame.display.set_mode((800,600))
fr = pygame.image.load("floor_rotated.png")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    win.fill((0,0,0))
    win.blit(fr, (0,0))
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()