# pseudocode

# import the necessary packages
import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
from googletrans import Translator, LANGUAGES


# define the function that will save the translated text
def save_translated_text(original_text_entry, translated_text, dest_language_combobox):
    saved_translation = open("saved_translation.txt", "a")
    saved_translation.write(
        f"Original text: {original_text_entry.get()}\nTranslated text: {translated_text.cget('text')}\nLanguage: {dest_language_combobox.get()}\n\n"
    )
    saved_translation.close()
    messagebox.showinfo("Save", "The translated text has been saved.")


# define the function that will translate the inputted text
def translate_text(original_text_entry, dest_language_combobox, translated_text):
    # create a translator object
    translator = Translator()

    # translate the inputted text to the desired language
    translated = translator.translate(
        original_text_entry.get(), dest=dest_language_combobox.get()
    )

    # return the translated text
    translated_text.config(text=translated.text)


def start_translator(icon_image, background_image2):
    # create the main window
    main_window = tk.Toplevel()
    main_window.title("CTranslator")
    main_window.geometry("460x260")
    main_window.resizable(False, False)
    main_window.iconphoto(False, icon_image)
    background_image2_label = tk.Label(main_window, image=background_image2)
    background_image2_label.place(relwidth=1, relheight=1)

    # add frame for original text
    original_text_frame = tk.LabelFrame(
        main_window,
        text="Original Text",
        font=("Arial Italic", 9),
        bg="#06265a",
        fg="white",
    )
    original_text_frame.place(x=10, y=65)

    # add the original text label
    original_text = tk.Label(
        original_text_frame,
        text="Enter the text to be translated: ",
        font=("Montserrat Medium", 12),
        bg="#06265a",
        fg="white",
    )
    original_text.pack(padx=3, pady=3)

    # add the original text entry
    original_text_entry = tk.Entry(
        original_text_frame, width=25, font=("Century Gothic Bold", 12)
    )
    original_text_entry.pack(padx=3, pady=3)

    # add the desired language label
    dest_language = tk.Label(
        original_text_frame,
        text="Choose the language: ",
        font=("Montserrat Medium", 12),
        bg="#06265a",
        fg="white",
    )
    dest_language.pack(padx=3, pady=3)

    # add combobox for the desired language
    dest_language_combobox = ttk.Combobox(
        original_text_frame, width=34, values=list(LANGUAGES.values())
    )
    dest_language_combobox.pack(padx=3, pady=3)

    # add the translate button
    translate_button = tk.Button(
        original_text_frame,
        text="Translate",
        width=15,
        bg="#030a16",
        fg="white",
        command=lambda: translate_text(
            original_text_entry, dest_language_combobox, translated_text
        ),
        font=("Arial Italic", 12),
    )
    translate_button.pack(padx=3, pady=3)

    # add frame for translated text
    translated_text_frame = tk.LabelFrame(
        main_window,
        text="Translated Text",
        font=("Arial Italic", 9),
        bg="#06265a",
        fg="white",
    )
    translated_text_frame.place(x=297, y=72)

    # add the translated text label
    translated_text_label = tk.Label(
        translated_text_frame,
        text="Translated Text: ",
        font=("Montserrat Medium", 12),
        bg="#06265a",
        fg="white",
    )
    translated_text_label.pack(padx=5, pady=5)

    # display the translated text
    translated_text = tk.Label(
        translated_text_frame,
        text="",
        font=("Century Gothic Bold", 12),
        bg="#06265a",
        fg="white",
    )
    translated_text.pack(padx=5, pady=5)

    # add a save button
    save_button = tk.Button(
        translated_text_frame,
        text="Save",
        font=("Arial Italic", 10),
        width=12,
        bg="#030a16",
        fg="white",
        command=lambda: save_translated_text(
            original_text_entry, translated_text, dest_language_combobox
        ),
    )
    save_button.pack(padx=5, pady=5)

    # add a done button
    done_button = tk.Button(
        translated_text_frame,
        text="Done",
        font=("Arial Italic", 10),
        width=12,
        bg="#030a16",
        fg="white",
        command=window.quit,
    )
    done_button.pack(padx=5, pady=5)


# create the initial window
window = tk.Tk()
window.title("CTranslator")
window.geometry("460x260")
window.resizable(False, False)
icon_image = PhotoImage(
    file="C:\\Users\\Ceian Cepillo\\Documents\\translator_final_project\\ctranslator_icon.png"
)
window.iconphoto(False, icon_image)
background_image = PhotoImage(
    file="C:\\Users\\Ceian Cepillo\\Documents\\translator_final_project\\ctranslator_background.png"
)
background_image_label = tk.Label(window, image=background_image)
background_image_label.place(relwidth=1, relheight=1)
background_image2 = PhotoImage(
    file="C:\\Users\\Ceian Cepillo\\Documents\\translator_final_project\\ctranslator_background2.png"
)

# add a start button
start_button = tk.Button(
    window,
    text="Start",
    font=("Arial Italic", 11),
    width=10,
    bg="#030a16",
    fg="white",
    command=lambda: start_translator(icon_image, background_image2),
)
start_button.place(x=118, y=210)

# add exit button
exit_button = tk.Button(
    window,
    text="Exit",
    font=("Arial Italic", 11),
    width=10,
    bg="#030a16",
    fg="white",
    command=window.quit,
)
exit_button.place(x=240, y=210)

# add the main loop
window.mainloop()
