import pyautogui
import window
import object_detection as od
import numpy as np

def cartesian_to_polar(x, y):
    pass

def polar_to_cartesian(r, theta):
    pass 

def slingshot(window_loc, window_scale):
    sling_locations = od.find_by_image("default_level_1.jpg", "ab_slingshot.jpg", .6)
    condensed_sling_locations, _ = od.condense_rectangles(sling_locations, 7, 7, 20)

    # +7 makes it close to the bottom right of the square and the +32 on the vertical vector accounts for the title bar of the window
    origin = (condensed_sling_locations[0][0] + 7 + window_loc[0], condensed_sling_locations[0][1] + 7 + window_loc[1] + 32)
    pyautogui.moveTo(origin)

    sling_dist = window_scale * 113

    #od.display_image("default_level_1.jpg", condensed_sling_locations)

    #pyautogui.dragRel(xOffset=-sling_dist, yOffset=sling_dist, button="primary", duration=1)

def main():
    window_loc = window.get_window_dimensions()

    window.swap_window()

    window.capture_window(window_loc)
    
    # Only need one axis to determine the scale of the entire screen because it keeps the same aspect ratio 
    window_scale = (window_loc[2] - window_loc[0]) / 1920

    slingshot(window_loc, window_scale)

main()