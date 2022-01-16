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

window.configure(background="black")
Label(window, text="Job Number:", fg="white", background="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)

job_entry = Entry(window, width=20, bg="white")
job_entry.grid(row=1, column=1, sticky=W)

button_start = tkinter.Button(text="Start", bd=3, bg="white", padx=25, pady=25, relief=GROOVE, command=start)
button_start.grid(row=2, column=0, sticky=E)

button_reset = tkinter.Button(text="Reset", bd=3, bg="white", padx=25, pady=25, relief=GROOVE, command=reset)
button_reset.grid(row=2, column=1, sticky=E)

button_stop = tkinter.Button(text="Stop", bd=3, bg="white", padx=25, pady=25, relief=GROOVE, command=stop_button)
button_stop.grid(row=4, column=0, sticky=E)

window.mainloop()
