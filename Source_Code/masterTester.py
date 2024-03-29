# turn algorithm
import numpy as np
import random
import time
from statistics import mean
# Numbering Convention
# white   =  0
# yellow  =  1
# red     =  2
# orange  =  3
# blue    =  4
# green   =  5
# **NOTE:White  face is taken while keeping Red    face towards yourself,
#        Yellow face is taken while keeping Red    face towards yourself,
#        Red    face is taken while keeping Yellow face towards yourself,
#        Orange face is taken while keeping Yellow face towards yourself,
#        Blue   face is taken while keeping Yellow face towards yourself,
#        Green  face is taken while keeping Yellow face towards yourself.


# Global variables
cube = np.array([[[], [], []], [[], [], []], [[], [], []],
                [[], [], []], [[], [], []], [[], [], []]])
final_moves = []
stepcount = 0
move_length = list([])

def prnt():
    global stepcount
    #print(stepcount, end = ": ")
    print("white ", list(cube[0]))
    print("yellow", list(cube[1]))
    print("red   ", list(cube[2]))
    print("orange", list(cube[3]))
    print("blue  ", list(cube[4]))
    print("green ", list(cube[5]))
    stepcount += 1


def clockwise(face):
    face[0], face[2] = face[2].copy(), face[0].copy()
    return np.transpose(face)


def anticlockwise(face):
    face = np.transpose(face)
    face[0], face[2] = face[2].copy(), face[0].copy()
    return face


def whiteclk():

    cube[2][0], cube[4][0], cube[3][0], cube[5][0] = cube[4][0].copy(
    ), cube[3][0].copy(), cube[5][0].copy(), cube[2][0].copy()
    cube[0] = clockwise(cube[0].copy())
    final_moves.append(0)
    # print("")
    #print("White Clockwise -")
    # prnt()


def whiteAclk():
    # print("")
    cube[2][0], cube[4][0], cube[3][0], cube[5][0] = cube[5][0].copy(
    ), cube[2][0].copy(), cube[4][0].copy(), cube[3][0].copy()
    cube[0] = anticlockwise(cube[0].copy())
    final_moves.append(10)
    #print("White Anticlockwise -")
    # prnt()


def yellowclk():
    # print("")
    cube[2][2], cube[4][2], cube[3][2], cube[5][2] = cube[5][2].copy(
    ), cube[2][2].copy(), cube[4][2].copy(), cube[3][2].copy()
    cube[1] = clockwise(cube[1].copy())
    final_moves.append(1)
    #print("Yellow Clockwise -")
    # prnt()


def yellowAclk():
    # print("")
    cube[2][2], cube[4][2], cube[3][2], cube[5][2] = cube[4][2].copy(
    ), cube[3][2].copy(), cube[5][2].copy(), cube[2][2].copy()
    cube[1] = anticlockwise(cube[1].copy())
    final_moves.append(11)
    #print("Yellow Anticlockwise -")
    # prnt()


def redclk():
    # print("")
    cube[0][2][0], cube[4][0][0], cube[1][2][0], cube[5][2][2] = cube[5][2][2].copy(
    ), cube[0][2][0].copy(), cube[4][0][0].copy(), cube[1][2][0].copy()
    cube[0][2][1], cube[4][1][0], cube[1][2][1], cube[5][1][2] = cube[5][1][2].copy(
    ), cube[0][2][1].copy(), cube[4][1][0].copy(), cube[1][2][1].copy()
    cube[0][2][2], cube[4][2][0], cube[1][2][2], cube[5][0][2] = cube[5][0][2].copy(
    ), cube[0][2][2].copy(), cube[4][2][0].copy(), cube[1][2][2].copy()
    cube[2] = clockwise(cube[2].copy())
    final_moves.append(2)
    #print("Red Clockwise -")
    # prnt()


def redAclk():
   # print("")
    cube[0][2][0], cube[4][0][0], cube[1][2][0], cube[5][2][2] = cube[4][0][0].copy(
    ), cube[1][2][0].copy(), cube[5][2][2].copy(), cube[0][2][0].copy()
    cube[0][2][1], cube[4][1][0], cube[1][2][1], cube[5][1][2] = cube[4][1][0].copy(
    ), cube[1][2][1].copy(), cube[5][1][2].copy(), cube[0][2][1].copy()
    cube[0][2][2], cube[4][2][0], cube[1][2][2], cube[5][0][2] = cube[4][2][0].copy(
    ), cube[1][2][2].copy(), cube[5][0][2].copy(), cube[0][2][2].copy()
    cube[2] = anticlockwise(cube[2].copy())
    final_moves.append(12)
    #print("Red Anticlockwise -")
    # prnt()


def orangeclk():
    # print("")
    cube[0][0][0], cube[4][0][2], cube[1][0][0], cube[5][2][0] = cube[4][0][2].copy(
    ), cube[1][0][0].copy(), cube[5][2][0].copy(), cube[0][0][0].copy()
    cube[0][0][1], cube[4][1][2], cube[1][0][1], cube[5][1][0] = cube[4][1][2].copy(
    ), cube[1][0][1].copy(), cube[5][1][0].copy(), cube[0][0][1].copy()
    cube[0][0][2], cube[4][2][2], cube[1][0][2], cube[5][0][0] = cube[4][2][2].copy(
    ), cube[1][0][2].copy(), cube[5][0][0].copy(), cube[0][0][2].copy()
    cube[3] = clockwise(cube[3].copy())
    final_moves.append(3)
   #print("Orange Clockwise -")
   # prnt()


def orangeAclk():
    # print("")
    cube[0][0][0], cube[4][0][2], cube[1][0][0], cube[5][2][0] = cube[5][2][0].copy(
    ), cube[0][0][0].copy(), cube[4][0][2].copy(), cube[1][0][0].copy()
    cube[0][0][1], cube[4][1][2], cube[1][0][1], cube[5][1][0] = cube[5][1][0].copy(
    ), cube[0][0][1].copy(), cube[4][1][2].copy(), cube[1][0][1].copy()
    cube[0][0][2], cube[4][2][2], cube[1][0][2], cube[5][0][0] = cube[5][0][0].copy(
    ), cube[0][0][2].copy(), cube[4][2][2].copy(), cube[1][0][2].copy()
    cube[3] = anticlockwise(cube[3].copy())
    final_moves.append(13)
    #print("Orange Anticlockwise -")
    # prnt()


def blueclk():
    # print("")
    cube[0][0][2], cube[2][0][2], cube[1][2][0], cube[3][2][0] = cube[2][0][2].copy(
    ), cube[1][2][0].copy(), cube[3][2][0].copy(), cube[0][0][2].copy()
    cube[0][1][2], cube[2][1][2], cube[1][1][0], cube[3][1][0] = cube[2][1][2].copy(
    ), cube[1][1][0].copy(), cube[3][1][0].copy(), cube[0][1][2].copy()
    cube[0][2][2], cube[2][2][2], cube[1][0][0], cube[3][0][0] = cube[2][2][2].copy(
    ), cube[1][0][0].copy(), cube[3][0][0].copy(), cube[0][2][2].copy()
    cube[4] = clockwise(cube[4].copy())
    final_moves.append(4)
    #print("Blue Clockwise -")
    # prnt()


