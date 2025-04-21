from tkinter import *

def action():
    km = round((int(mile_entry.get()) * 1.609344), 2)
    kmoutput_label.config(text=km)

window = Tk()
window.title("km->mile converter")
# window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

mile_entry = Entry(width=15)
mile_entry.insert(END, string="0")
mile_entry.grid(column=1, row=0)


mile_label = Label()
mile_label.config(text="Miles")
mile_label.grid(column=2, row=0)

isequal_label = Label()
isequal_label.config(text="is equal to")
isequal_label.grid(column=0, row=1)

kmoutput_label = Label()
kmoutput_label.config(text=0)
kmoutput_label.grid(column=1, row=1)


km_label = Label()
km_label.config(text="Km")
km_label.grid(column=2, row=1)


btn_click = Button(text="Calculate", command=action)
btn_click.grid(column=1, row=2)













window.mainloop()