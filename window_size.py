from win32gui import FindWindow, GetWindowRect

def get_window_dimensions():
    try:
        # FindWindow takes the Window Class name (can be None if unknown), and the window's display text. 
        window_handle = FindWindow(None, "Angry Birds 2")
        window_rect   = GetWindowRect(window_handle)
    except:
        return [0, 0, 0, 0]

    return window_rect