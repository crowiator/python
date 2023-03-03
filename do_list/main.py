from tkinter import *

def add_item():
    list_box.insert(END,user_input.get())
    user_input.delete(0, END)

def remove_item():
    #odstrani celu polozku
    #anchor -> oznacena polozka
    list_box.delete(ANCHOR)

def remove_all_items():
    #odstrani vsetke polozky
    list_box.delete(0,END)

def save_list():
    #ulozi ulohy do textoveho suboru
    with open("tasks.txt", "w") as file:
        my_tasks = list_box.get(0,END)
        for task in my_tasks:
            file.write(f"{task}\n")
            
#Okno
window = Tk()
window.title("To do list")
window.minsize(400,400)
window.resizable(False,False)

#Definicia fontov a bariev
main_font = ("Arial",12)
main_color = "blue"
button_color = "grey"
window.config(bg=main_color)

# Frames
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=main_color)
buttons_frame = Frame(window, bg=main_color)

input_frame.pack()
text_frame.pack()
buttons_frame.pack()

#Input frame
user_input = Entry(input_frame, width=35, borderwidth=3, font=main_font, bg="white", fg="black")
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button= Button(input_frame,text="Add", borderwidth=2, font=main_font, bg= button_color, command=add_item)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=15)


#Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0,column=1, sticky=N+S)



#Text frame
list_box = Listbox(text_frame, height=15, width=50, borderwidth=3, font=main_font,bg="white", fg="black", yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

#prepojenie
text_scrollbar.config(command=list_box.yview)

#Button frame-obsah
remove_button = Button(buttons_frame, text="Remove item", borderwidth=2, font=main_font, bg= button_color, command=remove_item)
clear_button = Button(buttons_frame, text="Clear all item", borderwidth=2, font=main_font, bg= button_color, command=remove_all_items)

save_button = Button(buttons_frame, text="Save", borderwidth=2, font=main_font, bg= button_color, command=save_list)
quit_button = Button(buttons_frame, text="Quit", borderwidth=2, font=main_font, bg= button_color, command=window.destroy)

remove_button.grid(row=0,column=0, padx=1, pady=10)
clear_button.grid(row=0,column=1, padx=1, pady=10)
save_button.grid(row=0,column=2, padx=1, pady=10)
quit_button.grid(row=0,column=3, padx=1, pady=10)
#hlavny cyklus
window.mainloop()