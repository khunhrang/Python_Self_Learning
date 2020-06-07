Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> GUI = Tk()
>>> GUI.geometry('500x300')
''
>>> B1 = Button(GUI,text='Hello')
>>> B1.pack()
>>> from tkinter import ttk
>>> B2 = ttk.Button(GUI,text='สวัสดี')
>>> B2.pack()
>>> def HelloWorld():
	print('Hello')

	
>>> B1.configure(command=HelloWorld)
>>> Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    Hello
NameError: name 'Hello' is not defined
>>> B1.place(x=200,=100)
SyntaxError: invalid syntax
>>> B1.place(x=200,y=100)
>>> B2.place(x=300,y=350)
>>> B2.place(x=300,y=200)
>>> 