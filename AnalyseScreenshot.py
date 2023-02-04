# We import the necessary packages
# import the needed packages
import cv2
import os
import argparse
import pytesseract
from PIL import Image
from MarketAbuse import sara_mkt_abuse

def AnalyseScreenshot():

    # We then Construct an Argument Parser
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image",
                    required=True,
                    help="Path to the image folder")


    ap.add_argument("-p", "--pre_processor",
                default="thresh",
                help="the preprocessor usage")
    args = vars(ap.parse_args())

    # We then read the image with text
    images = cv2.imread(args["image"])

    # convert to grayscale image
    gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

    # checking whether thresh or blur
    if args["pre_processor"] == "thresh":
        cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    if args["pre_processor"] == "blur":
        cv2.medianBlur(gray, 3)

    # memory usage with image i.e. adding image to memory
    filename = "{}.jpg".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    
    # find wood sell and buy price
    slash = text.find('/')
    letter_y = text.find('y')
    
    letter_l = text.find('l')
    letter_f = text.find('Food')
    
    buy = int(text[letter_y + 2: slash])
    sell = int(text[letter_l + 3 + 1: letter_f])
    
    # determine, if we should abuse
    if sell > buy:
        sara_mkt_abuse()    

AnalyseScreenshot()