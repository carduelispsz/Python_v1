import tkinter

def zlacz_napisy():
    a = float(a_entry.get())
    b = float(b_entry.get())
    wynik_label.configure(text=f"Wynik: {a*b/100*5.2} PLN")#5.2 to cena paliwa ktora zalozylem

def czysc_napisy():
   wynik_label.configure(text="Wynik: - ")

root = tkinter.Tk()
root.title('Prosty kalkulator')

a_label = tkinter.Label(master=root, text="Podaj dystans")
a_label.grid(row=0,column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0,column=1)

b_label = tkinter.Label(master=root, text="Spalanie l/100km")
b_label.grid(row=1,column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1,column=1)

c_label = tkinter.Label(master=root, text="Cena paliwa: 5.2 PLN")
c_label.grid(row=2,column=0)

dodaj_button = tkinter.Button(master=root, text="Przelicz", command=zlacz_napisy)
dodaj_button.grid(row=3,column=0)

dodaj_button = tkinter.Button(master=root, text="Czysc", command=czysc_napisy)
dodaj_button.grid(row=3,column=1)

wynik_label = tkinter.Label(master=root, text = "Wynik: - ")
wynik_label.grid(row=4,column=0)

root.mainloop()