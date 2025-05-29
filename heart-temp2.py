import tkinter
import RPi.GPIO as GPIO
import max30102
import hrcalc
import os
import glob
import time
from datetime import datetime
import pytz

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)

# Temperature sensor setup
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

# Define the temperature range
TEMP_MIN = 28.0
TEMP_MAX = 39.10

# Timezone setup
ist = pytz.timezone('Asia/Kolkata')

# Create a class for the Tkinter app
class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Display Labels
        self.TitleLbl = tkinter.Label(window, text="MAX30102 WITH RASPBERRY PI", font=("Arial", 20, 'bold'), fg="black", relief="raised", borderwidth=2)
        self.TitleLbl.pack(anchor=tkinter.CENTER, expand=True)

        self.DevLabel = tkinter.Label(window, text="DEVELOPER: RAVIVARMAN RAJENDIRAN", font=("Arial", 15, 'bold'), fg="dark orchid", relief="raised", borderwidth=1)
        self.DevLabel.pack(anchor=tkinter.CENTER, expand=True)

        self.PulseLbl = tkinter.Label(window, text="[Heart Pulse Rate: ]", font=("Arial", 20), fg="red", relief="ridge", borderwidth=2)
        self.PulseLbl.pack(anchor=tkinter.CENTER, expand=True)

        self.SPO2Lbl = tkinter.Label(window, text="[Oxygen Saturation: ]", font=("Arial", 20), fg="blue", relief="ridge", borderwidth=2)
        self.SPO2Lbl.pack(anchor=tkinter.CENTER, expand=True)

        self.TEMPCLbl = tkinter.Label(window, text="[Temperature in C: ]", font=("Arial", 20), fg="green", relief="ridge", borderwidth=2)
        self.TEMPCLbl.pack(anchor=tkinter.CENTER, expand=True)

        self.TEMPFLbl = tkinter.Label(window, text="[Temperature in F: ]", font=("Arial", 20), fg="green", relief="ridge", borderwidth=2)
        self.TEMPFLbl.pack(anchor=tkinter.CENTER, expand=True)

        # Initialize MAX30102 sensor
        self.m = max30102.MAX30102()
        self.hr2 = 0
        self.sp2 = 0

        # Set update interval
        self.delay = 1000  # 1 second

        # Start update loop
        self.update()

    def update(self):
        # Read sensor data
        red, ir = self.m.read_sequential()
        hr, hrb, sp, spb = hrcalc.calc_hr_and_spo2(ir, red)

        # Update Heart Rate and SPO2 labels
        if hrb and hr != -999 and hr < 105:
            self.hr2 = int(hr)
            self.PulseLbl['text'] = "[Heart Pulse Rate: " + str(self.hr2) + " bpm]"
        if spb and sp != -999 and sp < 100:
            self.sp2 = int(sp)
            self.SPO2Lbl['text'] = "[Oxygen Saturation: " + str(self.sp2) + "%]"

        # Read temperature
        temp_c, temp_f = read_temp()
        self.TEMPCLbl['text'] = "[Temperature in C: " + str(temp_c) + "]"
        self.TEMPFLbl['text'] = "[Temperature in F: " + str(temp_f) + "]"

        # Check for abnormal temperature range
        if temp_c < TEMP_MIN or temp_c > TEMP_MAX:
            print(f"\033[1;31mWarning: Temperature is abnormal!\033[0m")

        # Schedule the next update
        self.window.after(self.delay, self.update)


# Run the application
root = tkinter.Tk()
root.geometry("+{}+{}".format(250, 50))
app = App(root, "PULSE OXIMETER")
root.mainloop()
