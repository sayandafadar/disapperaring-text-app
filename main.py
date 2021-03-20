from tkinter import *

after_id = None


def disappear_text():
    text.clipboard_append(text.get(1.0, END))
    text.delete(1.0, END)
    text.config(text.insert(END, " ", 35))


window = Tk()
window.title("Disappearing Text App")


def handle_wait(self):
    global after_id
    if after_id is not None:
        window.after_cancel(after_id)

    after_id = window.after(5000, disappear_text)


title = Label(text="Start typing below......", font=('Arial', 20))
title.pack()

text = Text(height=50, width=100, font=('Arial', 18))
text.focus()
print(text.get("1.0", END))
text.pack()

text.bind('<Key>', handle_wait)

window.mainloop()
