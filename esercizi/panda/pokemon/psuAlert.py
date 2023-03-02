import psutil
from tkinter import messagebox

cont=0
while True:
    battery=psutil.sensors_battery()
    print(battery.percent)
    if battery.percent > 96.4 and battery.power_plugged:
        if cont==0:
            messagebox.showinfo("ATTENZIONE","Scollegare il cavo di alimantazione")
            cont=1
    if battery.power_plugged==False:
        cont=0