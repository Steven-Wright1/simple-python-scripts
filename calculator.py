#!/usr/bin/env python3

# creating new branch to develop calculator.py with a full GUI interface

import tkinter as tk
from tkinter import ttk

def main():

    root=tk.Tk()
    root.title("Simple Python Calculator")
    root.geometry('475x375')

    style = ttk.Style()
    style.configure('TButton',background='grey',padding=15)
    style.configure('cancel.TButton',background='brown3',padding=15)


    result = tk.Label(root,text="Display Field for result",background='white',padx=150,pady=20)
    result.grid(row=1,columnspan=4,padx=10,pady=20, sticky='nsew')

    button1 = ttk.Button(root,text="7",style='TButton')
    button1.grid(row=2, column=0,pady=5)
    button2 = ttk.Button(root,text="8",style='TButton')
    button2.grid(row=2,column=1)
    button3 = ttk.Button(root,text="9",style='TButton')
    button3.grid(row=2,column=2)
    button4 = ttk.Button(root,text="+",style='TButton')
    button4.grid(row=2,column=3)


    button5 = ttk.Button(root,text="4",style='TButton')
    button5.grid(row=3,column=0,pady=5)
    button6 = ttk.Button(root,text="5",style='TButton')
    button6.grid(row=3,column=1)
    button7 = ttk.Button(root,text="6",style='TButton')
    button7.grid(row=3,column=2)
    button8 = ttk.Button(root,text="-",style='TButton')
    button8.grid(row=3,column=3)

    button9 = ttk.Button(root,text="1",style='TButton')
    button9.grid(row=4,column=0,pady=5)
    button10 = ttk.Button(root,text="2",style='TButton')
    button10.grid(row=4,column=1)
    button11 = ttk.Button(root,text="3",style='TButton')
    button11.grid(row=4,column=2)
    button12 = ttk.Button(root,text="x",style='TButton')
    button12.grid(row=4,column=3)
    
    button13 = ttk.Button(root,text="C",style='cancel.TButton')
    button13.grid(row=5,column=0,pady=5)
    button14 = ttk.Button(root,text="0",style='TButton')
    button14.grid(row=5,column=1)
    button15 = ttk.Button(root,text="=",style='TButton')
    button15.grid(row=5,column=2)
    button16 = ttk.Button(root,text="÷",style='TButton')
    button16.grid(row=5,column=3)



    root.mainloop()
    

if __name__ == "__main__":
    main()