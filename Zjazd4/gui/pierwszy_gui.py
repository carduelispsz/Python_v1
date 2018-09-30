import tkinter

def zlacz_napisy():
    a = int(a_entry.get())
    b = int(b_entry.get())
    print(a+b)

def czysc_napisy():
   print(locals())
   print(globals())
   wynik_label.configure(text="Wynik: - ")

root = tkinter.Tk()
root.title('Prosty kalkulator')

a_label = tkinter.Label(master=root, text="a")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="abrakadabra")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

dodaj_button = tkinter.Button(master=root, text="Dodaj", command=zlacz_napisy)
dodaj_button.pack()

wynik_label = tkinter.Label(master=root, text = "Wynik: - ")
wynik_label.pack()

root.mainloop()