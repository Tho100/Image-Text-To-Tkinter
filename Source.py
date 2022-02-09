import tkinter as tk
from tkinter import *
import pytesseract as pts

window = Tk()
window.title('Main')
window.geometry('400x300')

def get_text(): 
    img = "C:\\users\\HP\\Documents\\my folder\\yourmom.png"
    print_text = pts.image_to_string(img)
    label = tk.Label(window,text=print_text)
    label.pack()

button = tk.Button(window,text='Show Text',command=get_text)
button.pack()

window.mainloop()
