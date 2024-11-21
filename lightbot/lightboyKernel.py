import numpy as np

def forward():
    global pos
    copy = pos[:]  # these [:]'s are apparently a good countermeasure against the trouble we had we had with mutable objects in class where python just instinctively went to the same memory address for mutable objects
    if facing == "r":  #ChatGPT helped me realise this ^
        pos[1] = pos[1] + 1
        if pos[1] > 9: #there was no elegant way to combine these
            pos = copy[:]
            return
        if mheight[pos[0],pos[1]] != mheight[copy[0],copy[1]]: # if statements elegantly cause i would run risking an index error
            pos = copy[:]
        return

    if facing == "l":
        pos[1] = pos[1] - 1
        if pos[1] < 0:
            pos = copy[:]
            return
        if mheight[pos[0],pos[1]] != mheight[copy[0],copy[1]]: 
            pos = copy[:]
        return

    if facing == "u":
        pos[0] = pos[0] + 1
        if pos[0] > 9:
            pos = copy[:]
            return
        if mheight[pos[0],pos[1]] != mheight[copy[0],copy[1]]:
            pos = copy[:]
        return

    if facing == "d":
        pos[0] = pos[0] - 1
        if pos[0] < 0:
            pos = copy[:]
            return
        if mheight[pos[0],pos[1]] != mheight[copy[0],copy[1]]:
            pos = copy[:]
        return
    

def turn1(): #counter-clockwise, <
    global facing
    dire = ['r','u','l','d']
    for i in range(len(dire)):
        if dire[i] == facing:
            index = i
            if index == 3:  #accounting for list index out of range, dont have to do this for turn2() since python has negative indexing
                index = -1
            break
    facing = dire[index+1]

def turn2(): #clockwise, >
    global facing
    dire = ['r','u','l','d']
    for i in range(len(dire)):
        if dire[i] == facing:
            index = i
            break
    facing = dire[index-1]


def jump():
    global pos
    copy = pos[:]
    if facing == "r":
        pos[1] = pos[1] + 1
        if pos[1] > 9:
            pos = copy[:]
            return
        if abs(mheight[pos[0],pos[1]] - mheight[copy[0],copy[1]]) != 1:
            pos = copy[:]
        return

    if facing == "l":
        pos[1] = pos[1] - 1
        if pos[1] < 0:
            pos = copy[:]
            return
        if abs(mheight[pos[0],pos[1]] - mheight[copy[0],copy[1]]) != 1: 
            pos = copy[:]
        return

    if facing == "u":
        pos[0] = pos[0] + 1
        if pos[0] > 9:
            pos = copy[:]
            return
        if abs(mheight[pos[0],pos[1]] - mheight[copy[0],copy[1]]) != 1:
            pos = copy[:]
        return

    if facing == "d":
        pos[0] = pos[0] - 1
        if pos[0] < 0:
            pos = copy[:]
            return
        if abs(mheight[pos[0],pos[1]] - mheight[copy[0],copy[1]]) != 1:
            pos = copy[:]
        return

def light():
    if mlight[pos[0],pos[1]]==1:
        mlight[pos[0],pos[1]]=-1
    elif mlight[pos[0],pos[1]]==-1:
        mlight[pos[0],pos[1]]=1
    else:
        mlight[pos[0],pos[1]]=0

def run(str):
    for letter in str:
        if letter == '@':
            light()
            continue
        if letter == '>':
            turn1()
            continue
        if letter == '<':
            turn2()
            continue
        if letter == '*':
            jump()
            continue
        if letter == '^':
            forward()
            continue
        return print("Unrecognized character found in commands")
