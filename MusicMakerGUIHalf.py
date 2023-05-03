import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FluidMusic")
        self.geometry("800x600")
        self.configure(bg="#FFDAB9")

        # Create a frame for the header
        self.header = tk.Frame(self, bg="#FFDAB9", height=100)
        self.header.pack(side="top", fill="x")

        # Add a logo to the header
        img = ImageTk.PhotoImage(Image.open("logo.png"))
        logo = tk.Label(self.header, image=img, bg="#FFDAB9")
        logo.image = img
        logo.pack(padx=10, pady=10)

        # Create a frame for the content
        self.content = tk.Frame(self, bg="#FFDAB9")
        self.content.pack(side="top", fill="both", expand=True)

        # Create a notebook widget to switch between screens
        self.notebook = ttk.Notebook(self.content)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Create the screens
        self.screen1 = tk.Frame(self.notebook, bg="#FFDAB9")
        self.screen2 = tk.Frame(self.notebook, bg="#FFDAB9")
        self.screen3 = tk.Frame(self.notebook, bg="#FFDAB9")
        self.helpscreen = tk.Frame(self.notebook, bg="#FFDAB9")

        self.notebook.add(self.screen1, text="Screen 1")
        self.notebook.add(self.screen2, text="Screen 2")
        self.notebook.add(self.screen3, text="Screen 3")
        self.notebook.add(self.helpscreen, text="Help")

        
        self.label1 = tk.Label(self.screen1, text="Welcome to FluidMusic!", fg="#0074D9", font=("Arial", 30), bg="#FFDAB9")
        self.label1.pack(padx=50, pady=(50, 0))
        def set_x(value):
            global x
            x = value
            print(f"x is now {x}")
        
        # 3 buttons for each playlist
        button11 = tk.Button(self.screen1, text="Playlist 1", fg="white", bg="#0074D9", font=("Arial", 20), command=lambda: set_x(1))
        button11.pack(pady=10)
        
        button12 = tk.Button(self.screen1, text="Playlist 2", fg="white", bg="#0074D9", font=("Arial", 20), command=lambda: set_x(2))
        button12.pack(pady=10)
        
        button13 = tk.Button(self.screen1, text="Playlist 3", fg="white", bg="#0074D9", font=("Arial", 20), command=lambda: set_x(3))
        button13.pack(pady=10)
        
        # Set the initial value of x to 0
        x = 0

        self.next_button1 = tk.Button(self.screen1, text="Get started", fg="white", bg="#0074D9", font=("Arial", 20), command=self.show_screen2)
        self.next_button1.pack(side="bottom", pady=(0, 10))

        self.label2 = tk.Label(self.screen2, text="What songs do you like?", fg="#0074D9", font=("Arial", 30), bg="#FFDAB9")
        self.label2.pack(padx=50, pady=(50, 0))

        textbox1 = tk.Text(self.screen2, height=3, width=40, font=("Arial", 12))
        textbox1.pack(padx=50, pady=(20, 0))

        def get_user_input():
           user_input = textbox1.get("1.0", "end-1c")
           arraysongs = [int(x) for x in user_input.split()]
           print(arraysongs)

        buttonget = tk.Button(self.screen2, text="Submit", command=get_user_input, fg="white", bg="#0074D9", font=("Arial", 16))
        buttonget.pack(pady=20)


        self.next_button2 = tk.Button(self.screen2, text="Next", fg="white", bg="#0074D9", font=("Arial", 16), command=self.show_screen3)
        self.next_button2.pack(side="bottom", pady=10)


        self.back_button1 = tk.Button(self.screen2, text="Back", fg="white", bg="#0074D9", font=("Arial", 20), command=self.show_screen1)
        self.back_button1.pack(side="left", padx=10)

        # Add widgets to screen 3
        # ...

        self.back_button2 = tk.Button(self.screen3, text="Back", fg="white", bg="#0074D9", font=("Arial", 20), command=self.show_screen2)
        self.back_button2.pack(side="left", padx=10)

        # Add widgets to the help screen
        self.labelhelp = tk.Label(self.helpscreen, text="FluidMusicTM lets you take ANY available online playlist, import the songs, \nand automagically see what new beats fit your taste.\nWhen prompted, select 10 songs that you would like to see more of. \nThen, let the software chug, and viola, your new reccomendations!", fg="#0074D9", font=("Arial", 10), bg="#FFDAB9")
        self.labelhelp.pack(padx=50, pady=(50, 0))
        self.back_button3 = tk.Button(self.helpscreen, text="Back", fg="white", bg="#0074D9", font=("Arial", 20), command=self.show_screen1)
        self.back_button3.pack(side="left", padx=10)

        # Show screen 1
        self.show_screen1()

    def show_screen1(self):
        self.notebook.select(self.screen1)

    def show_screen2(self):
        self.notebook.select(self.screen2)

    def show_screen3(self):
        self.notebook.select(self.screen3)

    def show_helpscreen(self):
        self.notebook.select(self.helpscreen)


gui = GUI()
gui.mainloop()
