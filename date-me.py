from tkinter import *
from tkinter import ttk
import random


#CONSTANTS
BACKGROUND_COLOR = '#856ff8'
DEFAULT_FONT_FAMILY = 'Calibri'
SCREEN_SIZE_WIDTH_HEIGHT = '450x300'
BUTTON_FONT_SIZE = '12'
MSG_FONT_SIZE = "16"


class DateMe:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.configure(background=BACKGROUND_COLOR)
        self.widget1.pack()
        
        self.msg = Label(self.widget1, text="Date me?")
        self.msg["font"] = (DEFAULT_FONT_FAMILY, MSG_FONT_SIZE, "bold")
        self.msg.configure(background = BACKGROUND_COLOR, foreground='WHITE', height=6)
        self.msg.pack ()
        
        self.yes = Button(self.widget1, text="yes")
        self.yes["font"] = (DEFAULT_FONT_FAMILY,BUTTON_FONT_SIZE)
        self.yes.configure(background=BACKGROUND_COLOR,command=self.happyness, width = 5)
        self.yes.pack (side=LEFT)
        
        self.no = Button(self.widget1, text= "no")
        self.no["font"] = (DEFAULT_FONT_FAMILY, BUTTON_FONT_SIZE)
        self.no.configure(background= BACKGROUND_COLOR, command = self.runAwayButton, width= 5)
        self.no.pack (side=RIGHT)
    def runAwayButton():
        a=1

        
    def happyness():
        a=1


def main():
    root = Tk(className='Date-me')
    root.geometry(SCREEN_SIZE_WIDTH_HEIGHT)
    root.configure(background= BACKGROUND_COLOR)
    root.eval('tk::PlaceWindow . center')
    DateMe(root)
    root.mainloop()
    
    
if __name__ == '__main__':
    main()