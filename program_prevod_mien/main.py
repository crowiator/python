from tkinter import *

#okno
window = Tk()
window.title("Prevod mien")
window.minsize(300,300)
window.resizable(False,False)
window.config(bg="orange")

#1 euro je 23.75 CZK
def count_currency():
    amount = float(input_amount.get())/23.75
    result_label["text"]= round(amount,2)


# input
input_amount= Entry(width=10, font=("Arial", 20), bg="white",fg="black")
input_amount.grid(row=0,column=0, padx=10, pady=10)

#label
czk_label = Label(text="CZK", font=("Arial", 15, "bold"), bg="orange")
czk_label.grid(row=0, column=1)

result_label = Label(text="0", font=("Arial", 15), bg="orange")
result_label.grid(row=1, column=0)

euro_label = Label(text="EUR", font=("Arial", 15, "bold"), bg="orange")
euro_label.grid(row=1, column=1)

# button
count_button= Button(text="Prepocitaj",font=("Arial", 15, "bold"), command=count_currency)
count_button.grid(row=0,column=2, padx=10, pady=10)


#hlavny cyklus
window.mainloop()