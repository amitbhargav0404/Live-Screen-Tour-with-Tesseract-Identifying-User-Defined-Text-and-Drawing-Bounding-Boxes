import cv2
import pytesseract
import pyautogui
import numpy as np
import time
import re 
from PIL import Image, ImageGrab


font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
pattern = r'[^a-zA-Z0-9]'

# Capture the screen and perform OCR to recognize text
def capture_screen():
    screen = ImageGrab.grab(bbox=(252, 331, 966, 522))
    pattern = r'[^a-zA-Z0-9]'
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    text = pytesseract.image_to_string(screen,lang='eng', config='--psm 6')
    live_text_filtered = re.sub(pattern, '', text)
    return screen, live_text_filtered

# Show the recognized text as a message on the screen
def show_message(screen, live_text_filtered,org,font_scale=1):
    screen = np.array(screen)
    # Calculate the size of the message box based on the length of the text
    (w, h), _ = cv2.getTextSize("Hello, World!", font, fontScale=font_scale, thickness=1)
    x = int(screen.shape[1]/2 - w/2)
    y = int(screen.shape[0]/2 - h/2)
    # Draw a white rectangle as the background of the message box
    cv2.rectangle(screen, (x-2, y-2), (x+w+10, y+h+10), (255, 255, 255), -1)
    # Draw the text on the message box
    cv2.putText(screen, "Hello, World!", (x, y+h), font, fontScale=font_scale, color=(0, 0, 0), thickness=0, lineType=cv2.LINE_AA)
    # Show the screen with the message
    cv2.imshow("Screen", screen)
    cv2.waitKey(1)
    # screen = np.array(screen)
    # # Calculate the size of the message box based on the length of the text
    # (w, h), _ = cv2.getTextSize("Welcome to my program!", font, fontScale=font_scale, thickness=1)
    # x = int(screen.shape[1]/2 - w/2)
    # y = int(screen.shape[0]/2 - h/2)
    # # Draw a white rectangle as the background of the message box
    # cv2.rectangle(screen, (x-2, y-2), (x+w+10, y+h+10), (255, 255, 255), -1)
    # # Draw the text on the message box
    # cv2.putText(screen, "Welcome to my program!", (x, y+h), font, fontScale=font_scale, color=(0, 0, 0), thickness=0, lineType=cv2.LINE_AA)
    # # Show the screen with the message
    # cv2.imshow("Screen", screen)
    # cv2.waitKey(1)


def main():
    # Load the pre-defined image for comparison
    original_image = Image.open('License3.png')
    # Convert the original image to grayscale
    original_image_grayscale = original_image.convert('L')
    # Extract text from the original image and filter out noise values
    original_text = pytesseract.image_to_string(original_image_grayscale, lang='eng', config='--psm 6')
    original_text_filtered = re.sub(pattern, '', original_text)
    # Start capturing the screen and comparing it to the pre-defined image
    while True:
        # Capture the screen and recognize text
        screen, live_text_filtered = capture_screen()
        # Compare the recognized text to the pre-defined image text
        print("original_text_filtered:-",original_text_filtered)
        print("live_text_filtered:- ",live_text_filtered)
        if original_text_filtered == live_text_filtered:
            # Show the recognized text as a message on the screen
            org = (screen.shape[1]-200, 50)
            show_message(screen, "Hello, World!",org=org,font_scale=0.5)
            # Wait for a short time to avoid overwhelming the CPU
            print("value come here ?:----")
            
            
            cv2.waitKey(100)
        else:
            # Clear the message box and continue capturing the screen
            # cv2.imshow("User Guided Screen", screen)
            # cv2.waitKey(1)
            print("value come here:-----")
        # Check if the 'q' key is pressed to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the resources used by OpenCV
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()