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
text = input("Enter the text to be translated: ")

# print the supported languages

# ask the user to input the language they would like to translate to

# call the function to translate the inputted text

# print the translated text
