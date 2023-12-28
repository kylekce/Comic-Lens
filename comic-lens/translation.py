from googletrans import Translator


class Translation:
    def __init__(self):
        self.translator = Translator()

    def translate_to(self, text, dest, src):
        """Translate text from src to dest"""
        translation = self.translator.translate(text, dest, src)

        return translation.text
