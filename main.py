from tkinter import *
from tkinter import ttk

class Application:
    wn_title = "Tetris"
    
    def __init__(self, wn_width, wn_height):
        self.wn_width = wn_width
        self.wn_height = wn_height
        
    def start(name) : 
        window = Tk()
        window.title("Tetris")
        window = Tk()
        window.title("Tetris")
        window.configure(bg="#242424")
        window.geometry("500x500")
        window.resizable(0,0)
        window.mainloop()
        
tetris = Application("500", "500")
tetris.start()