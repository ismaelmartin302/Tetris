from pynput import keyboard as kb
log_Keyboard = []
def press(key):
    match (key):
        case kb.Key.left:
            print("Left")
        case kb.Key.right:
            ("Right")
        case kb.Key.space: 
            log_Keyboard.append(" ")
        case kb.Key.esc:
            return False
    log_Keyboard.append(str(key))
		
kb.Listener(press).run()
print((log_Keyboard))