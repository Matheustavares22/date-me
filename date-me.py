from tkinter import *
from tkinter import ttk
import random


#CONSTANTS
BACKGROUND_COLOR = '#856ff8'
DEFAULT_FONT_FAMILY = 'Calibri'
SCREEN_SIZE_WIDTH_HEIGHT = '450x300'
BUTTON_FONT_SIZE = '12'
MSG_FONT_SIZE = "16"


class DateMeApp:
    def __init__(self):
        self.root = Tk(className='Date-me')
        self.root.geometry(SCREEN_SIZE_WIDTH_HEIGHT)
        self.root.configure(background=BACKGROUND_COLOR)
        self.root.eval('tk::PlaceWindow . center')
        
        self.create_widgets()
        
    def create_widgets(self):       
        self.msg = Label(self.root, text="Date me?")
        self.msg["font"] = (DEFAULT_FONT_FAMILY, MSG_FONT_SIZE, "bold")
        self.msg.configure(background = BACKGROUND_COLOR, foreground='WHITE', height=5)
        self.msg.pack ()
        
        button_frame = Frame(self.root)
        button_frame.configure(background=BACKGROUND_COLOR)
        button_frame.pack()
        
        self.yes = Button(button_frame, text="yes")
        self.yes["font"] = (DEFAULT_FONT_FAMILY,BUTTON_FONT_SIZE)
        self.yes.configure(background=BACKGROUND_COLOR,command=self.happiness, width = 5)
        self.yes.pack (side=LEFT)
        
        self.no = Button(button_frame, text= "no")
        self.no["font"] = (DEFAULT_FONT_FAMILY, BUTTON_FONT_SIZE)
        self.no.configure(background= BACKGROUND_COLOR, command = self.runAwayButton, width= 5)
        self.no.pack (side=RIGHT)
        
    def runAwayButton():
        # TODO
        pass

        
    def happiness(self):
        new_window = Toplevel(self.root)
        new_window.title("SO YOU CHOOSE HAPPINESS")
        new_window.configure(background=BACKGROUND_COLOR)
        new_window
        
        
        #gif_label = Label(new_window, image='path_to_gif')
        #gif_label.pack()

        exit_button = Button(new_window, text="Exit", command=self.root.destroy)
        exit_button.pack()


def main():
    app = DateMeApp()
    app.root.mainloop()
    
    
if __name__ == '__main__':
    main()