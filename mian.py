from tkinter import *
from tkinter import font
from tkinter import filedialog
from pygame import *
import pygame
import os


#file=str(input("file adres: "))
#front
titleN='ASH_Music_Player v1.0'
#//////////////////
geter= Tk()
geter.title(titleN)
geter.resizable(0,0)
#geter.iconbitmap(r'C:\Users\arman\OneDrive\Desktop\porg\mp\final\ash1.ico')
#geter.iconphoto(False,'ash1.ico')
geter.iconbitmap('ash1.ico')
def fileadd():
    global file
    file = filedialog.askdirectory()

    textclo.config(state=NORMAL)
    textclo.insert('1.0','  Thank You For Using Me')
    textclo.config(state=DISABLED)
    geter.after(3000,lambda:geter.destroy())
filebtn = Button(text='Select File Address',activebackground='#345',width=20,height=1,font=('Imprint MT Shadow',16),bd=5,
bg= '#00008B',fg="white",command=fileadd)    
filebtn.pack()
textclo = Text(width=25 , height=1,font=('Freestyle Script',20),padx= 15,bd=5,
bg="#00008B",fg="white",state=DISABLED)
textclo.pack()

geter.mainloop()
#//////////////////

root = Tk()
root.geometry("600x420")
root.resizable(0,0)
root.title(titleN)
#root.iconbitmap(r'C:\Users\arman\OneDrive\Desktop\porg\mp\ash1.ico')
root.iconbitmap('ash1.ico')
status=StringVar()
status.set("Nothing Play!!!")
pygame.init()
pygame.mixer.init()

#back def
def playsong():
    trackname.config(state=NORMAL)
    trackname.delete('1.0',END)
    trackname.insert('1.0',playlist.get(ACTIVE))
    trackname.config(state=DISABLED)
    status.set("Playing")
    #playsong
    
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()

    #print(playlist.index())
    #pygame.mixer.music.queue()

    
    

def stopsong():
    trackname.config(state=NORMAL)
    trackname.delete('1.0',END)
    trackname.config(state=DISABLED)

    status.set("Stopped")

    #stopsong
    pygame.mixer.music.stop()


def pausesong():
    status.set("paused")
    pygame.mixer.music.pause()

def unpausesonge():
    status.set("Playing")
    pygame.mixer.music.unpause()
    
#front
def autoplay():
    pygame.mixer.music.play()
    
    pass

trackframe = LabelFrame(root, text='Track Name',font=('Imprint MT Shadow',15,"bold"),
bg='#97FFFF',fg='#CD0000', bd=5 ,relief=GROOVE)

trackframe.place(x=0,y=197.5,width=600,height=120)

trackname = Text(trackframe,width=50 , height=2,font=('Freestyle Script',20),padx= 10,bd=5,
bg="#00008B",fg="white",state=DISABLED)

trackname.grid(row=0 , column= 0 ,padx=5 , pady=10)

trackstatus= Label(trackframe, textvariable = status , font=('Imprint MT Shadow',10),
bg= '#00008B',fg="white")

trackstatus.grid(row=0,column=1,padx=2,pady=10)

buttonframe=LabelFrame(root,text='Control Panel',font=('Imprint MT Shadow',15,"bold"),
bg='#97FFFF',fg='#CD0000',bd=5, relief=GROOVE)

buttonframe.place(x=0,y=320,width=600,height=100)

playbtn = Button(buttonframe,text='Play',activebackground='#345',width=9,height=1,font=('Imprint MT Shadow',16),bd=5,
bg= '#00008B',fg="white",command=playsong)

playbtn.grid(row=0,column=0,padx=6,pady=5)


pausebtn = Button(buttonframe,text='Pause',activebackground='#345',width=9,height=1,font=('Imprint MT Shadow',16),bd=5,
bg= '#00008B',fg="white",command=pausesong)

pausebtn.grid(row=0,column=1,padx=6,pady=5)

unpausebtn = Button(buttonframe,text='Unpause',activebackground='#345',width=9,height=1,font=('Imprint MT Shadow',16),bd=5,
bg= '#00008B',fg="white",command=unpausesonge)

unpausebtn.grid(row=0,column=2,padx=6,pady=5)


stop = Button(buttonframe,text='STOP',activebackground='#345',width=9,height=1,font=('Imprint MT Shadow',16),bd=5,
bg= '#00008B',fg="white",command=stopsong)

stop.grid(row=0,column=3,padx=6,pady=5)

  
playlistframe = LabelFrame(root , text='Play list',font=('Imprint MT Shadow',15,"bold"),
bg='#838B8B',fg='#FFD700', bd=5 ,relief=GROOVE)

playlistframe.place(x=0,y=0,width=600,height=195)

scroll_y = Scrollbar(playlistframe,orient=VERTICAL)

playlist = Listbox(playlistframe, selectbackground='gold',selectmode=SINGLE ,
font=('Imprint MT Shadow',12), bg= 'silver' , fg='navyblue',bd=5,relief=GROOVE,yscrollcommand=scroll_y.set) 

scroll_y.config(command=playlist.yview)

scroll_y.pack(side=RIGHT,fill=Y)
playlist.pack(fill=BOTH)

#os.chdir(r"C:\Users\arman\Downloads\Telegram Desktop")
os.chdir(file)
tracknames = os.listdir()
for track in tracknames:
    if ".mp3" in track:
        playlist.insert(END,track )
    else:
        pass

#back



root.mainloop()
