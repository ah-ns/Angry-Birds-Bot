import cv2 as cv
import easyocr as ocr
import window
import object_detection
from email_whisper import send_email

# Find the area to be monitored
def get_image(path: str) -> list[int, int, int, int]:
    """ Gets image corners to search within

    :param str path: Where to save the image
    :return: window_bounds
    :rtype: list[int, int, int, int]
    """
    window.swap_window("Warframe")

    # Find the bounds of the chat box with open cv
    
    return window_bounds

# Detect when a whisper is sent
def detect_whisper(window_bounds: list, path: str) -> bool:
    # Capture area determined from get_image
    window.capture_window(window_bounds, path, 5)

    # Use color match to see if purple appears in the picture (signaling a whisper)
    
    # return True if *purple is detected* 

# Uses optical character recognition to detect words in pictures
def image_to_text(image: str) -> str:
    image_reader = ocr.Reader(['en'])
    result = image_reader.readtext(image)

    # Figure out how to separate username from the message in the result
    
    return username, text

def main():
    window_bounds = get_image()

    while True:
        if detect_whisper(window_bounds, "C:\\Users\\ahns\\Programming\\Python\\Remote_Whisper\\Image.jpg"):
            image_to_text("C:\\Users\\ahns\\Programming\\Python\\Remote_Whisper\\Image.jpg")

            send_email(username, text)

if __name__ == "__main__":
    main()