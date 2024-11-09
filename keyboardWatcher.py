from pynput import keyboard as kb
log_Keyboard = ""
def press(key):
    global log_Keyboard
    match (key):
        case kb.Key.left:
            print("Left")
        case kb.Key.right:
            ("Right")
        case kb.Key.space: 
            log_Keyboard += " "
        case kb.Key.esc:
            return False
    log_Keyboard += str(key)
		
kb.Listener(press).run()
print((log_Keyboard))