import pytest

from translation import Translation
from ocr import OCR


# Test Translation
def test_translate_to_english():
    translation = Translation()
    translated_text = translation.translate_to("こんにちは", "en", "ja")
    assert translated_text == "Hello"


def test_translate_to_japanese():
    translation = Translation()
    translated_text = translation.translate_to("Hello", "ja", "en")
    assert translated_text == "こんにちは"


def test_translate_to_korean():
    translation = Translation()
    translated_text = translation.translate_to("Hello", "ko", "en")
    assert translated_text == "안녕하세요"


def test_translate_to_chinese_simplified():
    translation = Translation()
    translated_text = translation.translate_to("Hello", "zh-cn", "en")
    assert translated_text == "你好"


def test_translate_to_chinese_traditional():
    translation = Translation()
    translated_text = translation.translate_to("Hello", "zh-tw", "en")
    assert translated_text == "你好"


# Test OCR
def test_image_to_string():
    ocr = OCR()
    text = ocr.image_to_string("pytesseract_test_data/test-small.jpg", "eng")
    assert text == "This\n"


def test_image_to_string_2():
    ocr = OCR()
    text = ocr.image_to_string("pytesseract_test_data/test.png", "eng")
    expected_text = (
        "This is a lot of 12 point text to test the\n"
        "ocr code and see If it works on all types\n"
        "of file format.\n\n"
        "The quick brown dog Jumped over the\n"
        "lazy fox. The quick brown dog Jumped\n"
        "over the lazy fox. The quick brown dog\n"
        "jumped over the lazy fox. The quick\n"
        "brown dog jumped over the lazy fox.\n"
    )
    assert text.strip() == expected_text.strip()
