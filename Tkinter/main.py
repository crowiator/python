from tkinter import *
#grid - zlata cesta

#okno
window = Tk()
window.title("Prevod men")
window.minsize(500,500)
window.resizable(False, False)

#label
label_1 = Label(text="Prvni label", font=("Helvetica",20))
# label_1.pack()
# label_1.place(x=0,y=0)
label_1.grid(row=0,column=0)
label_2 = Label(text="druhy label", font=("Helvetica", 20))
# label_2.pack()
# label_2.place(x=200,y=200)
label_2.grid(row=1,column=1)



label_3 = Label(text="Treti label", font=("Helvetica",20))
# label_3.pack()
label_3.grid(row=2,column=2)


#hlavni cyklus
window.mainloop()