from tkinter import *
window = Tk()
window.title('Tkinter window example')
c = Canvas(window, width=800, height=500, bg='lightblue')
c.create_text(400, 250, text='This is an example of a Tkinter window', fill='black')
c.pack()
