import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FluidMusic")
        self.configure(bg="lightblue")
        self.geometry("800x600")

        self.screen1 = tk.Frame(self, bg="lightblue", width=800, height=600)
        self.screen2 = tk.Frame(self, bg="lightblue", width=800, height=600)
        self.screen3 = tk.Frame(self, bg="lightblue", width=800, height=600)


        self.title_label = tk.Label(self.screen1, text="FluidMusic", fg="black", font=("Arial", 40))
        self.title_label.pack(padx=50, pady=50)

        self.subtitle_label = tk.Label(self.screen1, text="A unique experience for all music listeners!", fg="black", font=("Arial", 20))
        self.subtitle_label.pack(padx=50, pady=10)

        self.label1 = tk.Label(self.screen1, text="Screen 1", fg="black", font=("Arial", 30))
        self.label1.pack(padx=50, pady=50)

    
        self.label2 = tk.Label(self.screen2, text="Select up to 15 songs!", fg="black", font=("Arial", 30))
        self.label2.pack(padx=50, pady=50)


        self.label3 = tk.Label(self.screen3, text="Screen 3", fg="black", font=("Arial", 30))
        self.label3.pack(padx=50, pady=50)


        self.next_button1 = tk.Button(self.screen1, text="Next", fg="white", bg="blue", font=("Arial", 20), command=self.show_screen2)
        self.next_button1.pack(side="bottom")
        #help button
        self.help_button = tk.Button(self.screen1, text="Help", fg="white", bg="blue", font=("Arial", 20), command=self.show_screen2)
        self.help_button.pack(side="bottom")

        self.next_button2 = tk.Button(self.screen2, text="Next", fg="white", bg="blue", font=("Arial", 20), command=self.show_screen3)
        self.next_button2.pack(side="bottom")


        self.back_button1 = tk.Button(self.screen2, text="Back", fg="white", bg="blue", font=("Arial", 20), command=self.show_screen1)
        self.back_button1.pack(side="left")


        self.back_button2 = tk.Button(self.screen3, text="Back", fg="white", bg="blue", font=("Arial", 20), command=self.show_screen2)
        self.back_button2.pack(side="left")

        # Show screen 1
        self.screen1.pack()

    def show_screen1(self):
        # go back to screen 1
        self.screen1.pack()
        self.screen2.pack_forget()
        self.screen3.pack_forget()

    def show_screen2(self):
       
        self.screen1.pack_forget()
        self.screen2.pack()
        self.screen3.pack_forget()

    def show_screen3(self):

        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack()
        
gui = GUI()
gui.mainloop()