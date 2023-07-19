# turn algorithm
import random
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
cube = np.array(
    [[[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []]]
)
final_moves = []
stepcount = 0


def prnt():
    global stepcount
    print(stepcount, end=" :")
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
    print("")
    cube[2][0], cube[4][0], cube[3][0], cube[5][0] = (
        cube[4][0].copy(),
        cube[3][0].copy(),
        cube[5][0].copy(),
        cube[2][0].copy(),
    )
    cube[0] = clockwise(cube[0].copy())
    final_moves.append(0)
    print("White Clockwise -")
    prnt()


def whiteAclk():
    print("")
    cube[2][0], cube[4][0], cube[3][0], cube[5][0] = (
        cube[5][0].copy(),
        cube[2][0].copy(),
        cube[4][0].copy(),
        cube[3][0].copy(),
    )
    cube[0] = anticlockwise(cube[0].copy())
    final_moves.append(10)
    print("White Anticlockwise -")
    prnt()


def yellowclk():
    print("")
    cube[2][2], cube[4][2], cube[3][2], cube[5][2] = (
        cube[5][2].copy(),
        cube[2][2].copy(),
        cube[4][2].copy(),
        cube[3][2].copy(),
    )
    cube[1] = clockwise(cube[1].copy())
    final_moves.append(1)
    print("Yellow Clockwise -")
    prnt()


def yellowAclk():
    print("")
    cube[2][2], cube[4][2], cube[3][2], cube[5][2] = (
        cube[4][2].copy(),
        cube[3][2].copy(),
        cube[5][2].copy(),
        cube[2][2].copy(),
    )
    cube[1] = anticlockwise(cube[1].copy())
    final_moves.append(11)
    print("Yellow Anticlockwise -")
    prnt()


def redclk():
    print("")
    cube[0][2][0], cube[4][0][0], cube[1][2][0], cube[5][2][2] = (
        cube[5][2][2].copy(),
        cube[0][2][0].copy(),
        cube[4][0][0].copy(),
        cube[1][2][0].copy(),
    )
    cube[0][2][1], cube[4][1][0], cube[1][2][1], cube[5][1][2] = (
        cube[5][1][2].copy(),
        cube[0][2][1].copy(),
        cube[4][1][0].copy(),
        cube[1][2][1].copy(),
    )
    cube[0][2][2], cube[4][2][0], cube[1][2][2], cube[5][0][2] = (
        cube[5][0][2].copy(),
        cube[0][2][2].copy(),
        cube[4][2][0].copy(),
        cube[1][2][2].copy(),
    )
    cube[2] = clockwise(cube[2].copy())
    final_moves.append(2)
    print("Red Clockwise -")
    prnt()


def redAclk():
    print("")
    cube[0][2][0], cube[4][0][0], cube[1][2][0], cube[5][2][2] = (
        cube[4][0][0].copy(),
        cube[1][2][0].copy(),
        cube[5][2][2].copy(),
        cube[0][2][0].copy(),
    )
    cube[0][2][1], cube[4][1][0], cube[1][2][1], cube[5][1][2] = (
        cube[4][1][0].copy(),
        cube[1][2][1].copy(),
        cube[5][1][2].copy(),
        cube[0][2][1].copy(),
    )
    cube[0][2][2], cube[4][2][0], cube[1][2][2], cube[5][0][2] = (
        cube[4][2][0].copy(),
        cube[1][2][2].copy(),
        cube[5][0][2].copy(),
        cube[0][2][2].copy(),
    )
    cube[2] = anticlockwise(cube[2].copy())
    final_moves.append(12)
    print("Red Anticlockwise -")
    prnt()


def orangeclk():
    print("")
    cube[0][0][0], cube[4][0][2], cube[1][0][0], cube[5][2][0] = (
        cube[4][0][2].copy(),
        cube[1][0][0].copy(),
        cube[5][2][0].copy(),
        cube[0][0][0].copy(),
    )
    cube[0][0][1], cube[4][1][2], cube[1][0][1], cube[5][1][0] = (
        cube[4][1][2].copy(),
        cube[1][0][1].copy(),
        cube[5][1][0].copy(),
        cube[0][0][1].copy(),
    )
    cube[0][0][2], cube[4][2][2], cube[1][0][2], cube[5][0][0] = (
        cube[4][2][2].copy(),
        cube[1][0][2].copy(),
        cube[5][0][0].copy(),
        cube[0][0][2].copy(),
    )
    cube[3] = clockwise(cube[3].copy())
    final_moves.append(3)
    print("Orange Clockwise -")
    prnt()


def orangeAclk():
    print("")
    cube[0][0][0], cube[4][0][2], cube[1][0][0], cube[5][2][0] = (
        cube[5][2][0].copy(),
        cube[0][0][0].copy(),
        cube[4][0][2].copy(),
        cube[1][0][0].copy(),
    )
    cube[0][0][1], cube[4][1][2], cube[1][0][1], cube[5][1][0] = (
        cube[5][1][0].copy(),
        cube[0][0][1].copy(),
        cube[4][1][2].copy(),
        cube[1][0][1].copy(),
    )
    cube[0][0][2], cube[4][2][2], cube[1][0][2], cube[5][0][0] = (
        cube[5][0][0].copy(),
        cube[0][0][2].copy(),
        cube[4][2][2].copy(),
        cube[1][0][2].copy(),
    )
    cube[3] = anticlockwise(cube[3].copy())
    final_moves.append(13)
    print("Orange Anticlockwise -")
    prnt()


def blueclk():
    print("")
    cube[0][0][2], cube[2][0][2], cube[1][2][0], cube[3][2][0] = (
        cube[2][0][2].copy(),
        cube[1][2][0].copy(),
        cube[3][2][0].copy(),
        cube[0][0][2].copy(),
    )
    cube[0][1][2], cube[2][1][2], cube[1][1][0], cube[3][1][0] = (
        cube[2][1][2].copy(),
        cube[1][1][0].copy(),
        cube[3][1][0].copy(),
        cube[0][1][2].copy(),
    )
    cube[0][2][2], cube[2][2][2], cube[1][0][0], cube[3][0][0] = (
        cube[2][2][2].copy(),
        cube[1][0][0].copy(),
        cube[3][0][0].copy(),
        cube[0][2][2].copy(),
    )
    cube[4] = clockwise(cube[4].copy())
    final_moves.append(4)
    print("Blue Clockwise -")
    prnt()


def blueAclk():
    print("")
    cube[0][0][2], cube[2][0][2], cube[1][2][0], cube[3][2][0] = (
        cube[3][2][0].copy(),
        cube[0][0][2].copy(),
        cube[2][0][2].copy(),
        cube[1][2][0].copy(),
    )
    cube[0][1][2], cube[2][1][2], cube[1][1][0], cube[3][1][0] = (
        cube[3][1][0].copy(),
        cube[0][1][2].copy(),
        cube[2][1][2].copy(),
        cube[1][1][0].copy(),
    )
    cube[0][2][2], cube[2][2][2], cube[1][0][0], cube[3][0][0] = (
        cube[3][0][0].copy(),
        cube[0][2][2].copy(),
        cube[2][2][2].copy(),
        cube[1][0][0].copy(),
    )
    cube[4] = anticlockwise(cube[4].copy())
    final_moves.append(14)
    print("Blue Anticlockwise -")
    prnt()


def greenclk():
    print("")
    cube[0][0][0], cube[2][0][0], cube[1][2][2], cube[3][2][2] = (
        cube[3][2][2].copy(),
        cube[0][0][0].copy(),
        cube[2][0][0].copy(),
        cube[1][2][2].copy(),
    )
    cube[0][1][0], cube[2][1][0], cube[1][1][2], cube[3][1][2] = (
        cube[3][1][2].copy(),
        cube[0][1][0].copy(),
        cube[2][1][0].copy(),
        cube[1][1][2].copy(),
    )
    cube[0][2][0], cube[2][2][0], cube[1][0][2], cube[3][0][2] = (
        cube[3][0][2].copy(),
        cube[0][2][0].copy(),
        cube[2][2][0].copy(),
        cube[1][0][2].copy(),
    )
    cube[5] = clockwise(cube[5].copy())
    final_moves.append(5)
    print("Green Clockwise -")
    prnt()


def greenAclk():
    print("")
    cube[0][0][0], cube[2][0][0], cube[1][2][2], cube[3][2][2] = (
        cube[2][0][0].copy(),
        cube[1][2][2].copy(),
        cube[3][2][2].copy(),
        cube[0][0][0].copy(),
    )
    cube[0][1][0], cube[2][1][0], cube[1][1][2], cube[3][1][2] = (
        cube[2][1][0].copy(),
        cube[1][1][2].copy(),
        cube[3][1][2].copy(),
        cube[0][1][0].copy(),
    )
    cube[0][2][0], cube[2][2][0], cube[1][0][2], cube[3][0][2] = (
        cube[2][2][0].copy(),
        cube[1][0][2].copy(),
        cube[3][0][2].copy(),
        cube[0][2][0].copy(),
    )
    cube[5] = anticlockwise(cube[5].copy())
    final_moves.append(15)
    print("Green Anticlockwise -")
    prnt()


def remove(string):
    return string.replace(" ", "").replace("]", "").replace("[", "")


if __name__ == "__main__":
    cube = np.array(
        [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
            [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
            [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
        ]
    )
    for i in range(0, 1000):
        rn = random.randint(1, 12)
        if rn == 1:
            whiteclk()
        if rn == 2:
            whiteAclk()
        if rn == 3:
            redclk()
        if rn == 4:
            redAclk()
        if rn == 5:
            yellowclk()
        if rn == 6:
            yellowAclk()
        if rn == 7:
            orangeclk()
        if rn == 8:
            orangeAclk()
        if rn == 9:
            blueclk()
        if rn == 10:
            blueAclk()
        if rn == 11:
            greenclk()
        if rn == 12:
            greenAclk()
    print()
    print(remove(str(np.ravel(cube[0]))))
    print(remove(str(np.ravel(cube[1]))))
    print(remove(str(np.ravel(cube[2]))))
    print(remove(str(np.ravel(cube[3]))))
    print(remove(str(np.ravel(cube[4]))))
    print(remove(str(np.ravel(cube[5]))))
    print()
