def mostrar():
   x = 40
   print(f"O valor é {x}")

#######################
## INTERFACE GRÁFICA ##

from tkinter import *

jan = Tk()
jan.title("Mostrar objetos")
#jan.iconbitmap("nome.ico")
x,y = 350,200
jan.geometry(f"{x}x{y}") #jan.geometry("350x200")

#Label a pedir o nome, caixa de texto e botão
lnome = Label(jan, text = "Insira o seu nome completo:")
enome = Entry(jan, background = "pink")
bok = Button(jan, text = 'OK', bg = "Lightblue", fg="Orange",
             command = mostrar)

#posicionar os objetos na contentor "jan" através PACK
#lnome.pack(side="left")
#enome.pack(side="left", fill=Y)
#bok.pack(side="bottom", fill=BOTH)

#posicionar os objetos na contentor "jan" através GRID
#lnome.grid(row = 0, column = 0)
#enome.grid(row = 0, column = 1)
#bok.grid(row = 1, column = 0)

#posicionar os objetos na contentor "jan" através PLACE
lnome.place(x = 20, y = 50)
lnome.update() #para recalcular o tamanho do objeto no contentor "jan"
enome.place(x = 20 + lnome.winfo_width()  , y = 50) #x é atualizado para 20 + comp. do texto anterior
bok.place(x = 100, y = 70)

jan.mainloop()
