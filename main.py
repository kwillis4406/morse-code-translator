from data import letters_to_morse, morse_to_letters
from tkinter import *
from tkinter import messagebox


# Global Variables #
TITLE_FONT = ("Courier", 28, "bold")


# Functions #
def translate_text(text_input: str):
    """Takes text input as string, translates to Morse Code & runs update_result_text(translated text)."""
    text = text_input.upper()
    translated_list = []
    # converts characters in {text} to corresponding values in {letters_to_morse} and appends to {translated_list}
    # includes error handling for invalid characters not in {letters_to_morse}, returning error messagebox
    for letter in text:
        try:
            new_code = letters_to_morse[letter]
            translated_list.append(new_code)
        except KeyError:
            messagebox.showinfo(title="Error", message=f"Invalid character '{letter}'.")
            break
    result = ""
    # converts {translated_list} to string {result}
    for code in translated_list:
        result += f"{code} "
    update_result_text(result)


def translate_code(code_input: str):
    """Takes Morse Code input as string, translates to text & runs update_result_text(translated code)."""
    # creates list of all word blocks of {code_input}
    code_list = code_input.split()
    translated_list = []
    # converts word blocks in {code_list} to corresponding values in {morse_to_letters} and appends to {translated_list}
    # includes error handling for invalid word blocks not in {morse_to_letters}, returning error messagebox
    for code in code_list:
        try:
            new_letter = morse_to_letters[code]
            translated_list.append(new_letter)
        except KeyError:
            messagebox.showinfo(title="Error", message=f"Invalid character '{code}'.\nCheck your input and mode.")
            break
    result = ""
    # converts {translated_list} to string {result}
    for char in translated_list:
        result += f"{char}"
    update_result_text(result)


def execute_translation():
    """Gets string input from Input Box and runs selected mode (translate_text or translate_code) on the string"""
    to_translate = entry_input.get("1.0", "end")
    if translation_mode.get() == "Text to Morse Code":
        translate_text(to_translate)
    elif translation_mode.get() == "Morse Code to Text":
        translate_code(to_translate)


def apply_uppercase():
    """Converts text in Result Box to uppercase"""
    upper_text = result_output.get("1.0", "end").upper()
    update_result_text(upper_text)


def apply_lowercase():
    """Converts text in Result Box to lowercase"""
    lower_text = result_output.get("1.0", "end").lower()
    update_result_text(lower_text)


def update_result_text(output):
    """Clears Result Box and inserts inputted string"""
    result_output.delete(1.0, END)
    result_output.insert(END, output)


# Window Configuration #
window = Tk()
window.title("Morse Code Translator")
window.config(padx=50, pady=50)


# Title #
title_label = Label(text="Morse Code Translator", font=TITLE_FONT)
title_label.grid(column=0, row=0, columnspan=2)


# Translation Selector #
translation_mode = StringVar()
translation_mode.set("Text to Morse Code")
mode_selector = OptionMenu(window, translation_mode, "Text to Morse Code", "Morse Code to Text")
mode_selector.grid(column=0, row=2, sticky="w")


# Entry Box #
entry_label = Label(text="Input:")
entry_label.grid(column=0, row=3, sticky="w")

entry_scrollbar = Scrollbar(window)
entry_scrollbar.grid(column=1, row=4, sticky="nsw")

entry_input = Text(width=100, height=10, wrap=WORD, yscrollcommand=entry_scrollbar.set)
entry_input.grid(column=0, row=4)
entry_input.focus()

entry_scrollbar.config(command=entry_input.yview, jump=1)


# Submit Button #
submit_button = Button(width=14, text="Submit", command=execute_translation)
submit_button.grid(column=0, row=5, sticky="e")


# Result Box #
result_label = Label(text="Translation:")
result_label.grid(column=0, row=6, sticky="w")

result_scrollbar = Scrollbar(window)
result_scrollbar.grid(column=1, row=7, sticky="nsw")

result_output = Text(width=100, height=10, wrap=WORD, yscrollcommand=result_scrollbar.set)
result_output.grid(column=0, row=7)

result_scrollbar.config(command=result_output.yview, jump=1)


# Change Result Box Text-case Buttons #
upper_button = Button(width=14, text="Uppercase", command=apply_uppercase)
upper_button.grid(column=0, row=8, sticky="e")

lower_button = Button(width=14, text="Lowercase", command=apply_lowercase)
lower_button.grid(column=0, row=8, sticky="w")


# Window Mainloop #
window.mainloop()
