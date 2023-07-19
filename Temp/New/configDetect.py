import cv2 as cv
import numpy as np
from collections import Counter
colour_arr = []
clicks = 0


def clickEvent(event, x, y, flags, params):
    global clicks
    if event == cv.EVENT_LBUTTONDOWN:
        clicks += 1


if __name__ == "__main__":
    cam = cv.VideoCapture(0)

    while (1):
        _, img = cam.read()
        cube_width = 65
        frame_size = [639, 479]
        #gap =10
        ptx1 = (frame_size[0]/2)-(1.5*cube_width)
        pty1 = (frame_size[1]/2)-(1.5*cube_width)
        ptx2 = (frame_size[0]/2)-(0.5*cube_width)
        pty2 = (frame_size[1]/2)-(1.5*cube_width)
        ptx3 = (frame_size[0]/2)+(0.5*cube_width)
        pty3 = (frame_size[1]/2)-(1.5*cube_width)
        ptx4 = (frame_size[0]/2)-(1.5*cube_width)
        pty4 = (frame_size[1]/2)-(0.5*cube_width)
        ptx5 = (frame_size[0]/2)-(0.5*cube_width)
        pty5 = (frame_size[1]/2)-(0.5*cube_width)
        ptx6 = (frame_size[0]/2)+(0.5*cube_width)
        pty6 = (frame_size[1]/2)-(0.5*cube_width)
        ptx7 = (frame_size[0]/2)-(1.5*cube_width)
        pty7 = (frame_size[1]/2)+(0.5*cube_width)
        ptx8 = (frame_size[0]/2)-(0.5*cube_width)
        pty8 = (frame_size[1]/2)+(0.5*cube_width)
        ptx9 = (frame_size[0]/2)+(0.5*cube_width)
        pty9 = (frame_size[1]/2)+(0.5*cube_width)
        ROI_1 = np.array([[(ptx1, pty1), (ptx1+cube_width, pty1), (ptx1+cube_width,
                         pty1+cube_width), (ptx1, pty1+cube_width)]], dtype=np.int32)
        ROI_2 = np.array([[(ptx2, pty2), (ptx2+cube_width, pty2), (ptx2+cube_width,
                         pty2+cube_width), (ptx2, pty2+cube_width)]], dtype=np.int32)
        ROI_3 = np.array([[(ptx3, pty3), (ptx3+cube_width, pty3), (ptx3+cube_width,
                         pty3+cube_width), (ptx3, pty3+cube_width)]], dtype=np.int32)
        ROI_4 = np.array([[(ptx4, pty4), (ptx4+cube_width, pty4), (ptx4+cube_width,
                         pty4+cube_width), (ptx4, pty4+cube_width)]], dtype=np.int32)
        ROI_5 = np.array([[(ptx5, pty5), (ptx5+cube_width, pty5), (ptx5+cube_width,
                         pty5+cube_width), (ptx5, pty5+cube_width)]], dtype=np.int32)
        ROI_6 = np.array([[(ptx6, pty6), (ptx6+cube_width, pty6), (ptx6+cube_width,
                         pty6+cube_width), (ptx6, pty6+cube_width)]], dtype=np.int32)
        ROI_7 = np.array([[(ptx7, pty7), (ptx7+cube_width, pty7), (ptx7+cube_width,
                         pty7+cube_width), (ptx7, pty7+cube_width)]], dtype=np.int32)
        ROI_8 = np.array([[(ptx8, pty8), (ptx8+cube_width, pty8), (ptx8+cube_width,
                         pty8+cube_width), (ptx8, pty8+cube_width)]], dtype=np.int32)
        ROI_9 = np.array([[(ptx9, pty9), (ptx9+cube_width, pty9), (ptx9+cube_width,
                         pty9+cube_width), (ptx9, pty9+cube_width)]], dtype=np.int32)
        ROI = [ROI_1, ROI_2, ROI_3, ROI_4, ROI_5, ROI_6, ROI_7, ROI_8, ROI_9]
        ROI_IMG = cv.drawContours(img, ROI, -1, (0, 255, 0), 3)

        if clicks >= 1:
            clicks = 0
            for i in range(0, 9):
                arr = []
                for j in range(ROI[i][0][0][1], ROI[i][0][2][1]):
                    arr1 = []
                    for k in range(ROI[i][0][0][0], ROI[i][0][1][0]):
                        if (not (img[j][k][0] == 0 and img[j][k][1] == 255 and img[j][k][2] == 0)):
                            arr1.append(img[j][k])
                    if (arr1 != []):
                        arr.append(arr1)
                colour_arr.append(arr)
            # for i in range(0, len(colour_arr[0][0])):
            #    print("ROI = ",colour_arr[0][0][i][0])
            print("Colour array", colour_arr[0][0])

            unique_rows, counts = np.unique([colour_arr[0][0]], return_counts=True)
            max_index = counts.argmax()
            print("The most repeated row is:", unique_rows[max_index])

       # print(img[ROI[0][0][0][0]][ROI[0][0][0][1]])
       # print(ROI[0][0][0])

        cv.imshow("frame", ROI_IMG)
        cv.setMouseCallback("frame", clickEvent)
        k = cv.waitKey(1)
        if k == ord('q'):
            break
        # 65 x 65
        # 639 X 479

    cv.destroyAllWindows()
