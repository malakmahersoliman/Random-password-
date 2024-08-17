import string
import random
from tkinter import *
from tkinter import font

# Function to generate a password based on the selected strength
def passgen():
    length = val.get()
    if choice.get() == 1:  
        characters = string.ascii_lowercase
    elif choice.get() == 2: 
        characters = string.ascii_letters + string.digits
    elif choice.get() == 3:  
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Select a strength!"

    return "".join(random.sample(characters, length))

def selection():
    selected_option = choice.get()

def callback():
    password = passgen()
    lsum.config(text=f"✨ {password} ✨")

# Tkinter window setup
root = Tk()
root.geometry("400x400")
root.title("Password Generator")
root.config(bg="#f7f7f7")

# Custom font styles
title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=10, weight="bold")
password_font = font.Font(family="Helvetica", size=18, weight="bold")


title = StringVar()
Label(root, textvariable=title, bg="#f7f7f7", fg="#333", font=title_font).pack(pady=10)
title.set("Select the Strength of Your Password")

# Radio button variable
choice = IntVar()


R1 = Radiobutton(root, text="Poor", variable=choice, value=1, command=selection, bg="#f7f7f7", font=label_font).pack(anchor=CENTER)
R2 = Radiobutton(root, text="Average", variable=choice, value=2, command=selection, bg="#f7f7f7", font=label_font).pack(anchor=CENTER)
R3 = Radiobutton(root, text="Advanced", variable=choice, value=3, command=selection, bg="#f7f7f7", font=label_font).pack(anchor=CENTER)


lenlabel = StringVar()
lenlabel.set("Password Length")
lentitle = Label(root, textvariable=lenlabel, bg="#f7f7f7", font=label_font).pack(pady=10)


val = IntVar()
spinlength = Spinbox(root, from_=8, to_=24, textvariable=val, width=5, font=label_font, justify=CENTER)
spinlength.pack(pady=5)


passgenButton = Button(root, text="Generate Password", command=callback, bd=3, bg="#ffcccc", fg="#333", height=2, font=button_font, relief=RAISED)
passgenButton.pack(pady=15)


lsum = Label(root, text="", bg="#ffffff", fg="#ff6666", font=password_font, wraplength=350, bd=2, relief="solid", padx=10, pady=10)
lsum.pack(pady=20)


root.mainloop()
