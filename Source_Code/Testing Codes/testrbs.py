# turn algorithm
import numpy as np

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


def prnt():
    print("white ", cube[0])
    print("yellow", cube[1])
    print("red   ", cube[2])
    print("orange", cube[3])
    print("blue  ", cube[4])
    print("green ", cube[5])


def clockwise(face):
    face[0], face[2] = face[2].copy(), face[0].copy()
    print("Clockwise")
    return np.transpose(face)


def anticlockwise(face):
    face = np.transpose(face)
    face[0], face[2] = face[2].copy(), face[0].copy()
    print("Anticlockwise")
    return face


def whiteclk():

    print("White ", end="")
    newredArray = cube[2]
    cube[2][0], cube[4][0], cube[3][0], cube[5][0] = cube[4][0].copy(
    ), cube[3][0].copy(), cube[5][0].copy(), cube[2][0].copy()
    cube[0] = clockwise(cube[0])


def whiteAclk():

    print("White ", end="")
    cube[2][0], cube[4][0], cube[3][0], cube[5][0] = cube[5][0].copy(
    ), cube[2][0].copy(), cube[4][0].copy(), cube[3][0].copy()
    cube[0] = anticlockwise(cube[0])


def yellowclk():

    print("Yellow ", end="")
    cube[2][2], cube[4][2], cube[3][2], cube[5][2] = cube[5][2].copy(
    ), cube[2][2].copy(), cube[4][2].copy(), cube[3][2].copy()
    cube[1] = clockwise(cube[1])


def yellowAclk():

    print("Yellow ", end="")
    cube[2][2], cube[4][2], cube[3][2], cube[5][2] = cube[4][2].copy(
    ), cube[3][2].copy(), cube[5][2].copy(), cube[2][2].copy()
    cube[1] = anticlockwise(cube[1])


def redclk():

    print("Red ", end="")
    cube[0][2][0], cube[4][0][0], cube[1][2][0], cube[5][2][2] = cube[5][2][2].copy(
    ), cube[0][2][0].copy(), cube[4][0][0].copy(), cube[1][2][0].copy()
    cube[0][2][1], cube[4][1][0], cube[1][2][1], cube[5][1][2] = cube[5][1][2].copy(
    ), cube[0][2][1].copy(), cube[4][1][0].copy(), cube[1][2][1].copy()
    cube[0][2][2], cube[4][2][0], cube[1][2][2], cube[5][0][2] = cube[5][0][2].copy(
    ), cube[0][2][2].copy(), cube[4][2][0].copy(), cube[1][2][2].copy()
    cube[2] = clockwise(cube[2])


def redAclk():

    print("Red ", end="")
    cube[0][2][0], cube[4][0][0], cube[1][2][0], cube[5][2][2] = cube[4][0][0].copy(
    ), cube[1][2][0].copy(), cube[5][2][2].copy(), cube[0][2][0].copy()
    cube[0][2][1], cube[4][1][0], cube[1][2][1], cube[5][1][2] = cube[4][1][0].copy(
    ), cube[1][2][1].copy(), cube[5][1][2].copy(), cube[0][2][1].copy()
    cube[0][2][2], cube[4][2][0], cube[1][2][2], cube[5][0][2] = cube[4][2][0].copy(
    ), cube[1][2][2].copy(), cube[5][0][2].copy(), cube[0][2][2].copy()
    cube[2] = anticlockwise(cube[2])


def orangeclk():

    print("Orange ", end="")
    cube[0][0][0], cube[4][0][2], cube[1][0][0], cube[5][2][0] = cube[4][0][2].copy(
    ), cube[1][0][0].copy(), cube[5][2][0].copy(), cube[0][0][0].copy()
    cube[0][0][1], cube[4][1][2], cube[1][0][1], cube[5][1][0] = cube[4][1][2].copy(
    ), cube[1][0][1].copy(), cube[5][1][0].copy(), cube[0][0][1].copy()
    cube[0][0][2], cube[4][2][2], cube[1][0][2], cube[5][0][0] = cube[4][2][2].copy(
    ), cube[1][0][2].copy(), cube[5][0][0].copy(), cube[0][0][2].copy()
    cube[3] = clockwise(cube[3])


def orangeAclk():

    print("Orange ", end="")
    cube[0][0][0], cube[4][0][2], cube[1][0][0], cube[5][2][0] = cube[5][2][0].copy(
    ), cube[0][0][0].copy(), cube[4][0][2].copy(), cube[1][0][0].copy()
    cube[0][0][1], cube[4][1][2], cube[1][0][1], cube[5][1][0] = cube[5][1][0].copy(
    ), cube[0][0][1].copy(), cube[4][1][2].copy(), cube[1][0][1].copy()
    cube[0][0][2], cube[4][2][2], cube[1][0][2], cube[5][0][0] = cube[5][0][0].copy(
    ), cube[0][0][2].copy(), cube[4][2][2].copy(), cube[1][0][2].copy()
    cube[3] = anticlockwise(cube[3])


