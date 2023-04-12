from tkinter.ttk import *
from tkinter import *
from threading import *
from pygame import mixer
import os
from datetime import datetime
from time import sleep

from PIL import ImageTk, Image

#color
black = "#000000"
baby_blue = "#b3cde0"
blue = "#0000FF"
blue_velvet	= "#162252"
light_gray = "#D3D3D3"
baby_gray = "#EFECEC"
gray = "#333333"
blue_gray = "#36454f"

#Window tkinter
win = Tk()
win.title("Alarm Clock!!")
win.geometry('380x310')
win.configure(bg = "#ffffff")

#frames
line = Frame(win, width=400, height=5, bg=blue_velvet)
line.grid(row=0, column=0)

body = Frame(win, width=400, height=400, bg=baby_gray)
body.grid(row=1, column=0)

#add Image
img = Image.open("alarm-clock-icon.png")
img.resize((130, 130))
img = ImageTk.PhotoImage(img)

app_image = Label(body, height=100, image= img, bg=baby_gray)
app_image.place(x = 250, y=20)

#add title
name = Label(body, text = "Alarm Clock", height=1, font=('Ivy 20 bold'), bg = baby_gray, fg = blue_velvet )
name.place(x=50, y=50)

#time 
#hour
hour = Label(body, text="hour", height=1, font="Ivy 15 bold", bg=light_gray, fg=blue_velvet )
hour.place(x=50, y = 140)

com_hour = Combobox(body, width=2, font=('arial 15'))
com_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
com_hour.current(0)
com_hour.place(x=50, y=180)

#minute
minute = Label(body, text="minute", height=1, font="Ivy 15 bold", bg=light_gray, fg=blue_velvet)
minute.place(x=120, y = 140)

com_minute = Combobox(body, width=2, font=('arial 15'))
com_minute['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
com_minute.current(0)
com_minute.place(x=120, y=180)

#second
second = Label(body, text="second", height=1, font="Ivy 15 bold", bg=light_gray, fg=blue_velvet )
second.place(x=210, y = 140)

com_second = Combobox(body, width=2, font=('arial 15'))
com_second['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
com_second.current(0)
com_second.place(x=210, y=180)

def alarmStart():
    t = Thread(target = alarm)
    t.start()
    
selected = IntVar()

def alarmStop():
    print("inactive alarm: ", selected.get())
    mixer.music.stop()
  


#button
button = Radiobutton(body, font=('arial 15 bold'), value=1, text= "Start", bg=baby_blue, command = alarmStart, variable=selected )
button.place(x=60, y = 230)



#the alarm sound

def sound():
    mixer.music.load("alarm-sound.mp3")
    mixer.music.play()
    selected.set(0)

    #button stop
    button2 = Radiobutton(body, font=('arial 15 bold'), value=2, text= "Stop", bg=baby_blue, command = alarmStop, variable=selected )
    button2.place(x=200, y = 230)

#function for alarm

def alarm():
    while True:
        control = selected.get()

        alarm_hour = com_hour.get()
        alarm_minute = com_minute.get()
        alarm_second = com_second.get()
        
        #current time
        now = datetime.now()
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        
        #check
        if control == 1:
            if alarm_hour == hour:
                if alarm_minute == minute:
                    if alarm_second == second:
                        #play sound
                        sound()
        sleep(1)


mixer.init()

win.mainloop()