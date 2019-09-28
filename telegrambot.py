import sys
import time
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
# set up GPIO output channel
GPIO.setup(18, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    if chat_id == "@Odddoodle":
        command = msg['text']
        print('Got command: %s' % command)

        if command == 'off' or command == 'Off' or command == 'OFF':
            #bot.sendMessage(chat_id,"turning" + command)
            bot.sendMessage(chat_id,"turning On")
            GPIO.output(18,GPIO.HIGH)
            #on(11)
        elif command == 'on' or command == 'On' or command == 'ON':
            bot.sendMessage(chat_id,"turning Off")
            GPIO.output(18,GPIO.LOW)
            #off(11)
        else:
            bot.sendMessage(chat_id,"sorry cont do nothin")
    else:
        print("unauthorized!")

bot = telepot.Bot('903555004:AAEMh0BWCVbIjh2pv-yPWDC7sjo3vFZdpRI')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()

    except:
        print('Other error or exception occured!')
        GPIO.cleanup()
