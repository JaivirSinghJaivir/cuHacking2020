import pygame
import json
# import action
import csv

def create_location(d):
    location

pygame.init()

with open("dataset.json", 'r') as f:
    d = json.load(f)

eugene_list = []
eugene_position = 0

with open("location_data.json", 'r') as f2:
    location_data = json.load(f2)
   

for i in d.keys():
    if d[i]["guest-id"] == "Eugene": 
        #add to list
        eugene_list.append(d[i])

# print(eugene_list)

win = pygame.display.set_mode((1080,600))
pygame.display.set_caption("First Game")
fr = pygame.image.load("floor_rotated2.png")
fr = pygame.transform.scale(fr, (1080, 600))

x = 50
y = 50
width = 20
height = 20
val = 5

run = True

# list = {}

while run:
    # if (eugene_position > eugene_list.len()):
    #     print("finished")
    
    win.fill((0,0,0))
    win.blit(fr, (0,0))
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= val

    if keys[pygame.K_RIGHT]:
        x += val

    if keys[pygame.K_UP]:
        y -= val

    if keys[pygame.K_DOWN]:
        y += val

    for location in location_data:
        if (location["device-id"] == eugene_list[eugene_position]["device-id"]):
            print(location["device-id"])
            if (x < location["x"]):
                x += val
            elif (x > location["x"]):
                x -= val
            elif (y < location["y"]):
                y += val 
            elif (y > location["y"]):
                y -= val
            else:
                eugene_position += 1
        # print(location["device-id"])
        # print(eugene_list[eugene_position]["device-id"])
        # print("ff")

    
    
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()