from random import randint
from tkinter import *
from tkinter import ttk
import time

#variaabled
noodid_sharp = ("E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#")
noodid_flat = ("E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb")
noodid_naturaal = ("E", "F", "G", "A", "B", "C", "D")


keeled = {"E":0, "A":5, "D":10, "G":15, "B":19, "e":24}
viimased_5 = list()


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


    def guesser():

        #clear        
        for widget in mainframe.winfo_children():
            widget.destroy()

        def generate_note():
            global keel_ja_fret, õige_noot_sharp, õige_noot_flat
            keeled_list = list(keeled.keys())
            random_keel = keeled_list[randint(0, 5)]
            random_fret = randint(1, 12)
            keel_ja_fret = f"{random_keel}{random_fret}"

            pitch = keeled[f"{random_keel}"] + random_fret
            õige_noot_sharp = noodid_sharp[pitch % 12]
            õige_noot_flat = noodid_flat[pitch % 12]
            print(keel_ja_fret)
            print(õige_noot_flat)

        def duplicate_checker():
            if keel_ja_fret in viimased_5:
                print("duplicate detected")
                return True
            return False

        def naturaal_checker():
            if õige_noot_flat in noodid_naturaal:
                return True
            return False

        def appender():
            print("appender calliti")
            viimased_5.append(keel_ja_fret)
            if len(viimased_5) > 5:
                viimased_5.pop(0)
            print(viimased_5)

        while True:
            generate_note()
            if not duplicate_checker() and naturaal_checker():
                break

        appender()

        #Label1 (noot+fret)
        ttk.Label(mainframe, text=keel_ja_fret, font=(('Helvetica', 24, 'bold'))).grid(column=1, row=0)

        #vvastus
        vastus = StringVar()
        vastus_entry = ttk.Entry(mainframe, width=10, textvariable=vastus, font=(('Helvetica', 24, 'bold')))
        vastus_entry.grid(column=1, row=1)
        vastus_entry.focus_set()

        #check
        result = StringVar()
        ttk.Label(mainframe, textvariable=result, font=(('Helvetica', 24, 'bold'))).grid(column=1, row=2)

        def check(*args):
            result.set("")
            vastus_väärtus = vastus.get()
            print(f"Vastus: {vastus_väärtus}")
            if vastus_väärtus == õige_noot_flat or vastus_väärtus == õige_noot_sharp:
                print("õige vastus")
                result.set(":D")
                root.update_idletasks()

                time.sleep(1)
                guesser()
            else:
                print("vale vastus")
                result.set("D:")
            root.update_idletasks()

        root.bind("<Return>", check)
        
    root.minsize(400,400)

    guesser()
    root.mainloop()

def main():
    render()

main()

