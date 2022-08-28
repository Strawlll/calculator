from tkinter import *
from style import *
import math

root = Tk()
# User Interface Widget Creation
root.geometry('720x480')
root.title('Calculator')

number_frames = Frame(root, bg='#000000')
number_frames.pack(side=LEFT, expand=YES, fill=BOTH)

result_frame = Frame(root, bg='#000000')
result_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

result_screen = Label(result_frame, text='', **result_screen_style)
result_screen.pack()

numbers = list(range(1, 10, 1))
for num in numbers:
    btn_num = Button(number_frames, text=num, **button_style)
    if num % 3 != 0:
        btn_num.grid(row=math.ceil(num / 3), column=num % 3)
    else:
        btn_num.grid(column=3, row=math.ceil(num / 3))

btn_num_0 = Button(number_frames, text=0, **button_style)
btn_num_0.grid(column=1, row=4)

btn_plus = Button(number_frames, text='+', **button_style)
btn_plus.grid(column=4, row=1)

btn_subtract = Button(number_frames, text='-', **button_style)
btn_subtract.grid(column=4, row=2)

btn_multiply = Button(number_frames, text='*', **button_style)
btn_multiply.grid(column=4, row=3)

btn_divide = Button(number_frames, text='/', **button_style)
btn_divide.grid(column=4, row=4)

btn_equal = Button(number_frames, text='=', **button_style)
btn_equal.grid(column=2, row=4)

btn_clean = Button(number_frames, text='C', **button_style)
btn_clean.grid(column=3, row=4)


# Functionality:
def update_result_screen(clicked_button):
    current_text = str(result_screen.cget('text'))
    updated_text = current_text + str(clicked_button.cget('text'))
    result_screen.configure(text=updated_text)


for widget in number_frames.winfo_children():
    widget_text = widget.cget('text')
    if type(widget_text) == int or widget_text in ['+', '-', '*', '/']:
        widget.configure(command= lambda widget=widget: update_result_screen(widget))


def clean_screen():
    result_screen.configure(text='')


btn_clean.configure(command=clean_screen)


def calculation():
    screen_text = result_screen.cget('text')
    result_screen.configure(text=eval(screen_text))


btn_equal.configure(command=calculation)
root.mainloop()
