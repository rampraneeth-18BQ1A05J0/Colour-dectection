import cv2
from tkinter import messagebox
import pandas as pd
from datetime import datetime as dt


#declaring global variables (are used later on)
clicked = False
r = g = b = hue = hsls = hsll = xpos = ypos = 0
imageName=""
info = dt.now()

#Reading csv file with pandas and giving names to each column
index=["color","hex","R","G","B","Hue","Saturation","Lightness"]
csv = pd.read_csv('colourDataSet.csv', names=index, header=None)
    
def getColor(y,x):
    global imageName,r,g,b
    imgObj = cv2.imread(imageName)
    b,g,r = imgObj[y,x]
    return b,g,r

#function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):
    global hue,hsls,hsll
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color"]
            hue=str(csv.loc[i,"Hue"])
            hsls=str(csv.loc[i,"Saturation"])
            hsll=str(csv.loc[i,"Lightness"])
    return cname

#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked,imageName
        clicked = True
        xpos = x
        ypos = y
        b,g,r = getColor(y,x)
        print(b,g,r)
        b = int(b)
        g = int(g)
        r = int(r)
        
def Filewrite(text,opfile):
    global xpos,ypos
    opfile.write("At x="+str(xpos)+' '+"y="+str(ypos)+'\t'+text+'\n')
    print("At x="+str(xpos)+' '+"y="+str(ypos)+'\t'+text+'\n')


def start(imName):
    global clicked,r,g,b,xpos,ypos,csv,imageName
    error=0
    opfile=open("ColourDetectionResults.txt",'a')
    
    imName=imName.strip()
    imageName=imName
    img = cv2.imread(imName)
    
    opfile.write("Image = "+imName+'\n'+"At "+str(info)+"\n")
    print("Image "+imName,'\n'+"At "+str(info)+"\n")
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_function)

    while(1):
        try:
            cv2.imshow("image",img)
        except:
            error=1
            break
        if (clicked):
            #Creating text string to display( Color name and RGB values )
            text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b) + ' Hue='+str(hue) + ' Saturation%='+str(hsls) + ' Lightness%='+str(hsll)
            Filewrite(text,opfile)                  
            clicked=False

        #Break the loop when user hits 'esc' key    
        if cv2.waitKey(20) & 0xFF ==27:
                break

    if error==1:
        messagebox.showerror('Error','Image Not Found')
    opfile.close()      
    cv2.destroyAllWindows()
