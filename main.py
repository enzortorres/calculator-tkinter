from tkinter import Tk, Frame, Label, Button
from modulos import *

tk = Tk()
tk.title('Primeira calculadora')
tk.geometry('300x470')
tk.resizable(False, False)

frame_display = Frame(tk, bg='#000', width=300, height=100)
frame_display.pack_propagate(False)
frame_display.columnconfigure(0, weight=1)
frame_display.grid(row=0, column=0)

conta_text = Label(
    frame_display, text="0", font="Arial 20",
    bg="black", fg="white", justify="right", anchor="e"
)
conta_text.pack(fill="both", pady=40, padx=5)

frame_button = Frame(tk, bg="#CECECE", width=300, height=300)
frame_button.grid(row=1,column=0, pady=5)

for i in range(4):
    frame_button.columnconfigure(i, weight=1)

button_clear = Button(frame_button, text="C", command=lambda: clear(conta_text),
                    width=9, height=4, bg="#CECECE")
button_clear.grid(row=0, column=0)

button_remove = Button(frame_button, text="<-", command=lambda: remove(conta_text),
                    width=9, height=4, bg="#CECECE")
button_remove.grid(row=0, column=1)

button_divide = Button(frame_button, text="/", command=lambda: divide(conta_text),
                    width=9, height=4, bg="#CECECE")
button_divide.grid(row=0, column=2)

button_multiplica = Button(frame_button, text="*", command=lambda: multiplica(conta_text),
                    width=9, height=4, bg="#CECECE")
button_multiplica.grid(row=0, column=3)

button_7 = Button(frame_button, text=7, command=lambda: add_number(conta_text, 7),
                    height=4, width=9, bg="white") 
button_7.grid(row=1, column=0)

button_8 = Button(frame_button, text=8, command=lambda: add_number(conta_text, 8),
                    height=4, width=9, bg="white") 
button_8.grid(row=1, column=1)

button_9 = Button(frame_button, text=9, command=lambda: add_number(conta_text, 9),
                    height=4, width=9, bg="white") 
button_9.grid(row=1, column=2)

button_sub = Button(frame_button, text="-", command= lambda: subtracao(conta_text), 
                    height=4, width=9, bg="#CECECE")
button_sub.grid(row=1, column=3)

button_4 = Button(frame_button, text=4, command=lambda: add_number(conta_text, 4),
                    height=4, width=9, bg="white") 
button_4.grid(row=2, column=0)

button_5 = Button(frame_button, text=5, command=lambda: add_number(conta_text, 5),
                    height=4, width=9, bg="white") 
button_5.grid(row=2, column=1)

button_6 = Button(frame_button, text=6, command=lambda: add_number(conta_text, 6),
                    height=4, width=9, bg="white") 
button_6.grid(row=2, column=2)

button_soma = Button(frame_button, text="+", command= lambda: soma(conta_text), 
                    height=4, width=9, bg="#CECECE")
button_soma.grid(row=2, column=3)

button_1 = Button(frame_button, text=1, command=lambda: add_number(conta_text, 1),
                    height=4, width=9, bg="white") 
button_1.grid(row=3, column=0, sticky="n")

button_2 = Button(frame_button, text=2, command=lambda: add_number(conta_text, 2),
                    height=4, width=9, bg="white") 
button_2.grid(row=3, column=1, sticky="n")

button_3 = Button(frame_button, text=3, command=lambda: add_number(conta_text, 3),
                    height=4, width=9, bg="white") 
button_3.grid(row=3, column=2, sticky="n")

button_0 = Button(frame_button, text=0, command=lambda: add_number(conta_text, 3),
                    height=4, width=20, bg="white")
button_0.grid(row=4, column=0, columnspan=2, sticky="n")

button_virgula = Button(frame_button, text=".", command=lambda: add_number(conta_text, "."),
                    height=4, width=9, bg="white")
button_virgula.grid(row=4, column=2, sticky="n")

button_result = Button(frame_button, text="=", command= lambda: result(conta_text), 
                    height=9, width=9, bg="orange")
button_result.grid(row=3, column=3, rowspan=2)


tk.mainloop()