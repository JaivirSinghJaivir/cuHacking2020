import pygame

pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Murder on the 2nd Floor")
fr = pygame.image.load("floor_rotated2.png")
clock = pygame.time.Clock()

def text_objects(text, font):
    ts = font.render(text, True, (0, 0, 0))
    return ts, ts.get_rect()

def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        if click[0] == 1:
            core()
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)

def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        win.fill((255, 255, 255))
        lt = pygame.font.Font('FreeSansBold.ttf', 55)
        TextSurf, TextRect = text_objects("Murder on the 2nd Floor", lt)
        TextRect.center = (400, 300)
        win.blit(TextSurf, TextRect)

        button('Start',150,450,100,50,(0,200,0),(0,255,0))
        button('Quit',550,450,100,50,(200,0,0),(255,0,0))

        pygame.display.update()
        clock.tick(15)

def core():
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
        clock.tick(60)


intro()
core()
pygame.quit()