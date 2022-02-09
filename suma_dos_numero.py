"""
programa que suma 2 números
"""

from tkinter import *

root = Tk()

root.title("Suma de Numeros")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

miFrame = Frame()

miFrame.pack()

miFrame.config(width="650", height="750")



#------------------------Funcion suma----------------------------

def sumar():

    primero = float(caja1.get())
    segundo = float(caja2.get())
    sumar = primero + segundo

    return variable1.set(sumar)

#----------------------------------------------------------------

variable1 = StringVar()

etiqueta1 = Label(miFrame, text="Sistema de Suma de Dos Números")
etiqueta1.grid(row=2, column=1, padx=60, pady=20, columnspan=2)


n1Label = Label(miFrame, text="Primer Número:")
n1Label.grid(row=5, column=1, sticky='e', padx=10, pady=10)

caja1 = Entry(miFrame, text="primer número", justify="right")
caja1.grid(row=5, column=2, padx=10, pady=10)



n2Label = Label(miFrame, text="Segundo Número:")
n2Label.grid(row=7, column=1, sticky='e', padx=10, pady=10)

caja2 = Entry(miFrame, text="segundo número", justify="right")
caja2.grid(row=7, column=2, padx=10, pady=10)



boton1 = Button(miFrame, text="Sumar",width=13, command=sumar)
boton1.grid(row=9, column=2,  padx=10, pady=20)



respLabel = Label(miFrame, text="Resultado:")
respLabel.grid(row=14, column=1, sticky='e', padx=10, pady=10)

caja3 = Entry(miFrame, textvariable=variable1, justify="right")
caja3.grid(row=14, column=2, padx=10, pady=15)



miImagen = PhotoImage(file="pp.png")
firma = Label(miFrame, image=miImagen)
firma.grid(row=20, column=1, padx=10, pady=10, columnspan=2)




root.mainloop()