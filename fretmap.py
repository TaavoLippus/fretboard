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

    rows = 8
    columns = 4
    for row in range(rows):
        mainframe.rowconfigure(row, weight=10)
    for column in range(columns):
        mainframe.columnconfigure(column, weight =10)


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
        prompt = ttk.Label(mainframe, text=keel_ja_fret, font=(('Helvetica', 24, 'bold')))
        prompt.grid(row=0, column=1, columnspan=2, sticky='NSEW')
        prompt.configure(anchor='center')

        #vvastus
        vastus = StringVar()
        button_E = ttk.Button(mainframe, text="E", command=lambda: [vastus.set("E"), check()]).grid(row=2, column=0)
        button_A = ttk.Button(mainframe, text="A", command=lambda: [vastus.set("A"), check()]).grid(row=2, column=1)
        button_D = ttk.Button(mainframe, text="D", command=lambda: [vastus.set("D"), check()]).grid(row=2, column=2)
        button_G = ttk.Button(mainframe, text="G", command=lambda: [vastus.set("G"), check()]).grid(row=2, column=3)
        button_B = ttk.Button(mainframe, text="B", command=lambda: [vastus.set("B"), check()]).grid(row=3, column=0, columnspan=2)
        button_C = ttk.Button(mainframe, text="C", command=lambda: [vastus.set("C"), check()]).grid(row=3, column=1, columnspan=2)
        button_F = ttk.Button(mainframe, text="F", command=lambda: [vastus.set("F"), check()]).grid(row=3, column=2, columnspan=2)

        #check
        result = StringVar()
        result.set("-_-")
        ttk.Label(mainframe, textvariable=result, font=(('Helvetica', 24, 'bold'))).grid(column=1, row=5, columnspan=2)

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

