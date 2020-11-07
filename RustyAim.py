# https://pypi.org/project/pynput/

# This is required as pynput does not support direct input, which RUST needs to control the mouse
# This will substitute as pynput.mouse.Controller()
import mouse as system_mouse
from pynput import mouse

# We need this as otherwise there would be a delay during any mouse movements
import threading

def adjustRecoil(xDelta, yDelta):
    th = threading.Thread(target = lambda x, y: system_mouse._os_mouse.move_relative(x, y), args = (xDelta, yDelta,))
    th.start()

adjusting = False
left_pressed = False
right_pressed = False
def on_click(x, y, button, pressed):
    global adjusting
    global left_pressed
    global right_pressed

    if button == mouse.Button.left:
        print("Left")
        left_pressed = pressed

        if right_pressed and pressed == True and not adjusting:
            adjusting = True
            print("Adjusting Recoil")

            adjustRecoil(0, 86)

            adjusting = False

    if button == mouse.Button.right:
        print("Right")
        right_pressed = pressed

def on_scroll(x, y, dx, dy):
    print("scrolled")

from pynput import keyboard

def on_press(key):
    print("pressed")
    mouse_listener.stop()
    return False

def on_release(key):
    print("released")

# Setup the listener threads
keyboard_listener = keyboard.Listener(on_press = on_press, on_release = on_release)
mouse_listener = mouse.Listener(on_click = on_click, on_scroll = on_scroll)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
