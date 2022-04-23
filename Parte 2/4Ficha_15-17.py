def sair():
   jan.destroy()

def limpar():
   enome.delete(0,END) #apaga desde a posição 0 até ao fim
   emorada.delete(0,END)
   enome.focus()
   lmostrar["text"]=""
   
def leitura():
   nome = enome.get()
   morada = emorada.get()
   frase = f"Nome: {nome} e a Morada: {morada}"
   lmostrar["text"] = frase
  

def relogio():
   #atualizar a label com as horas -> lhoras['text'] = horas
   horas = strftime('%H : %M : %S')
   lhoras.configure(text=horas) # lhoras['text'] = horas
   lhoras.after(1000,relogio)
   
#######################
## INTERFACE GRÁFICA ##
from tkinter import *
from time import strftime

#15
jan = Tk()
jan.title("1ª janela")
jan.iconbitmap("lion.ico")
ljan, ajan = 350, 300

#17
posx = jan.winfo_screenwidth()//2 - ljan//2 #metade ecra larg - metade janela larg 
posy = jan.winfo_screenheight()//2 - ajan//2 #metade ecra alt - metade janela alt
jan.geometry(f"{ljan}x{ajan}+{posx}+{posy}") #posicionar no ecra1 - resolução ecra1
##### fim 17   https://pypi.org/project/screeninfo/

lnome = Label(jan, text="Nome:")
lmorada = Label(jan, text="Morada:")
enome = Entry(jan, width = 30)
emorada = Entry(jan, width = 30, state="readonly")
lnome.grid(row = 0, column = 0, padx=20) #padx afasta 20px das margens do objeto
enome.grid(row = 0, column = 1)
lmorada.grid(row = 1, column = 0, padx=20)
emorada.grid(row = 1, column = 1)

bdados = Button(jan, text="Ler Dados", bd=5, width=10)
blimpar = Button(jan, text="Limpar", bd=5, width=10)
bsair = Button(jan, text="Sair", bg="red", bd=5, width=5)

bdados.grid(row = 2, column = 0,
            pady = 10, padx=10, sticky = "w")
blimpar.grid(row = 2, column = 1)
bsair.grid(row = 2, column = 2)

lresultado = Label(jan, text="Os dados lidos são:")
lresultado.grid(row = 3, column = 0)

lmostrar = Label(jan)
lmostrar.grid(row = 4, column = 0)

enome.focus()
#a
bdados.configure(command=leitura)

#b
blimpar.configure(command=limpar)

#c
bsair.configure(command=sair)

#16
#fonte = ("Arial",16,"bold")
lhoras = Label(jan, font="Arial,16,bold")
lhoras.place(x=30, y=250)

relogio()

#17




jan.mainloop()
