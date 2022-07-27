import time
from pynput.keyboard import Key, Controller
from pynput import keyboard
from concurrent.futures import ThreadPoolExecutor
import win32api
import ctypes

controller = Controller()
x = True

print(f"Toggled: {x}")


# Switch bool function
def on_activate():
    global x
    x = not x
    # In case you want to see this debug, change the file (pyw -> py)
    print(f"Toggled: {x}")


def listener():
    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+i'),
        on_activate
    )

    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)
    ) as l:
        l.join()

# Detect caps lock
def is_capslock_on():
    return True if ctypes.WinDLL("User32.dll").GetKeyState(0x14) else False

# Main code
def main():
    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(listener)

    while True:
        if x == True:
            v = win32api.GetKeyState(0xBA)

            if v < 0:
                controller.press(Key.backspace)
                controller.release(Key.backspace)

                # finally, press ñ detecting if its a cap or not
                if(is_capslock_on()):
                    controller.press("Ñ")
                    controller.release("Ñ")
                    time.sleep(0.1)
                

                else:
                    controller.press("ñ")
                    controller.release("ñ")
                    time.sleep(0.1)


if __name__ == "__main__":
    main()