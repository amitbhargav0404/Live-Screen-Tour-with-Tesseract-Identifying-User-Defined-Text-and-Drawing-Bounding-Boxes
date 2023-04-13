# Live-Screen-Tour-with-Tesseract-Identifying-User-Defined-Text-and-Drawing-Bounding-Boxes
Have you ever wanted to guide someone through a process on your computer screen, but found it difficult to point out specific areas of interest? Or perhaps you want to automate a process that involves reading text from your screen. Tesseract, an open-source OCR engine, can help you recognize text in live screen captures and highlight specific areas of interest. In this blog post, we will explore how to use Tesseract to identify user-defined text and draw bounding boxes around it.

First, let's set up our environment by installing the necessary libraries. We will use OpenCV, a popular computer vision library, to capture the screen and draw rectangles, and PyTesseract, a Python wrapper for Tesseract, to recognize text in the screen capture.

```import cv2
import pytesseract
import pyautogui
import numpy as np
```
Next, we define a capture_screen() function that captures the screen and searches for user-defined text using Tesseract. In this example, we are searching for the text "hello". If the search text is found in the recognized text, we use the image_to_boxes() method in PyTesseract to get the bounding boxes of each character in the text. We then draw a red rectangle around each word that contains the search text.

```def capture_screen():
    while True:
        # Capture the screen and resize it
        screen = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        screen = cv2.resize(screen, (0,0), fx=0.5, fy=0.5) # resize to 50%
        # Use Tesseract to recognize text in the screen
        text = pytesseract.image_to_string(screen)
        # Define the text to look for
        search_text = "hello"
        # Check if the search text is in the recognized text
        if search_text in text.lower():
            # Get the bounding boxes of each character in the recognized text
            boxes = pytesseract.image_to_boxes(screen)
            # Draw a rectangle around each word that contains the search text
            for b in boxes.splitlines():
                b = b.split(' ')
                x,y,w,h = int(b[1]), int(screen.shape[0]) - int(b[2]), int(b[3]), int(b[4])
                if b[0].lower() == search_text:
                    cv2.rectangle(screen, (x,y), (w,h), (0,0,255), 2)
        # Display the annotated screen
        cv2.imshow("Screen", screen)
        # Wait for a key press
        key = cv2.waitKey(1)
        # If the key is the letter q, break the loop
        if key == ord("q"):
            break
    # Clean up
    cv2.destroyAllWindows()
```
Now we can call the capture_screen() function to start capturing the live screen and recognizing text. The code will continue to run until the user presses the "q" key, at which point the program will exit.

```capture_screen()```

That's it! With just a few lines of code, we can now guide someone through a process on our computer screen and highlight specific areas of interest. This technique can be useful for creating user guides, automating repetitive tasks, or simply making it easier to collaborate remotely.

In conclusion, we hope this blog post has helped you learn how to use Tesseract and OpenCV to recognize text in live screen captures and draw bounding boxes around user-defined text. Happy coding
