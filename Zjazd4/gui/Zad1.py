import tkinter

def zlacz_napisy():
    a = float(a_entry.get())
    b = float(b_entry.get())
    wynik_label.configure(text=f"Wynik: {a*b/100*5.2}")#5.2 to cena paliwa ktora zalozylem

def czysc_napisy():
   wynik_label.configure(text="Wynik: - ")

root = tkinter.Tk()
root.title('Prosty kalkulator')

a_label = tkinter.Label(master=root, text="Podaj dystans")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="Spalanie l/100km")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

dodaj_button = tkinter.Button(master=root, text="Dodaj", command=zlacz_napisy)
dodaj_button.pack()

wynik_label = tkinter.Label(master=root, text = "Wynik: - ")
wynik_label.pack()

root.mainloop()