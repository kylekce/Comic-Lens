import pytesseract.pytesseract
from PIL import Image


class OCR:
    def __init__(self):
        # Get the supported languages
        # supported_languages = pytesseract.get_languages()
        # print("Supported Languages:", supported_languages)
        pass

    def image_to_string(self, image_path, language):
        """Open the image"""
        img = Image.open(image_path)

        # Perform OCR
        text = pytesseract.image_to_string(img, lang=language)

        return text
