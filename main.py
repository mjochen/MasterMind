import tkinter
import tkinter.messagebox
import customtkinter
from functions import *

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


dummy_text = "•"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
            
        self.colors = get_all_colors()

        # configure window
        self.title(f"My version of Mastermind")
        self.geometry(f"{456}x{485}")
        
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.playing_field_frame = customtkinter.CTkFrame(self)
        # self.playing_field_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
                
        self.color_optionmenus = []
        for i in range(4):
            self.color_optionmenus.append(customtkinter.CTkOptionMenu(self, values=self.colors, width=30, height=30))
            # self.color_optionmenus[i].variable = i
            self.color_optionmenus[i].grid(row=1, column=i, padx=5, pady=5)
            
        button = customtkinter.CTkButton(self, text="?", command=self.test_code_event, width=30, height=30)
        button.grid(row=1, column=4, padx=5, pady=5)
        
        self.option_labels = []
        for i in range(10):
            row = []
            for j in range(5):
                row.append(customtkinter.CTkLabel(self, width=30, height=30))
                row[j].grid(row=i+2, column=j, padx=5, pady=5)
            self.option_labels.append(row)
        
        self.counting_label = customtkinter.CTkLabel(self, width=150, height=30)
        self.counting_label.grid(row=12, column=0, columnspan=4, padx=5, pady=5)
        
        button = customtkinter.CTkButton(self, text="Cheat!", command=self.cheat_event, width=40, height=30)
        button.grid(row=12, column=4, padx=5, pady=5)
        
        self.start_new_game()

    def cheat_event(self):
        print(self.possibles)
        
        
        
    def start_new_game(self):
        self.code = get_random_code(self.colors)
        self.attempts = []
        
        for row in self.option_labels:
            for label in row[:-1]:
                label.configure(text=dummy_text)
            row[-1].configure(text="")
            
        self.possibles = all_possibles()
        self.counting_label.configure(text=f"Nr of options: {len(self.possibles)}")
        
        # self.title(f"My version of Mastermind {self.code}")
        
    def test_code_event(self):
        attempt = "".join([ i.get() for i in self.color_optionmenus ])
        if attempt == self.code:
            tkinter.messagebox.showinfo("Mastermind", "You won!")
            
        for i in range(len(self.option_labels)-1, 0, -1):
            for j, label in enumerate(self.option_labels[i]):
                label.configure(text=self.option_labels[i-1][j].cget("text"))
        
        for i, label in enumerate(self.option_labels[0][:-1]):
            label.configure(text = self.color_optionmenus[i].get())
        
        self.attempts.append( [attempt, test_attempt(attempt, self.code)] )            
        self.option_labels[0][-1].configure(text = self.attempts[-1][1])
        
        if self.option_labels[-1][0].cget("text") != dummy_text:
            tkinter.messagebox.showinfo("Mastermind", "You lost!")
            # self.destroy()
        
        
        self.possibles = filter_possibles(self.possibles, self.attempts[-1][0], self.attempts[-1][1])
        self.counting_label.configure(text=f"Nr of options: {len(self.possibles)}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
