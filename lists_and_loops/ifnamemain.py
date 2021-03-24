print(__name__)
import tkinter

my_tk = tkinter.Tk()
my_tk.title('Hello there')
my_tk.geometry('700x500')
my_tk.mainloop()  # this thing is a while loop hidden

# totally forbidden stuff
# on GL, Graphics don't work. you have a text shell only, there's no windows, graphics, anything like that.