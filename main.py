from tkinter import *
from tkinter import ttk
from pynput import keyboard as kb

def press(key):

	match (key):
		case kb.Key.left:
			print("Left")
		case kb.Key.right:
			print("Right")
		case kb.Key.esc: 
			return False

kb.Listener(press).run()
# class Application:
#     wn_title = "Tetris"
#     wn_width = 500
#     wn_height = 500
#     wn_bgColor = "#242424"
            
#     def start(self) : 
#         window = Tk()
#         window.title(self.wn_title)
#         window.configure(bg=self.wn_bgColor)
#         window.geometry(f"{self.wn_width}x{self.wn_height}")
#         window.resizable(0,0)
#         window.mainloop()
        
# tetris = Application()
# tetris.start()