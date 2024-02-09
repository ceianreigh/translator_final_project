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
window.geometry("460x260")
window.resizable(False, False)
window.iconphoto(
    False,
    PhotoImage(
        file="C:\\Users\\Ceian Cepillo\\Documents\\translator_final_project\\ctranslator_icon.png.png"
    ),
)

# add a heading
heading = tk.Label(
    window, text="Welcome to CTranslator", font=("Bernard MT Condensed", 30)
)
heading.place(x=45, y=0)

# add frame for original text
original_text_frame = tk.LabelFrame(
    window, text="Original Text", font=("Arial Italic", 9)
)
original_text_frame.place(x=10, y=50)

# add the original text label
original_text = tk.Label(
    original_text_frame,
    text="Enter the text to be translated: ",
    font=("Montserrat Medium", 12),
)
original_text.pack(padx=5, pady=5)

# add the original text entry
original_text_entry = tk.Entry(
    original_text_frame, width=25, font=("Century Gothic Bold", 12)
)
original_text_entry.pack(padx=5, pady=5)

# add the desired language label
dest_language = tk.Label(
    original_text_frame, text="Choose the language: ", font=("Montserrat Medium", 12)
)
dest_language.pack(padx=5, pady=5)

# add combobox for the desired language
dest_language_combobox = ttk.Combobox(
    original_text_frame, values=list(LANGUAGES.values())
)
dest_language_combobox.pack(padx=5, pady=5)

# add the translate button
translate_button = tk.Button(
    original_text_frame,
    text="Translate",
    command=translate_text,
    font=("Arial Italic", 12),
)
translate_button.pack(padx=5, pady=5)

# add frame for translated text
translated_text_frame = tk.LabelFrame(
    window, text="Translated Text", font=("Arial Italic", 9)
)
translated_text_frame.place(x=297, y=90)

# add the translated text label
translated_text_label = tk.Label(
    translated_text_frame, text="Translated Text: ", font=("Montserrat Medium", 12)
)
translated_text_label.pack(padx=5, pady=5)

# display the translated text
translated_text = tk.Label(
    translated_text_frame, text="", font=("Century Gothic Bold", 12)
)
translated_text.pack(padx=5, pady=5)

# add a done button
done_button = tk.Button(
    translated_text_frame, text="Done", font=("Arial Italic", 10), command=window.quit
)
done_button.pack(padx=5, pady=5)

# create the initial window
window = tk.Tk()
window.title("CTranslator")
window.geometry("460x260")
window.resizable(False, False)
window.iconphoto(
    False,
    PhotoImage(
        file="C:\\Users\\Ceian Cepillo\\Documents\\translator_final_project\\ctranslator_icon.png.png"
    ),
)

# add a start button
start_button = tk.Button(window, text="Start")
start_button.pack()


# add the main loop
window.mainloop()
