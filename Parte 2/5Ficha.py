'''
#######################
## INTERFACE GRÁFICA ##
from tkinter import *
#1
jan = Tk()
jan['bg']="Grey"
jan.title("Exercícios 1 e 2")
jan.iconbitmap("lion.ico")
ljan, ajan = 800, 600
posx, posy = 250, 250
jan.geometry(f"{ljan}x{ajan}+{posx}+{posy}")

#2
posx = jan.winfo_screenwidth()//2 - ljan//2 #metade ecra larg - metade janela larg 
posy = jan.winfo_screenheight()//2 - ajan//2 #metade ecra alt - metade janela alt
jan.geometry(f"{ljan}x{ajan}+{posx}+{posy}") #posicionar no ecra1 - resolução ecra1


jan.mainloop()
'''
#################################################################
'''
#Ex3
#######################
## INTERFACE GRÁFICA ##
from tkinter import *

jan = Tk()
jan.title("Frames")
jan.iconbitmap("lion.ico")
ljan, ajan = 200, 100
posx = jan.winfo_screenwidth()//2 - ljan//2 #metade ecra larg - metade janela larg 
posy = jan.winfo_screenheight()//2 - ajan//2 #metade ecra alt - metade janela alt
jan.geometry(f"{ljan}x{ajan}+{posx}+{posy}") #posicionar no ecra1 - resolução ecra1

##Frame
f1 = Frame(jan)

lUser = Label(f1, text = "Utilizador:")
lPass = Label(f1, text = "Password:")
eUser = Entry(f1)
ePass = Entry(f1, show='@')
bLogin = Button(f1, text='Login', width=7, height=2, bd=4)

lUser.grid(row=0, column=0)
lPass.grid(row=1, column=0)
eUser.grid(row=0, column=1)
ePass.grid(row=1, column=1)
bLogin.grid(row=2, column=1)

f1.grid()

eUser.focus() #colcar o cursor do rato ativo dentro da entry

jan.mainloop()
'''
##############################################################

#Ex4
'''
#######################
## INTERFACE GRÁFICA ##
from tkinter import *

jan = Tk()
jan.title("Label")
jan.iconbitmap("lion.ico")
ljan, ajan = 400, 300
posx = jan.winfo_screenwidth()//2 - ljan//2 #metade ecra larg - metade janela larg 
posy = jan.winfo_screenheight()//2 - ajan//2 #metade ecra alt - metade janela alt
jan.geometry(f"{ljan}x{ajan}+{posx}+{posy}") #posicionar no ecra1 - resolução ecra1
f1=Frame(jan)


lb1 = Label(f1, text = "Python(Tkinter) - Objeto label",
            font="Arial,15", bd=1, relief="solid",pady=15,padx=15)

lb1.pack(anchor="center", fill=X)

fonte = ('Comic Sans MS', 15)
lb2 = Label(f1, text = "Label com texto e largura e altura \
fixas.\nAlinhamento\nExpande \
com redimensionamento", font = fonte,
            bd = 1, relief = 'solid', bg = 'yellow', fg='blue',
            width = 50, height = 10, anchor='w', justify='center')

lb2.pack(expand='yes')


f1.pack(expand=YES, fill=BOTH)
jan.mainloop()
'''


#Ex5 e Ex6
'''
def trocar(nomebotao):  
   nomebotao['fg'], nomebotao['bg'] = nomebotao['bg'],nomebotao['fg']

#######################
## INTERFACE GRÁFICA ##
from tkinter import *
jan = Tk()
jan.title("Botões")
jan.iconbitmap("lion.ico")
ljan, ajan = 400, 300
posx = jan.winfo_screenwidth()//2 - ljan//2 #metade ecra larg - metade janela larg 
posy = jan.winfo_screenheight()//2 - ajan//2 #metade ecra alt - metade janela alt
jan.geometry(f"{ljan}x{ajan}+{posx}+{posy}") #posicionar no ecra1 - resolução ecra1
f1=Frame(jan)
f2=Frame(jan)


#Criar botões na F1
bred = Button(f1, text = 'RED', fg = 'RED',
              width=7, bd=5, anchor = W, command=lambda:trocar(bred))
bblue = Button(f1, text = 'BLUE', fg = 'blue',
              width=7, bd=5, command=lambda:trocar(bblue))
bpink = Button(f1, text = 'PINK', fg = 'pink',
              width=7, bd=5, command=lambda:trocar(bpink))

bred.pack(side='left')
bblue.pack(side='left')
bpink.pack(side='left')

#Criar botões na F2
bgreen = Button(f2, text = 'GREEN', fg = '#0F0',
              width=7, bd=5, command=trocaverde)

bgreen.pack(side='left')

f1.pack()
f2.pack()
jan.mainloop()
'''

#Ex7

#######################
## INTERFACE GRÁFICA ##
from tkinter import *
jan = Tk()
jan.title("Esticar linhas e colunas com GRID")
jan.iconbitmap("lion.ico")
ljan, ajan = 400, 300
posx = jan.winfo_screenwidth()//2 - ljan//2 #metade ecra larg - metade janela larg 
posy = jan.winfo_screenheight()//2 - ajan//2 #metade ecra alt - metade janela alt
jan.geometry(f"{ljan}x{ajan}+{posx}+{posy}") #posicionar no ecra1 - resolução ecra1

l1 = Label(jan, text='Label 1',width=20,
           fg = 'white', bg='red')
l2 = Label(jan, text='Label 2', width=20,
           fg = 'white', bg='green')
l3 = Label(jan, text='Label 3', width=20,
           fg = 'white', bg='blue')
l4 = Label(jan, text='Label 4', width=20,
           fg = 'white', bg='brown')
l5 = Label(jan, text='Label 5', width=20,
           fg = 'white', bg='Lightblue')
l6 = Label(jan, text='Label 6', width=20,
           fg = 'white', bg='orange')
l7 = Label(jan, text='Label 7', width=20,
           fg = 'white', bg='Lightgreen')

l1.grid(row=0 , column=0, rowspan=2,sticky='ns')
l2.grid(row=0 , column=1 )
l3.grid(row=0 , column=2 )
l4.grid(row=1 , column=1, columnspan=2,sticky='we')
l5.grid(row=2 , column=0, columnspan=2,stick='we')
l6.grid(row=2 , column=2, rowspan=2,stick='ns')
l7.grid(row=3 , column=0, columnspan=2,stick='we')


jan.mainloop()








