from googletrans import Translator


class Translation:
    def __init__(self):
        self.translator = Translator()

    def translate_to(self, text, dest, src):
        """
        Translate text from src to dest

        Parameters:
        - text (str): Text to translate.
        - dest (str): Language code for the destination language.
        - src (str): Language code for the source language.

        Returns:
        - str: Translated text.
        """
        translation = self.translator.translate(text, dest, src)

        return translation.text
