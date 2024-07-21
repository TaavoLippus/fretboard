from random import randint
from tkinter import *
from tkinter import ttk

#variaabled
noodid_sharp = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
noodid_flat = ["E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb"]

keeled = {"E":0, "A":5, "D":10, "G":15, "B":19, "e":24}


#generaator


def render():
    root = Tk()
    root.title("fretboard thingy")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky='nsew')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    mainframe.columnconfigure(0, weight=1)
    mainframe.columnconfigure(1, weight=1)
    mainframe.columnconfigure(2, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.rowconfigure(1, weight=1)
    mainframe.rowconfigure(2, weight=1)

    global keel_ja_fret, õige_noot_sharp, õige_noot_flat 
    keeled_list = list(keeled.keys())
    random_keel = keeled_list[randint(0,5)]
    random_fret = randint(1, 12)
    keel_ja_fret = f"{random_keel}{random_fret}"

    pitch = keeled[f"{random_keel}"] + random_fret
    õige_noot_sharp = noodid_sharp[pitch%12]
    õige_noot_flat = noodid_flat[pitch%12]

    #Label1 (noot+fret)
    ttk.Label(mainframe, text=keel_ja_fret, font = (('Helvetica', 24, 'bold'))).grid(column=1, row=0)

    #vvastus
    vastus = StringVar()
    vastus_entry = ttk.Entry(mainframe, width=10, textvariable=vastus)
    vastus_entry.grid(column=1, row= 1)


    #check
    result = StringVar()
    ttk.Label(mainframe, width=10, textvariable=result).grid(column=1, row=2)
    
    def check(*args):
        print(f"{õige_noot_sharp}")
        vastus_väärtus = vastus.get()
        print(f"{vastus_väärtus}")
        if vastus_väärtus == õige_noot_flat or vastus_väärtus == õige_noot_sharp:
            result.set(":D")
        else:
            result.set("D:")
    

    root.bind("<Return>", check)

    #render
    root.minsize(400,400)
    root.mainloop()


def main():
    render()

main()

