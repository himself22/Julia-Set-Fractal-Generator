import pygame, sys, math
from pygame.locals import *

pygame.init()

"""
Hi! I've explained what every part does... so if you are interested you can read through!
However if you just want to create cool pictures of fractals, I recommend messing around
with the "c" value below (which is right before colorList lol), increasing the width a
little bit (OR A LOT MUHAHAHAHA), and also changing the values below to something like:

leastX = -2
maxX = 2
leastY = -2
maxY = 2

And every once in a while mess around with color_mode, but IT ONLY TAKES VALUES OF
1 AND 2.

If you're looking for good "c" values to use, I would go to wikipedia and look at some of
the examples they have, and maybe copy the "c" values into this program and then mess around.
You can find examples here:

https://en.wikipedia.org/wiki/Julia_set#Quadratic_polynomials
https://en.wikipedia.org/wiki/Julia_set#Examples_of_Julia_sets

If you're looking at the second link, they change the equation that is used to generate
the fractal. You can change that, but right now it is set to "z = z*z + c"

Make something better than what wikipedia has! Show them who's boss!


***********************

NOTE:
There is a bug! OH NOOOO. Okay so sometimes, depending on the width you set, there will
appear these horizontal black lines which are really annoying. :/
To fix this, increase the width by like 20.

I know what's causing the problem, but I haven't been able to fix it. :(

***********************

Feel free to mess with all of this...

"""


leastX = -1.6
maxX = 1.6
leastY = -1
maxY = 1
"""
These are the dimensions of the plane that will be drawn.
You might want to change these dimensions to fit the fractal drawing.
For example the Mandelbrot fractal fits nicely when the X range is
(-2,1) and the Y range is (-1,1). This also allows you to zoom in
if you can figure out the dimensions that you want to zoom in. To
help with this, I have the function "drawAxes". I understand this
isn't ideal, but I'm not a great programmer, so I'll try to think
of a way to make it easier or maybe I'll just google it. :)
"""



width = 500
"""
This determines the width of the fractal image generated. The height
is calculated using the dimensions given above. Again... this isn't
ideal but I'm new! Sorryyy.
"""

detail = 1
"""
I wouldn't mess with detail too much. I just used it when I was writing the
program to generate quick, but less detailed fractals. If "detail"
is set to 2, the program will only calculate and color every other
pixel, which obviously doesn't look as nice, but it's convient for
quick checks to make sure everyrthing it working.
"""

accuracy = 1000
"""
Accuracy is just how many times the program checks for the infinite
series to diverge. 1000 seems to be fine, I'm sure a lower number
like 500 or even 250 would be fine too... I like 1000.
If you know how fractals like these are created work then you know
about the series stuff and you can probably make this program better
so please do. AHHHHHHHHHHHHHHHHHHHHH
"""


color_mode = 2
"""
color_mode is very important!!!! It changes the way the fractal is colored.
This first setting (set it equal to 1) makes it look all pink and blue and
swag. The second one is more rainbow colored.
THIS VALUE ONLY TAKES VALUES OF 1 OR 2!!
"""


