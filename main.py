def on_logo_long_pressed():
    keyboard.send_string("" + keyboard.modifiers(keyboard._Modifier.CONTROL) + str(tabi))
    keyboard.send_string("" + keyboard.modifiers(keyboard._Modifier.CONTROL) + "w")
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_bluetooth_connected():
    serial.write_line("con")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    serial.write_line("dis")
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    global tabi
    tabi += -1
    basic.show_number(tabi)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    keyboard.send_string("" + keyboard.modifiers(keyboard._Modifier.CONTROL) + "t")
    keyboard.send_string("chrome://restart")
    keyboard.send_string(keyboard.keys(keyboard._Key.ENTER))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global tabi
    tabi += 1
    basic.show_number(tabi)
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function():
    global lock
    if lock == False:
        keyboard.send_string("" + keyboard.modifiers(keyboard._Modifier.CONTROL) + keyboard.modifiers(keyboard._Modifier.SHIFT) + "w")
        keyboard.send_string("" + keyboard.modifiers(keyboard._Modifier.CONTROL) + "n")
        keyboard.send_string("https://www.yout-ube.com/watch?v=LLh0WOuP89Y")
        keyboard.send_string(keyboard.keys(keyboard._Key.ENTER))
    basic.pause(100)
    lock = not (lock)
buttonClicks.on_button_held(buttonClicks.AorB.A, my_function)

tabi = 0
lock = False
lock = False
tabi = 1
media.start_media_service()
keyboard.start_keyboard_service()

def on_forever():
    if lock:
        keyboard.send_string("" + keyboard.modifiers(keyboard._Modifier.CONTROL) + "n")
        keyboard.send_string("chrome://restart")
        keyboard.send_string(keyboard.keys(keyboard._Key.ENTER))
    basic.pause(300)
basic.forever(on_forever)
