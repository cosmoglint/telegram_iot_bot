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
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'on':
       bot.sendMessage(chat_id, command)
       GPIO.output(pin,GPIO.HIGH)
       #on(11)
    elif command == 'off':
       bot.sendMessage(chat_id, command)
       GPIO.output(pin,GPIO.LOW)
       #off(11)

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
