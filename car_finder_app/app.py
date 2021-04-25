#stl
import os
import sys
import inspect

#image browsing
from PIL import Image, ImageTk

import tkinter.filedialog as tkFileDialog
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Label, Style

from classes.mediator import Mediator


# Set current path to project root
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0,parentdir) 



# print("Result : ", Mediator.processUserInput("img/audi.jpg"))

class PackManager(Frame):
    # Path to the browsed image
    img_path = ""
    # Image (tkinter integration)
    tkimage = None
    # Image displayer component
    img_displayer = None
    # Predict button component
    predictButton = None
    # Result label component
    resultLabel = None

    # Frame constructor
    def __init__(self):
        super().__init__()
        self.initUI()

    # App exit function (called on button quit)
    def quit(self):
        self.master.destroy()

    # Browse button behaviour
    def b_file_browser(e):
        # Width to resize the image for display
        new_width = 700
        
        # Launch file browser for JPEG files only (.jpg) and copy it in img_path
        path = tkFileDialog.askopenfilename(filetypes=[("JPEG image (.jpg)",'.jpg')])
        e.img_path = path

        # Change label state for User Experience (UX)
        e.resultLabel.configure(text="( -_-)旦~ Waiting...")
            
        # Open the image and resize it for display purposes then display image
        original = Image.open(path)
        multiplier = new_width / original.width
        new_height = int(original.height * multiplier)
        resized = original.resize((new_width, new_height), Image.ANTIALIAS)
        e.tkimage = ImageTk.PhotoImage(resized)
        e.img_displayer.configure(image=e.tkimage)
        e.img_displayer.image = e.tkimage

        # Resize window to image size
        e.master.geometry(f"{new_width}x{new_height+40}")

        # Enable predict button
        e.predictButton.configure(state="normal")

    # Predict button behaviour
    def guess(e):
        # Call mediator function to guess what brand of car it is
        guess_str = Mediator.processUserInput(e.img_path)
        # Change label state to display the result found
        e.resultLabel.configure(text="(づ ￣ ³￣)づ旦~ I think it's a "+guess_str)
        # Disable the predict button to avoid multiple useless prediction
        e.predictButton.configure(state="disabled")

    # Info button behaviour
    def displayInfo(e):
        # Change the label to display tips on how the app works
        e.resultLabel.configure(text="(☞ﾟ∀ﾟ)☞旦~ JPEG only, crop to max for better results")

    # Frame building function
    def initUI(self):
        # Window settings
        self.master.title("Car Brand Finder")
        self.style = Style()
        self.style.theme_use("alt")

        # Create main frame
        frame = Frame(self, relief=RAISED)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        # Create the image displayer
        self.img_displayer = Label(self,image = self.tkimage, width=600)
        self.img_displayer.image = self.tkimage
        self.img_displayer.pack()

        # Create the quit button
        closeButton = Button(self, text="Close", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        # Create the info button
        infoButton = Button(self, text="Info", command=self.displayInfo)
        infoButton.pack(side=RIGHT, padx=5, pady=5)
        # Create the browse button
        browseButton = Button(self, text="Browse image", command=self.b_file_browser)
        browseButton.pack(side=RIGHT, padx=5, pady=5)
        # Create the predict button
        self.predictButton = Button(self, text="Predict", state="disabled", command=self.guess)
        self.predictButton.pack(side=RIGHT, padx=5, pady=5)
        # Create the result (display) label
        self.resultLabel = Label(self, text="( -_-)旦~ Waiting...")
        self.resultLabel.pack(side=RIGHT, padx=5, pady=5)

# App main loop
def main():
    # Initiate the TKInter User Interface
    root = Tk()
    # Define window size
    root.geometry("700x200+300+300")
    # Display the main frame
    app = PackManager()
    # Launch the app loop
    root.mainloop()

# Launch the app
if __name__ == '__main__':
    main()