def blueAclk():
    # print("")
    cube[0][0][2], cube[2][0][2], cube[1][2][0], cube[3][2][0] = cube[3][2][0].copy(
    ), cube[0][0][2].copy(), cube[2][0][2].copy(), cube[1][2][0].copy()
    cube[0][1][2], cube[2][1][2], cube[1][1][0], cube[3][1][0] = cube[3][1][0].copy(
    ), cube[0][1][2].copy(), cube[2][1][2].copy(), cube[1][1][0].copy()
    cube[0][2][2], cube[2][2][2], cube[1][0][0], cube[3][0][0] = cube[3][0][0].copy(
    ), cube[0][2][2].copy(), cube[2][2][2].copy(), cube[1][0][0].copy()
    cube[4] = anticlockwise(cube[4].copy())
    final_moves.append(14)
    #print("Blue Anticlockwise -")
    # prnt()


def greenclk():
    # print("")
    cube[0][0][0], cube[2][0][0], cube[1][2][2], cube[3][2][2] = cube[3][2][2].copy(
    ), cube[0][0][0].copy(), cube[2][0][0].copy(), cube[1][2][2].copy()
    cube[0][1][0], cube[2][1][0], cube[1][1][2], cube[3][1][2] = cube[3][1][2].copy(
    ), cube[0][1][0].copy(), cube[2][1][0].copy(), cube[1][1][2].copy()
    cube[0][2][0], cube[2][2][0], cube[1][0][2], cube[3][0][2] = cube[3][0][2].copy(
    ), cube[0][2][0].copy(), cube[2][2][0].copy(), cube[1][0][2].copy()
    cube[5] = clockwise(cube[5].copy())
    final_moves.append(5)
    #print("Green Clockwise -")
    # prnt()


def greenAclk():
    # print("")
    cube[0][0][0], cube[2][0][0], cube[1][2][2], cube[3][2][2] = cube[2][0][0].copy(
    ), cube[1][2][2].copy(), cube[3][2][2].copy(), cube[0][0][0].copy()
    cube[0][1][0], cube[2][1][0], cube[1][1][2], cube[3][1][2] = cube[2][1][0].copy(
    ), cube[1][1][2].copy(), cube[3][1][2].copy(), cube[0][1][0].copy()
    cube[0][2][0], cube[2][2][0], cube[1][0][2], cube[3][0][2] = cube[2][2][0].copy(
    ), cube[1][0][2].copy(), cube[3][0][2].copy(), cube[0][2][0].copy()
    cube[5] = anticlockwise(cube[5].copy())
    final_moves.append(15)
    #print("Green Anticlockwise -")
    # prnt()


def redr():
    blueAclk()
    yellowclk()
    blueclk()
    yellowclk()
    redclk()
    yellowAclk()
    redAclk()


def oranger():
    greenAclk()
    yellowclk()
    greenclk()
    yellowclk()
    orangeclk()
    yellowAclk()
    orangeAclk()


def bluer():
    orangeAclk()
    yellowclk()
    orangeclk()
    yellowclk()
    blueclk()
    yellowAclk()
    blueAclk()


def greenr():
    redAclk()
    yellowclk()
    redclk()
    yellowclk()
    greenclk()
    yellowAclk()
    greenAclk()


def redl():
    greenclk()
    yellowAclk()
    greenAclk()
    yellowAclk()
    redAclk()
    yellowclk()
    redclk()


def orangel():
    blueclk()
    yellowAclk()
    blueAclk()
    yellowAclk()
    orangeAclk()
    yellowclk()
    orangeclk()


def bluel():
    redclk()
    yellowAclk()
    redAclk()
    yellowAclk()
    blueAclk()
    yellowclk()
    blueclk()


def greenl():
    orangeclk()
    yellowAclk()
    orangeAclk()
    yellowAclk()
    greenAclk()
    yellowclk()
    greenclk()


def camscan():
    # Initial scan +8 (White all)
    blueclk()     # +3 (red[3], red[6], red[9])
    greenAclk()   # +3 (red[1], red[4], red[7])
    blueclk()     # +3 (yellow[3], yellow[6], yellow[9])
    greenAclk()   # +3 (yellow[1], yellow[4], yellow[7])
    blueclk()     # +3 (orange[1], orange[3], orange[7])
    greenAclk()   # +3 (orange[3], orange[6], orange[9])
    redclk()      # +1 (green[2])
    orangeAclk()  # +1 (green[8])
    redAclk()     # +0
    orangeclk()   # +0
    redAclk()     # +1 (blue[2])
    orangeclk()   # +1 (blue[8])
    redclk()      # +0
    orangeAclk()  # +0
    blueclk()     # +0
    greenAclk()   # +0

    redclk()      # +3 (green[3], green[6], green[9])
    orangeAclk()  # +3 (green[1], green[4], green[7])
    redclk()      # +1 (yellow[8])
    orangeAclk()  # +1 (yellow[2])
    redclk()      # +3 (blue[1], blue[3], blue[7])
    orangeAclk()  # +3 (blue[3], blue[6], blue[9])
    blueclk()     # +1 (red[8])
    greenAclk()   # +1 (red[2])
    blueAclk()    # +0
    greenclk()    # +0
    blueAclk()    # +1 (orange[8])
    greenclk()    # +1 (orange[2])
    blueclk()     # +0
    greenAclk()   # +0
    redclk()      # +0
    orangeAclk()  # +0


def ycross():
    ycross = []
    ycross.append(cube[2][2][1])
    ycross.append(cube[3][2][1])
    ycross.append(cube[4][2][1])
    ycross.append(cube[5][2][1])
    return ycross


if __name__ == "__main__":
    loopcount = 0
    
    while (1):
        loopcount += 1
        final_moves = []
        colour = ["white", "yellow", "red", "orange", "blue", "green"]
        cube = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [
            1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]], [[3, 3, 3], [3, 3, 3], [3, 3, 3]], [[4, 4, 4], [4, 4, 4], [4, 4, 4]], [[5, 5, 5], [5, 5, 5], [5, 5, 5]]])
        for i in range(0, 500):
            rn = random.randint(1, 12)
            if (rn == 1):
                whiteclk()
            if (rn == 2):
                whiteAclk()
            if (rn == 3):
                redclk()
            if (rn == 4):
                redAclk()
            if (rn == 5):
                yellowclk()
            if (rn == 6):
                yellowAclk()
            if (rn == 7):
                orangeclk()
            if (rn == 8):
                orangeAclk()
            if (rn == 9):
                blueclk()
            if (rn == 10):
                blueAclk()
            if (rn == 11):
                greenclk()
            if (rn == 12):
                greenAclk()
        iconfig = cube.copy()
        stepcount = 1
        # All callable functions
        #  whiteclk()
        #  whiteAclk()
        #  yellowclk()
        #  yellowAclk()
        #  redclk()
        #  redAclk()
        #  orangeclk()
        #  orangeAclk()
        #  blueclk()
        #  blueAclk()
        #  greenclk()
        #  greenAclk()

