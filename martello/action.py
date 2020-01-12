import pygame
from math import *


class action:
    def __init__(self):
        pass


    def activity(self,Colour,ID_w,ID_h,FP_w,FP_h,Action_Str,Screen):
# FP_w => Final Participant Width Across the Screen
# FP_h => Final Participant Height Across the Screen
# ID_w => Inital Determinant Width Across the Screen
# ID_h => Initial Determinant Height Across the Screen
        angd = atan(-(FP_h-ID_h)/(FP_w-ID_w)) # Angled Difference Between the Inital and Final

        high = round((FP_h-ID_h)/8)
        wide = round((FP_w-ID_w)/8)


        if Action_Str == "new client": # This happens when an access point and identified user connect
            # Signal Surrounding the Initial
            pygame.draw.arc(Screen,Colour,[ID_w-12,ID_h-12,24,24],angd-3*pi/9,angd+3*pi/9,2)
            pygame.draw.arc(Screen,Colour,[ID_w-16,ID_h-16,32,32],angd-3*pi/9,angd+3*pi/9,2)
            pygame.draw.arc(Screen,Colour,[ID_w-20,ID_h-20,40,40],angd-3*pi/9,angd+3*pi/9,2)
            # Signal Surrounding the Final
            pygame.draw.arc(Screen,Colour,[FP_w-12,FP_h-12,24,24],pi+angd-3*pi/9,pi+angd+3*pi/9,2)
            pygame.draw.arc(Screen,Colour,[FP_w-16,FP_h-16,32,32],pi+angd-3*pi/9,pi+angd+3*pi/9,2)
            pygame.draw.arc(Screen,Colour,[FP_w-20,FP_h-20,40,40],pi+angd-3*pi/9,pi+angd+3*pi/9,2)

        elif Action_Str == "unlocked no keycard": # This happens when someone opens the door without a keycard
            # Key Image Surrounding the Door
            pygame.draw.arc(Screen,Colour,[FP_w-18,FP_h-8,16,16],0,2*pi,4)
            pygame.draw.line(Screen,Colour,[FP_w-4,FP_h],[FP_w+10,FP_h],3)
            pygame.draw.line(Screen,Colour,[FP_w+4,FP_h],[FP_w+4,FP_h+4],3)
            pygame.draw.line(Screen,Colour,[FP_w+8,FP_h],[FP_w+8,FP_h+4],3)
            # Line Through the Surrounding Key
            pygame.draw.line(Screen,(255,0,0),[FP_w+10,FP_h+25],[FP_w-10,FP_h+9],3)
            pygame.draw.line(Screen,(255,0,0),[FP_w+10,FP_h+9],[FP_w-10,FP_h+25],3)
            # Line Between the Door and Person
            pygame.draw.line(Screen,Colour,[FP_w-wide,FP_h-high],[ID_w+wide,ID_h+high],4)

        elif Action_Str == "door closed": # This happens when someone opens the door
            # Closed Door Icon
            pygame.draw.rect(Screen,Colour,[FP_w-12,FP_h-20,24,40],2)
            pygame.draw.polygon(Screen,Colour,[[FP_w-6,FP_h-16],[FP_w+12,FP_h-20],[FP_w+12,FP_h+20],[FP_w-6,FP_h+24]])
            # Line Between the Door and Person
            pygame.draw.line(Screen,Colour,[FP_w-wide,FP_h-high],[ID_w+wide,ID_h+high],4)

        elif Action_Str == "successful keycard unlock": # This happens when someone opens the door with a keycard
            # Key Icon over Door
            pygame.draw.arc(Screen,Colour,[FP_w-18,FP_h-8,16,16],0,2*pi,4)
            pygame.draw.arc(Screen,Colour,[FP_w-10,FP_h,6,6],pi,2*pi,2)
            pygame.draw.line(Screen,Colour,[FP_w-4,FP_h],[FP_w+10,FP_h],4)
            pygame.draw.line(Screen,Colour,[FP_w+4,FP_h],[FP_w+4,FP_h+4],4)
            pygame.draw.line(Screen,Colour,[FP_w+8,FP_h],[FP_w+8,FP_h+4],4)
            # Green Check Mark over Key
            pygame.draw.line(Screen,(0,255,0),[FP_w-10,FP_h+11],[FP_w+4,FP_h+23],3)
            pygame.draw.line(Screen,(0,255,0),[FP_w+4,FP_h+23],[FP_w+10,FP_h+17],3)
            # Line Between the Door and Person
            pygame.draw.line(Screen,Colour,[FP_w-wide,FP_h-high],[ID_w+wide,ID_h+high],4)

        elif Action_Str == "motion detected": # This happens when motion is detected in a room
            pygame.draw.arc(Screen,(150,150,150),[FP_w-12,FP_h-12,24,24],-2*pi/11,2*pi/11,2)
            pygame.draw.arc(Screen,(150,150,150),[FP_w-16,FP_h-16,32,32],-2*pi/11,2*pi/11,2)
            pygame.draw.arc(Screen,(150,150,150),[FP_w-20,FP_h-20,40,40],-2*pi/11,2*pi/11,2)

            pygame.draw.arc(Screen,(150,150,150),[FP_w-12,FP_h-12,24,24],pi-2*pi/11,pi+2*pi/11,2)
            pygame.draw.arc(Screen,(150,150,150),[FP_w-16,FP_h-16,32,32],pi-2*pi/11,pi+2*pi/11,2)
            pygame.draw.arc(Screen,(150,150,150),[FP_w-20,FP_h-20,40,40],pi-2*pi/11,pi+2*pi/11,2)

            pygame.draw.arc(Screen,(150,150,150),[FP_w-12,FP_h-12,24,24],pi/2-2*pi/11,pi/2+2*pi/11,2)
            pygame.draw.arc(Screen,(150,150,150),[FP_w-16,FP_h-16,32,32],pi/2-2*pi/11,pi/2+2*pi/11,2)
            pygame.draw.arc(Screen,(150,150,150),[FP_w-20,FP_h-20,40,40],pi/2-2*pi/11,pi/2+2*pi/11,2)

            pygame.draw.arc(Screen,(150,150,150),[FP_w-12,FP_h-12,24,24],-pi/2-2*pi/11,-pi/2+2*pi/11,2)
            pygame.draw.arc(Screen,(150,150,150),[FP_w-16,FP_h-16,32,32],-pi/2-2*pi/11,-pi/2+2*pi/11,2)
            pygame.draw.arc(Screen,(150,150,150),[FP_w-20,FP_h-20,40,40],-pi/2-2*pi/11,-pi/2+2*pi/11,2)


        elif Action_Str == "user connected": # This happens when =someone connects to an access point
            # Signal Surrounding the Initial
            pygame.draw.arc(Screen,Colour,[ID_w-12,ID_h-12,24,24],angd-3*pi/9,angd+3*pi/9,2)
            pygame.draw.arc(Screen,Colour,[ID_w-16,ID_h-16,32,32],angd-3*pi/9,angd+3*pi/9,2)
            pygame.draw.arc(Screen,Colour,[ID_w-20,ID_h-20,40,40],angd-3*pi/9,angd+3*pi/9,2)
            # Signal Surrounding the Final
            pygame.draw.arc(Screen,Colour,[FP_w-12,FP_h-12,24,24],pi+angd-3*pi/9,pi+angd+3*pi/9,2)
            pygame.draw.arc(Screen,Colour,[FP_w-16,FP_h-16,32,32],pi+angd-3*pi/9,pi+angd+3*pi/9,2)
            pygame.draw.arc(Screen,Colour,[FP_w-20,FP_h-20,40,40],pi+angd-3*pi/9,pi+angd+3*pi/9,2)

        elif Action_Str == "user disconnected": # This happens when someone disconnects from an access point
            # Crossed out circle over the access point
            pygame.draw.line(Screen,Colour,[FP_w-10,FP_h+10],[FP_w+10,FP_h-10],4)
            pygame.draw.ellipse(Screen,Colour,[FP_w-12,FP_h-12,FP_w+12,FP_h+12],4)

        elif Action_Str == "on hook": # This happens when someone is using the phone
            # Phone in a room
            pygame.draw.arc(Screen,Colour,[FP_w-16,FP_h-12,32,16],-pi/8,9*pi/8,4)
            pygame.draw.arc(Screen,Colour,[FP_w-8,FP_h-8,16,12],-pi/4,5*pi/4,4)
            pygame.draw.line(Screen,Colour,[FP_w-16,FP_h],[FP_w-8,FP_h],4)
            pygame.draw.line(Screen,Colour,[FP_w+16,FP_h],[FP_w+8,FP_h],4)

        elif Action_Str == "off hook": # This happens when someone gets off the phone
            # Phone in a room
            pygame.draw.arc(Screen,Colour,[FP_w-16,FP_h-12,32,16],-pi/8,9*pi/8,4)
            pygame.draw.arc(Screen,Colour,[FP_w-8,FP_h-8,16,12],-pi/4,5*pi/4,4)
            pygame.draw.line(Screen,Colour,[FP_w-16,FP_h],[FP_w-8,FP_h],4)
            pygame.draw.line(Screen,Colour,[FP_w+16,FP_h],[FP_w+8,FP_h],4)
            # Red line over the phone
            pygame.draw.line(Screen,(255,0,0),[FP_w-16,FP_h-12],[FP_w+16,FP_h+6],3)



    # Testing Code
#win = pygame.display.set_mode((1000,600))
#pygame.display.set_caption("Murder on the 2nd Floor")


#movement = action()
#movement.activity((255,0,255),45,45,100,100,"new client",win)
#movement.activity((255,255,0),345,45,300,150,"off hook",win)
#movement.activity((255,0,0),645,45,750,200,"motion detected",win)
#movement.activity((255,255,255),800,30,850,90,"successful keycard unlock",win)
#movement.activity((0,255,0),45,200,145,300,"unlocked no keycard",win)
#movement.activity((0,255,255),200,245,250,300,"door closed",win)
#movement.activity((255,255,255),300,350,350,300,"user connected",win)
#pygame.display.update()
#pygame.time.delay(20000)

