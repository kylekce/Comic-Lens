import pytesseract.pytesseract
from PIL import Image


class OCR:
    def __init__(self):
        pass

    def ocr(self, image_path):
        # Open the image
        img = Image.open(image_path)

        # Perform OCR
        text = pytesseract.image_to_string(img)
        print("OCR Result:", text)

        return text