# Top Layer Logic

        ### White Edges Search ###
        if not (cube[0][2][1] == 0 and cube[2][0][1] == 2):
            ## white piece ##
            # white  face
            if cube[0][0][1] == 0 and cube[3][0][1] == 2:
                orangeclk()
                orangeclk()
                yellowclk()
                yellowclk()
                redclk()
                redclk()
            elif cube[0][1][2] == 0 and cube[4][0][1] == 2:
                blueclk()
                blueclk()
                yellowAclk()
                redclk()
                redclk()
            elif cube[0][1][0] == 0 and cube[5][0][1] == 2:
                greenclk()
                greenclk()
                yellowclk()
                redclk()
                redclk()    


            # red    face
            if ((cube[2][2][1] == 0 and cube[1][2][1] == 2) or (cube[2][0][1] == 0 and cube[0][2][1] == 2)):
                redclk()
            if (cube[2][1][0] == 0 and cube[5][1][2] == 2):
                greenclk()
                yellowclk()
                # greenAclk()
            elif (cube[2][1][2] == 0 and cube[4][1][0] == 2):
                blueAclk()
                yellowAclk()
                # blueclk()

            # orange face
            if ((cube[3][2][1] == 0 and cube[1][0][1] == 2) or (cube[3][0][1] == 0 and cube[0][0][1] == 2)):
                orangeclk()
            if (cube[3][1][0] == 0 and cube[4][1][2] == 2):
                blueclk()
                yellowAclk()
                # blueAclk()
            elif (cube[3][1][2] == 0 and cube[5][1][0] == 2):
                greenAclk()
                yellowclk()
                # greenclk()
            # blue   face
            if (cube[4][1][2] == 0 and cube[3][1][0] == 2):
                blueclk()
                blueclk()
            elif (cube[4][0][1] == 0 and cube[0][1][2] == 2):
                blueAclk()
            elif (cube[4][2][1] == 0 and cube[1][1][0] == 2):
                blueclk()
            if (cube[4][1][0] == 0 and cube[2][1][2] == 2):
                redAclk()
            # green  face
            if (cube[5][1][0] == 0 and cube[3][1][2] == 2):
                greenclk()
                greenclk()
            elif (cube[5][0][1] == 0 and cube[0][1][0] == 2):
                greenclk()
            elif (cube[5][2][1] == 0 and cube[1][1][2] == 2):
                greenAclk()
            if (cube[5][1][2] == 0 and cube[2][1][0] == 2):
                redclk()
            # yellow face
            if (cube[3][2][1] == 2 and cube[1][0][1] == 0):
                yellowclk()
                yellowclk()
            elif (cube[5][2][1] == 2 and cube[1][1][2] == 0):
                yellowclk()
            elif (cube[4][2][1] == 2 and cube[1][1][0] == 0):
                yellowAclk()
            if (cube[2][2][1] == 2 and cube[1][2][1] == 0):
                redclk()
                redclk()
        print("red white piece solved")
        if (not (cube[0][0][1] == 0 and cube[3][0][1] == 3)):
            ## white orange piece##
            # white  face
            if (cube[0][1][0] == 0 and cube[5][0][1] == 3):
                greenclk()
                greenclk()
            elif (cube[0][1][2] == 0 and cube[4][0][1] == 3):
                blueclk()
                blueclk()

            # red    face
            if (cube[2][2][1] == 0 and cube[1][2][1] == 3):
                redclk()
                greenclk()
                yellowAclk()
                # greenAclk()
                redAclk()
            elif (cube[2][1][0] == 0 and cube[5][1][2] == 3):
                greenclk()
                yellowAclk()
                # greenAclk()
            elif (cube[2][1][2] == 0 and cube[4][1][0] == 3):
                blueAclk()
                yellowclk()
                # blueclk()

            # orange face
            if ((cube[3][2][1] == 0 and cube[1][0][1] == 3) or (cube[3][0][1] == 0 and cube[0][0][1] == 3)):
                orangeclk()
            if (cube[3][1][0] == 0 and cube[4][1][2] == 3):
                blueclk()
                yellowclk()
               # blueAclk()
            elif (cube[3][1][2] == 0 and cube[5][1][0] == 3):
                greenAclk()
                yellowAclk()
                # greenclk()
            # blue   face
            if (cube[4][1][0] == 0 and cube[2][1][2] == 3):
                blueclk()
                blueclk()
            elif (cube[4][0][1] == 0 and cube[0][1][2] == 3):
                blueclk()
            elif (cube[4][2][1] == 0 and cube[1][1][0] == 3):
                blueAclk()
            if (cube[4][1][2] == 0 and cube[3][1][0] == 3):
                orangeclk()
            # green  face
            if (cube[5][1][2] == 0 and cube[2][1][0] == 3):
                greenclk()
                greenclk()
            elif (cube[5][0][1] == 0 and cube[0][1][0] == 3):
                greenAclk()
            elif (cube[5][2][1] == 0 and cube[1][1][2] == 3):
                greenclk()
            if (cube[5][1][0] == 0 and cube[3][1][2] == 3):
                orangeAclk()
            # yellow face
            if (cube[2][2][1] == 3 and cube[1][2][1] == 0):
                yellowclk()
                yellowclk()
            elif (cube[5][2][1] == 3 and cube[1][1][2] == 0):
                yellowAclk()
            elif (cube[4][2][1] == 3 and cube[1][1][0] == 0):
                yellowclk()
            if (cube[3][2][1] == 3 and cube[1][0][1] == 0):
                orangeclk()
                orangeclk()
        print("orange white piece solved")
        if (not (cube[0][1][2] == 0 and cube[4][0][1] == 4)):
            ## white blue piece ##
            # white  face
            if (cube[0][1][0] == 0 and cube[5][0][1] == 4):
                greenclk()
                greenclk()
            # red    face
            if (cube[2][1][0] == 0 and cube[5][1][2] == 4):
                redclk()
                redclk()
                blueclk()
                redclk()
                redclk()
            elif (cube[2][2][1] == 0 and cube[1][2][1] == 4):
                redAclk()
                blueclk()
                redclk()
            elif (cube[2][1][2] == 0 and cube[4][1][0] == 4):
                blueclk()
            # orange face
            if (cube[3][1][2] == 0 and cube[5][1][0] == 4):
                orangeclk()
                orangeclk()
                blueAclk()
                orangeclk()
                orangeclk()
            elif (cube[3][2][1] == 0 and cube[1][0][1] == 4):
                orangeclk()
                blueAclk()
                orangeAclk()
            elif (cube[3][1][0] == 0 and cube[4][1][2] == 4):
                blueclk()
            # blue   face
            if ((cube[4][2][1] == 0 and cube[1][1][0] == 4) or (cube[4][0][1] == 0 and cube[0][1][2] == 4)):
                blueclk()
            if (cube[4][1][0] == 0 and cube[2][1][2] == 4):
                redclk()
                yellowclk()
                redAclk()
            elif (cube[4][1][2] == 0 and cube[3][1][0] == 4):
                orangeAclk()
                yellowAclk()
                orangeclk()
            # green  face
            if ((cube[5][2][1] == 0 and cube[1][1][2] == 4) or (cube[5][0][1] == 0 and cube[0][1][0] == 4)):
                greenclk()
            if (cube[5][1][0] == 0 and cube[3][1][2] == 4):
                orangeclk()
                yellowAclk()
                orangeAclk()
            elif (cube[5][1][2] == 0 and cube[2][1][0] == 4):
                redAclk()
                yellowclk()
                redclk()
            # yellow face
            if (cube[5][2][1] == 4 and cube[1][1][2] == 0):
                yellowclk()
                yellowclk()
            elif (cube[3][2][1] == 4 and cube[1][0][1] == 0):
                yellowAclk()
            elif (cube[2][2][1] == 4 and cube[1][2][1] == 0):
                yellowclk()
            if (cube[4][2][1] == 4 and cube[1][1][0] == 0):
                blueclk()
                blueclk()
        print("blue white piece solved")
        if (not (cube[0][1][0] == 0 and cube[5][0][1] == 5)):
            ## white green   piece ##
            # red    face
            if (cube[2][1][2] == 0 and cube[4][1][0] == 5):
                redclk()
                redclk()
                greenAclk()
                redclk()
                redclk()
            elif (cube[2][2][1] == 0 and cube[1][2][1] == 5):
                redclk()
                greenAclk()
                redAclk()
            elif (cube[2][1][0] == 0 and cube[5][1][2] == 5):
                greenAclk()
            # orange face
            if (cube[3][1][0] == 0 and cube[4][1][2] == 5):
                orangeclk()
                orangeclk()
                greenclk()
                orangeclk()
                orangeclk()
            elif (cube[3][2][1] == 0 and cube[1][0][1] == 5):
                orangeAclk()
                greenclk()
                orangeclk()
            elif (cube[3][1][2] == 0 and cube[5][1][0] == 5):
                greenclk()
            # blue   face
            if (cube[4][2][1] == 0 and cube[1][1][0] == 5):
                blueclk()
                redclk()
                yellowAclk()
                redAclk()
                blueAclk()
            elif (cube[4][1][0] == 0 and cube[2][1][2] == 5):
                redclk()
                yellowAclk()
                redAclk()
            elif (cube[4][1][2] == 0 and cube[3][1][0] == 5):
                orangeAclk()
                yellowclk()
                orangeclk()
            # green  face
            if ((cube[5][2][1] == 0 and cube[1][1][2] == 5) or (cube[5][0][1] == 0 and cube[0][1][0] == 5)):
                greenclk()
            if (cube[5][1][0] == 0 and cube[3][1][2] == 5):
                orangeclk()
                yellowclk()
                orangeAclk()
            elif (cube[5][1][2] == 0 and cube[2][1][0] == 5):
                redAclk()
                yellowAclk()
                redclk()
            # yellow face
            if (cube[4][2][1] == 5 and cube[1][1][0] == 0):
                yellowclk()
                yellowclk()
            elif (cube[2][2][1] == 5 and cube[1][2][1] == 0):
                yellowAclk()
            elif (cube[3][2][1] == 5 and cube[1][0][1] == 0):
                yellowclk()
            if (cube[5][2][1] == 5 and cube[1][1][2] == 0):
                greenclk()
                greenclk()
        print("green white piece solved")
        ## White Corners Search ##

