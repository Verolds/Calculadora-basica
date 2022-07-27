from tkinter import *
import tkinter.ttk as ttk

ventana = Tk()

#CAMBIAR NOMBRE DE LA VENTANA
ventana.title("Calculadora") 
#CAMBIAR ICONO DE LA VENTANA
icono= PhotoImage(file='calcu.png')
ventana.iconphoto(True, icono)
#POSICION
ventana.geometry('+400+200')
#CAMBIAR ESTILO DEL BOTON
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = 'black', foreground = "#00ff00", borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active',"#B5B2B2")])

expr = ''
text = StringVar()

def click(num):
    global expr
    expr += str(num)
    text.set(expr)
#BORRAR TODOS LOS ELEMENTOS 
def clr():
    global expr
    expr = ''
    entry.delete(0,END)
#BORRAR UN ELEMENTO
def backspace():
    global expr
    expr = expr[:-1]
    entry.delete(len(entry.get())-1,END)
#REALIZAR LA OPERACION
def igual():
    global expr
    ttl = str(eval(expr))
    text.set(ttl)
    expr = ttl

#FILA 0 'PANTALLA'
entry = Entry(ventana,
            font =("Arial", 20),
            fg="#00ff00",
            bg="black",
            justify='right',
            highlightthickness=1,
            highlightcolor= "#B5B2B2",
            textvariable= text )   
entry.grid(row=0, columnspan=5, sticky='nsew')
#FILA 1
boton_7 = ttk.Button(ventana, text='7', command=lambda:click(7))
boton_7.grid(row=1, column=0)
boton_8 = ttk.Button(ventana, text='8', command=lambda:click(8))
boton_8.grid(row=1, column=1)
boton_9 = ttk.Button(ventana, text='9', command=lambda:click(9))
boton_9.grid(row=1, column=2)
boton_del = ttk.Button(ventana, text='DEL', command=backspace)
boton_del.grid(row=1, column=3)
boton_c = ttk.Button(ventana, text='AC', command=clr)
boton_c.grid(row=1, column=4)
#FILA 2
boton_4 = ttk.Button(ventana, text='4', command=lambda:click(4))
boton_4.grid(row=2, column=0)
boton_5 = ttk.Button(ventana, text='5', command=lambda:click(5) )
boton_5.grid(row=2, column=1)
boton_6 = ttk.Button(ventana, text='6', command=lambda:click(6) )
boton_6.grid(row=2, column=2)
boton_p2 = ttk.Button(ventana, text='(', command=lambda:click('('))
boton_p2.grid(row=2, column=3)
boton_p2 = ttk.Button(ventana, text=')', command=lambda:click(')'))
boton_p2.grid(row=2, column=4)
#FILA 3
boton_1 = ttk.Button(ventana, text='1', command=lambda:click(1))
boton_1.grid(row=3, column=0)
boton_2 = ttk.Button(ventana, text='2', command=lambda:click(2))
boton_2.grid(row=3, column=1)
boton_3 = ttk.Button(ventana, text='3', command=lambda:click(3))
boton_3.grid(row=3, column=2)
boton_multi = ttk.Button(ventana, text='x', command=lambda:click('*'))
boton_multi.grid(row=3, column=3)
boton_div = ttk.Button(ventana, text='/', command=lambda:click('/'))
boton_div.grid(row=3, column=4)
#FILA 4
boton_0 = ttk.Button(ventana, text='0', command=lambda:click(0))
boton_0.grid(row=4, column=0)
boton_p = ttk.Button(ventana, text='.', command=lambda:click('.'))
boton_p.grid(row=4, column=1)
boton_suma = ttk.Button(ventana, text='+', command=lambda:click('+'))
boton_suma.grid(row=4, column=2)
boton_resta = ttk.Button(ventana, text='-', command=lambda:click('-'))
boton_resta.grid(row=4, column=3)
boton_suma = ttk.Button(ventana, text='^', command=lambda:click('**'))
boton_suma.grid(row=4, column=4)
#FILA 5
boton_i = ttk.Button(ventana, text='=', command=igual)
boton_i.grid(row=5, columnspan=5, sticky='nsew')

ventana.mainloop()