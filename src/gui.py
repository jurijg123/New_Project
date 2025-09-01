import tkinter as tk
import string
import random

from datetime import date
import pyperclip as pc
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import simpledialog as smpd
import os

from .logic import Funkcije

class Buttons:
    
    def show(self):
        izbor_label.config(text = clicked.get())
        self.pillar = clicked.get()
        
    def show2(self):
        izbor_label_2.config(text = clicked2.get())
        self.stranka = clicked2.get()
        
    def button(self):
        self.f = Funkcije()
        self.f.ustvari()
        
    def copy_button(self):
        self.f.copy()
        
    def add_partner(self):
        self.new_partner = smpd.askstring(title='Nova stranka', prompt='Dodaj stranko', parent=root)
        label_new_p.config(text = self.new_partner)
        
    
    
b = Buttons()

usr = Funkcije().get_path_set(pillar2="None")[2] #Dobimo ime vodje/vpisovalca projekta

def start_gui():
    root = tk.Tk()
    #root.mainloop()
            
    width = 500
    height = 400
    scr_width = root.winfo_screenwidth()
    scr_height = root.winfo_screenheight()
    
    root.iconbitmap(Funkcije().get_path_set(pillar2="None")[1])
    root.geometry('%dx%d+%d+%d' % (width, height, (scr_width-width)/2, (scr_height-height)/2))
    root.resizable(False, False)
    root.title('Ustvari projektno mapo')
            
    proj_name = tk.StringVar()
    clicked = tk.StringVar()
    clicked2 = tk.StringVar()
            
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10, fill='x', expand=True)
    
    #ime projekta
    project_label = ttk.Label(frame, text="Ime projekta:")
    project_label.pack(fill='x', expand=True)
    
    project_entry = ttk.Entry(frame, textvariable=proj_name)
    project_entry.pack(fill='x', expand=True)
    project_entry.focus()
    
    # nova stranka
    label_new_p = ttk.Label(frame, text="")
    label_new_p.pack(expand=True)
    
    #dropdown pillar
    options = [" ", "Automation", "Product Development"]
            
    clicked.set(" ")
    drop = ttk.OptionMenu(root, clicked, *options)
    drop.place(x = 260, y = 310)
    #drop.pack()
    
    #dropdown stranke
    options_2i = []
    pillar2 = ["01A", "02P"]
    for i in Funkcije().get_path_set(pillar2=pillar2)[0]:
        for j in os.listdir(i):
            options_2i.append(j)
    
    if len(options_2i) != 0:
        options_2i.remove("Konceptualizacija")
        options_2i.remove("Past Projects")
        options_2i.remove("Solidworks")
        options_2i.sort()
    options_2 = list(dict.fromkeys(options_2i))
    options_2.insert(0, " ")
            
    clicked2.set("")
    drop2 = ttk.OptionMenu(root, clicked2, *options_2)
    drop2.place(x = 120, y = 310)
    #drop2.pack()
    
    #prikaz
    koda_label = ttk.Label(frame, text=" ")
    koda_label.pack(fill='x', expand=True)
    
    
    #buttons
    button1 = ttk.Button(frame, text='Ustvari kodo', command=b.button)
    button1.pack(pady=10)
    
    button2 = ttk.Button(frame, text='Kopiraj',command=b.copy_button)
    button2.pack(pady=10)
    
    button3 = ttk.Button(frame, text='Dodaj stranko', command=b.add_partner)
    button3.pack(pady=10)
    
    root.mainloop()
