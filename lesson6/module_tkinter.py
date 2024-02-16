import tkinter

app = tkinter.Tk()


x = 0.0
app.geometry("250x200")
label = tkinter.Label(app, text=x)
label2 = tkinter.Label(app, text='')
field = tkinter.Entry(app, width=20)


def update_button():
    global x
    x += 1
    label.configure(text=x)
    label2.configure(text=f"--- {field.get()} ---")


button = tkinter.Button(app, anchor="center", text="Нажми", command=update_button)


label.grid(column=0, row=0)
button.grid(column=1, row=0)
field.grid(column=2, row=0)
label2.grid(column=0, row=1)


if __name__ == '__main__':
    app.mainloop()
