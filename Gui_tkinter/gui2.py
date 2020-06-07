Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> GUI = Tk()
>>> GUI.geometry('500x300')
''
>>> B1 = ttk.Button(GUI,text='Hello')
>>> B1.place(x=100,y=100)
>>> L1 = ttk.Label(GUI,text='ข้อความจะโชว์ตำแหน่งนี้')
>>> L1.pack()
>>> 
>>> result = StringVar()
>>> L2 = ttk.Label(GUI,textvariable=result)
>>> L2.pack(pady=20)
>>> result.set('---------')
>>> result.set('HELLO KITTY')
>>> B2 = ttk.Button(GUI,text='สวัสดี')
>>> B2.place(x=200,y=100)
>>> def Hello():
	result.set('Hello')

	
>>> def Sawatdee():
	result.set('สวัสดี')

	
>>> B1.configure(command=Hello)
>>> B2.configure(command=Sawatdee)
>>> def Hello():
	result.set('ปลาแซลม่อน 20 บาท')

	
>>> B1.configure(command=Hello)
>>> B1.configure(text='ปลาแซลม่อน')
>>> def Sawatdee():
	result.set('ปลากระพง 50 บาท')

	
>>> B2.configure(command=Sawatdee)
>>> B2.configure(text='ปลากระพง')
>>> 