from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("Hi there, everyone!")
        
    def createWidgets(self):
        
        self.hi_there = Button(self, text="Hello", fg="blue", command=self.say_hi)
        #be careful of this. the () at the end of the command will call the command right away 
        # and not when the button is pushed
        #self.hi_there = Button(self, text="Hello", fg="blue", command=self.say_hi())
#        self.hi_there["text"] = "Hello"
#        self.hi_there["fg"] = "blue"
#        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})
        
        self.QUIT = Button(self, text="Goodbye", fg="red", command=self.quit)
        #be careful of this. the () at the end of the command will keep the command from being 
        # executed when the button is pushed
        #self.QUIT = Button(self, text="Goodbye", fg="red", command=self.quit())
#        self.QUIT["text"] = "Goodbye"
#        self.QUIT["fg"] = "red"
#        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
root = Tk()
app = Application(master=root)
app.mainloop()