import win32gui
from PIL import ImageGrab
import time

WINDOW_NAME = "Angry Birds 2"

def get_window_dimensions():
    try:
        # FindWindow takes the Window Class name (can be None if unknown), and the window's display text. 
        window_handle = win32gui.FindWindow(None, WINDOW_NAME)
        window_rect   = win32gui.GetWindowRect(window_handle)
    except:
        return [0, 0, 0, 0]

    return window_rect

def swap_window():
    # hwnd is the window handle
    hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    win32gui.SetForegroundWindow(hwnd)

def capture_window(window_loc):
    time.sleep(.5)
    image = ImageGrab.grab(window_loc)
    image.save("C:\\Users\\ahns\\Programming\\Python\\Image.jpg")