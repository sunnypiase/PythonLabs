from TextTranslator import TextTranslator


def menu():
    translator = TextTranslator()

    while True:
        print("Options:")
        print("1. Translate text")
        print("2. Detect language")
        print("3. Lookup language code")
        print("4. Quit")

        match input("Select an option (1/2/3/4): "):
            case "1":
                txt = input("Enter the text to translate: ")
                lang = input("Enter the target language code: ")
                translation = translator.translate(txt, lang)
                print(f"Translation: {translation}\n")
            case "2":
                txt = input("Enter the text to detect the language: ")
                detection_result = translator.langDetect(txt)
                print(f"Language Detection: {detection_result}\n")
            case "3":
                lang = input("Enter the language code to look up: ")
                lang_name = translator.codeLang(lang)
                print(f"Language Name: {lang_name}\n")
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    menu()
