
from Tkinter import *

###main:
window = Tk()
window.title("test")

def displayDoge():
    """Displays an image of a cute doge"""
    #Creates a new window with a title.
    dogebox = Toplevel()
    dogebox.title("Much WOW very excite!")
    #Loads the doge picture.
    dogeGif = PhotoImage(file="happydoge.png")
    #Adds the image to the window and keeps the window open.
    dogeLabel = Label(master=dogebox, image=dogeGif)
    dogeLabel.image = dogeGif
    dogeLabel.pack()
    dogebox.mainloop()


window.mainloop()
