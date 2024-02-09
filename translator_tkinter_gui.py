# pseudocode

# import the necessary packages
import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
from googletrans import Translator, LANGUAGES


# define the function that will translate the inputted text
def translate_text():
    # create a translator object
    translator = Translator()

    # translate the inputted text to the desired language
    translated = translator.translate(
        original_text_entry.get(), dest=dest_language_combobox.get()
    )

    # return the translated text
    translated_text.config(text=translated.text)


# create the window
window = tk.Tk()
window.title("CTranslator")
window.geometry("500x300")

# add frame for original text
original_text_frame = tk.LabelFrame(window, text="Original Text")
original_text_frame.pack()

# add the original text label
original_text = tk.Label(original_text_frame, text="Enter the text to be translated: ")
original_text.pack()

# add the original text entry
original_text_entry = tk.Entry(original_text_frame)
original_text_entry.pack()

# add the desired language label
dest_language = tk.Label(original_text_frame, text="Choose the language: ")
dest_language.pack()

# add combobox for the desired language
dest_language_combobox = ttk.Combobox(
    original_text_frame, values=list(LANGUAGES.values())
)
dest_language_combobox.pack()

# add the translate button
translate_button = tk.Button(
    original_text_frame, text="Translate", command=translate_text
)
translate_button.pack()

# add frame for translated text
translated_text_frame = tk.LabelFrame(window, text="Translated Text")
translated_text_frame.pack()

# add the translated text label
translated_text_label = tk.Label(translated_text_frame, text="Translated Text: ")
translated_text_label.pack()

# display the translated text
translated_text = tk.Label(translated_text_frame, text="")
translated_text.pack()


# add a done button
done_button = tk.Button(window, text="Done", command=window.quit)
done_button.pack()

# add the main loop
window.mainloop()
