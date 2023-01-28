import os
import pytesseract
from PIL import Image
import re
import cv2

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
folder_path = os.path.join(desktop_path, "New folder")

image_path = os.path.join(folder_path, "81uy5mDuvxL.jpg")

# Read image using OpenCV
image = cv2.imread(image_path)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive threshold to make the text more visible
gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Save the preprocessed image
cv2.imwrite(os.path.join(folder_path, "81uy5mDuvxL.jpg"), gray)

# Open the preprocessed image and convert to grayscale
image = Image.open(os.path.join(folder_path, "81uy5mDuvxL.jpg"))

# Run tesseract OCR on image
text = pytesseract.image_to_string(image)

# Print extracted text
print(text)