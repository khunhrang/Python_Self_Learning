#flashcard.py

from tkinter import *
from tkinter import ttk
import random

GUI = Tk()
GUI.geometry('500x300')

v_eng = StringVar()
v_thai = StringVar()

L1 = ttk.Label(GUI,textvariable=v_eng,font=('Angsana New',30))
L1.pack(pady=10)

L2 = ttk.Label(GUI,textvariable=v_thai,font=('Angsana New',30))
L2.pack(pady=10)

vocab = {'cat':'แมว','dog':'สุนัข','KFC':'ไก่ทอด'}
vocabeng = list(vocab.keys())

def English():
    v_eng.set(random.choice(vocabeng))
    v_thai.set('')
    
def Thai():
    v_thai.set(vocab[v_eng.get()])

def Check():
    print('Check:', v_check.get())
    if v_check.get() == vocab[v_eng.get()]:
        v_score.set(int(v_score.get()) + 1)
        
v_check = StringVar()

E1 = ttk.Entry(GUI,textvariable=v_check,font=('Angsana New',20))
E1.pack(pady=10)
    
F1 = Frame(GUI)
F1.pack()


B1 = ttk.Button(F1,text='ENG',command=English)
B1.grid(row=0,column=0,ipadx=20,ipady=10)

B2 = ttk.Button(F1,text='ไทย',command=Thai)
B2.grid(row=0,column=1,ipadx=20,ipady=10)

B3 = ttk.Button(F1,text='เช็คความหมาย',command=Check)
B3.grid(row=0,column=1,ipadx=20,ipady=10)

v_score = StringVar()
v_score.set('0')

Score = ttk.Label(GUI,textvariable=v_score,font=('Angsana New',30),foreground='red')
Score.place(x=430,y=30)

GUI.mainloop()
