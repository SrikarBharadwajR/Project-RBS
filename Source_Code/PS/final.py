import numpy as np
import cv2



color_no = np.array(
    [[[0, 0, 111], [255, 52, 255]],  # white
     [[15, 66, 205], [26, 255, 255]],  # yellow
     [[0, 123, 69], [5, 255, 255]],  # red
     [[6, 165, 95], [19, 255, 255]],  # orange
     [[97, 33, 31], [130, 255, 255]],  # blue
     [[37, 92, 64], [95, 255, 120]]]  # green
)
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        [x1, y1, z1], [a1, b1, c1] = color_no[0]  # calling color pixels
        [x2, y2, z2], [a2, b2, c2] = color_no[1]
        [x3, y3, z3], [a3, b3, c3] = color_no[2]
        [x4, y4, z4], [a4, b4, c4] = color_no[3]
        [x5, y5, z5], [a5, b5, c5] = color_no[4]
        [x6, y6, z6], [a6, b6, c6] = color_no[5]

    
        color = cv2.cvtColor(roi1, cv2.COLOR_BGR2HSV)  # roi1
        lower_w = np.array([x1, y1, z1])
        upper_w = np.array([a1, b1, c1])
        mask_w = cv2.inRange(color, lower_w, upper_w)
        result_w = cv2.bitwise_and(roi1, roi1, mask=mask_w)

        lower_y = np.array([x2, y2, z2])
        upper_y = np.array([a2, b2, c2])
        mask_y = cv2.inRange(color, lower_y, upper_y)
        result_y = cv2.bitwise_and(roi1, roi1, mask=mask_y)

        lower_r = np.array([x3, y3, z3])
        upper_r = np.array([a3, b3, c3])
        mask_r = cv2.inRange(color, lower_r, upper_r)
        result_r = cv2.bitwise_and(roi1, roi1, mask=mask_r)
        

        lower_o = np.array([x4, y4, z4])
        upper_o = np.array([a4, b4, c4])
        mask_o = cv2.inRange(color, lower_o, upper_o)
        result_o = cv2.bitwise_and(roi1, roi1, mask=mask_o)

        lower_b = np.array([x5, y5, z5])
        upper_b = np.array([a5, b5, c5])
        mask_b = cv2.inRange(color, lower_b, upper_b)
        result_b = cv2.bitwise_and(roi1, roi1, mask=mask_b)

        lower_g = np.array([x6, y6, z6])
        upper_g = np.array([a6, b6, c6])
        mask_g = cv2.inRange(color, lower_g, upper_g)
        result_g = cv2.bitwise_and(roi1, roi1, mask=mask_g)

        pixels_w = np.count_nonzero(result_w)
        pixels_y = np.count_nonzero(result_y)
        pixels_r = np.count_nonzero(result_r)
        pixels_o = np.count_nonzero(result_o)
        pixels_b = np.count_nonzero(result_b)
        pixels_g = np.count_nonzero(result_g)



        color2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2HSV)  # roi2
        lower_w2 = np.array([x1, y1, z1])
        upper_w2 = np.array([a1, b1, c1])
        mask_w2 = cv2.inRange(color2, lower_w2, upper_w2)
        result_w2 = cv2.bitwise_and(roi2, roi2, mask=mask_w2)

        lower_y2 = np.array([x2, y2, z2])
        upper_y2 = np.array([a2, b2, c2])
        mask_y2 = cv2.inRange(color2, lower_y2, upper_y2)
        result_y2 = cv2.bitwise_and(roi2, roi2, mask=mask_y2)

        lower_r2 = np.array([x3, y3, z3])
        upper_r2 = np.array([a3, b3, c3])
        mask_r2 = cv2.inRange(color2, lower_r2, upper_r2)
        result_r2 = cv2.bitwise_and(roi2, roi2, mask=mask_r2)

        lower_o2 = np.array([x4, y4, z4])
        upper_o2 = np.array([a4, b4, c4])
        mask_o2 = cv2.inRange(color2, lower_o2, upper_o2)
        result_o2 = cv2.bitwise_and(roi2, roi2, mask=mask_o2)

        lower_b2 = np.array([x5, y5, z5])
        upper_b2 = np.array([a5, b5, c5])
        mask_b2 = cv2.inRange(color2, lower_b2, upper_b2)
        result_b2 = cv2.bitwise_and(roi2, roi2, mask=mask_b2)

        lower_g2 = np.array([x6, y6, z6])
        upper_g2 = np.array([a6, b6, c6])
        mask_g2 = cv2.inRange(color2, lower_g2, upper_g2)
        result_g2 = cv2.bitwise_and(roi2, roi2, mask=mask_g2)

        pixels_w2 = np.count_nonzero(result_w2)
        pixels_y2 = np.count_nonzero(result_y2)
        pixels_r2 = np.count_nonzero(result_r2)
        pixels_o2 = np.count_nonzero(result_o2)
        pixels_b2 = np.count_nonzero(result_b2)
        pixels_g2 = np.count_nonzero(result_g2)

    

        color3 = cv2.cvtColor(roi3, cv2.COLOR_BGR2HSV)  # roi3
        lower_w3 = np.array([x1, y1, z1])
        upper_w3 = np.array([a1, b1, c1])
        mask_w3 = cv2.inRange(color3, lower_w3, upper_w3)
        result_w3 = cv2.bitwise_and(roi3, roi3, mask=mask_w3)

        lower_y3 = np.array([x2, y2, z2])
        upper_y3 = np.array([a2, b2, c2])
        mask_y3 = cv2.inRange(color3, lower_y3, upper_y3)
        result_y3 = cv2.bitwise_and(roi3, roi3, mask=mask_y3)

        lower_r3 = np.array([x3, y3, z3])
        upper_r3 = np.array([a3, b3, c3])
        mask_r3 = cv2.inRange(color3, lower_r3, upper_r3)
        result_r3 = cv2.bitwise_and(roi3, roi3, mask=mask_r3)

        lower_o3 = np.array([x4, y4, z4])
        upper_o3 = np.array([a4, b4, c4])
        mask_o3 = cv2.inRange(color3, lower_o3, upper_o3)
        result_o3 = cv2.bitwise_and(roi3, roi3, mask=mask_o3)

        lower_b3 = np.array([x5, y5, z5])
        upper_b3 = np.array([a5, b5, c5])
        mask_b3 = cv2.inRange(color3, lower_b3, upper_b3)
        result_b3 = cv2.bitwise_and(roi3, roi3, mask=mask_b3)

        lower_g3 = np.array([x6, y6, z6])
        upper_g3 = np.array([a6, b6, c6])
        mask_g3 = cv2.inRange(color3, lower_g3, upper_g3)
        result_g3 = cv2.bitwise_and(roi3, roi3, mask=mask_g3)

        pixels_w3 = np.count_nonzero(result_w3)
        pixels_y3 = np.count_nonzero(result_y3)
        pixels_r3 = np.count_nonzero(result_r3)
        pixels_o3 = np.count_nonzero(result_o3)
        pixels_b3 = np.count_nonzero(result_b3)
        pixels_g3 = np.count_nonzero(result_g3)

        color4 = cv2.cvtColor(roi4, cv2.COLOR_BGR2HSV)  # roi4
        lower_w4 = np.array([x1, y1, z1])
        upper_w4 = np.array([a1, b1, c1])
        mask_w4 = cv2.inRange(color4, lower_w4, upper_w4)
        result_w4 = cv2.bitwise_and(roi4, roi4, mask=mask_w4)

        lower_y4 = np.array([x2, y2, z2])
        upper_y4 = np.array([a2, b2, c2])
        mask_y4 = cv2.inRange(color4, lower_y4, upper_y)
        result_y4 = cv2.bitwise_and(roi4, roi4, mask=mask_y4)

        lower_r4 = np.array([x3, y3, z3])
        upper_r4 = np.array([a3, b3, c3])
        mask_r4 = cv2.inRange(color4, lower_r4, upper_r4)
        result_r4 = cv2.bitwise_and(roi4, roi4, mask=mask_r4)

        lower_o4 = np.array([x4, y4, z4])
        upper_o4 = np.array([a4, b4, c4])
        mask_o4 = cv2.inRange(color4, lower_o4, upper_o4)
        result_o4 = cv2.bitwise_and(roi4, roi4, mask=mask_o4)

        lower_b4 = np.array([x5, y5, z5])
        upper_b4 = np.array([a5, b5, c5])
        mask_b4 = cv2.inRange(color4, lower_b4, upper_b4)
        result_b4 = cv2.bitwise_and(roi4, roi4, mask=mask_b4)

        lower_g4 = np.array([x6, y6, z6])
        upper_g4 = np.array([a6, b6, c6])
        mask_g4 = cv2.inRange(color4, lower_g4, upper_g4)
        result_g4 = cv2.bitwise_and(roi4, roi4, mask=mask_g4)

        pixels_w4 = np.count_nonzero(result_w4)
        pixels_y4 = np.count_nonzero(result_y4)
        pixels_r4 = np.count_nonzero(result_r4)
        pixels_o4 = np.count_nonzero(result_o4)
        pixels_b4 = np.count_nonzero(result_b4)
        pixels_g4 = np.count_nonzero(result_g4)

        color5 = cv2.cvtColor(roi5, cv2.COLOR_BGR2HSV)  # roi5
        lower_w5 = np.array([x1, y1, z1])
        upper_w5 = np.array([a1, b1, c1])
        mask_w5 = cv2.inRange(color5, lower_w5, upper_w5)
        result_w5 = cv2.bitwise_and(roi5, roi5, mask=mask_w5)

        lower_y5 = np.array([x2, y2, z2])
        upper_y5 = np.array([a2, b2, c2])
        mask_y5 = cv2.inRange(color5, lower_y5, upper_y5)
        result_y5 = cv2.bitwise_and(roi5, roi5, mask=mask_y5)

        lower_r5 = np.array([x3, y3, z3])
        upper_r5 = np.array([a3, b3, c3])
        mask_r5 = cv2.inRange(color5, lower_r5, upper_r5)
        result_r5 = cv2.bitwise_and(roi5, roi5, mask=mask_r5)

        lower_o5 = np.array([x4, y4, z4])
        upper_o5 = np.array([a4, b4, c4])
        mask_o5 = cv2.inRange(color5, lower_o5, upper_o5)
        result_o5 = cv2.bitwise_and(roi5, roi5, mask=mask_o5)

        lower_b5 = np.array([x5, y5, z5])
        upper_b5 = np.array([a5, b5, c5])
        mask_b5 = cv2.inRange(color5, lower_b5, upper_b5)
        result_b5 = cv2.bitwise_and(roi5, roi5, mask=mask_b5)

        lower_g5 = np.array([x6, y6, z6])
        upper_g5 = np.array([a6, b6, c6])
        mask_g5 = cv2.inRange(color5, lower_g5, upper_g5)
        result_g5 = cv2.bitwise_and(roi5, roi5, mask=mask_g5)

        pixels_w5 = np.count_nonzero(result_w5)
        pixels_y5 = np.count_nonzero(result_y5)
        pixels_r5 = np.count_nonzero(result_r5)
        pixels_o5 = np.count_nonzero(result_o5)
        pixels_b5 = np.count_nonzero(result_b5)
        pixels_g5 = np.count_nonzero(result_g5)

        color6 = cv2.cvtColor(roi6, cv2.COLOR_BGR2HSV)  # roi6
        lower_w6 = np.array([x1, y1, z1])
        upper_w6 = np.array([a1, b1, c1])
        mask_w6 = cv2.inRange(color6, lower_w6, upper_w6)
        result_w6 = cv2.bitwise_and(roi6, roi6, mask=mask_w6)

        lower_y6 = np.array([x2, y2, z2])
        upper_y6 = np.array([a2, b2, c2])
        mask_y6 = cv2.inRange(color6, lower_y6, upper_y6)
        result_y6 = cv2.bitwise_and(roi6, roi6, mask=mask_y6)

        lower_r6 = np.array([x3, y3, z3])
        upper_r6 = np.array([a3, b3, c3])
        mask_r6 = cv2.inRange(color6, lower_r6, upper_r6)
        result_r6 = cv2.bitwise_and(roi6, roi6, mask=mask_r6)

        lower_o6 = np.array([x4, y4, z4])
        upper_o6 = np.array([a4, b4, c4])
        mask_o6 = cv2.inRange(color6, lower_o6, upper_o6)
        result_o6 = cv2.bitwise_and(roi6, roi6, mask=mask_o6)

        lower_b6 = np.array([x5, y5, z5])
        upper_b6 = np.array([a5, b5, c5])
        mask_b6 = cv2.inRange(color6, lower_b6, upper_b6)
        result_b6 = cv2.bitwise_and(roi6, roi6, mask=mask_b6)

        lower_g6 = np.array([x6, y6, z6])
        upper_g6 = np.array([a6, b6, c6])
        mask_g6 = cv2.inRange(color6, lower_g6, upper_g6)
        result_g6 = cv2.bitwise_and(roi6, roi6, mask=mask_g6)

        pixels_w6 = np.count_nonzero(result_w6)
        pixels_y6 = np.count_nonzero(result_y6)
        pixels_r6 = np.count_nonzero(result_r6)
        pixels_o6 = np.count_nonzero(result_o6)
        pixels_b6 = np.count_nonzero(result_b6)
        pixels_g6 = np.count_nonzero(result_g6)

        color7 = cv2.cvtColor(roi7, cv2.COLOR_BGR2HSV)  # roi7
        lower_w7 = np.array([x1, y1, z1])
        upper_w7 = np.array([a1, b1, c1])
        mask_w7 = cv2.inRange(color7, lower_w7, upper_w7)
        result_w7 = cv2.bitwise_and(roi7, roi7, mask=mask_w7)

        lower_y7 = np.array([x2, y2, z2])
        upper_y7 = np.array([a2, b2, c2])
        mask_y7 = cv2.inRange(color7, lower_y7, upper_y7)
        result_y7 = cv2.bitwise_and(roi7, roi7, mask=mask_y7)

        lower_r7 = np.array([x3, y3, z3])
        upper_r7 = np.array([a3, b3, c3])
        mask_r7 = cv2.inRange(color7, lower_r7, upper_r7)
        result_r7 = cv2.bitwise_and(roi7, roi7, mask=mask_r7)

        lower_o7 = np.array([x4, y4, z4])
        upper_o7 = np.array([a4, b4, c4])
        mask_o7 = cv2.inRange(color7, lower_o7, upper_o7)
        result_o7 = cv2.bitwise_and(roi7, roi7, mask=mask_o7)

        lower_b7 = np.array([x5, y5, z5])
        upper_b7 = np.array([a5, b5, c5])
        mask_b7 = cv2.inRange(color7, lower_b7, upper_b7)
        result_b7 = cv2.bitwise_and(roi7, roi7, mask=mask_b7)

        lower_g7 = np.array([x6, y6, z6])
        upper_g7 = np.array([a6, b6, c6])
        mask_g7 = cv2.inRange(color7, lower_g7, upper_g7)
        result_g7 = cv2.bitwise_and(roi7, roi7, mask=mask_g7)

        pixels_w7 = np.count_nonzero(result_w7)
        pixels_y7 = np.count_nonzero(result_y7)
        pixels_r7 = np.count_nonzero(result_r7)
        pixels_o7 = np.count_nonzero(result_o7)
        pixels_b7 = np.count_nonzero(result_b7)
        pixels_g7 = np.count_nonzero(result_g7)

        color8 = cv2.cvtColor(roi8, cv2.COLOR_BGR2HSV)  # roi8
        lower_w8 = np.array([x1, y1, z1])
        upper_w8 = np.array([a1, b1, c1])
        mask_w8 = cv2.inRange(color8, lower_w8, upper_w8)
        result_w8 = cv2.bitwise_and(roi8, roi8, mask=mask_w8)

        lower_y8 = np.array([x2, y2, z2])
        upper_y8 = np.array([a2, b2, c2])
        mask_y8 = cv2.inRange(color8, lower_y8, upper_y8)
        result_y8 = cv2.bitwise_and(roi8, roi8, mask=mask_y8)

        lower_r8 = np.array([x3, y3, z3])
        upper_r8 = np.array([a3, b3, c3])
        mask_r8 = cv2.inRange(color8, lower_r8, upper_r8)
        result_r8 = cv2.bitwise_and(roi8, roi8, mask=mask_r8)

        lower_o8 = np.array([x4, y4, z4])
        upper_o8 = np.array([a4, b4, c4])
        mask_o8 = cv2.inRange(color8, lower_o8, upper_o8)
        result_o8 = cv2.bitwise_and(roi8, roi8, mask=mask_o8)

        lower_b8 = np.array([x5, y5, z5])
        upper_b8 = np.array([a5, b5, c5])
        mask_b8 = cv2.inRange(color8, lower_b8, upper_b8)
        result_b8 = cv2.bitwise_and(roi8, roi8, mask=mask_b8)

        lower_g8 = np.array([x6, y6, z6])
        upper_g8 = np.array([a6, b6, c6])
        mask_g8 = cv2.inRange(color8, lower_g8, upper_g8)
        result_g8 = cv2.bitwise_and(roi8, roi8, mask=mask_g8)

        pixels_w8 = np.count_nonzero(result_w8)
        pixels_y8 = np.count_nonzero(result_y8)
        pixels_r8 = np.count_nonzero(result_r8)
        pixels_o8 = np.count_nonzero(result_o8)
        pixels_b8 = np.count_nonzero(result_b8)
        pixels_g8 = np.count_nonzero(result_g8)

        color9 = cv2.cvtColor(roi9, cv2.COLOR_BGR2HSV)  # roi9
        lower_w9 = np.array([x1, y1, z1])
        upper_w9 = np.array([a1, b1, c1])
        mask_w9 = cv2.inRange(color9, lower_w9, upper_w9)
        result_w9 = cv2.bitwise_and(roi9, roi9, mask=mask_w9)

        lower_y9 = np.array([x2, y2, z2])
        upper_y9 = np.array([a2, b2, c2])
        mask_y9 = cv2.inRange(color9, lower_y9, upper_y9)
        result_y9 = cv2.bitwise_and(roi9, roi9, mask=mask_y9)

        lower_r9 = np.array([x3, y3, z3])
        upper_r9 = np.array([a3, b3, c3])
        mask_r9 = cv2.inRange(color9, lower_r9, upper_r9)
        result_r9 = cv2.bitwise_and(roi9, roi9, mask=mask_r9)

        lower_o9 = np.array([x4, y4, z4])
        upper_o9 = np.array([a4, b4, c4])
        mask_o9 = cv2.inRange(color9, lower_o9, upper_o9)
        result_o9 = cv2.bitwise_and(roi9, roi9, mask=mask_o9)

        lower_b9 = np.array([x5, y5, z5])
        upper_b9 = np.array([a5, b5, c5])
        mask_b9 = cv2.inRange(color9, lower_b9, upper_b9)
        result_b9 = cv2.bitwise_and(roi9, roi9, mask=mask_b9)

        lower_g9 = np.array([x6, y6, z6])
        upper_g9 = np.array([a6, b6, c6])
        mask_g9 = cv2.inRange(color9, lower_g9, upper_g9)
        result_g9 = cv2.bitwise_and(roi9, roi9, mask=mask_g9)

        pixels_w9 = np.count_nonzero(result_w9)
        pixels_y9 = np.count_nonzero(result_y9)
        pixels_r9 = np.count_nonzero(result_r9)
        pixels_o9 = np.count_nonzero(result_o9)
        pixels_b9 = np.count_nonzero(result_b9)
        pixels_g9 = np.count_nonzero(result_g9)

        if pixels_w > 0:  # checking pixels in roi1
            print(0,end="")
        elif pixels_y > 0:
            print(1,end="")
        elif pixels_r > 0:
            print(2,end="")
        elif pixels_o > 0:
            print(3,end="")
        elif pixels_b > 0:
            print(4,end="")
        elif pixels_g > 0:
            print(5,end="")

        if pixels_w2 > 0:  # checking pixels in roi2
            print(0,end="")
        elif pixels_y2 > 0:
            print(1,end="")
        elif pixels_r2 > 0:
            print(2,end="")
        elif pixels_o2 > 0:
            print(3,end="")
        elif pixels_b2 > 0:
            print(4,end="")
        elif pixels_g2 > 0:
            print(5,end="")

        if pixels_w3 > 0:  # checking pixels in roi3
            print(0,end="")
        elif pixels_y3 > 0:
            print(1,end="")
        elif pixels_r3 > 0:
            print(2,end="")
        elif pixels_o3 > 0:
            print(3,end="")
        elif pixels_b3 > 0:
            print(4,end="")
        elif pixels_g3 > 0:
            print(5,end="")

        if pixels_w4 > 0:  # checking pixels in roi4
            print(0,end="")

        elif pixels_y4 > 0:
            print(1,end="")

        elif pixels_r4 > 0:
            print(2,end="")

        elif pixels_o4 > 0:
            print(3,end="")

        elif pixels_b4 > 0:
            print(4,end="")

        elif pixels_g4 > 0:
            print(5,end="")

        if pixels_w5 > 0:  # checking pixels in roi5
            print(0,end="")

        elif pixels_y5 > 0:
            print(1,end="")

        elif pixels_r5 > 0:
            print(2,end="")

        elif pixels_o5 > 0:
            print(3,end="")

        elif pixels_b5 > 0:
            print(4,end="")

        elif pixels_g5 > 0:
            print(5,end="")

        if pixels_w6 > 0:  # checking pixels in roi6
            print(0,end="")

        elif pixels_y6 > 0:
            print(1,end="")

        elif pixels_r6 > 0:
            print(2,end="")

        elif pixels_o6 > 0:
            print(3,end="")

        elif pixels_b6 > 0:
            print(4,end="")

        elif pixels_g6 > 0:
            print(5,end="")

        if pixels_w7 > 0:  # checking pixels in roi7
            print(0,end="")

        elif pixels_y7 > 0:
            print(1,end="")

        elif pixels_r7 > 0:
            print(2,end="")

        elif pixels_o7 > 0:
            print(3,end="")

        elif pixels_b7 > 0:
            print(4,end="")

        elif pixels_g7 > 0:
            print(5,end="")

        if pixels_w8 > 0:  # checking pixels in roi8
            print(0,end="")
            
        elif pixels_y8 > 0:
            print(1,end="")
            
        elif pixels_r8 > 0:
            print(2,end="")
            
        elif pixels_o8 > 0:
            print(3,end="")
            
        elif pixels_b8 > 0:
            print(4,end="")
            
        elif pixels_g8 > 0:
            print(5,end="")

        if pixels_w9 > 0:  # checking pixels in roi9
            print(0)
            
        elif pixels_y9 > 0:
            print(1)
            
        elif pixels_r9 > 0:
            print(2)
            
        elif pixels_o9 > 0:
            print(3)
            
        elif pixels_b9 > 0:
            print(4)
            
        elif pixels_g9 > 0:
            print(5)
            
        


