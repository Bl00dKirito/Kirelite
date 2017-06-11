import signal
import subprocess

from trigger import snowboydecoder
from core.profile.loader import loadProfile

data = loadProfile()
interrupted = False
subprocess.call(['python', 'query.py'])

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def activate():
    subprocess.call(['python', 'query.py'])

models = ['trigger/resources/kirelite.pmdl','trigger/resources/ki.pmdl']

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)

print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=activate,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
