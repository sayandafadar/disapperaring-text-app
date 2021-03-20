import tkinter as tk

file = '/fonts/UbuntuMono-Regular.ttf'


class Application(tk.Frame):

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self)
        self.pack()

        self._after_id = None
        self.text = tk.Text(self)
        self.text.config(bg="Black", fg="#32ff6a", font=(file, 15))
        self.text.focus()
        self.text.pack()
        self.text.bind('<Key>', self.handle_wait)

    def handle_wait(self, event):
        if self._after_id is not None:
            self.after_cancel(self._after_id)

        self._after_id = self.after(3000, self.disappear_text)

    def disappear_text(self):
        self.clipboard_clear()
        self.text.clipboard_append(self.text.get(1.0, tk.END))
        self.text.delete(1.0, tk.END)
        self.text.config(self.text.insert(tk.END, " ", 35))


root = tk.Tk()
root.title("Disappearing Text App")
root.config(bg="Black")
app = Application(root)
app.mainloop()