# VideoCapture object to read from the webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Webcam")
cv2.setMouseCallback("Webcam", mouse_callback)

# Loop through each frame from the webcam
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Get the dimensions of the frame
    height, width, _ = frame.shape
    # changeable values to shift the whole figure/cubes along the frame
    colour = (0, 255, 0)
    thickness = 2
    gap = 10
    x_offset = 0
    y_offset = 100
    cube_width = 55
    middle_cube_width = cube_width//2
    coord = (width//2+x_offset, height//2+y_offset)
    # initializing dimensions of cubes for detecting cubelets by using arrays
    cubelet1 = [[coord[0]-(cube_width+gap+middle_cube_width), coord[1]-(cube_width+gap+middle_cube_width)], [coord[0]-(middle_cube_width+gap),            coord[1]-(gap+middle_cube_width)]]
    cubelet2 = [[coord[0]-(middle_cube_width),                coord[1]-(cube_width+gap+middle_cube_width)], [coord[0]+(middle_cube_width),                coord[1]-(gap+middle_cube_width)]]
    cubelet3 = [[coord[0]+(middle_cube_width+gap),            coord[1]-(cube_width+gap+middle_cube_width)], [coord[0]+(middle_cube_width+gap+cube_width), coord[1]-(gap+middle_cube_width)]]
    cubelet4 = [[coord[0]-(cube_width+gap+middle_cube_width), coord[1]-(middle_cube_width)],                [coord[0]-(middle_cube_width+gap),            coord[1]+(middle_cube_width)]]
    cubelet5 = [[coord[0]-(middle_cube_width),                coord[1]-(middle_cube_width)],                [coord[0]+(middle_cube_width),                coord[1]+(middle_cube_width)]]
    cubelet6 = [[coord[0]+(middle_cube_width+gap),            coord[1]-(middle_cube_width)],                [coord[0]+(middle_cube_width+gap+cube_width), coord[1]+(middle_cube_width)]]
    cubelet7 = [[coord[0]-(cube_width+gap+middle_cube_width), coord[1]+(middle_cube_width+gap)],            [coord[0]-(middle_cube_width+gap),            coord[1]+(middle_cube_width+gap+cube_width)]]
    cubelet8 = [[coord[0]-(middle_cube_width),                coord[1]+(middle_cube_width+gap)],            [coord[0]+(middle_cube_width),                coord[1]+(middle_cube_width+gap+cube_width)]]
    cubelet9 = [[coord[0]+(middle_cube_width+gap),            coord[1]+(middle_cube_width+gap)],            [coord[0]+(middle_cube_width+gap+cube_width), coord[1]+(middle_cube_width+gap+cube_width)]]
    # creating cubes with rectangle()
    cv2.rectangle(frame, cubelet1[0], cubelet1[1], colour, thickness)
    cv2.rectangle(frame, cubelet2[0], cubelet2[1], colour, thickness)
    cv2.rectangle(frame, cubelet3[0], cubelet3[1], colour, thickness)
    cv2.rectangle(frame, cubelet4[0], cubelet4[1], colour, thickness)
    cv2.rectangle(frame, cubelet5[0], cubelet5[1], colour, thickness)
    cv2.rectangle(frame, cubelet6[0], cubelet6[1], colour, thickness)
    cv2.rectangle(frame, cubelet7[0], cubelet7[1], colour, thickness)
    cv2.rectangle(frame, cubelet8[0], cubelet8[1], colour, thickness)
    cv2.rectangle(frame, cubelet9[0], cubelet9[1], colour, thickness)
    # creating roi for detection of color
    roi1 = frame[cubelet1[0][1]:cubelet1[1][1],  cubelet1[0][0]:cubelet1[1][0]]
    roi2 = frame[cubelet2[0][1]:cubelet2[1][1],  cubelet2[0][0]:cubelet2[1][0]]
    roi3 = frame[cubelet3[0][1]:cubelet3[1][1],  cubelet3[0][0]:cubelet3[1][0]]
    roi4 = frame[cubelet4[0][1]:cubelet4[1][1],  cubelet4[0][0]:cubelet4[1][0]]
    roi5 = frame[cubelet5[0][1]:cubelet5[1][1],  cubelet5[0][0]:cubelet5[1][0]]
    roi6 = frame[cubelet6[0][1]:cubelet6[1][1],  cubelet6[0][0]:cubelet6[1][0]]
    roi7 = frame[cubelet7[0][1]:cubelet7[1][1],  cubelet7[0][0]:cubelet7[1][0]]
    roi8 = frame[cubelet8[0][1]:cubelet8[1][1],  cubelet8[0][0]:cubelet8[1][0]]
    roi9 = frame[cubelet9[0][1]:cubelet9[1][1],  cubelet9[0][0]:cubelet9[1][0]]



    # showing the frame
    cv2.imshow("Webcam", frame)
    
   
    # Wait for a key press and check if it is the "q" key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
