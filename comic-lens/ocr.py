import cv2
import pytesseract.pytesseract
import numpy as np
from PIL import Image


class OCR:
    def __init__(self):
        # Get the supported languages
        # supported_languages = pytesseract.get_languages()
        # print("Supported Languages:", supported_languages)
        
        # Add tesseract to PATH
        pytesseract.pytesseract.tesseract_cmd = (
            "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        )

    def image_to_string(
        self,
        image_path,
        language,
        preview_path="preprocessed.png",
        resize_factor=5,
        blur_kernel_size=1,
    ):
        """
        Open and preprocess the image for OCR.

        Parameters:
        - image_path (str): Path to the input image.
        - language (str): Language code for OCR (e.g., "eng" for English).
        - preview_path (str): Path to save the preprocessed image for preview (default: "preprocessed.png").
        - resize_factor (float): Adjust the factor by which the image is resized. Larger values may improve OCR on high-resolution images. (default: 5).
        - blur_kernel_size (int): Adjust the kernel size for median blur. This controls the degree of smoothing applied to the image. (default: 5).

        Returns:
        - str: Extracted text using OCR.
        """

        # Open the image
        img = cv2.imread(image_path)

        # Resize the image
        img = cv2.resize(
            img, None, fx=resize_factor, fy=resize_factor, interpolation=cv2.INTER_CUBIC
        )

        # Convert to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply thresholding
        _, img_thresh = cv2.threshold(
            img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        # Apply median blur
        img_preprocessed = cv2.medianBlur(img_thresh, blur_kernel_size)

        # Save the preprocessed image for preview
        if preview_path:
            cv2.imwrite(preview_path, img_preprocessed)

        # Perform OCR
        text = pytesseract.image_to_string(img_preprocessed, lang=language)

        return text
