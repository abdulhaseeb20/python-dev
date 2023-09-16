
from tkinter import *
import datetime
import time
import winsound


def setAlarm(alarm_timer):
    while True:
        time.sleep(1)
        curr_time = datetime.datetime.now()
        curr = curr_time.strftime("%H:%M:%S")
        curr_date = curr_time.strftime("%d/%m/%Y")
        print("Date is: ", curr_date)
        print(curr)
        if curr == alarm_timer:
             print("Wake up now")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

def presentTime():
    alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    setAlarm(alarm_timer)


clock = Tk()

clock.title("Alarm Clock GUI")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="green",bg="#ffffec",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Set your alarm",fg="green",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "#ffd2b0",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "#ffd2b0",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "#ffd2b0",width = 15).place(x=200,y=30)

submit = Button(clock,text = "Set Alarm",fg="black",width = 10,command = presentTime).place(x =110,y=70)
clock.mainloop()