def blueclk():

    print("Blue ", end="")
    cube[0][0][2], cube[2][0][2], cube[1][2][0], cube[3][2][0] = cube[2][0][2].copy(
    ), cube[1][2][0].copy(), cube[3][2][0].copy(), cube[0][0][2].copy()
    cube[0][1][2], cube[2][1][2], cube[1][1][0], cube[3][1][0] = cube[2][1][2].copy(
    ), cube[1][1][0].copy(), cube[3][1][0].copy(), cube[0][1][2].copy()
    cube[0][2][2], cube[2][2][2], cube[1][0][0], cube[3][0][0] = cube[2][2][2].copy(
    ), cube[1][0][0].copy(), cube[3][0][0].copy(), cube[0][2][2].copy()
    cube[4] = clockwise(cube[4])


def blueAclk():

    print("Blue ", end="")
    cube[0][0][2], cube[2][0][2], cube[1][2][0], cube[3][2][0] = cube[3][2][0].copy(
    ), cube[0][0][2].copy(), cube[2][0][2].copy(), cube[1][2][0].copy()
    cube[0][1][2], cube[2][1][2], cube[1][1][0], cube[3][1][0] = cube[3][1][0].copy(
    ), cube[0][1][2].copy(), cube[2][1][2].copy(), cube[1][1][0].copy()
    cube[0][2][2], cube[2][2][2], cube[1][0][0], cube[3][0][0] = cube[3][0][0].copy(
    ), cube[0][2][2].copy(), cube[2][2][2].copy(), cube[1][0][0].copy()
    cube[4] = anticlockwise(cube[4])


def greenclk():

    print("Green ", end="")
    cube[0][0][0], cube[2][0][0], cube[1][2][2], cube[3][2][2] = cube[3][2][2].copy(
    ), cube[0][0][0].copy(), cube[2][0][0].copy(), cube[1][2][2].copy()
    cube[0][1][0], cube[2][1][0], cube[1][1][2], cube[3][1][2] = cube[3][1][2].copy(
    ), cube[0][1][0].copy(), cube[2][1][0].copy(), cube[1][1][2].copy()
    cube[0][2][0], cube[2][2][0], cube[1][0][2], cube[3][0][2] = cube[3][0][2].copy(
    ), cube[0][2][0].copy(), cube[2][2][0].copy(), cube[1][0][2].copy()
    cube[5] = clockwise(cube[5])


def greenAclk():

    print("Green ", end="")
    cube[0][0][0], cube[2][0][0], cube[1][2][2], cube[3][2][2] = cube[2][0][0].copy(
    ), cube[1][2][2].copy(), cube[3][2][2].copy(), cube[0][0][0].copy()
    cube[0][1][0], cube[2][1][0], cube[1][1][2], cube[3][1][2] = cube[2][1][0].copy(
    ), cube[1][1][2].copy(), cube[3][1][2].copy(), cube[0][1][0].copy()
    cube[0][2][0], cube[2][2][0], cube[1][0][2], cube[3][0][2] = cube[2][2][0].copy(
    ), cube[1][0][2].copy(), cube[3][0][2].copy(), cube[0][2][0].copy()
    cube[5] = anticlockwise(cube[5])


if __name__ == "__main__":
    ip = []
    colour = ["white", "yellow", "red", "orange", "blue", "green"]
    for i in range(0, 6):
        print("Input", colour[i], "face  ", end="")
        inp = input()
        inparr = []
        cnt = 0
        for j in range(0, 3):
            inparr0 = []
            for k in range(0, 3):
                inparr0.append(int(inp[cnt]))
                cnt += 1
            inparr.append(inparr0)
        ip.append(inparr)
    # ip = [[[5, 4, 5], [3, 0, 4], [4, 1, 4]], [[4, 1, 4], [3, 1, 2], [5, 2, 5]], [[1, 5, 1], [2, 2, 5], [1, 0, 1]], [
    #    [0, 0, 0], [2, 3, 1], [0, 3, 0]], [[3, 3, 2], [0, 4, 4], [3, 5, 2]], [[3, 0, 2], [4, 5, 1], [3, 5, 2]]]
    cube = np.array(ip)
    #All callable functions
    #  whiteclk()
    #  whiteAclk()
    #  yellowclk()
    yellowAclk()
    redclk()
    #  redAclk()
    #  orangeclk()
    #  orangeAclk()
    #  blueclk()
    #  blueAclk()
    #  greenclk()
    #  greenAclk()
    prnt()