import cv2 as cv
import numpy as np
import os

# Makes sure the working directory is the one this file is in
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Purpose: Debugging - resizes image to see where detections occur more closely
def resize_image(image: str):
    scale_percent = 500 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # Returns the specified image with transformed dimensions and interpolation formula 
    # (explained here -> https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121)
    return cv.resize(image, dim, interpolation = cv.INTER_AREA)

# Purpose: Uses template matching to find an image within another image
def find_by_image(haystack_name: str, needle_name: str, threshold: float) -> list[list[int, int]]:
    # Template Matching Example: https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
    haystack_img = cv.imread(haystack_name, cv.IMREAD_COLOR)
    needle_img = cv.imread(needle_name, cv.IMREAD_COLOR)

    # The reason width is the first value is because shape is (row, column), not like (x, y). 
    # The row is referenced first in arrays so this is the cause of the notation...
    needle_w = np.shape(needle_img)[0]
    needle_h = np.shape(needle_img)[1]

    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

    # Only want places where the confidence is at least 75% 
    # 'Where' function results in a list of row values and a list of column values
    locations: list[list[int], list[int]] = np.where(result >= threshold)
    # Using 'zip' function to combine x and y value lists, stepping in 
    # reverse through the row and column lists to create a 2D list with each element being a row,col pair
    locations: list[list[int, int]] = list(zip(locations[::-1][0], locations[::-1][1]))

    # For each row,col pair in locations
    for location in locations:
        # Each location found will correspond to the top left of the needle image
        top_left = location
        # The reason you add height is beacuse it is referencing an index(row),
        # not a coordinate, the higher the index in a list, the closer to the end.
        bottom_right = location[0] + needle_h, location[1] + needle_w
        # cv2.rectangle(image, start_point, end_point, color, thickness)
        cv.rectangle(haystack_img, top_left, bottom_right, color=(255,0,255), thickness=2)

    return locations

# Purpose: Turns an image into an array representing rgb values of pixels
def image_color_array(img_name: str) -> np.array:
    image = cv.imread(img_name, cv.IMREAD_COLOR)
    return np.array(image, dtype=np.uint8) # uint8 is used because rgb only ranges from 0-255, only 8 bits

# Purpose: Finds objects based on their color
# Parameters: target color is the color closest to the color you want to find...
# gap_color1 and 2 are the minimum diffence in value you want the other colors to be from the target color
def find_by_color(color_array: np.array, threshold: float, target_color: str,
                  gap_color1: int, gap_color2: int) -> list[list[int, int]]:
    locations = []

    # First needs to be enumerated into pixel rows
    for i, row in enumerate(color_array):
        # Then further needs to be enumerated into individual pixels
        for j, pixel in enumerate(row):
            r, g, b = [int(color) for color in pixel]
            
            if target_color == "r":
                if r >= threshold and r > g + gap_color1 and r > b + gap_color2:
                    locations.append([j, i])
            elif target_color == "g":
                if g >= threshold and g > r + gap_color1 and g > b + gap_color2:
                    locations.append([j, i])
            else:
                if b >= threshold and b > r + gap_color1 and b > g + gap_color2:
                    locations.append([j, i])

    return locations

# Purpose: Condenses rectangles that are near one another to avoid detecting something multiple times
# Parameters: original locations of found objects, w, h, how far the condensation will occur from
# Return: list with x, y, w, h for each of the condensed rectangles
def condense_rectangles(locations: list[list[int, int]], w: int, h: int,
                        distance_threshold: int) -> list[list[int, int]]:
    # Each rectangle will have its location in the form of x, y, w, h
    rectangles: list[list[int, int, int, int]] = [[int(location[0]), int(location[1]), w, h] for location in locations]
    
    # Group the rectangles based on their proximity to one another
    return cv.groupRectangles(rectangles, 1, distance_threshold)

# Purpose: Draws on the image to show where detections have occurred
def display_image(image_name: str, locations: list[list[int, int]]):
    image = cv.imread(image_name, cv.IMREAD_COLOR)

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
    """ example usage"""
    haystack_img = "Image.jpg"

    #needle_img = resize_image()

    haystack_color_array = image_color_array(haystack_img)

    # Find pigs
    locations = find_by_color(haystack_color_array, 225, "g", 150, 150)
    condensed_locations, _ = condense_rectangles(locations, 2, 2, 5)


    display_image(haystack_img, condensed_locations)
    
if __name__ == "__main__":
    main()