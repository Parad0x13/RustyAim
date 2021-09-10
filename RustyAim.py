# https://pypi.org/project/pynput/

# This is required as pynput does not support direct input, which RUST needs to control the mouse
# This will substitute as pynput.mouse.Controller()
import mouse as system_mouse
from pynput import mouse

# We need this as otherwise there would be a delay during any mouse movements
import threading

from time import sleep

isActive = False

def testing(x, y, delay):
    sleep(delay)
    system_mouse._os_mouse.move_relative(x, y)

def adjustRecoil(xDelta, yDelta, delay = 0):
    th = threading.Thread(target = lambda x, y, d: testing(x, y, d), args = (xDelta, yDelta, delay))
    th.start()

import random
def test():
    global adjusting
    global left_pressed
    global right_pressed

    adjusting = True

    minimum = 0.175
    maximum = 0.3
    for n in range(6):
        system_mouse._os_mouse.press("left")
        system_mouse._os_mouse.release("left")
        system_mouse._os_mouse.move_relative(0, 28)
        val = random.uniform(minimum, maximum)
        print(val)
        sleep(val)

    adjusting = False

def poo():
    global adjusting
    global left_pressed

    adjusting = True

    minimum = 0.175
    maximum = 0.4

    while left_pressed:
        system_mouse._os_mouse.press("left")
        system_mouse._os_mouse.release("left")
        system_mouse._os_mouse.move_relative(0, 28)
        val = random.uniform(minimum, maximum)
        print(val)
        sleep(val)

    adjusting = False

adjusting = False
left_pressed = False
right_pressed = False
def on_click(x, y, button, pressed):
    global left_pressed
    global right_pressed

    global adjusting
    global isActive
    print("Called: {}, {}".format(button, pressed))

    if button == mouse.Button.left: left_pressed = pressed
    if button == mouse.Button.right: right_pressed = pressed

    #if not isActive: return

    # TESTING
    if right_pressed and left_pressed:
        #print("Testing")
        for d in range(20):
            delta = 3.7/30.0    # ~1.233333 seconds I think?
            adjustRecoil(0, 10, delay = d * delta)
        #print("Done")
    # TESTING

    #if adjusting: return

    #if button == mouse.Button.left and not adjusting:
    #    print("Left")
    #    left_pressed = pressed

    #if button == mouse.Button.right and not adjusting:
    #    print("Right")
    #    right_pressed = pressed

    #print(left_pressed, right_pressed)

    # TESTING
    #if pressed == True and not adjusting:
    #if left_pressed and not adjusting:
    #if left_pressed and right_pressed and not adjusting:
    #    print("Attempting")

        #th = threading.Thread(target = test)
        #th.start()

    #    th = threading.Thread(target = poo)
    #    th.start()
    # TESTING

    """
    global adjusting
    global left_pressed
    global right_pressed

    if button == mouse.Button.left:
        print("Left")
        left_pressed = pressed

        if right_pressed and pressed == True and not adjusting:
            adjusting = True
            print("Adjusting Recoil")

            # This one is weird... doesn't act like the revolver at all
            adjustRecoil(0, 30)    # Revolver

            #adjustRecoil(0, 86)    # Python

            adjusting = False
    """

    #if button == mouse.Button.right:
    #    print("Right")
    #    right_pressed = pressed

def on_scroll(x, y, dx, dy):
    global isActive
    if not isActive: return

    print("scrolled")

from pynput import keyboard

def on_press(key):
    global isActive

    try:
        if key == key.f5:
            if isActive == True:
                isActive = False
                print("RustyAim Disabled")
            else:
                isActive = True
                print("RustyAim Enabled")
    except: pass

    if not isActive: return

    try:
        pass
        #if key.char == ("q"):
    except: pass

    #mouse_listener.stop()
    #return False

def on_release(key):
    global isActive
    if not isActive: return

# Setup the listener threads
keyboard_listener = keyboard.Listener(on_press = on_press, on_release = on_release)
mouse_listener = mouse.Listener(on_click = on_click, on_scroll = on_scroll)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
