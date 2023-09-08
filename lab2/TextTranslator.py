from googletrans import Translator
from googletrans import LANGUAGES
from googletrans import LANGCODES


class TextTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, txt, lang):
        try:
            translation = self.translator.translate(txt, dest=lang)
            return translation.text
        except Exception as e:
            return f"Translation error: {str(e)}"

    def langDetect(self, txt):
        try:
            detected = self.translator.detect(txt)
            return f"Detected(lang={detected.lang}, confidence={detected.confidence})"
        except Exception as e:
            return f"Language detection error: {str(e)}"

    def codeLang(self, lang):
        lang = str.lower(lang)
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        elif lang in LANGCODES:
            return LANGCODES[lang]
        else:
            return "Language not found"
