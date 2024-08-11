import time
import platform
from flask import Flask
from gpiozero import LED, Buzzer
from time import sleep

# Setup gpio pins
redLED = LED(13)
yellowLED = LED(19)
greenLED = LED(26)
blueLED = LED(21)

app = Flask(__name__)


@app.route('/systeminfo')
def get_current_time():
    return {'systime': time.time(),
            'machine': platform.machine(),
            'version': platform.version(),
            'platform': platform.platform(),
            'system': platform.system(),
            'processor': platform.processor()}

## LED Routes
@app.route('/red-on')
def red_on():
    redLED.on()
    return { 'message': "Red LED on" }

@app.route('/red-off')
def red_off():
    redLED.off()
    return { 'message': "Red LED off" }

@app.route('/yellow-on')
def yellow_on():
    yellowLED.on()
    return { 'message': "Yellow LED on" }

@app.route('/yellow-off')
def yellow_off():
    yellowLED.off()
    return { 'message': "Yellow LED off" }

@app.route('/green-on')
def green_on():
    greenLED.on()
    return { 'message': "Green LED on" }

@app.route('/green-off')
def green_off():
    greenLED.off()
    return { 'message': "Green LED off" }

@app.route('/blue-on')
def blue_on():
    blueLED.on()
    return { 'message': "Blue LED on" }

@app.route('/blue-off')
def blue_off():
    blueLED.off()
    return { 'message': "Blue LED off" }