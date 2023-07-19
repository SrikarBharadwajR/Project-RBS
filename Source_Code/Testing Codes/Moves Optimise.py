
final_moves = [3, 4, 11, 14, 2, 2, 2, 5, 5, 13,
               3, 3, 14, 3, 3, 3, 4, 1, 4, 5, 3, 1, 13, 5, 5]
colour = ["white", "yellow", "red", "orange", "blue", "green"]
ofinal_moves = final_moves.copy()
while (True):
    fm = []
    c = 0
    i = 0
    while(i< len(ofinal_moves)):
        if ((i < len(ofinal_moves)-3) and ofinal_moves[i] == ofinal_moves[i+1] and ofinal_moves[i+1] == ofinal_moves[i+2]):
            c += 1
            if (len(str(ofinal_moves[i])) == 1):
                fm.append(int(ofinal_moves[i]+10))
            if (len(str(ofinal_moves[i])) == 2):
                fm.append(int(ofinal_moves[i]-10))
            i = i+2
        elif ((i < len(ofinal_moves)-1) and str(ofinal_moves[i])[-1] == str(ofinal_moves[i+1])[-1] and ofinal_moves[i] != ofinal_moves[i+1]):
            c += 1
            i = i+1
        else:
            fm.append(ofinal_moves[i])
        print(fm)
        i+=1
    ofinal_moves = fm.copy()
    if (c == 0):
       break
    
print("Optimised Moves")
print(ofinal_moves)
for i in range(0, len(ofinal_moves)):
    b = str(ofinal_moves[i])
    print(colour[int(b[-1])], end=" ")
    if (len(str(ofinal_moves[i])) == 1):
        print("Clockwise")
    else:
        print("AntiClockwise")

print("Length of Final Moves ", len(final_moves))
print("Length of Optimised Final Moves ", len(ofinal_moves))
