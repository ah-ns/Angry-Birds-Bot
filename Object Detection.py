import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Purpose: Debugging - resizes image to see where detections occur more closely
def resize_image(image):
    scale_percent = 500 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # Returns the specified image with transformed dimensions and interpolation formula (explained here -> https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121)
    return cv.resize(image, dim, interpolation = cv.INTER_AREA)

# Purpose: Turns an image into an array representing rgb values of pixels
def image_color_array(image):
    return np.array(image, dtype=np.uint8) # uint8 is used because rgb only ranges from 0-255, only 8 bits

# Purpose: Finds objects based on their color
def find_by_color(color_array, threshold):
    locations = []

    # First needs to be enumerated into pixel rows
    for i, row in enumerate(color_array):
        # Then further needs to be enumerated into individual pixels
        for j, pixel in enumerate(row):
            r, g, b = [int(color) for color in pixel]
            
            if g >= threshold and g > r + 150 and g > b + 150:
                locations.append((j, i))

    return locations

# Purpose: Condenses rectangles that are near one another to avoid detecting something multiple times
# Parameters: original locations of found objects, w, h, how far the condensation will occur from
# Return: list with x, y, w, h for each of the condensed rectangles
def condense_rectangles(locations, w, h, distance_threshold):
    rectangles = [[int(location[0]), int(location[1]), w, h] for location in locations]
    
    return cv.groupRectangles(rectangles, 1, distance_threshold)

# Purpose: Draws on the image to show where detections have occurred
def display_image(image, locations):
    # Prevents errors from occuring when there are no initial detections
    if len(locations) > 0:
        for (x, y, w, h) in locations:
            top_left = (x, y)
            # The reason you add height is beacuse it is referencing an index, not a coordinate
            bottom_right = (x + w, y + h) 
            # cv2.rectangle(image, start_point, end_point, color, thickness)
            cv.rectangle(image, top_left, bottom_right, color=(255,0,255), thickness=1)

    cv.imshow('Result', image)
    # Must be used so the image doesn't vanish instantly
    cv.waitKey()

def main():
    # Template Matching Example: https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
    haystack_img = cv.imread('ab_level_6.jpg', cv.IMREAD_UNCHANGED)
    needle_img = cv.imread('ab_pig.jpg', cv.IMREAD_UNCHANGED)

    #needle_img = resize_image(needle_img)

    haystack_color_array = image_color_array(haystack_img)

    locations = find_by_color(haystack_color_array, 225)
    condensed_locations, _ = condense_rectangles(locations, 2, 2, 5)

    display_image(haystack_img, condensed_locations)

main()

"""
# The reason width is the first value is because shape is (row, column), not (x, y). 
# The row is referenced first in arrays so this is the cause of the notation...
needle_w = np.shape(needle_img)[0]
needle_h = np.shape(needle_img)[1]

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

# Only want places where the confidence is at least 75% 
threshold = 0.75
# 'Where' function results in a list of x values and a list of y values
locations = np.where(result >= threshold)
# Using 'zip' function to combine x and y value lists
locations = list(zip(locations[::-1][0], locations[::-1][1]))

for location in locations:
    top_left = location
    # The reason you add height is beacuse it is referencing an index, not a coordinate
    bottom_right = location[0] + needle_h, location[1] + needle_w
    # cv2.rectangle(image, start_point, end_point, color, thickness)
    cv.rectangle(haystack_img, top_left, bottom_right, color=(255,0,255), thickness=2)

cv.imshow('Result', haystack_img)
cv.waitKey()
"""