import tkinter as tk
from tkinter import END

from PIL import Image, ImageTk

root = tk.Tk()
s = 0

root.title("Sentence Checker")
root.config(bg="#252833")
canvas = tk.Canvas(root, width=900, height=300, bg="#252833", highlightthickness=0)
canvas.grid(columnspan=3, rowspan=3)

# Logo
logo = Image.open('Logo.JPG')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instruct = tk.Label(root, text="Copy and paste the text you would like to check, then press Check", font="Raleway")
instruct.grid(columnspan=3, column=0, row=1)


# Sentence logic
def count_text():
    text = text_box.get("1.0", 'end-1c')
    period = len(text.split('. '))
    question = len(text.split('? '))
    exclamation = len(text.split('! '))
    sentence = period + question + exclamation - 2
    word = len(text.split())
    characters = len(text)
    print("The number of sentences in text are : " + str(sentence))
    print("The number of words in text are : " + str(word))
    print("The number of characters in text are : " + str(characters))

    stats = tk.Label(root, text="Sentences: " + str(sentence) + " Words: " + str(word) + " Characters: " + str(characters), font="Raleway")
    stats.grid(columnspan=3, column=1, row=5)


# Clear text field
def clear_text():
    text_box.delete('1.0', END)
    stats.grid(columnspan=3, column=1, row=5)


# check button
check_text = tk.StringVar()
check_btn = tk.Button(root, textvariable=check_text, command=count_text, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
check_text.set("Check")
check_btn.grid(column=1, row=2)

# clear button
text_clear = tk.StringVar()
clear_btn = tk.Button(root, textvariable=text_clear, command=clear_text, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
text_clear.set("Clear")
clear_btn.grid(column=1, row=4)

# Space for better formatting
canvas = tk.Canvas(root, width=900, height=100, bg="#252833", highlightbackground="#5796d9")
canvas.grid(columnspan=3)

# Text box
text_box = tk.Text(root, height=15, width=100, padx=15, pady=15, bg="#b6b9ba")
text_box.grid(column=1, row=3)

# numbers at the bottom
stats = tk.Label(root, text="Sentences: 0  Words: 0  Characters: 0 ", font="Raleway")
stats.grid(columnspan=3, column=1, row=5)

root.mainloop()
