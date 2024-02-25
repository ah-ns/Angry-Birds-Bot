import pyautogui
import window
import object_detection as od
import numpy as np
import time

# Purpose: converts a coordinate argument in cartesian form to a coordinate in polar form
def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta_deg = np.degrees(np.arctan2(y, x))
     
    return r, theta_deg

# Purpose: converts a coordinate argument in polar form to a coordinate in cartesian form
def polar_to_cartesian(r, theta):
    theta = np.radians(theta)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y

# Purpose: return the launch angle in degrees to hit the lowest detected pig
def find_launch_angle(pig_locations):
    pass

# Determines where the slingshot is located on the screen, then pulls the slingshot
def slingshot(window_loc, window_scale):
    # Get the slingshot location
    sling_locations = od.find_by_image("Image.jpg", "ab_slingshot.jpg", .6)
    condensed_sling_locations, _ = od.condense_rectangles(sling_locations, 7, 7, 20)

    # +7 on each coordinate makes it close to the bottom right of the square
    origin = (condensed_sling_locations[0][0] + 7 + window_loc[0], condensed_sling_locations[0][1] + 7 + window_loc[1])
    pyautogui.moveTo(origin)

    #od.display_image("Image.jpg", condensed_sling_locations)

    # Determines where the sling will be dragged
    max_sling_dist = window_scale * 113
    launch_angle = 145 # Make a function to determine at what angle to launch
    x, y = polar_to_cartesian(max_sling_dist, launch_angle)
    pyautogui.dragRel(xOffset=x, yOffset=y, duration=1)

def main():
    # Get window location
    window_loc = window.get_window_location()
    print(f"Top left: {window_loc[0]}, {window_loc[1]} Bottom right: {window_loc[2]}, {window_loc[3]}")

    window.swap_window()

    # Screenshot the window and cut out the title bar of the window
    window.capture_window((window_loc[0], window_loc[1] + 32, window_loc[2], window_loc[3]))

    # Only need one axis to determine the scale of the entire screen because it keeps the same aspect ratio 
    window_scale = (window_loc[2] - window_loc[0]) / 1920

    slingshot(window_loc, window_scale)

main()
