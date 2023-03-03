# import tkinter

# #Okno
# window = tkinter.Tk()
# window.title("Prevod mien")
# window.minsize(width=500, height=500)
# window.resizable(False,False)
# window.config(bg="orange")

# #okno 2
# window2 = tkinter.Tk()
# window2.title("Prevod mien")
# window.geometry("300x400+0+0")
# window2.resizable(False,False)
# window2.config(bg="orange")


# #label 
# greet_label = tkinter.Label(text="CZK", fg="black", font=("Arial", 24, "bold"))
# #pridanie do window
# greet_label.pack()


# #hlavni cyklus
# window.mainloop()

# Naimportujte tkinter
from tkinter import *
# Vytvořte jedno okno o rozměru 500 na 500 a nastavte hlavní cyklus
window = Tk()
window.minsize(width=500, height=500)

# # Do okna přidejte ikonku s názvem icon.ico.
# window.iconbitmap("icon.icns")
# Nastavte popisek okna "Přepočet kurzu"
window.title("Přepočet kurzu")
# Vytvořte label s textem "Eura" a názvem currency, jeho font nastavte na Cambria, 20 pixelů, tučný (bold)
currency = Label(text="Eura",bg="black",fg="white",font=("Cambria",20, "bold"))
currency.pack()

currency2 = Label(text="CZK",bg="black",fg="white",font=("Cambria",20, "bold"))
currency2.pack()
# Barvu pozadí celého okna! nastavte na černou
window.config(bg="black")
# Barvu pozadí labelu nastavte na černou
# Barvu textu labelu nastavte na bílou (fg)

#hlavni cyklus
window.mainloop()