#level visualizer

import vpython as vp
import numpy as np
import ast as ast

with open(r"C:\Users\eren1\Desktop\work\phys290\lightbot\levels\level2.txt",'r') as file:  #Read levels file
    mheight = np.array(ast.literal_eval(file.readline()))
    mlight = np.array(ast.literal_eval(file.readline()))
    position = file.readline()

xmax , ymax = len(mheight[0]) , len(mheight)             # get dimensions

facing = position[2]  #initial conditions
pos = [position[0],position[1]]


for i in range(ymax):          #build terrain
    for j in range(xmax):
        a = 0
 
        for k in range(mheight[i,j]+1):
            vp.box(size=vp.vector(1,1,0.5),pos=vp.vector(i,j,k/2))
            a = k/2
        if mlight[i,j] == 0:
            vp.box(size=vp.vector(1,1,0.01),pos=vp.vector(i,j,a+0.255),color=vp.vector(0.5,0.5,0.5))
        elif mlight[i,j] == 1:
            vp.box(size=vp.vector(1,1,0.01),pos=vp.vector(i,j,a+0.255),color=vp.color.cyan)
        else:
            vp.box(size=vp.vector(1,1,0.01),pos=vp.vector(i,j,a+0.255),color=vp.color.yellow)
            

            
vp.scene.up = vp.vector(-1, -1, 0)  # Combines x and y directions for a tilt
vp.scene.camera.pos = vp.vector(5, 5, 5)  # Optional: Move the camera to see the effect better
vp.scene.camera.axis = vp.vector(-5, -5, -5)  # Look toward the origin


while True: #vpython closes immediately without this. may become a problem in the future with animations but ill see
    pass
