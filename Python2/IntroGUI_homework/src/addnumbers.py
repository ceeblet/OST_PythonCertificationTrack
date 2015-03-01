from tkinter import *

class Application(Frame):
    """Application main window class."""
    def __init__(self,master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame=Frame(self)
        self.text1_in=Entry(top_frame)
        self.text2_in=Entry(top_frame)
        self.label=Label(top_frame,text="Output label")
        self.text1_in.pack(side=LEFT)
        self.text2_in.pack(side=LEFT)
        self.label.pack()
        top_frame.pack(side=TOP)
        
        bottom_frame=Frame(self)
        bottom_frame.pack(side=TOP)
        self.QUIT=Button(bottom_frame,text="Quit",command=self.quit)
        self.QUIT.pack(side=LEFT)
        self.handleb=Button(bottom_frame,text="Sum",command=self.handle)
        self.handleb.pack(side=LEFT)
        
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        text1=self.text1_in.get()
        text2=self.text2_in.get()
#        operation=self.r.get()
        try:
            first = float(text1)
            second = float(text2)
            output = first + second
        except:
            output="***ERROR***"
        self.label.config(text=output)
        
root=Tk()
app=Application(master=root)
app.mainloop()
