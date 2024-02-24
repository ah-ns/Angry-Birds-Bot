import pyautogui as pag
import window_size
import object_detection as od

def main():
    window_dims = window_size.get_window_dimensions()

    locations = od.find_by_image("default_level_1.jpg", "ab_slingshot.jpg", .6)
    condensed_locations, _ = od.condense_rectangles(locations, 7, 7, 20)

    # +14 makes it close to the bottom right of the square and the +32 on the vertical vector accounts for the title bar of the window
    click_point = (condensed_locations[0][0] + 14 + window_dims[0], condensed_locations[0][1] + 14 + window_dims[1] + 32)
    pag.moveTo(click_point)

    od.display_image("default_level_1.jpg", condensed_locations)
main()