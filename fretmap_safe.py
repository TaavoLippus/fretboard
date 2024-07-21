from random import randint
import tkinter as tk

#variaabled
noodid_sharp = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
noodid_flat = ["E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb"]

keeled = {"E":0, "A":5, "D":10, "G":15, "B":19, "e":24}


#generaator
def generaator():
    global rand_keel_ja_fret, rand_õige_noot_sharp, rand_õige_noot_flat 
    keeled_list = list(keeled.keys())
    random_keel = keeled_list[randint(0,5)]
    random_fret = randint(1, 12)
    rand_keel_ja_fret = f"{random_keel}{random_fret}"

    pitch = keeled[f"{random_keel}"] + random_fret
    rand_õige_noot_sharp = noodid_sharp[pitch%12]
    rand_õige_noot_flat = noodid_flat[pitch%12]

#funktsioon
def test(keel_ja_fret, õige_noot_sharp, õige_noot_flat):

    print(keel_ja_fret)
    pakkumine = input("kirjuta noot: ")

    if pakkumine == õige_noot_sharp: {
        print("õige!!!!!")
    } 
    elif pakkumine == õige_noot_flat: {
        print("õige!!!!!")
    }
    else: {
        print("vale :(")
    }

def main():
    generaator()
    test(rand_keel_ja_fret, rand_õige_noot_sharp, rand_õige_noot_flat)

def render():
    window = tk.Tk()

main()

