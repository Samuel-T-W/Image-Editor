import graphics
from graphics import *
def stat(image):
    print("stats button has been pressed")
    print("image stats....")
    print("calculating image histogram")
    #intialize variables and create some lists
    count=0
    mred=0
    mgreen=0
    mblue=0
    nred=[]
    ngreen=[]
    nblue=[]

#make list of each colors and arange it inaccending order
# create a histogram and calculate the mean of all rgb values
    for col in range(image.getHeight()):
        for row in range(image.getWidth()):
            r, g, b = image.getPixel(row,col)
            # append every value of rgb
            nred.append(r)
            nblue.append(b)
            ngreen.append(g)
            #create an accumulator to sum up all values of r, g and b indivually
            mred+=r
            mgreen+=g
            mblue+=b
            #count the total amount of pixels int the image
            count+=1


    print("  RED"," BLUE"," GREEN")
    # print the histogram
    for i in range(256):
        print(i,nred.count(i),"",nblue.count(i),"",ngreen.count(i))
    print("red mean : ", mred/count )
    print("green mean : ", mgreen/count )
    print("blue mean : ", mblue/count)
    print("Number of pixels is ",count)



def openImage(picFile,win):
    # draw the image on a center point
    img = Image(Point(400, 350), picFile)
    width = img.getWidth()
    height = img.getHeight()
    img.draw(win)
    return img
def convertToNegative(image):
    print("Converting to color negative...")
    for col in range(image.getHeight()):
        for row in range(image.getWidth()):
            r, g, b = image.getPixel(row,col)
            image.setPixel(row,col, color_rgb(255-r,255-g,255-b))
        update()
    print("   ...Done.")

def convertToGrayscale(img):
    print("Converting to grayscale...")
    for col in range(img.getHeight()):
        for row in range(img.getWidth()):
            #acquires the pixles from the image
            (r, g, b) = img.getPixel(row,col)
            #sets new pixles for the image
            average = (int((r + g + b) / 3))
            img.setPixel(row, col, color_rgb(average, average, average))

        update()
    print("   ...Done.")

def bminus(image):
    br=25
    # go through every pixel and add brightness
    for col in range(image.getHeight()):
        for row in range(image.getWidth()):
            r, g, b = image.getPixel(row,col)
            r-=br
            g-=br
            b-=br
           # if higher than 255 assign it 255
            if r>255:
                r=255
            if g>255:
                g=255
            if b>255:
                b=255
             # if less than 0 then assign it 0
            if r<0:
                r=0
            if g<0:
                g=0
            if b<0:
                b=0
            #set the new pixels to their position
            image.setPixel(row,col, color_rgb(r,g,b))
        #update the pixels
        update()
    print("   ...Done.")

def bplus(image):
    br=25
    # go through every pixel and add brightness
    for col in range(image.getHeight()):
        for row in range(image.getWidth()):
            r, g, b = image.getPixel(row,col)
            r+=br
            g+=br
            b+=br
           # if higher than 255 assign it 255
            if r>255:
                r=255
            if g>255:
                g=255
            if b>255:
                b=255
             # if less than 0 then assign it 0
            if r<0:
                r=0
            if g<0:
                g=0
            if b<0:
                b=0
            #set the new pixels to their position
            image.setPixel(row,col, color_rgb(r,g,b))
        #update the pixels
        update()
    print("   ...Done.")

def buttons(win):
    # draw a rectangle for every option
    r1=Rectangle(Point(10,5),Point(150,45))
    r2=Rectangle(Point(160,5),Point(300,45))
    r3=Rectangle(Point(310,5),Point(450,45))
    r41=Rectangle(Point(460,5),Point(520,45))
    r42=Rectangle(Point(530,5),Point(590,45))
    r5=Rectangle(Point(680,5),Point(780,45))
    r6=Rectangle(Point(600,5),Point(670,45))
    r1.draw(win)
    r2.draw(win)
    r3.draw(win)
    r41.draw(win)
    r42.draw(win)
    r5.draw(win)
    r6.draw(win)
    # draw a text in the center of the rectangle
    o1=Text(Point(80,25),"image stat")
    o2=Text(Point(230,25),"negative")
    o3=Text(Point(380,25),"gray scale")
    o41=Text(Point(480,25)," b +")
    o42=Text(Point(560,25)," b -")
    o5=Text(Point(730,25),"quit")
    o6=Text(Point(635,25),"save")
    o1.draw(win)
    o2.draw(win)
    o3.draw(win)
    o41.draw(win)
    o42.draw(win)
    o5.draw(win)
    o6.draw(win)
def keyhandle(k,win,image):
    if k=="q":
        win.close()
    elif k=="b":
        adjustb()
    elif k=="g":
        convertToGrayscale(image)
    elif k=="s":
        stats(image)
    elif k=="n":
        convertToNegative(image)
def save(image):
     #saves the image with ppm format
    image.save("cs.ppm")
    print(".....saved")

def mousehandle(p,win,image):
    #get thex and y coordinates of the point
    x=p.getX()
    y=p.getY()
    #if the x and y of the point is inbetween a certain range which
    #equals the width and height of the box execute that function
    if 10<=x<=150 and 5<=y<=45 :
        stat(image)
    elif 160<=x<=300 and 5<=y<=45:
        convertToNegative(image)
    elif 310<=x<=450 and 5<=y<=45:
        convertToGrayscale(image)
    elif 460<=x<=520 and 5<=y<=45:
        bplus(image)
    elif 530<=x<=590 and 5<=y<=45:
        bminus(image)
    elif 600<=x<=670 and 5<=y<=45:
        save(image)
    elif 680<=x<=780 and 5<=y<=45:
        win.close()
def main():
    win= GraphWin("Image Processer",800,600)
    infile = input("Enter the name of a GIF or PNG file to convert: ")
    image=openImage(infile,win)
    buttons(win)
    while "t":
        key=win.checkKey()
        if key:
           keyhandle(key,win,image)
        mouse=win.checkMouse()
        if mouse:
           mousehandle(mouse,win,image)

    print()
    print("Done")
main()
