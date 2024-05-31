import win32gui
import sys
from PIL import ImageGrab
import time

def get_window_location(window_name: str) -> list[int, int, int, int]:
    try:
        # FindWindow takes the Window Class name (can be None if unknown), and the window's display text. 
        window_handle = win32gui.FindWindow(None, window_name)
        window_rect   = win32gui.GetWindowRect(window_handle)
    except Exception:
        print("No window found.")
        sys.exit(1)

    return window_rect

def swap_window(window_name: str):
    window_handle = win32gui.FindWindow(None, window_name)
    win32gui.SetForegroundWindow(window_handle)

def capture_window(window_loc: list, save_path: str, interval: float):
    if window_loc:
        time.sleep(interval)
        image = ImageGrab.grab(window_loc)
        image.save(save_path)
    else:
        print("No window found")
        exit()