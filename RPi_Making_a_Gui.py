"""
SIT210 - 5.2C RPi - Making a Gui
This program is simply about creating a program in python
which provides the user with three simple buttons for
activating three LEDs
Uses BCM rather than Board for GPIO, so pin number rather than GPIO number
"""

import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font
from gpiozero import LED

GPIO.setmode(GPIO.BCM)

# Device setup

red_led = LED(23)			# Red LED
green_led = LED(24)  		# Green LED
blue_led = LED(25)		  	# Blue LED

# GUI Setup
window = Tk()
window.title("Triple Button LED Toggle")
the_font = tkinter.font.Font(family='Gentium', size=12, weight="bold")

# Switch Functions
# Each switch function conducts a simple check to identify the LED state, then does the relevant actions

# For each function, the program will either turn off an led, or turn on the led and turn the others off
# It will also change the button text in the process
def red_led_switch():
    if red_led.is_lit:
        red_led.off()
        red_led_button["text"]="Turn on Red LED"
    else:
        red_led.on()
        red_led_button["text"]="Turn off Red LED"
        if green_led.is_lit:
            green_led.off()
            green_led_button["text"]="Turn on Green LED"
        if blue_led.is_lit:
            blue_led.off()
            blue_led_button["text"]="Turn on Blue LED"

def green_led_switch():
    if green_led.is_lit:
        green_led.off()
        green_led_button["text"]="Turn on Green LED"
    else:
        green_led.on()
        green_led_button["text"]="Turn off Green LED"
        if red_led.is_lit:
            red_led.off()
            red_led_button["text"]="Turn on Red LED"
        if blue_led.is_lit:
            blue_led.off()
            blue_led_button["text"]="Turn on Blue LED"

def blue_led_switch():
    if blue_led.is_lit:
        blue_led.off()
        blue_led_button["text"]="Turn on Blue LED"
    else:
        blue_led.on()
        blue_led_button["text"]="Turn off Blue LED"
        if red_led.is_lit:
            red_led.off()
            red_led_button["text"]="Turn on Red LED"
        if green_led.is_lit:
            green_led.off()
            green_led_button["text"]="Turn on Green LED"


# Close function to ensure the program finishes cleanly for the GPIO
def close_program():
    GPIO.cleanup()
    window.destroy()

# Button definitions
red_led_button = Button(window, text='Turn on Red LED', font=the_font, command=red_led_switch, bg='red', height=1, width=20)
red_led_button.grid(row=0, column=0)

green_led_button = Button(window, text='Turn on Green LED', font=the_font, command=green_led_switch, bg='green', height=1, width=20)
green_led_button.grid(row=0, column=1)

blue_led_button = Button(window, text='Turn on Blue LED', font=the_font, command=blue_led_switch, bg='blue', height=1, width=20)
blue_led_button.grid(row=0, column=2)

exitButton = Button(window, text='Exit Program', font=the_font, command=close_program, bg='gray', height=1, width=10)
exitButton.grid(row=1, column=1)

# Protocol Events - Clean window closure - Capture the pressing of the X on the window

window.protocol("WM_DELETE_WINDOW", close_program)

window.mainloop() # Maintain Window Loop