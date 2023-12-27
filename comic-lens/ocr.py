import pytesseract
from PIL import Image

# Open an image file
image_path = "tests/data/test.jpg"
img = Image.open(image_path)

# Perform OCR
text = pytesseract.image_to_string(img)

# Print the result
print("OCR Result:", text)
