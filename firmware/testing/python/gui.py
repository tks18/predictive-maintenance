# run with python .\gui.py
# install: https://lawsie.github.io/guizero/
# change value of THRESHOLD to change pass-fail criteria (input a decimal value)
# change string "Pressure = " any other requirement(s)

from serial_read import serial_data_findbystring
from guizero import App, Text, Picture

THRESHOLD = 23.00

# Action you would like to perform
def value_update():
    value = serial_data_findbystring("Pressure = ")
    text.value = value
    print(value)
    if (value and value > THRESHOLD):
        text.text_color = "#00ff00" # green
        app.bg = "#009900"
        #picture.value = "pass-min.png"
    elif (value and value < THRESHOLD):
        text.text_color = "#ff3333" # red
        app.bg = "#990000"
        #picture.value = "fail-min.png"
    else: # no value
        text.text_color = "#121212"
        app.bg = "#121212"        

app = App("Swayatt Drishtigochar", bg = "#121212") # #121212: black

text = Text(app, text=value_update)
#picture = Picture(app)

text.repeat(100, value_update)  # Schedule call to every "n"ms(1s = 1000ms)

app.display()
