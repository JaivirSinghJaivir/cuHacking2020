import pygame
import json
import csv

pygame.init()

win = pygame.display.set_mode((1080, 600))
pygame.display.set_caption("Murder on the 2nd Floor")
fr = pygame.image.load("floor_rotated2.png")
fr = pygame.transform.scale(fr, (1080, 600))
clock = pygame.time.Clock()
names = []

# def create_event_list(d: dict):

def get_names():
    return names()

def create_event_by_person(guest_id: str, d: dict) -> list:
    person_list = []
    for i in d.keys():
        if d[i]["guest-id"] == guest_id:
            person_list.append(d[i])
    return person_list

def load_data(filename: str) -> dict:
    with open(filename, 'r') as f:
        d = json.load(f)
    return d

def location_list(people: list, dataset: dict) -> list:
    mega_list = []
    for person in people:
        mega_list.append(create_event_by_person(person, dataset))
    return mega_list

def mssg(m, ft, x, y):
    TextSurf, TextRect = text_objects(m, ft)
    TextRect.center = (x, y)
    win.blit(TextSurf, TextRect)

def text_objects(text, font):
    ts = font.render(text, True, (0, 0, 0))
    return ts, ts.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))
        if click[0] == 1:
            if action != None:
                if action == 'start':
                    core()
                elif action == 'quit':
                    pygame.quit()
                    quit()
                elif action == 'cs':
                    char_selection()
                elif action == 'sel':
                    pygame.draw.rect(win, ac, (x, y, w, h))
                    names.append(msg) if msg not in names else names.remove(msg)
                elif action == 'back':
                    names.append(msg) if msg not in names else names.remove(msg)
                    intro()
    else:
        pygame.draw.rect(win, ic, (x, y, w, h))
    mssg(msg, pygame.font.Font("freesansbold.ttf", 20), x+(w/2), y+(h/2))


def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.fill((255, 255, 255))
        mssg('Murder on the 2nd Floor', pygame.font.Font('FreeSansBold.ttf', 75), 540, 200)

        button('Start', 150, 450, 100, 50, (0, 200, 0), (0, 255, 0), 'cs')
        button('Quit', 830, 450, 100, 50, (200, 0, 0), (255, 0, 0), 'quit')

        pygame.display.update()
        clock.tick(15)

def char_selection():
    selected_names = []
    cs = True
    while cs:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.fill((255, 255, 255))
        mssg('Select one or more people to follow', pygame.font.Font("freesansbold.ttf", 30), 540, 50)

        button('Veronica', 100, 250, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Jason', 250, 250, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Thomas', 400, 250, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Eugene', 550, 250, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Salina', 700, 250, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Rob', 850, 250, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Kristina', 100, 400, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Alok', 250, 400, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Marc-Andre', 400, 400, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Dave', 550, 400, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('James', 700, 400, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')
        button('Harrison', 850, 400, 100, 50, (170, 170, 0), (255, 255, 0), 'sel')

        button('Done', 875, 500, 100, 50, (170, 170, 0), (255, 255, 0), 'start')

        pygame.display.update()
        clock.tick(15)


def core():
    dataset = load_data("dataset.json")
    location_data = load_data("location_data.json")

    x = location_data[0]["x"]
    y = location_data[0]["y"]
    width = 20
    height = 20
    val = 5
    run = True

    p_position = 0
    l_position = 0

    p_list = location_list(["Eugene", "Veronica"], dataset)

    flag = True
    color = (255, 0, 0)

    while run:
        win.fill((0, 0, 0))
        win.blit(fr, (0, 0))
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        pygame.display.update()
        clock.tick(60)

        if flag == True:
            for location in location_data:
                
                if (location["device-id"] == p_list[p_position][l_position]["device-id"]):
                    x = location["x"]
                    y = location["y"]
                    l_position += 1
                    break
                    # pygame.time.delay(100)

            #next person
            if l_position >= len(p_list[p_position]):
                p_position += 1
                l_position = 0
                #code here the new color
                color = (255, 255, 0)
            #no more people
            if p_position == len(p_list): 
                flag = False

        pygame.draw.rect(win, color, (x, y, width, height))

        button('Back', 875, 500, 100, 50, (170, 170, 0), (255, 255, 0), 'back')
        pygame.display.update()


intro()
core()
pygame.quit()
quit()