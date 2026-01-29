bluetooth.onBluetoothConnected(function () {
    serial.writeLine("con")
})
bluetooth.onBluetoothDisconnected(function () {
    serial.writeLine("dis")
})
input.onButtonPressed(Button.A, function () {
    tabi += -1
    basic.showNumber(tabi)
})
input.onButtonPressed(Button.AB, function () {
    keyboard.sendString("" + keyboard.modifiers(keyboard._Modifier.control) + "t")
    keyboard.sendString("chrome://restart")
    keyboard.sendString(keyboard.keys(keyboard._Key.enter))
})
input.onButtonPressed(Button.B, function () {
    tabi += 1
    basic.showNumber(tabi)
})
buttonClicks.onButtonHeld(buttonClicks.AorB.A, function () {
    if (lock == false) {
        keyboard.sendString("" + keyboard.modifiers(keyboard._Modifier.control) + keyboard.modifiers(keyboard._Modifier.shift) + "w")
        keyboard.sendString("" + keyboard.modifiers(keyboard._Modifier.control) + "n")
        keyboard.sendString("https://www.yout-ube.com/watch?v=LLh0WOuP89Y")
        keyboard.sendString(keyboard.keys(keyboard._Key.enter))
    }
    basic.pause(100)
    lock = !(lock)
})
input.onLogoEvent(TouchButtonEvent.Released, function () {
    keyboard.sendString("" + keyboard.modifiers(keyboard._Modifier.control) + ("" + tabi))
    keyboard.sendString("" + keyboard.modifiers(keyboard._Modifier.control) + "w")
})
let tabi = 0
let lock = false
lock = false
tabi = 1
media.startMediaService()
keyboard.startKeyboardService()
basic.forever(function () {
    if (lock) {
        keyboard.sendString("" + keyboard.modifiers(keyboard._Modifier.control) + "n")
        keyboard.sendString("chrome://restart")
        keyboard.sendString(keyboard.keys(keyboard._Key.enter))
    }
    basic.pause(300)
})
