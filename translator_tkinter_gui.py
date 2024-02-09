# pseudocode

# import the necessary packages
import tkinter as tk
from tkinter import PhotoImage, messagebox

# create the window
window = tk.Tk()
window.title("CTranslator")

# add frame for original text
original_text_frame = tk.LabelFrame(window, text="Original Text")
original_text_frame.pack()

# add the original text label
original_text = tk.Label(original_text_frame, text="Enter the text to be translated: ")
original_text.pack()

# add the original text entry
original_text_entry = tk.Entry(original_text_frame)
original_text_entry.pack()

# add the main loop
window.mainloop()
