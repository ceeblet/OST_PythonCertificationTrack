import os
from tkinter import *

ALL = N+S+E+W

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        root.bind("<Return>", self.file_open)
        
        self.f1 = Frame(self, bg="red", width=100, height=75)
        self.f1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=ALL)

        self.f2 = Frame(self, bg="green", width=100, height=75)
        self.f2.grid(row=1, column=0, rowspan=2, columnspan=2, sticky=ALL)

        self.f3 = Frame(self, bg="blue", width=150, height=150)
        self.f3.grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)

        self.file_name_field = Entry(self.f3, bg="#fff")
        self.file_name_field.pack(anchor=N, side=TOP, fill=X, expand=False)
        self.file_contents = Text(self.f3, width=10, height=10)
        self.file_contents.pack(anchor=N, side=TOP, fill=BOTH, expand=True)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.label1 = Label(self.f1, bg="red", text="Frame 1")
        self.label1.grid(row=0, sticky=ALL)
        
        self.label2 = Label(self.f2, bg="green", text="Frame 2")
        self.label2.grid(row=1, sticky=ALL)
        
        # self.label3 = Label(self.f3, bg="blue", text="Frame 3")
        # self.label3.grid(row=0, sticky=ALL)

        button_names = ["red", "blue", "green", "black", "open"]
        for c in range(5):
            self.columnconfigure(c, weight=1)
            button = Button(self, text="{0}".format(button_names[c]))
            button.grid(row=3, column=c, sticky=ALL)

            if button_names[c] == "open":
                button.bind("<Button-1>", self.file_open)
            else:
                button.bind("<Button-1>", lambda event, color=button_names[c]: self.change_color(event, color))


        # self.label1.bind("<Button-1>", self.click_report)
        # self.label2.bind("<Button-1>", self.click_report)

        self.f1.bind("<Button-1>", self.click_report)
        self.f2.bind("<Button-1>", self.click_report)


    def click_report(self, event):
        frm = ""
        location = event.widget.grid_info()
        frm_coords = (location["row"], location["column"])
        if frm_coords == ("0", "0"):
            frm = "Frame 1"
        elif frm_coords == ("1", "0"):
            frm = "Frame 2"
        print("user button 1 click in {0} at ({1}, {2})".format(frm, event.x, event.y))

    def file_open(self, event):
        self.file_contents.delete(1.0, END)
        fname = self.file_name_field.get()
        if os.path.exists(fname):
            print("Opening file: {0}".format(fname))
            lines = open(fname, 'r').readlines()
            for line in lines:
                self.file_contents.insert(INSERT, line)
        else:
            print("The file does not exist, please try again.")

    def change_color(self, event, color):
        self.file_contents.configure(fg=color)

root = Tk()
app = Application(master=root)
app.mainloop()