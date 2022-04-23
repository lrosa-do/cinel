
#######################
## INTERFACE GRÁFICA ##
from tkinter import *
#1
jan = Tk()
#2
jan.title("Primeira janela em Tk")
#3
jan.configure(bg="Orange") #jan["bg"] = "Orange"
#4
jan.geometry("400x330")
#5
jan.resizable(False,False)
#6
fonte = ("Comic Sans MS", 14, "bold")
#7
jan.iconbitmap("bola2.ico")
#8
jan.geometry("400x330+300+500")
#9
#texto = Label(jan, text="Olá Python").pack()
texto = Label(jan, text="Olá Python")
texto.place(x=20, y=20)
#10
#texto["font"]=fonte
texto.configure(font=fonte)
#11
ctexto = Entry(jan)
ctexto.place(x = 20, y = 55)
ctexto.focus() #coloca o cursor do texto dentro da caixa
#12
bsair = Button(jan, text = "Sair")
bsair.place(x = 20, y = 75.5)

#13
def bazar():
   jan.destroy()
   
bsair.configure(command=bazar)
#14
bsair.configure(bg="Blue", fg="white", bd=4)

jan.mainloop()
