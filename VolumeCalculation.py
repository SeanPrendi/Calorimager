from ImgDimension import getAllDims
import math

def calcVolume(img1, img2, width):
    dim1, dim2, dim3 = getAllDims(img1, img2, width)
    avgDiameter = (dim1+dim2+dim3)/3
    avgRadius = avgDiameter/2
    return (4/3)*math.pi*(avgRadius)**3

