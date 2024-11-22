import tkinter

screen=tkinter.Tk()
screen.geometry("800x600")
screen.title("BASICS")

label=tkinter.Label(screen,text="Hi!!!")
label.pack()

text=tkinter.Text(screen,width=20,height=5)
text.pack()

button=tkinter.Button(screen,text="hello")
button.pack()

entry=tkinter.Entry(screen)
entry.pack()

screen.mainloop()