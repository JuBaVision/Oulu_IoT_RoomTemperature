import time
from sense_hat import SenseHat
import socket
sense = SenseHat()
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

HOST = '172.16.17.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        temp = str(round(sense.get_temperature_from_humidity(), 2))
        s.sendall(str.encode(temp))
        sense.clear()
        temp_flt = float(temp)
        if (temp_flt > 22):
            sense.show_message(temp,scroll_speed=0.05, text_colour=white, back_colour=red)
        elif (temp_flt < 20):
            sense.show_message(temp,scroll_speed=0.05, text_colour=white, back_colour=blue)
        else:
            sense.show_message(temp,scroll_speed=0.05, text_colour=white)
        time.sleep(1)
