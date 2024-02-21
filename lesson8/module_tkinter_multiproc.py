import sys
import time
import tkinter
import multiprocessing as mp

app = tkinter.Tk()


x = 0.0
app.geometry("250x200")
label = tkinter.Label(app, text=x)
label2 = tkinter.Label(app, text='')
field = tkinter.Entry(app, width=20)


class LongProcess(mp.Process):
    def __init__(self, ):
        mp.Process.__init__(self)
        self.exit = mp.Event()

    def run(self):
        while not self.exit.is_set():
            pass
        print("Exit")

    def shutdown(self):
        print("shutdown")
        self.exit.set()


def long_process():
    p = LongProcess()
    p.start()
    time.sleep(10)
    p.shutdown()
    print("Процесс завершен")
    sys.exit(0)


def update_button():
    global x
    x += 1
    long_process()
    # p = mp.Process(target=long_process)
    # p.start()
    # if not p.is_alive():
    #     label2.configure(text="Процесс завершен")

    label.configure(text=x)
    label2.configure(text=f"--- {field.get()} ---")


button = tkinter.Button(app, anchor="center", text="Нажми", command=update_button)


label.grid(column=0, row=0)
button.grid(column=1, row=0)
field.grid(column=2, row=0)
label2.grid(column=0, row=1)


if __name__ == '__main__':
    app.mainloop()