# 2n    d Layer Logic
        # Edges Search

        # Red Blue piece
        if (not (cube[0][2][2] == 0 and cube[2][0][2] == 2 and cube[4][0][0] == 4)):
            ##Top Layer##

            # White face
            if (cube[0][0][2] == 0 and cube[3][0][0] == 4 and cube[4][0][2] == 2):
                orangeAclk()
                yellowclk()
                orangeclk()
            elif (cube[0][0][0] == 0 and cube[5][0][0] == 4 and cube[3][0][2] == 2):
                orangeclk()
                yellowAclk()
                orangeAclk()
            elif (cube[0][2][0] == 0 and cube[2][0][0] == 4 and cube[5][0][2] == 2):
                greenclk()
                yellowclk()
                greenAclk()
            # Red face
            if (cube[0][2][0] == 2 and cube[2][0][0] == 0 and cube[5][0][2] == 4):
                redAclk()
                yellowAclk()
                redclk()
            elif (cube[0][2][2] == 4 and cube[2][0][2] == 0 and cube[4][0][0] == 2):
                blueAclk()
                yellowclk()
                blueclk()
            # Blue  face
            if (cube[0][2][2] == 2 and cube[2][0][2] == 4 and cube[4][0][0] == 0):
                redclk()
                yellowAclk()
                redAclk()
            elif (cube[0][0][2] == 4 and cube[4][0][2] == 0 and cube[3][0][0] == 2):
                blueclk()
                yellowclk()
                blueAclk()
            # Orange face
            if (cube[0][0][0] == 4 and cube[3][0][2] == 0 and cube[5][0][0] == 2):
                orangeclk()
                yellowAclk()
                orangeAclk()
            elif (cube[0][0][2] == 2 and cube[4][0][2] == 4 and cube[3][0][0] == 0):
                blueclk()
                yellowAclk()
                blueAclk()
            # Green face
            if (cube[0][0][0] == 2 and cube[3][0][2] == 4 and cube[5][0][0] == 0):
                greenAclk()
                yellowAclk()
                greenclk()
            elif (cube[0][2][0] == 4 and cube[5][0][2] == 0 and cube[2][0][0] == 2):
                redAclk()
                yellowclk()
                redclk()
            # Yellow face
            if (cube[1][0][2] == 0 and cube[5][2][0] == 2 and cube[3][2][2] == 4):
                yellowAclk()
            elif (cube[1][2][0] == 0 and cube[4][2][0] == 2 and cube[2][2][2] == 4):
                yellowclk()
            elif (cube[1][2][2] == 0 and cube[2][2][0] == 2 and cube[5][2][2] == 4):
                yellowclk()
                yellowclk()
            if (cube[1][0][0] == 0 and cube[3][2][0] == 2 and cube[4][2][2] == 4):
                blueclk()
                yellowAclk()
                blueAclk()
            ##Bottom Layer##
            if (cube[1][2][2] == 4 and cube[5][2][2] == 2 and cube[2][2][0] == 0):
                yellowclk()
                yellowclk()
            elif (cube[1][2][0] == 4 and cube[2][2][2] == 2 and cube[4][2][0] == 0):
                yellowclk()
            elif (cube[1][0][2] == 4 and cube[3][2][2] == 2 and cube[5][2][0] == 0):
                yellowAclk()
            if (cube[1][0][0] == 4 and cube[4][2][2] == 2 and cube[3][2][0] == 0):
                redclk()
                yellowAclk()
                redAclk()
            if (cube[1][2][0] == 2 and cube[2][2][2] == 0 and cube[4][2][0] == 4):
                yellowAclk()
            elif (cube[1][0][0] == 2 and cube[4][2][2] == 0 and cube[3][2][0] == 4):
                yellowclk()
                yellowclk()
            elif (cube[1][0][2] == 2 and cube[3][2][2] == 0 and cube[5][2][0] == 4):
                yellowclk()
            if (cube[1][2][2] == 2 and cube[5][2][2] == 0 and cube[2][2][0] == 4):
                blueAclk()
                yellowclk()
                blueclk()
        print("White Red Blue is solved")

        # Blue Orange piece
        if (not (cube[0][0][2] == 0 and cube[4][0][2] == 4 and cube[3][0][0] == 3)):
            ##Top Layer##

            # White face
            if (cube[0][0][0] == 0 and cube[5][0][0] == 3 and cube[3][0][2] == 4):
                orangeclk()
                yellowclk()
                orangeAclk()
            elif (cube[0][2][0] == 0 and cube[2][0][0] == 3 and cube[5][0][2] == 4):
                greenclk()
                yellowAclk()
                greenAclk()
            # Red face
            if (cube[0][2][0] == 4 and cube[2][0][0] == 0 and cube[5][0][2] == 3):
                redAclk()
                yellowAclk()
                redclk()
            # Blue face
            if (cube[0][0][2] == 3 and cube[4][0][2] == 0 and cube[3][0][0] == 4):
                orangeAclk()
                yellowclk()
                orangeclk()
            # Orange face
            if (cube[0][0][0] == 3 and cube[3][0][2] == 0 and cube[5][0][0] == 4):
                orangeclk()
                yellowclk()
                orangeAclk()
            elif (cube[0][0][2] == 4 and cube[4][0][2] == 3 and cube[3][0][0] == 0):
                blueclk()
                yellowAclk()
                blueAclk()
            # Green face
            if (cube[0][0][0] == 4 and cube[3][0][2] == 3 and cube[5][0][0] == 0):
                orangeclk()
                yellowAclk()
                orangeAclk()
            elif (cube[0][2][0] == 3 and cube[5][0][2] == 0 and cube[2][0][0] == 4):
                greenclk()
                yellowclk()
                greenAclk()
            # Yellow face
            if (cube[1][2][2] == 0 and cube[2][2][0] == 4 and cube[5][2][2] == 3):
                yellowAclk()
            elif (cube[1][2][0] == 0 and cube[4][2][0] == 4 and cube[2][2][2] == 3):
                yellowclk()
                yellowclk()
            elif (cube[1][0][0] == 0 and cube[3][2][0] == 4 and cube[4][2][2] == 3):
                yellowclk()
            if (cube[1][0][2] == 0 and cube[5][2][0] == 4 and cube[3][2][2] == 3):
                orangeclk()
                yellowAclk()
                orangeAclk()
            ##Bottom Layer##
            # Red face 4 -> 3 & 2 -> 4
            if (cube[1][2][2] == 3 and cube[5][2][2] == 4 and cube[2][2][0] == 0):
                yellowAclk()
            elif (cube[1][2][0] == 3 and cube[2][2][2] == 4 and cube[4][2][0] == 0):
                yellowclk()
                yellowclk()
            elif (cube[1][0][0] == 3 and cube[4][2][2] == 4 and cube[3][2][0] == 0):
                yellowclk()
            if (cube[1][0][2] == 3 and cube[3][2][2] == 4 and cube[5][2][0] == 0):
                blueclk()
                yellowAclk()
                blueAclk()

            if (cube[1][0][0] == 4 and cube[4][2][2] == 0 and cube[3][2][0] == 3):
                yellowAclk()
            elif (cube[1][0][2] == 4 and cube[3][2][2] == 0 and cube[5][2][0] == 3):
                yellowclk()
                yellowclk()
            elif (cube[1][2][2] == 4 and cube[5][2][2] == 0 and cube[2][2][0] == 3):
                yellowclk()
            if (cube[1][2][0] == 4 and cube[2][2][2] == 0 and cube[4][2][0] == 3):
                orangeAclk()
                yellowclk()
                orangeclk()
        print("White Blue Orange is solved")

        # Orange Green piece
        if (not (cube[0][0][0] == 0 and cube[3][0][2] == 3 and cube[5][0][0] == 5)):
            ##Top Layer##

         # White face
            if (cube[0][2][0] == 0 and cube[2][0][0] == 5 and cube[5][0][2] == 3):
                greenclk()
                yellowclk()
                greenAclk()
            # Red face
            if (cube[0][2][0] == 3 and cube[2][0][0] == 0 and cube[5][0][2] == 5):
                redAclk()
                yellowAclk()
                redclk()
            # Orange face
            if (cube[0][0][0] == 5 and cube[3][0][2] == 0 and cube[5][0][0] == 3):
                greenAclk()
                yellowclk()
                greenclk()
            # Green face
            if (cube[0][0][0] == 3 and cube[3][0][2] == 5 and cube[5][0][0] == 0):
                orangeclk()
                yellowAclk()
                orangeAclk()
            elif (cube[0][2][0] == 5 and cube[5][0][2] == 0 and cube[2][0][0] == 3):
                greenclk()
                yellowclk()
                greenAclk()
            # Yellow face
            if (cube[1][2][0] == 0 and cube[4][2][0] == 3 and cube[2][2][2] == 5):
                yellowAclk()
            elif (cube[1][0][0] == 0 and cube[3][2][0] == 3 and cube[4][2][2] == 5):
                yellowclk()
                yellowclk()
            elif (cube[1][0][2] == 0 and cube[5][2][0] == 3 and cube[3][2][2] == 5):
                yellowclk()
            if (cube[1][2][2] == 0 and cube[2][2][0] == 3 and cube[5][2][2] == 5):
                greenclk()
                yellowAclk()
                greenAclk()
         ##Bottom Layer##

            if (cube[1][2][0] == 5 and cube[2][2][2] == 3 and cube[4][2][0] == 0):
                yellowAclk()
            elif (cube[1][0][0] == 5 and cube[4][2][2] == 3 and cube[3][2][0] == 0):
                yellowclk()
                yellowclk()
            elif (cube[1][0][2] == 5 and cube[3][2][2] == 3 and cube[5][2][0] == 0):
                yellowclk()
            if (cube[1][2][2] == 5 and cube[5][2][2] == 3 and cube[2][2][0] == 0):
                orangeclk()
                yellowAclk()
                orangeAclk()

            if (cube[1][2][0] == 3 and cube[2][2][2] == 0 and cube[4][2][0] == 5):
                yellowclk()
            elif (cube[1][0][2] == 3 and cube[3][2][2] == 0 and cube[5][2][0] == 5):
                yellowAclk()
            elif (cube[1][2][2] == 3 and cube[5][2][2] == 0 and cube[2][2][0] == 5):
                yellowclk()
                yellowclk()
            if (cube[1][0][0] == 3 and cube[4][2][2] == 0 and cube[3][2][0] == 5):
                greenAclk()
                yellowclk()
                greenclk()
        print("White Orange Green is solved")

        # Green Red piece
        if (not (cube[0][2][0] == 0 and cube[5][0][2] == 5 and cube[2][0][0] == 2)):
            ##Top Layer##
            # Red face
            if (cube[0][2][0] == 5 and cube[2][0][0] == 0 and cube[5][0][2] == 2):
                greenclk()
                yellowAclk()
                greenAclk()
            # Green face
            if (cube[0][2][0] == 2 and cube[5][0][2] == 0 and cube[2][0][0] == 5):
                redAclk()
                yellowclk()
                redclk()
            # Yellow face
            if (cube[1][0][0] == 0 and cube[3][2][0] == 5 and cube[4][2][2] == 2):
                yellowclk()
                yellowclk()
            elif (cube[1][0][2] == 0 and cube[5][2][0] == 5 and cube[3][2][2] == 2):
                yellowclk()
            elif (cube[1][2][0] == 0 and cube[4][2][0] == 5 and cube[2][2][2] == 2):
                yellowAclk()
            if (cube[1][2][2] == 0 and cube[2][2][0] == 5 and cube[5][2][2] == 2):
                redAclk()
                yellowclk()
                redclk()
            ##Bottom Layer##
            # Blue  face

            if (cube[1][0][2] == 2 and cube[3][2][2] == 5 and cube[5][2][0] == 0):
                yellowclk()
                yellowclk()
            elif (cube[1][2][2] == 2 and cube[5][2][2] == 5 and cube[2][2][0] == 0):
                yellowclk()
            elif (cube[1][0][0] == 2 and cube[4][2][2] == 5 and cube[3][2][0] == 0):
                yellowAclk()
            if (cube[1][2][0] == 2 and cube[2][2][2] == 5 and cube[4][2][0] == 0):
                greenclk()
                yellowAclk()
                greenAclk()

            if (cube[1][2][2] == 5 and cube[5][2][2] == 0 and cube[2][2][0] == 2):
                yellowAclk()
            elif (cube[1][2][0] == 5 and cube[2][2][2] == 0 and cube[4][2][0] == 2):
                yellowclk()
                yellowclk()
            elif (cube[1][0][0] == 5 and cube[4][2][2] == 0 and cube[3][2][0] == 2):
                yellowclk()

            if (cube[1][0][2] == 5 and cube[3][2][2] == 0 and cube[5][2][0] == 2):
                redAclk()
                yellowclk()
                redclk()
        print("White Green Red is solved")

        # 2nd Layer
        while (not (cube[2][1][0] == 2 and cube[2][1][1] == 2 and cube[2][1][2] == 2 and cube[3][1][0] == 3 and cube[3][1][1] == 3 and cube[3][1][2] == 3 and cube[4][1][0] == 4 and cube[4][1][1] == 4 and cube[4][1][2] == 4 and cube[5][1][0] == 5 and cube[5][1][1] == 5 and cube[5][1][2] == 5)):
            # Red Blue Piece
            if (not (cube[2][1][2] == 2 and cube[4][1][0] == 4)):
                # Search 2nd Layer
                if (cube[4][1][2] == 2 and cube[3][1][0] == 4):
                    bluer()
                elif (cube[3][1][2] == 2 and cube[5][1][0] == 4):
                    oranger()
                elif (cube[5][1][2] == 2 and cube[2][1][0] == 4):
                    greenr()
                elif (cube[4][1][2] == 4 and cube[3][1][0] == 2):
                    orangel()
                elif (cube[3][1][2] == 4 and cube[5][1][0] == 2):
                    greenl()
                elif (cube[5][1][2] == 4 and cube[2][1][0] == 2):
                    redl()
                elif (cube[2][1][2] == 4 and cube[4][1][0] == 2):
                    bluel()
                # Search 3rd Layer
                if (cube[1][1][2] == 2 and cube[5][2][1] == 4):
                    yellowAclk()
                elif (cube[1][2][1] == 2 and cube[2][2][1] == 4):
                    yellowclk()
                    yellowclk()
                elif (cube[1][1][0] == 2 and cube[4][2][1] == 4):
                    yellowclk()
                if (cube[1][0][1] == 2 and cube[3][2][1] == 4):
                    bluel()

                if (cube[1][0][1] == 4 and cube[3][2][1] == 2):
                    yellowclk()
                elif (cube[1][2][1] == 4 and cube[2][2][1] == 2):
                    yellowAclk()
                elif (cube[1][1][0] == 4 and cube[4][2][1] == 2):
                    yellowclk()
                    yellowclk()
                if (cube[1][1][2] == 4 and cube[5][2][1] == 2):
                    redr()
            print("Red Blue is solved")
            # Blue Orange Piece
            if (not (cube[4][1][2] == 4 and cube[3][1][0] == 3)):
                # Search 2nd Layer
                if (cube[2][1][2] == 4 and cube[4][1][0] == 3):
                    redr()
                elif (cube[3][1][2] == 4 and cube[5][1][0] == 3):
                    oranger()
                elif (cube[5][1][2] == 4 and cube[2][1][0] == 3):
                    greenr()
                elif (cube[2][1][2] == 3 and cube[4][1][0] == 4):
                    bluel()
                elif (cube[3][1][2] == 3 and cube[5][1][0] == 4):
                    greenl()
                elif (cube[5][1][2] == 3 and cube[2][1][0] == 4):
                    redl()
                elif (cube[4][1][2] == 3 and cube[3][1][0] == 4):
                    orangel()
            # Search 3rd Layer
                if (cube[1][0][1] == 4 and cube[3][2][1] == 3):
                    yellowclk()
                elif (cube[1][2][1] == 4 and cube[2][2][1] == 3):
                    yellowAclk()
                elif (cube[1][1][0] == 4 and cube[4][2][1] == 3):
                    yellowclk()
                    yellowclk()
                if (cube[1][1][2] == 4 and cube[5][2][1] == 3):
                    orangel()
                if (cube[1][0][1] == 3 and cube[3][2][1] == 4):
                    yellowclk()
                    yellowclk()
                elif (cube[1][1][2] == 3 and cube[5][2][1] == 4):
                    yellowclk()
                elif (cube[1][1][0] == 3 and cube[4][2][1] == 4):
                    yellowAclk()
                if (cube[1][2][1] == 3 and cube[2][2][1] == 4):
                    bluer()
            print("Blue Orange is solved")
            # Orange Green Piece
            if (not (cube[3][1][2] == 3 and cube[5][1][0] == 5)):
                # Search 2nd Layer
                if (cube[2][1][2] == 3 and cube[4][1][0] == 5):
                    redr()
                elif (cube[4][1][2] == 3 and cube[3][1][0] == 5):
                    bluer()
                elif (cube[5][1][2] == 3 and cube[2][1][0] == 5):
                    greenr()
                elif (cube[2][1][2] == 5 and cube[4][1][0] == 3):
                    bluel()
                elif (cube[4][1][2] == 5 and cube[3][1][0] == 3):
                    orangel()
                elif (cube[5][1][2] == 5 and cube[2][1][0] == 3):
                    redl()
                elif (cube[3][1][2] == 5 and cube[5][1][0] == 3):
                    greenl()
            # Search 3rd Layer
                if (cube[1][0][1] == 3 and cube[3][2][1] == 5):
                    yellowclk()
                    yellowclk()
                elif (cube[1][1][2] == 3 and cube[5][2][1] == 5):
                    yellowclk()
                elif (cube[1][1][0] == 3 and cube[4][2][1] == 5):
                    yellowAclk()
                if (cube[1][2][1] == 3 and cube[2][2][1] == 5):
                    greenl()
                if (cube[1][0][1] == 5 and cube[3][2][1] == 3):
                    yellowAclk()
                elif (cube[1][1][2] == 5 and cube[5][2][1] == 3):
                    yellowclk()
                    yellowclk()
                elif (cube[1][2][1] == 5 and cube[2][2][1] == 3):
                    yellowclk()
                if (cube[1][1][0] == 5 and cube[4][2][1] == 3):
                    oranger()
            print("Orange Green is solved")
            # Green Red Piece
            if (not (cube[5][1][2] == 5 and cube[2][1][0] == 2)):
                # Search 2nd Layer
                if (cube[2][1][2] == 5 and cube[4][1][0] == 2):
                    redr()
                elif (cube[4][1][2] == 5 and cube[3][1][0] == 2):
                    bluer()
                elif (cube[3][1][2] == 5 and cube[5][1][0] == 2):
                    oranger()
                elif (cube[2][1][2] == 2 and cube[4][1][0] == 5):
                    bluel()
                elif (cube[4][1][2] == 2 and cube[3][1][0] == 5):
                    orangel()
                elif (cube[3][1][2] == 2 and cube[5][1][0] == 5):
                    greenl()
                elif (cube[5][1][2] == 2 and cube[2][1][0] == 5):
                    redl()
            # Search 3rd Layer
                if (cube[1][0][1] == 5 and cube[3][2][1] == 2):
                    yellowAclk()
                elif (cube[1][1][2] == 5 and cube[5][2][1] == 2):
                    yellowclk()
                    yellowclk()
                elif (cube[1][2][1] == 5 and cube[2][2][1] == 2):
                    yellowclk()
                if (cube[1][1][0] == 5 and cube[4][2][1] == 2):
                    redl()
                if (cube[1][1][2] == 2 and cube[5][2][1] == 5):
                    yellowAclk()
                elif (cube[1][2][1] == 2 and cube[2][2][1] == 5):
                    yellowclk()
                    yellowclk()
                elif (cube[1][1][0] == 2 and cube[4][2][1] == 5):
                    yellowclk()
                if (cube[1][0][1] == 2 and cube[3][2][1] == 5):
                    greenr()
            print("Green Red is solved")

        # Check yellow piece on yellow face
        yellowedges = []
        if (cube[1][0][1] == 1):
            yellowedges.append(2)
        if (cube[1][1][0] == 1):
            yellowedges.append(4)
        if (cube[1][1][2] == 1):
            yellowedges.append(6)
        if (cube[1][2][1] == 1):
            yellowedges.append(8)
        # Solve for yellow cross
        if (not (len(yellowedges) == 4)):
            # For no yellow corners on yellow face
            if (len(yellowedges) == 0):
                for i in range(1, 3):
                    redclk()
                    greenclk()
                    yellowclk()
                    greenAclk()
                    yellowAclk()
                    redAclk()
                blueclk()
                redclk()
                yellowclk()
                redAclk()
                yellowAclk()
                blueAclk()
            # For L and | yellow corners in yellow face
            elif (len(yellowedges) == 2):
                if (cube[1][1][2] == 1 and cube[1][0][1] == 1):
                    yellowAclk()
                elif (cube[1][1][0] == 1 and cube[1][2][1] == 1):
                    yellowclk()
                if ((cube[1][0][1] == 1 and cube[1][1][0] == 1) or (cube[1][1][2] == 1 and cube[1][2][1] == 1)):
                    redclk()
                    greenclk()
                    yellowclk()
                    greenAclk()
                    yellowAclk()
                    redAclk()
                if (cube[1][0][1] == 1 and cube[1][2][1] == 1):
                    yellowAclk()
                if (cube[1][1][0] == 1 and cube[1][1][2] == 1):
                    redclk()
                    greenclk()
                    yellowclk()
                    greenAclk()
                    yellowAclk()
                    redAclk()
        print("Yellow Cross is formed")
        # Aligning the cross with their respective faces
        # ycross() = []
        # ycross().append(cube[2][2][1])
        # ycross().append(cube[3][2][1])
        # ycross().append(cube[4][2][1])
        # ycross().append(cube[5][2][1])
        # ilst = [2, 4, 3, 5]
        # ind = ycross().index(2)
        # temp = ycross()[0:ind]
        # ycross() = ycross()[ind:] + temp
        # print("ycross() = ",ycross() == ilst)
        # if (not (ycross() == ilst)):
        # ycross() = ycross()()
        if (ycross() == [5, 4, 3, 2] or ycross() == [3, 2, 4, 5] or ycross() == [4, 5, 2, 3] or ycross() == [2, 3, 5, 4]):
            greenclk()
            yellowclk()
            yellowclk()
            greenAclk()
            yellowAclk()
            greenclk()
            yellowAclk()
            greenAclk()
        # ycross() = ycross()()

        side = -3
        if (ycross() == [4, 2, 3, 5] or ycross() == [3, 4, 5, 2] or ycross() == [5, 3, 2, 4] or ycross() == [2, 5, 4, 3]):
            # 1. blue orange
            # 2. orange green
            # 3. green red
            # 4. red blue
            yellowclk()
            side = 1
        elif (ycross() == [3, 5, 2, 4] or ycross() == [5, 2, 4, 3] or ycross() == [2, 4, 3, 5] or ycross() == [4, 3, 5, 2]):
            yellowAclk()
            side = -1
        # ycross() = ycross()()
        if (side == 1 or ycross() == [5, 3, 4, 2] or ycross() == [2, 5, 3, 4] or ycross() == [4, 2, 5, 3] or ycross() == [3, 4, 2, 5]):
            greenclk()
            yellowclk()
            yellowclk()
            greenAclk()
            yellowAclk()
            greenclk()
            yellowAclk()
            greenAclk()
        elif (side == -1 or ycross() == [2, 4, 5, 3] or ycross() == [4, 3, 2, 5] or ycross() == [3, 5, 4, 2] or ycross() == [5, 2, 3, 4]):
            blueAclk()
            yellowclk()
            yellowclk()
            blueclk()
            yellowclk()
            blueAclk()
            yellowclk()
            blueclk()
        print("Yellow Cross is aligned")
        # ycross() = ycross()()
        if (ycross() == [4, 5, 3, 2]):
            yellowclk()
        elif (ycross() == [5, 4, 2, 3]):
            yellowAclk()
        elif (ycross() == [3, 2, 5, 4]):
            yellowclk()
            yellowclk()
    # 3rd layer corners
        if (not (np.array_equal(cube[1], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) and np.array_equal(cube[2][2], [2, 2, 2]) and np.array_equal(cube[3][2], [3, 3, 3]) and np.array_equal(cube[4][2], [4, 4, 4]))):
            # corners aligning in right position

            # Red Blue
            if ((cube[2][2][2] == 2 and cube[1][2][0] == 5 and cube[4][2][0] == 1) or (cube[2][2][2] == 5 and cube[1][2][0] == 1 and cube[4][2][0] == 2) or (cube[2][2][2] == 1 and cube[1][2][0] == 2 and cube[4][2][0] == 5)):
                redclk()
                yellowAclk()
                orangeAclk()
                yellowclk()
                redAclk()
                yellowAclk()
                orangeclk()
                yellowclk()

        # Blue Orange
            elif ((cube[4][2][2] == 2 and cube[1][0][0] == 5 and cube[3][2][0] == 1) or (cube[4][2][2] == 1 and cube[1][0][0] == 2 and cube[3][2][0] == 5) or (cube[4][2][2] == 5 and cube[1][0][0] == 1 and cube[3][2][0] == 2)):
                redAclk()
                yellowclk()
                orangeclk()
                yellowAclk()
                redclk()
                yellowclk()
                orangeAclk()
                yellowAclk()

            # Orange Green
            elif ((cube[3][2][2] == 1 and cube[1][0][2] == 2 and cube[5][2][0] == 5) or (cube[3][2][2] == 5 and cube[1][0][2] == 1 and cube[5][2][0] == 2) or (cube[3][2][2] == 2 and cube[1][0][2] == 5 and cube[5][2][0] == 1)):
                greenAclk()
                yellowclk()
                blueclk()
                yellowAclk()
                greenclk()
                yellowclk()
                blueAclk()
                yellowAclk()
            while (not ((cube[2][2][2] == 4 and cube[1][2][0] == 2 and cube[4][2][0] == 1) or (cube[2][2][2] == 1 and cube[1][2][0] == 4 and cube[4][2][0] == 2) or (cube[2][2][2] == 2 and cube[1][2][0] == 1 and cube[4][2][0] == 4))):
                blueAclk()
                yellowclk()
                greenclk()
                yellowAclk()
                blueclk()
                yellowclk()
                greenAclk()
                yellowAclk()
        # corner aligning in right orientation
            # red green orange

            while(not (np.array_equal(cube, [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]], [[3, 3, 3], [3, 3, 3], [3, 3, 3]], [[4, 4, 4], [4, 4, 4], [4, 4, 4]], [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]))):
                if ((cube[1][0][0] == 1 and cube[1][0][2] == 5 and cube[1][2][2] == 5 and cube[1][2][0] == 1 and np.array_equal(cube[4][2], [4, 4, 4])) or (cube[5][2][2] == 2 and cube[1][2][2] == 5 and cube[2][2][0] == 1 and cube[4][2][2] == 3 and cube[1][0][0] == 4 and cube[3][2][0] == 1) or (cube[2][2][2] == 1 and cube[1][2][0] == 4 and cube[4][2][0] == 2 and cube[3][2][2] == 1 and cube[1][0][2] == 5 and cube[5][2][0] == 3)):
                    greenclk()
                    yellowclk()
                    yellowclk()
                    greenAclk()
                    yellowAclk()
                    greenclk()
                    yellowAclk()
                    greenAclk()
                    blueAclk()
                    yellowclk()
                    yellowclk()
                    blueclk()
                    yellowclk()
                    blueAclk()
                    yellowclk()
                    blueclk()
                if ((cube[1][0][0] == 1 and cube[1][0][2] == 3 and cube[1][2][2] == 2 and cube[1][2][0] == 1 and np.array_equal(cube[4][2], [4, 4, 4])) or (cube[5][2][2] == 1 and cube[1][2][2] == 2 and cube[2][2][0] == 5 and cube[4][2][2] == 3 and cube[1][0][0] == 4 and cube[3][2][0] == 1) or (cube[2][2][2] == 1 and cube[1][2][0] == 4 and cube[4][2][0] == 2 and cube[3][2][2] == 5 and cube[1][0][2] == 3 and cube[5][2][0] == 1)):
                    greenclk()
                    yellowclk()
                    yellowclk()
                    greenAclk()
                    yellowAclk()
                    greenclk()
                    yellowAclk()
                    greenAclk()
                    blueAclk()
                    yellowclk()
                    yellowclk()
                    blueclk()
                    yellowclk()
                    blueAclk()
                    yellowclk()
                    blueclk()
                print("Red green orange is aligned")
                # green orange blue
                if ((cube[1][2][0] == 1 and cube[1][0][2] == 3 and cube[1][0][0] == 3 and cube[1][2][2] == 1 and np.array_equal(cube[2][2], [2, 2, 2])) or (cube[3][2][2] == 5 and cube[1][0][2] == 3 and cube[5][2][0] == 1 and cube[2][2][2] == 4 and cube[1][2][0] == 2 and cube[4][2][0] == 1)):
                    orangeclk()
                    yellowclk()
                    yellowclk()
                    orangeAclk()
                    yellowAclk()
                    orangeclk()
                    yellowAclk()
                    orangeAclk()
                    redAclk()
                    yellowclk()
                    yellowclk()
                    redclk()
                    yellowclk()
                    redAclk()
                    yellowclk()
                    redclk()
                if ((cube[1][2][0] == 1 and cube[1][0][2] == 5 and cube[1][0][0] == 4 and cube[1][2][2] == 1 and np.array_equal(cube[2][2], [2, 2, 2])) or (cube[3][2][2] == 1 and cube[1][0][2] == 5 and cube[5][2][0] == 3 and cube[2][2][2] == 4 and cube[1][2][0] == 2 and cube[4][2][0] == 1)):
                    orangeclk()
                    yellowclk()
                    yellowclk()
                    orangeAclk()
                    yellowAclk()
                    orangeclk()
                    yellowAclk()
                    orangeAclk()
                    redAclk()
                    yellowclk()
                    yellowclk()
                    redclk()
                    yellowclk()
                    redAclk()
                    yellowclk()
                    redclk()
                print("Green orange blue is aligned")
                # orange blue red
                # or (cube[3][2][2] == 1 and cube[1][0][2] == 5 and cube[5][2][0] == 3 and cube[2][2][2] == 1 and cube[1][2][0] == 4 and cube[4][2][0] == 2)):
                if ((cube[1][0][2] == 1 and cube[1][0][0] == 4 and cube[1][2][0] == 4 and cube[1][2][2] == 1 and np.array_equal(cube[5][2], [5, 5, 5]))):
                    blueclk()
                    yellowclk()
                    yellowclk()
                    blueAclk()
                    yellowAclk()
                    blueclk()
                    yellowAclk()
                    blueAclk()
                    greenAclk()
                    yellowclk()
                    yellowclk()
                    greenclk()
                    yellowclk()
                    greenAclk()
                    yellowclk()
                    greenclk()
                if ((cube[1][0][2] == 1 and cube[1][0][0] == 3 and cube[1][2][0] == 2 and cube[1][2][2] == 1 and np.array_equal(cube[5][2], [5, 5, 5])) or (cube[3][2][2] == 1 and cube[1][0][2] == 5 and cube[5][2][0] == 3 and cube[2][2][2] == 4 and cube[1][2][0] == 2 and cube[4][2][0] == 1)):
                    blueclk()
                    yellowclk()
                    yellowclk()
                    blueAclk()
                    yellowAclk()
                    blueclk()
                    yellowAclk()
                    blueAclk()
                    greenAclk()
                    yellowclk()
                    yellowclk()
                    greenclk()
                    yellowclk()
                    greenAclk()
                    yellowclk()
                    greenclk()
                print("Orange blue red is aligned")
                # blue red green
                if ((cube[1][0][0] == 1 and cube[1][2][0] == 2 and cube[1][2][2] == 2 and cube[1][0][2] == 1 and np.array_equal(cube[3][2], [3, 3, 3])) or (cube[2][2][2] == 4 and cube[1][2][0] == 2 and cube[4][2][0] == 1 and cube[3][2][2] == 1 and cube[1][0][2] == 5 and cube[5][2][0] == 3) or (cube[4][2][2] == 1 and cube[1][0][0] == 3 and cube[3][2][0] == 4 and cube[5][2][2] == 1 and cube[1][2][2] == 2 and cube[2][2][0] == 5)):
                    redclk()
                    yellowclk()
                    yellowclk()
                    redAclk()
                    yellowAclk()
                    redclk()
                    yellowAclk()
                    redAclk()
                    orangeAclk()
                    yellowclk()
                    yellowclk()
                    orangeclk()
                    yellowclk()
                    orangeAclk()
                    yellowclk()
                    orangeclk()
                if ((cube[1][0][0] == 1 and cube[1][2][0] == 4 and cube[1][2][2] == 5 and cube[1][0][2] == 1 and np.array_equal(cube[3][2], [3, 3, 3])) or (cube[2][2][2] == 1 and cube[1][2][0] == 4 and cube[4][2][0] == 2 and cube[3][2][2] == 1 and cube[1][0][2] == 5 and cube[5][2][0] == 3) or (cube[4][2][2] == 1 and cube[1][0][0] == 3 and cube[3][2][0] == 4 and cube[5][2][2] == 2 and cube[1][2][2] == 5 and cube[2][2][0] == 1)):
                    redclk()
                    yellowclk()
                    yellowclk()
                    redAclk()
                    yellowAclk()
                    redclk()
                    yellowAclk()
                    redAclk()
                    orangeAclk()
                    yellowclk()
                    yellowclk()
                    orangeclk()
                    yellowclk()
                    orangeAclk()
                    yellowclk()
                    orangeclk()
                print("Blue red green is aligned")
        move_length.append(len(final_moves)-500)
        
        #print("Length of Optimised Final Moves ", len(ofinal_moves))
        for i in range(0, 6):
            print(str(np.ravel(list(iconfig[i]))).replace(
                " ", "").replace("]", "").replace("[", ""))
        print("Loop Count = ", loopcount)
        if (np.array_equal(cube, [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]], [[3, 3, 3], [3, 3, 3], [3, 3, 3]], [[4, 4, 4], [4, 4, 4], [4, 4, 4]], [[5, 5, 5], [5, 5, 5], [5, 5, 5]]])):
            print("")
            print("Cube is Solved !!")
            print("Average Length of Final Moves ", mean(move_length))
            #np.average(move_length, axis=0))
        else:
            print("Error found!!")
            print(cube)
            break
        #if time.process_time()>=10:
        #   break
