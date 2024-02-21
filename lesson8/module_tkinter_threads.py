import sys
import time
import tkinter
from threading import Thread

app = tkinter.Tk()


x = 0.0
app.geometry("250x200")
label = tkinter.Label(app, text=x)
label2 = tkinter.Label(app, text='')
field = tkinter.Entry(app, width=20)


def long_process():
    time.sleep(10)
    print("Процесс завершен")
    label2.configure(text=f"Процесс завершен")


def new_thread():
    t = Thread(target=long_process)
    t.start()


def update_button():
    global x
    x += 1
    new_thread()
    label.configure(text=x)
    label2.configure(text=f"--- {field.get()} ---")


button = tkinter.Button(app, anchor="center", text="Нажми", command=update_button)


label.grid(column=0, row=0)
button.grid(column=1, row=0)
field.grid(column=2, row=0)
label2.grid(column=0, row=1)


if __name__ == '__main__':
    app.mainloop()
