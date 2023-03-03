from tkinter import *
#Oknow
window =Tk()
window.title("Prevod men")
window.minsize(500,500)
window.resizable(False, False)

#Label2
label_1 = Label(text= "Novy label", font=("Helvetica", 20, "bold"))
label_1.pack()

label_1["text"] = "Novy label 2"
label_1.config(text="Novy label 3")

#tlacitko
def change_text():
    label_1["text"]= input_1.get()
    input_1.delete(0,END)
    


button_1 = Button(text="klikni na mne", command=change_text)
button_1.pack()


#Input(vstup)
input_1 = Entry()
input_1.insert(0,string="Vloz cislo")
input_1.focus()
input_1.pack()
#ziskanie dat
#print(input_1.get())

#textove pole
text_field = Text(width=40, height=10)
text_field.focus()
text_field.pack()

#Hlavni cyklus
window.mainloop()