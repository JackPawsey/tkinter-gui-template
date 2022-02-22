import tkinter as tk


class Start(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Title")
        # tk.Tk.iconbitmap(self, default="path/to/.ico")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (Page1, Page2):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Page1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Loading page
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        title = tk.Label(self, text="page1")
        title.place(x=760, y=400)
        abutton = tk.Button(self, text="next page", command=lambda: controller.show_frame(Page2))
        abutton.pack()


# Main page
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="page2")
        label.pack()


app = Start()
# app.resizable(width=False, height=False)
app.state("zoomed")
app.mainloop()
