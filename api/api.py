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


@app.route('/api/systeminfo')
def get_current_time():
    return {'systime': time.time(),
            'machine': platform.machine(),
            'version': platform.version(),
            'platform': platform.platform(),
            'system': platform.system(),
            'processor': platform.processor()}

## LED Routes
@app.route('/api/red-on')
def red_on():
    redLED.on()
    return { 'message': "Red LED on" }

@app.route('/api/red-off')
def red_off():
    redLED.off()
    return { 'message': "Red LED off" }

@app.route('/api/yellow-on')
def yellow_on():
    yellowLED.on()
    return { 'message': "Yellow LED on" }

@app.route('/api/yellow-off')
def yellow_off():
    yellowLED.off()
    return { 'message': "Yellow LED off" }

@app.route('/api/green-on')
def green_on():
    greenLED.on()
    return { 'message': "Green LED on" }

@app.route('/api/green-off')
def green_off():
    greenLED.off()
    return { 'message': "Green LED off" }

@app.route('/api/blue-on')
def blue_on():
    blueLED.on()
    return { 'message': "Blue LED on" }

@app.route('/api/blue-off')
def blue_off():
    blueLED.off()
    return { 'message': "Blue LED off" }