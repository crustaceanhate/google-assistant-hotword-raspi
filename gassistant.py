import snowboydecoder
import sys
import signal
import time
import logging
import threading

from assistant import Assistant
from motorcontroller import MotorController

class TalkThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(TalkThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    
interrupted = False

logging.basicConfig()
logger = logging.getLogger("daemon")
logger.setLevel(logging.DEBUG)

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def response_callback(talkthread, text):
    if talkthread.isAlive():
        talkthread.stop()
        talkthread.join()
    
    
    
model = sys.argv[1]
# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

motorcontroller = MotorController(mouth_open_pin=1,mouth_close_pin=2,body_towards_pin=4,body_away_pin=4)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5, audio_gain=10)
assistant = Assistant(language_code="en-AU",
                      device_model_id="bmbb-assistant-model-id",
                      device_id="bmbb-assistant")


def detect_callback():
    detector.terminate()
    snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)
    assistant.assist()
    snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)
    detector.start(detected_callback=detect_callback, interrupt_check=interrupt_callback, sleep_time=0.03)


print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detect_callback,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
