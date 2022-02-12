
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import frontend

answer= frontend.answer

#root window
root = Tk()
root.title('WeatherRecognization')
root['bg']='#E3EDF2'

#app name
title = Label(root, text="Weather Recognization",font=("Helvetica",30), bg="#e3edf2")
title.grid(column=0, row=0, columnspan=2,pady=5,padx=20)

#default image
img = ImageTk.PhotoImage(Image.open("2.png"))
imgFrame = Label(image=img, bg ="#E33DF2", width=200 , height=200)
imgFrame.grid(column=0, row=1, columnspan=2,pady=5,padx=20)

def choose():
    root.filename= filedialog.askopenfilename(initialdir="/",title="Select a File", filetypes = (("png jpg","*.png*""*.jpg*"),("all files","*.*")))
    path=root.filename
    imgDisplay(path)
    ans = answer(path)
    print(ans)
    result(ans)
    
#result
display=Label(root,text='cloudy:-- haze:-- rainy:-- sunny:--',font=("Helvetica",10),bg="#e3edf2")
display.grid(column=0, row=2, columnspan=2,pady=10,padx=20)

#image display
def imgDisplay(path):
    global img
    global imgFrame
    
    img= ImageTk.PhotoImage(Image.open(path))
    imgFrame= Label(image=img,width=200,height=200,bg='#E3EDF2').grid(column=0,row=1,columnspan=2)
    

#retrive data
categories=["cloud","haze","rainy","sunny"]
def result(prediction):
    print(prediction)
    global redisplay
    cloudy=str(prediction[0][0]*100)
    haze=str(prediction[0][1]*100)
    rainy=str(prediction[0][2]*100)
    sunny=str(prediction[0][3]*100)
    display.grid_forget()
    redisplay = Label(root,text='cloudy:'+cloudy + '% haze:'+haze+'% rainy:'+rainy+'% sunny:'+sunny+'%', font=("Helvetica",10),bg="#e3edf2")
    redisplay.grid(column=0, row=2, columnspan=2,pady=10,padx=20)


#choose btn for selecting image file
choosebtn = Button(root,text="choose image",padx=10,pady=5,border=0,bg='#ff8448',fg="white",font=("Helvetica",10),command=choose)
choosebtn.grid(column=1, row=3,pady=10,padx=20)

root.mainloop()

    