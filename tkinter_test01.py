from tkinter import *
def on_click():
    button['text'] = 'It is changed.'
root = Tk(className='aaa')
button = Button(root)
button['text'] = 'change it'
button['command'] = on_click    #事件关联函数
button.pack()
root.mainloop()
