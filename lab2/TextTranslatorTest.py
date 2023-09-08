import unittest
from TextTranslator import TextTranslator


class TestTextTranslator(unittest.TestCase):
    def setUp(self):
        self.text_translator = TextTranslator()

    def test_translate_english_to_ukrainian(self):
        txt = "Hello, how are you?"
        lang = "uk"

        translation = self.text_translator.translate(txt, lang)
        self.assertEqual(translation, "Привіт як ти?")

    def test_translate_ukrainian_to_english(self):
        txt = "Доброго дня. Як справи?"
        lang = "en"

        translation = self.text_translator.translate(txt, lang)
        self.assertEqual(translation, "Good day. How are you?")

    def test_translate_chinese_to_english(self):
        txt = "你好吗？"
        lang = "en"

        translation = self.text_translator.translate(txt, lang)
        self.assertEqual(translation, "Are you OK?")

    def test_detect_language_english(self):
        txt = "Hello, how are you?"

        detected_lang = self.text_translator.langDetect(txt)
        self.assertEqual(detected_lang, "Detected(lang=en, confidence=None)")

    def test_detect_language_ukrainian(self):
        txt = "Доброго дня. Як справи?"

        detected_lang = self.text_translator.langDetect(txt)
        self.assertEqual(detected_lang, "Detected(lang=uk, confidence=None)")

    def test_detect_language_chinese(self):
        txt = "你好吗？"

        detected_lang = self.text_translator.langDetect(txt)
        self.assertEqual(detected_lang, "Detected(lang=zh-CN, confidence=None)")

    def test_lookup_language_english(self):
        lang = "en"

        lang_name = self.text_translator.codeLang(lang)
        self.assertEqual(lang_name, "english")

    def test_lookup_language_english(self):
        lang = "Ukrainian"

        lang_name = self.text_translator.codeLang(lang)
        self.assertEqual(lang_name, "uk")

    def test_lookup_language_nonexistent(self):
        lang = "xyz"

        lang_name = self.text_translator.codeLang(lang)
        self.assertEqual(lang_name, "Language not found")

