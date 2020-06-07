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
    

B1 = ttk.Button(GUI,text='ENG',command=English)
B1.pack(ipadx=20,ipady=10)

B2 = ttk.Button(GUI,text='ไทย',command=Thai)
B2.pack(ipadx=20,ipady=10)

GUI.mainloop()
