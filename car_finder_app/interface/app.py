import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from classes.mediator import Mediator

# print("Result : ", Mediator.processUserInput("img/audi.jpg"))

from PIL import Image, ImageTk
import tkinter.filedialog as tkFileDialog
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Label, Style

tkimage = None

class PackManager(Frame):

    img_path = ""
    img_displayer = None
    predictButton = None
    resultLabel = None

    def __init__(self):
        super().__init__()
        self.initUI()

    def quit(self):
        self.master.destroy()

    # button behavior
    def b_file_browser(e):  
        new_width = 600
        path=tkFileDialog.askopenfilename(filetypes=[("JPEG image (.jpg)",'.jpg')])
        e.img_path = path
        e.resultLabel.configure(text="( -_-)旦~ Waiting...")
        original = Image.open(path)
        # resize
        multiplier = new_width / original.width
        new_height = int(original.height * multiplier)
        resized = original.resize((new_width, new_height), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        e.img_displayer.configure(image=tkimage)
        e.img_displayer.image = tkimage
        e.predictButton.configure(state="normal")

    def guess(e):
        guess_str = Mediator.processUserInput(e.img_path)
        e.resultLabel.configure(text="(づ ￣ ³￣)づ旦~ I think it's : "+guess_str)
        e.predictButton.configure(state="disabled")

    def displayInfo(e):
        e.resultLabel.configure(text="(☞ﾟ∀ﾟ)☞旦~ JPEG only, crop to max for better results")

    def initUI(self):
        self.master.title("Car Brand Finder")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        self.img_displayer=Label(self,image = tkimage, width=600)
        self.img_displayer.image = tkimage
        self.img_displayer.pack()

        closeButton = Button(self, text="Close", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        infoButton = Button(self, text="Info", command=self.displayInfo)
        infoButton.pack(side=RIGHT, padx=5, pady=5)
        browseButton = Button(self, text="Browse image", command=self.b_file_browser)
        browseButton.pack(side=RIGHT, padx=5, pady=5)
        self.predictButton = Button(self, text="Predict", state="disabled", command=self.guess)
        self.predictButton.pack(side=RIGHT, padx=5, pady=5)
        self.resultLabel = Label(self, text="( -_-)旦~ Waiting...")
        self.resultLabel.pack(side=RIGHT, padx=5, pady=5)

    

def main():

    root = Tk()
    root.geometry("700x700+300+300")
    app = PackManager()
    root.mainloop()

if __name__ == '__main__':
    main()