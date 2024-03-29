# pseudocode

# import the necessary packages
from googletrans import Translator, LANGUAGES


# define the function that will translate the inputted text
def translate_text(text, dest_language):
    # create a translator object
    translator = Translator()

    # translate the inputted text to the desired language
    translated_text = translator.translate(text, dest=dest_language)

    # return the translated text
    return translated_text.text


# ask the user to input the text they would like to translate
to_translate = input("Enter the text to be translated: ")

# print the supported languages
print("Supported languages:", LANGUAGES)

# ask the user to input the language they would like to translate to
dest_language = input("Enter the language code to be used for translation: ")

# call the function to translate the inputted text
translated_text = translate_text(to_translate, dest_language)

# print the original text
print("Original text: ", to_translate)

# print the translated text
print("Translated text:", translated_text)
