import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading

class Gui(tk.Tk):
    def __init__(self, make_function, open_built_function):
        super().__init__()
        #Funciones activables por botones
        self.make_function: function = make_function
        self.open_built_function: function = open_built_function

        self.title_image = tk.PhotoImage(file="./data/img/ui/title.png")

        self.extremity_value: tk.DoubleVar = tk.DoubleVar(value=1.0)

        #Una pequeña preparacion de la ventana
        self.title("Scam Download Site Generator")
        self.geometry("400x300")
        self.resizable(False, False)

    def extremity_slider_changed(self, event):
        self.extremity_label.configure(text="EXTREMITY: %d"%(int(self.extremity_scale.get())))

    def make_main_window(self):
        #Crea una ventana con toda la aplicacion
        self.clean_root()
        self.title = ttk.Label(self, image=self.title_image)
        self.title.pack()

        self.extremity_label = ttk.Label(self, text="EXTREMITY: 1")
        self.extremity_label.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        self.extremity_scale = ttk.Scale(self, from_=1, to=50, orient="horizontal", variable=self.extremity_value, command=self.extremity_slider_changed)
        self.extremity_scale.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

        self.description = ttk.Label(self, text="CLICK on Generate Site to generate a FREE 100% REAL\nNO FAKE Scam Download Site HTML.")
        self.description.pack()
        #El comando va a otro thread para que no se congele la GUI
        self.make_site_button = ttk.Button(self, text="Build Site", 
                                           command=lambda: threading.Thread(
                                               target= lambda: self.func_make_site(
                                                   int(self.extremity_scale.get())
                                                   )
                                               ).start()
                                           )
        self.make_site_button.pack(side=tk.LEFT, expand=True)

        self.open_built_site_button = ttk.Button(self, text="Open Built Site", 
                                                 command=lambda: self.open_built_function()
                                                 )
        self.open_built_site_button.pack(side=tk.LEFT, expand=True)

        self.info_button = ttk.Button(self, text="About...", 
                                                 command=self.show_info
                                                 )
        self.info_button.pack(side=tk.LEFT, expand=True)

    def make_building_window(self):
        self.clean_root()
        self.title = ttk.Label(self, text="Building site...")
        self.title.pack()
    
    def func_make_site(self, extremity: int):
        self.make_site_button.state(["disabled"])
        self.make_site_button.configure(text="Building...")

        self.make_status = self.make_function(extremity)
        self.make_site_button.state(["!disabled"])
        self.make_site_button.configure(text="Build Site")

        if self.make_status == 0:
            messagebox.showinfo(title="DOWNLOAD HERE NOW", message="Scam Download Site Generated.")
        if self.make_status == 1:
            messagebox.showerror(title="SCAM ALERT", message="Program data not found. Redownload the program.")
        if self.make_status == 2:
            messagebox.showwarning(title="NYEH HEH HEH", message="Site generated. Couldnt scrape wikipedia for information and images.")
    
    def show_info(self):
        messagebox.showinfo(title="Do you want to give me your ██████████",
                            message=
'''WHAT IS THIS STUPIDITY?????????
This application (this is even an application?) generates scam pirate download-like HTML pages, getting the games from a database, scraping wikipedia to search for information and then applying the info to an HTML template.
To make an HTML page you simply specify the EXTREMITY COEFFICIENT and click \"Build Page\".
The EXTREMITY COEFFICIENT controls how crazy the pirate site builder gets when putting their DOWNLOAD messages.

WHO MADE THIS STUPIDITY???????????????????????????
This \"coding meme\" or whatever thing this is, was made by URROVA, out of the most pure existencial boredom.
His website: https://urrova.github.io/'''
                            )

    def clean_root(self):
        for ele in self.winfo_children():
            ele.destroy()