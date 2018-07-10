from tkinter import *


class ConversionGUI:
    def __init__(self, master):
        self.master = master
        master.title('Image Testing')

        self.image = PhotoImage(file='/Users/19ecornish/Downloads/IMG_5024 (1).gif')
#        self.image = PhotoImage.zoom(self.image, 40, 30)

        self.ImageLabel = Label(master, image=self.image)
        self.ImageLabel.grid()


root = Tk()
root.geometry('600x400')
gui = ConversionGUI(root)
root.mainloop()
