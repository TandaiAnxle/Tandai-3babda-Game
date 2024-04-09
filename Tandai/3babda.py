from tkinter import*


def click():
    print("You are Retarded")

window = Tk()

button = Button(window, text="Special Button",command=click, state=ACTIVE)
button.pack()
window.geometry("500x500")
window.title("TandaiProject")
window.config(background="grey")


window.mainloop()