from tkinter import *
from tkinter import ttk

#setup
root = Tk()
root.title("tkinter_test")
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.pack(fill="both", expand=True)

#grid configure
rows = 8
columns = 4
for row in range(rows):
    mainframe.rowconfigure(row, weight=10)
for column in range(columns):
    mainframe.columnconfigure(column, weight =10)

#grid pattern
for row in range(rows):
    for column in range(columns):
        print(f"row={row}, column={column}")
        if (column+row)%2 != 0:
            print("red")
            ttk.Label(mainframe, text="TEST", background='red').grid(row=row, column=column, sticky='NSEW')
        else:
            print("blue")
            ttk.Label(mainframe, text="TEST", background='blue').grid(row=row, column=column, sticky='NSEW')


#prompt label
prompt = ttk.Label(mainframe, text="PROMPT", background='white')
prompt.grid(row=0, column=1, columnspan=2, sticky='NSEW')
prompt.configure(anchor='center')

#buttonid
button_E = ttk.Button(mainframe, text="E").grid(row=2, column=0)
button_A = ttk.Button(mainframe, text="A").grid(row=2, column=1)
button_D = ttk.Button(mainframe, text="D").grid(row=2, column=2)
button_G = ttk.Button(mainframe, text="G").grid(row=2, column=3)
button_B = ttk.Button(mainframe, text="B").grid(row=3, column=0, columnspan=2)
button_C = ttk.Button(mainframe, text="C").grid(row=3, column=1, columnspan=2)
button_F = ttk.Button(mainframe, text="F").grid(row=3, column=2, columnspan=2)

#placement

root.minsize(400,400)
root.mainloop()