from tkinter import *

ALL = N+S+E+W

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        f1 = Frame(self, bg="red", width=100, height=75)
        #f1.label(text="frame 1")
        f1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)
        f2 = Frame(self, bg="green", width=100, height=75)
        #f2.label(text="frame 2")
        f2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)
        f3 = Frame(self, bg="blue", width=150, height=150)
        #f3.label(text="frame 3")
        f3.grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)
        self.rowconfigure(0, weight=1)
        Label(self, bg="red", text="Frame 1").grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.rowconfigure(4, weight=1)
        Label(self, bg="green", text="Frame 2").grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)
        Label(self, bg="blue", text="Frame 3").grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)

        for c in range(5):
            #self.rowconfigure(r, weight=1)
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c + 1)).grid(row=3, column=c, sticky=ALL)
root = Tk()
app = Application(master=root)
app.mainloop()