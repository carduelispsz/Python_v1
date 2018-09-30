import tkinter
import urllib.request
import json


def g_pogoda():
    miasto = a_entry.get()
    with urllib.request.urlopen(f"http://www.metaweather.com/api/location/search/?query={miasto}") as f:
        data = f.read()
        data = json.loads(data)

    with urllib.request.urlopen(f"http://www.metaweather.com/api/location/{data[0]['woeid']}") as f:
        data = f.read()
        data = json.loads(data)

    pogoda = (data['consolidated_weather'])

    #print(f"{p['applicable_date']} - {p['the_temp']}")

    wynik_label.configure(text=f"Wynik: {p['applicable_date']} - {p['the_temp']} PLN")

root = tkinter.Tk()
root.title('Prognoza pogody')

a_label = tkinter.Label(master=root, text="City name")
a_label.grid(row=0,column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0,column=1)


dodaj_button = tkinter.Button(master=root, text="Confirm", command = g_pogoda)
dodaj_button.grid(row=0,column=2)


wynik_label = tkinter.Label(master=root, text = "Wynik: - ")
wynik_label.grid(row=4,column=0)

root.mainloop()