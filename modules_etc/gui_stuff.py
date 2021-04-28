"""
    The end of the semester:

        Everything I'm about to say now is not for project 3, or the final, it's for your future life,
            enjoyment, anything but this class.
        Forbidden for use on P2, P3, Final.

    GUI examples
    Flask <-- web development
"""

import tkinter
from tkinter.messagebox import showinfo, showerror, showwarning


# what is tkinter?
# it's the Graphical User Interface package that's provided with python.

# CLI = Command line interface (GL, linux command line, windows powershell, WSL, cmd) past: everybody uses CLI's what's a GUI?
# GUI = Graphical User Interface = present: GUIs are the only interfaces with computers, what is a CLI?
# True Programmers you are now: Behind every gui* there is a CLI  *probably.
# CLI's allow you access under the hood in general

def press_button():
    print('You have pressed the button')
    showinfo("First GUI Tutorial", the_string.get())
    # StringVar.get() gets us the underlying str
    # StringVar mutable version of a string.
    # python strings are "immutable"


def add_components(main_window):
    # every window, every button, every edit box, menu bar, is a "window"
    # main window doesn't have a parent.
    # text, row, column are all called "keyword arguments"
    my_button = tkinter.Button(main_window, text="Press Me", command=press_button)
    my_button.grid(row=0, column=0)

    # i want a text box.  give me that
    my_string_var = tkinter.StringVar(main_window)
    # textvariable links the StringVar to the Entry
    # width = 20 just makes sure that we have 20 characters of width so we can type things.
    your_text_box = tkinter.Entry(main_window, textvariable=my_string_var, width=20, bg='black', fg='white')
    your_text_box.grid(row=1, column=0)
    return my_string_var


if __name__ == '__main__':
    # tk meaningless garbage set of characters really

    my_window = tkinter.Tk()
    # this will change the title.
    my_window.title('Python GUI Tutorial')
    # string width"x"height
    my_window.geometry('800x400')
    """
        while my window isn't destroyed:
            message = get_messages_for_my_window()
                Click event, Typing, Resizing, No event.  
            process_message_for_my_windows(message)
    """

    the_string = add_components(my_window)
    my_window.mainloop()

    print('We are at the end.')
