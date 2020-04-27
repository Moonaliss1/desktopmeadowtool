import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master


root = tk.Tk()
root.title("")
app = Application(master=root)
def goinvis(self):
    root.wm_attributes("-alpha",0.0)

root.bind("<Button-3>",goinvis)
app.mainloop()
