import cv2 as cv
import numpy as np
from imutils import perspective, contours
from scipy.spatial import distance as dist

# Naive Method and Bounding Box Drawing Adopted from:
# https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/

def runImg(img1, width):
    image = cv.imread(img1, flags=cv.IMREAD_COLOR)
    image = cv.resize(image, (540, 540))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.fastNlMeansDenoising(gray, h=20)

    cannyEdges = cv.Canny(gray, 50, 150)
    cannyEdges = cv.dilate(cannyEdges, None, iterations=2)
    cannyEdges = cv.erode(cannyEdges, None, iterations=2)
    contour = cv.findContours(cannyEdges.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[1]
    contour = contours.sort_contours(contour)[0]

    for c in contour:
        if cv.contourArea(c) < 120:
            continue

        original = image.copy()
        boundingBox = cv.minAreaRect(c)
        boundingBox = cv.boxPoints(boundingBox)
        boundingBox = np.array(boundingBox, dtype="int")

        boundingBox = perspective.order_points(boundingBox)
        cv.drawContours(original, [boundingBox.astype("int")], -1, (0, 255, 0), 2)

        for (x, y) in boundingBox:
            cv.circle(original, (int(x), int(y)), 5, (0, 0, 255), -1)

        (topL, topR, bottomR, bottomL) = boundingBox
        (topMidX, topMidY) = ((topL[0] + topR[0])/2, (topL[1] + topR[1])/2)
        (botMidX, botMidY) = ((bottomL[0] + bottomR[0])/2, (bottomL[1] + bottomR[1])/2)
        (leftMidX, leftMidY) = ((topL[0] + bottomL[0])/2, (topL[1] + bottomL[1])/2)
        (rightMidX, rightMidY) = ((topR[0] + bottomR[0])/2, (topR[1] + bottomR[1])/2)

        cv.line(original, (int(topMidX), int(topMidY)), (int(botMidX), int(botMidY)),
            (255, 0, 255), 2)
        cv.line(original, (int(leftMidX), int(leftMidY)), (int(rightMidX), int(rightMidY)),
            (255, 0, 255), 2)

        dA = dist.euclidean((topMidX, topMidY), (botMidX, botMidY))
        dB = dist.euclidean((leftMidX, leftMidY), (rightMidX, rightMidY))
        try:
            pixelsPerMetric
        except:
            pixelsPerMetric = dB / width

        dimA = dA / pixelsPerMetric
        dimB = dB / pixelsPerMetric

        cv.putText(original, "{:.1f}in".format(dimA),
            (int(topMidX), int(topMidY - 10)), cv.FONT_HERSHEY_SIMPLEX,
            0.65, (255, 255, 255), 2)
        cv.putText(original, "{:.1f}in".format(dimB),
            (int(rightMidX - 20), int(rightMidY)), cv.FONT_HERSHEY_SIMPLEX,
            0.65, (255, 255, 255), 2)

        cv.imshow("Image", original)
        cv.waitKey(0)
    cv.destroyAllWindows()
    return (dimA, dimB)

def getAllDims(img1, img2, width):
    dimA, dimB, dimC = None, None, None
    while dimC == None:
        if dimA == None and dimB == None:
            (dimA, dimB) = runImg(img1, width)
        else:
            dimC = runImg(img2, width)[0]
    return (dimA, dimB, dimC)

# print(getAllDims('images/IMG_2990.jpeg', 'images/IMG_2989.jpeg', 1.9))