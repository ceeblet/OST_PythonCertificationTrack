from tkinter import *

ALL = N+S+E+W

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        self.f1 = Frame(self, bg="red", width=100, height=75)
        #f1.label(text="frame 1")
        self.f1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.f2 = Frame(self, bg="green", width=100, height=75)
        #f2.label(text="frame 2")
        self.f2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.f3 = Frame(self, bg="blue", width=150, height=150)
        #f3.label(text="frame 3")
        self.f3.grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)
        self.rowconfigure(0, weight=1)
        self.label1 = Label(self, bg="red", text="Frame 1")
        self.label1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.rowconfigure(4, weight=1)
        self.label2 = Label(self, bg="green", text="Frame 2")
        self.label2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.label3 = Label(self, bg="blue", text="Frame 3")
        self.label3.grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)

        for c in range(5):
            #self.rowconfigure(r, weight=1)
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c + 1)).grid(row=3, column=c, sticky=ALL)

        self.label1.bind("<Button-1>", self.click_report)
        self.label2.bind("<Button-1>", self.click_report)
        #self.f1.bind("<Button-1>", self.click_report)
        #self.f2.bind("<Button-1>", self.click_report)

    def click_report(self, event):
        frm = ""
        location = event.widget.grid_info()
        frm_coords = (location["row"], location["column"])
        if frm_coords == ("0", "0"):
            frm = "Frame 1"
        elif frm_coords == ("1", "0"):
            frm = "Frame 2"
        print("user button1 click in {0} at ({1}, {2})".format(frm, event.x, event.y))

root = Tk()
app = Application(master=root)
app.mainloop()
