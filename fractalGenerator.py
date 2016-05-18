import pygame, sys, math
from pygame.locals import *

pygame.init()

leastX = -1.6
maxX = 1.6
leastY = -1
maxY = 1


"""
This determines the width of the fractal image generated. The height
is calculated using the dimensions given above.
"""
width = 500

detail = 1

"""
Accuracy is just how many times the program checks for the infinite
series to diverge.
"""
accuracy = 1000

color_mode = 1

c = complex(-0.8, .156)


"""
This determines how the fractal is colored when "color_mode" is set to 2.
"""
colorList = [(255,0,0),
             (255,106,0),
             (255,216,0),
             (182,255,0),
             (76,255,0),
             (0,255,33),
             (0,255,144),
             (0,255,255),
             (0,148,255),
             (0,38,255),
             (72,0,255),
             (178,0,255),
             (255,0,220),
             (255,0,110)]




maxY = float(maxY)
maxX = float(maxX)
leastY = float(leastY)
leastX = float(leastX)
detail = float(detail)


height = (maxY - leastY) * float(width) / (maxX - leastX)
height = int(height)
size = width, height
surface = pygame.display.set_mode(size)
arr = pygame.PixelArray(surface)
incr = detail*((maxX - leastX)/(float(width)))

def drawAxes():
    list5 = frange(leastX,maxX,incr)
    list6 = frange(leastY,maxY,incr)
    for x in list5:
        arr[cx(x) - 1,cy(0)] = (0,0,0)
    for y in list6:
        arr[cx(0),cy(y) - 1] = (0,0,0)
    pygame.display.flip()


def cy(coord):
    return int(((height)/(leastY - maxY)*coord) + (height * maxY)/(maxY - leastY))

def cx(coord):
    return int(((width)/(maxX - leastX)*coord) + (width * leastX)/(leastX - maxX))

def frange(start, end, increment):
    current = start
    outputList = [float('%10.75f' % current)]
    while current < end:
        current += increment
        outputList = outputList + [float('%10.75f' % current)]
    return outputList

##################################################################
##################################################################

list1 = frange(leastX,maxX,incr)
list2 = frange(leastY,maxY,incr)

for x in list1:
    for y in list2:
        z = complex(x,y)
        point = z
        k = 0
        """
        k is the number of iterations in the recursive series so far.
        point is just used to save what point we are currently graphing.
        z is the starting term for the recursive series.
        """
        
        while k < accuracy and abs(z) < 2.0:
            """
            If the absolute value of the current term in the series is greater
            than 2, we know that it will diverge to infinity because of math.
            """
            z = z*z + c
            k += 1

        if k == accuracy:
            """
            If k is the same as accuracy (the number of checks to see if the series diverges),
            then the point we tested is part of the fractal
            """
            xp = cx(point.real)
            yp = cy(point.imag)

            if xp < width and yp < height:
                if color_mode == 1:
                    arr[xp,yp] = (245, 100, 100)

                if color_mode == 2:
                    arr[xp,yp] = (255,255,255)

                
        if k < accuracy:

            xp = cx(point.real)
            yp = cy(point.imag)
            if color_mode == 1:
                yo = 75* math.log10(k+1)

                if xp < width and yp < height and yp > 0 and xp > 0:
                    arr[xp,yp] = (yo,70,100)
            if color_mode == 2:
                if xp < width and yp < height and yp > 0 and xp > 0:
                    while k > (len(colorList) - 1):
                        k = k - len(colorList)

                    arr[xp,yp] = colorList[k]
    pygame.display.flip()

pygame.image.save(arr.make_surface(), 'juliaSet.png')
"""
Saves the generated fractal
"""

print "Done!"

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





        
