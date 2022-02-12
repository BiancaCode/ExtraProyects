"""
Programa de facturacion
"""

from tkinter import *

root = Tk()

root.title("Programa de Facturación")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

miFrame = Frame()

miFrame.pack()

miFrame.config(width="650", height="750")

#-----------------------Variables-----------------------------
tot = StringVar()
sub = StringVar()
imp = StringVar()

#------------------------Funciones----------------------------
def subtotales():
    subtotal = float(caja1.get()) + float(caja2.get())
    impuestos(float(subtotal))
    subtotal = str(subtotal)
    return sub.set(subtotal)

def impuestos(sub):
    imp7 = round(sub * 0.07, 2)
    grantotal(float(sub), float(imp7))
    imp7 = str(imp7)
    return imp.set(imp7)

def grantotal(sub, imp7):
    rest7 = sub + imp7
    rest7 = str(rest7)
    return tot.set(rest7)




#---------------------------------------------------------------

tot = StringVar()

etiqueta1 = Label(miFrame, text="Sistema de Facturación")
etiqueta1.grid(row=2, column=1, padx=60, pady=20, columnspan=2)


n1Label = Label(miFrame, text="Primer Producto:")
n1Label.grid(row=5, column=1, sticky='e', padx=10, pady=10)

caja1 = Entry(miFrame, text="primer número", justify="right")
caja1.grid(row=5, column=2, padx=10, pady=10)



n2Label = Label(miFrame, text="Segundo Producto:")
n2Label.grid(row=7, column=1, sticky='e', padx=10, pady=10)

caja2 = Entry(miFrame, text="precio", justify="right")
caja2.grid(row=7, column=2, padx=10, pady=10)



boton1 = Button(miFrame, text="Sumar",width=13, command=subtotales)
boton1.grid(row=9, column=2,  padx=10, pady=20)


#-------------------------------------------------------------------------


respLabel = Label(miFrame, text="Subtotal:")
respLabel.grid(row=14, column=1, sticky='e', padx=10, pady=10)

caja3 = Entry(miFrame, textvariable=sub, justify="right")
caja3.grid(row=14, column=2, padx=10, pady=15)



respLabel = Label(miFrame, text="Impuesto:")
respLabel.grid(row=15, column=1, sticky='e', padx=10, pady=10)

caja3 = Entry(miFrame, textvariable=imp, justify="right")
caja3.grid(row=15, column=2, padx=10, pady=15)




respLabel = Label(miFrame, text="Total:")
respLabel.grid(row=16, column=1, sticky='e', padx=10, pady=10)

caja3 = Entry(miFrame, textvariable=tot, justify="right")
caja3.grid(row=16, column=2, padx=10, pady=15)



#-----------------------------------------------------------------

miImagen = PhotoImage(file="pp.png")
firma = Label(miFrame, image=miImagen)
firma.grid(row=20, column=1, padx=10, pady=10, columnspan=2)




root.mainloop()