c = complex(-0.8, .156)
"""
Julia set fractals and their shapes are determined by this constant
number, which is sometimes a complex number. Change this number, and
you can change the whole fractal!
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

"""
This determines how the fractal is colored when "color_mode" is set to 2.
"""


maxY = float(maxY)
maxX = float(maxX)
leastY = float(leastY)
leastX = float(leastX)
detail = float(detail)
"""
I'm too lazy to add a decimal and a 0 to stuff.
"""


height = (maxY - leastY) * float(width) / (maxX - leastX)
height = int(height)
size = width, height
surface = pygame.display.set_mode(size)
arr = pygame.PixelArray(surface)
incr = detail*((maxX - leastX)/(float(width)))
"""
Calculations and stuff...
"incr" is the increment of a list used later in the program.
"""

def drawAxes():
    list5 = frange(leastX,maxX,incr)
    list6 = frange(leastY,maxY,incr)
    for x in list5:
        arr[cx(x) - 1,cy(0)] = (0,0,0)
    for y in list6:
        arr[cx(0),cy(y) - 1] = (0,0,0)
    pygame.display.flip()
"""
Draws the axes at y = 0 and x = 0 if you want.
"""


def cy(coord):
    return int(((height)/(leastY - maxY)*coord) + (height * maxY)/(maxY - leastY))
"""
Okay so there are two sets of coordinate planes. The first one is the
for the complex plane that represents the actual plane a fractal is
drawn on. It ranges from like [-2,2] on both the x and y axes... from
what I've seen from experimenting. These points are useless tho for
pygame. So what this function does is it CONVERTS the coordinate point
of the fractal to something usable for pygame.
It's used for graphing.
This one is for x coordinates
"""

def cx(coord):
    return int(((width)/(maxX - leastX)*coord) + (width * leastX)/(leastX - maxX))
"""
Same thing as before but instead used for y coordinates.
"""

def frange(start, end, increment):
    current = start
    outputList = [float('%10.75f' % current)]
    while current < end:
        current += increment
        outputList = outputList + [float('%10.75f' % current)]
    return outputList
"""
So unfortunately there is a limited accuracy to the fractals being generated,
because there's a limited number of pixels. This list creates the exact imaginary
numbers and coordinates we will be using for whatever dimensions you want.
But really it's just the range() function but for decimals...
definitely a better way to do this... but I don't program often.
"""

##################################################################
##################################################################

list1 = frange(leastX,maxX,incr)
list2 = frange(leastY,maxY,incr)
"""
These are lists the points that will be placed on the screen.
It's like the resolution... maybe idk.
"""

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
            """
            calculates the next term in the recursive series.
            You should mess with the equation, there are so many possibilities.
            """

        if k == accuracy:
            """
            If k is the same as accuracy (the number of checks to see if the series diverges),
            then the point we tested is part of the fractal
            """
            xp = cx(point.real)
            yp = cy(point.imag)
            """
            xp and yp are the points were graphing.
            we use cy and cx functions to calculate the points we are graphing from
            the original complex number we had.
            """
            if xp < width and yp < height:
                if color_mode == 1:
                    arr[xp,yp] = (245, 100, 100)
                    """
                    These tuples determine the color of the colored point. Anytime you see
                    'arr[xp,yp]' = (number,number,number)
                    you should try changing stuff to change the colors.
                    Note which color_mode you are in tho.
                    """
                if color_mode == 2:
                    arr[xp,yp] = (255,255,255)
                """
                If the point is part of the fractal, we assign it a certain color.
                """
                
        if k < accuracy:
            """
            If k is less than the accuracy, we still color is a particular color,
            depending on how many iterations it took for the series to diverge to
            infinity.
            """
            xp = cx(point.real)
            yp = cy(point.imag)
            if color_mode == 1:
                yo = 75* math.log10(k+1)
                """
                This is the equation I use when I color fractals in color_mode = 1. I
                was messing around with it one day and I tried the log function, it
                looked amazing.
                Feel free to change it! :) Smiley faces look really cool it IDLE.
                """
                if xp < width and yp < height and yp > 0 and xp > 0:
                    arr[xp,yp] = (yo,70,100)
            if color_mode == 2:
                if xp < width and yp < height and yp > 0 and xp > 0:
                    while k > (len(colorList) - 1):
                        k = k - len(colorList)
                    """
                    Yea so for this color scheme I took a list with a certain number
                    of elements, and then scaled down the k value until it was in
                    the range of that list, and then used the corresponding color
                    to color the set of points that took k iterations to diverge.
                    """
                    arr[xp,yp] = colorList[k]
    pygame.display.flip()

pygame.image.save(arr.make_surface(), 'juliaSet.png')
"""
Saves the fractal generated.
"""

print "Done!"

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





        
