import pygame
import math


class action(self,Colour,ID_w,ID_h,FP_w,FP_h,Action_Str,Screen)
    def __init__(self):
        pass


    def activity(self,Colour,ID_w,ID_h,FP_w,FP_h,Action_Str,Screen):
# FP_w => Final Participant Width Across the Screen
# FP_h => Final Participant Height Across the Screen
# ID_w => Inital Determinant Width Across the Screen
# ID_h => Initial Determinant Height Across the Screen
angd = atan((FP_h-ID_h)/(FP_w-ID_w)) # Angled Difference Between the Inital and Final

high = round((FP_h-ID_h)/15)
wide = round((FP_w-ID_w)/15)


if Action_Str == "new client" # This happens when an access point and identified user connect
    # Signal Surrounding the Initial
    pygame.draw.arc(Screen,Colour,[ID_w-4,ID_h-4,8,8],angd-pi/8,angd+pi/8,2)
    pygame.draw.arc(Screen,Colour,[ID_w-6,ID_h-6,12,12],angd-pi/9,angd+pi/9,2)
    pygame.draw.arc(Screen,Colour,[ID,w-8,ID_h-8,16,16],angd-pi/10,angd+pi/10,2)
    # Signal Surrounding the Final
    pygame.draw.arc(Screen,Colour,[FP_w-4,FP_h-4,8,8],angd+9*pi/8,angd+7*pi/8,2)
    pygame.draw.arc(Screen,Colour,[FP_w-6,FP_h-6,12,12],angd+10*pi/9,angd+8*pi/9,2)
    pygame.draw.arc(Screen,Colour,[FP_w-8,FP_h-8,16,16],angd+11*pi/10,angd+9*pi/10)

elif Action_Str == "unlocked no keycard" # This happens when someone opens the door without a keycard
    # Key Image Surrounding the Door
    pygame.draw.arc(Screen,Colour,[FP_w-7,FP_h-2,4,4],0,pi,2)
    pygame.draw.arc(Screen,Colour,[FP_w-7,FP_h-2,4,4],pi,2*pi,2)
    pygame.draw.line(Screen,Colour,[FP_w-2,FP_h],[FP_w+5,FP_h],2)
    pygame.draw.line(Screen,Colour,[FP_w+2,FP_h],[FP_w+2,FP_h-2],2)
    pygame.draw.line(Screen,Colour,[FP_w+4,FP_h],[FP_w+4,FP_h-2],2)
    # Line Through the Surrounding Key
    pygame.draw.line(Screen,(255,0,0),[FP_w+5,FP_h+4],[FP_w-5,FP_h-4],3)
    # Line Between the Door and Person
    pygame.draw.line(Screen,Colour,[FP_w-wide,FP_h-high],[ID_w+wide,ID_h+high],2)

elif Action_Str == "door closed" # This happens when someone opens the door
    # Closed Door Icon
    pygame.draw.rect(Screen,Colour,[FP_w-6,FP_h-10,12,10],2)
    pygame.draw.rect(Screen,Colour,[FP_w-4,FP_h-8,8,8])
    # Line Between the Door and Person
    pygame.draw.line(Screen,Colour,[FP_w-wide,FP_h-high],[ID_w+wide,ID_h+high],2)

elif Action_Str == "seccessful keycard unlock" # This happens when someone opens the door with a keycard
    # Key Icon over Door
    pygame.draw.arc(Screen,Colour,[FP_w-7,FP_h-2,4,4],0,pi,2)
    pygame.draw.arc(Screen,Colour,[FP_w-7,FP_h-2,4,4],pi,2*pi,2)
    pygame.draw.arc(Screen,Colour,[FP_w-5,FP_h,3,3],pi,2*pi,2)
    pygame.draw.line(Screen,Colour,[FP_w-2,FP_h],[FP_w+5,FP_h],2)
    pygame.draw.line(Screen,Colour,[FP_w+2,FP_h],[FP_w+2,FP_h-2],2)
    pygame.draw.line(Screen,Colour,[FP_w+4,FP_h],[FP_w+4,FP_h-2],2)
    # Green Check Mark over Key
    pygame.draw.line(Screen,(0,255,0),[FP_w-5,FP_h-4],[FP_w+2,FP_h+2],3)
    pygame.draw.line(Screen,(0,255,0),[FP_w+2,FP_h+2],[FP_w+5,FP_h-1],3)
    # Line Between the Door and Person
    pygame.draw.line(Screen,Colour,[FP_w-wide,FP_h-high],[ID_w+wide,ID_h+high],2)

elif Action_Str == "motion detected" # This happens when motion is detected in a room
    pygame.draw.rect(Screen,(100,100,100),[FD_w-15,FD_h-15,30,30])

elif Action_Str == "user connected" # This happens when =someone connects to an access point
    # Wifi Signal from the User
    pygame.draw.arc(Screen,Colour,[ID_w-4,ID_h-4,8,8],angd-pi/8,angd+pi/8,2)
    pygame.draw.arc(Screen,Colour,[ID_w-6,ID_h-6,12,12],angd-pi/9,angd+pi/9,2)
    pygame.draw.arc(Screen,Colour,[ID,w-8,ID_h-8,16,16],angd-pi/10,angd+pi/10,2)
    # Wifi Signal from the access point
    pygame.draw.arc(Screen,Colour,[FP_w-4,FP_h-4,8,8],angd+9*pi/8,angd+7*pi/8,2)
    pygame.draw.arc(Screen,Colour,[FP_w-6,FP_h-6,12,12],angd+10*pi/9,angd+8*pi/9,2)
    pygame.draw.arc(Screen,Colour,[FP_w-8,FP_h-8,16,16],angd+11*pi/10,angd+9*pi/10)

elif Action_Str == "user disconnected" # This happens when someone disconnects from an access point
    # Crossed out circle over the access point
    pygame.draw.line(Screen,Colour,[FP_w-5,FP_h+5],[FP_w+5,FP_h-5],3)
    pygame.draw.ellipse(Screen,Colour,[FP_w-6,FP_h-6,FP_w+6,FP_h+6],3)

elif Action_Str == "on hook" # This happens when someone is using the phone
    # Phone in a room
    pygame.draw.arc(Screen,Colour,[FP_w-8,FP_h-6,16,8],-pi/8,9*pi/8,3)
    pygame.draw.arc(Screen,Colour,[FP_w-4,FP_h-4,8,6],-pi/4,5*pi/4,3)
    pygame.draw.line(Screen,Colour,[FP_w-8,FP_h],[FP_w-4,FP_h],3)
    pygame.draw.line(Screen,Colour,[FP_w+8,FP_h],[FP_w+4,FP_h],3)

elif Action_Str == "off hook" # This happens when someone gets off the phone
    # Phone in a room
    pygame.draw.arc(Screen,Colour,[FP_w-8,FP_h-6,16,8],-pi/8,9*pi/8,3)
    pygame.draw.arc(Screen,Colour,[FP_w-4,FP_h-4,8,6],-pi/4,5*pi/4,3)
    pygame.draw.line(Screen,Colour,[FP_w-8,FP_h],[FP_w-4,FP_h],3)
    pygame.draw.line(Screen,Colour,[FP_w+8,FP_h],[FP_w+4,FP_h],3)
    # Red line over the phone
    pygame.draw.line(Screen,(255,0,0),[FP_w-8,FP_h-6],[FP_w+8,FP_h+6],3)
