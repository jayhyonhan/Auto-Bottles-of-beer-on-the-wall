import pyperclip, keyboard

def wait_for_paste():
    while not(keyboard.is_pressed("ctrl+v")):
        pass
    print("paste detected!")
    while not(keyboard.is_pressed("enter")):
        pass
    print("message sent!")

start_int = int(input("Starting number: "))

while start_int > 0:
    pyperclip.copy(f"{start_int} bottles of beer on the wall, {start_int} bottles of beer. You take one down, pass it around {start_int-1} bottles of beer on the wall")
    wait_for_paste()
    start_int -= 1
