#!/usr/bin/env python3
from eye import *


LCDMenu("", "", "", "END")

while KEYRead() != KEY4:

    if ((PSDGet(PSD_FRONT)>500) and (PSDGet(PSD_FRONT)<1500)): #if leader is too far away
        LCDPrintf("Following Leader at 500 m/s\n","") #the follower will speed up
        VWStraight(200,500)
    
    elif ((PSDGet(PSD_FRONT)<500) and (PSDGet(PSD_FRONT)>50)): #if the leader is nearby
        LCDPrintf("Following Leader slowly at 100 m/s\n", "") #the follower will slow down
        VWStraight(200, 100)

    elif ((PSDGet(PSD_FRONT)<50) or (PSDGet(PSD_LEFT)<50) or (PSDGet(PSD_RIGHT)<50)): #if there are obstacles or if it's too close
        LCDPrintf("Too close\n", "") #the follower will stop for a while
        OSWait(500)
    
    else:
        LCDPrintf("Finding Leader\n","") # the follower will rotate to find its leader
        VWTurn(15,200)
        VWWait()