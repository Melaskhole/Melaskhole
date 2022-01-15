import tkinter
from tkinter import *
import cv2
from pyzbar.pyzbar import decode
import pyautogui

data_perm = None
clock = True
stop = False


def start():
    global clock
    while clock:

        def reader():

            def screen():
                im = pyautogui.screenshot()
                im.save("SS1.png")

            screen()

            img = cv2.imread("SS1.png")
            global data_perm
            detect_barcode = decode(img)

            if not detect_barcode:
                pass
                print("no barcode")

            else:
                for barcode in decode(img):
                    mydata = barcode.data.decode("utf-8")
                    data_val = data_perm
                if mydata != data_val:
                    with open("Results.txt", "a") as f:
                        f.write(mydata)
                        f.write(",,")
                        data_perm = mydata
                        print(mydata)

        if stop is True:
            break

        reader()
        print(clock)
        #updates gui without needing threading
        window.update_idletasks()
        window.update()


def reset():
    global clock
    global stop
    stop = False
    clock = True


def stop_button():
    global stop
    global clock
    stop = True
    clock = False


window = Tk()
window.title("Barcode Scanner")
window.geometry("240x200")
window.minsize(240, 200)
window.maxsize(240, 200)
Start = PhotoImage(file="start.png")
Reset = PhotoImage(file="reset.png")
Stop = PhotoImage(file="Stop.png")
window.configure(background="black")
Label(window, text="Job Number:", fg="white", background="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)

job_entry = Entry(window, width=18, bg="grey")
job_entry.grid(row=1, column=1, sticky=W)

button1 = tkinter.Button(image=Start, bd=0, bg="black", command=start)
button1.grid(row=2, column=0, sticky=E)

button2 = tkinter.Button(image=Reset, bd=0, bg="black", command=reset)
button2.grid(row=2, column=1, sticky=E)

button3 = tkinter.Button(image=Stop, bd=0, bg="black", command=stop_button)
button3.grid(row=3, column=0, sticky=E)

window.mainloop()
