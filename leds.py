#importamos los paquetes Tiempo, telepot (Telegram Bot) y RPi.GPIO
import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

#definimos los puertos GPIO a utilizar y les atribuímos un nombre como en Arduino.
white = 26
yellow = 19
red = 13
green = 6

now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
 
#LED White
#Estructura: GPIO.setup(puerto, GPIO.(entrada o salida))
GPIO.setup(white, GPIO.OUT)
GPIO.output(white, 0) #Off initially
#LED Yellow
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0) #Off initially
 #LED Red
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0) #Off initially
#LED green
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0) #Off initially

#definimos estructura de mensaje vía Telegram
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if 'on' in command:
        message = "Turned on "
        if 'white' in command:
            message = message + "white "
            GPIO.output(white, 1)
        if 'yellow' in command:
            message = message + "yellow "
            GPIO.output(yellow, 1)
        if 'red' in command:
            message = message + "red "
            GPIO.output(red, 1)
        if 'green' in command:
            message = message + "green "
            GPIO.output(green, 1)
        if 'all' in command:
            message = message + "all "
            GPIO.output(white, 1)
            GPIO.output(yellow, 1)
            GPIO.output(red, 1)
            GPIO.output(green, 1)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
        message = "Turned off "
        if 'white' in command:
            message = message + "white "
            GPIO.output(white, 0)
        if 'yellow' in command:
            message = message + "yellow "
            GPIO.output(yellow, 0)
        if 'red' in command:
            message = message + "red "
            GPIO.output(red, 0)
        if 'green' in command:
            message = message + "green "
            GPIO.output(green, 0)
        if 'all' in command:
            message = message + "all "
            GPIO.output(white, 0)
            GPIO.output(yellow, 0)
            GPIO.output(red, 0)
            GPIO.output(green, 0)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)

telegram_bot = telepot.Bot('INSERTAR_TOKEN_ID')

MessageLoop(telegram_bot, action).run_as_thread()

while 1:
    time.sleep(10)
