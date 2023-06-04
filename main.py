#Задание 1 Дедюхин Вячеслав 44 22 120
# from sys import argv
# import math
# script, x = argv
# x=int(x)
# if x <= 1.2:
#     y = (math.cos(math.pi * x))**2
# else:
#     y = (math.abs(math.ln(x+0.2)))**0.5
# print("y=",y)


#Задание 3 Дедюхин Вячеслав 44 22 120
import tkinter as tk
import math
window  = tk.Tk()
def schot(*args):
    f = "задано число {}".format(chislo.get())
    frame1.configure(text=f)
    x=int(chislo.get())
    if x <= 1.2:
        y = (math.cos(math.pi * x)) ** 2
    else:
        y = (abs(math.log((x + 0.2),math.e))) ** 0.5
    f = ('y =', y)
    frame2.configure(text=f)
frame1=tk.Label(window,text='Введите X')
chislo=tk.Entry(window,width=50)
frame2=tk.Label(window)
frame1.pack()
chislo.pack()
frame2.pack()
window.bind('<Return>',schot)
window.mainloop()
