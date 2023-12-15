import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=456
        height=485
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_850=tk.Listbox(root)
        GListBox_850["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_850["font"] = ft
        GListBox_850["fg"] = "#333333"
        GListBox_850["justify"] = "center"
        GListBox_850.place(x=20,y=30,width=80,height=25)

        GListBox_990=tk.Listbox(root)
        GListBox_990["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_990["font"] = ft
        GListBox_990["fg"] = "#333333"
        GListBox_990["justify"] = "center"
        GListBox_990.place(x=100,y=30,width=80,height=25)

        GListBox_272=tk.Listbox(root)
        GListBox_272["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_272["font"] = ft
        GListBox_272["fg"] = "#333333"
        GListBox_272["justify"] = "center"
        GListBox_272.place(x=180,y=30,width=80,height=25)

        GListBox_981=tk.Listbox(root)
        GListBox_981["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_981["font"] = ft
        GListBox_981["fg"] = "#333333"
        GListBox_981["justify"] = "center"
        GListBox_981.place(x=260,y=30,width=80,height=25)

        GButton_465=tk.Button(root)
        GButton_465["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_465["font"] = ft
        GButton_465["fg"] = "#000000"
        GButton_465["justify"] = "center"
        GButton_465["text"] = "Button"
        GButton_465.place(x=370,y=30,width=70,height=25)
        GButton_465["command"] = self.GButton_465_command

        GLabel_199=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_199["font"] = ft
        GLabel_199["fg"] = "#333333"
        GLabel_199["justify"] = "center"
        GLabel_199["text"] = "label"
        GLabel_199.place(x=20,y=70,width=70,height=25)

        GLabel_612=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_612["font"] = ft
        GLabel_612["fg"] = "#333333"
        GLabel_612["justify"] = "center"
        GLabel_612["text"] = "label"
        GLabel_612.place(x=100,y=70,width=70,height=25)

        GLabel_386=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_386["font"] = ft
        GLabel_386["fg"] = "#333333"
        GLabel_386["justify"] = "center"
        GLabel_386["text"] = "label"
        GLabel_386.place(x=170,y=70,width=70,height=25)

        GLabel_859=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_859["font"] = ft
        GLabel_859["fg"] = "#333333"
        GLabel_859["justify"] = "center"
        GLabel_859["text"] = "label"
        GLabel_859.place(x=260,y=70,width=70,height=25)

    def GButton_465_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
