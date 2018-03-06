from pynput import keyboard
import time

from data_recorder import DataRecorder
from server.network.local import Networking

class SpeechBoxUI(object):

    def __init__(self):
        self.networking=Networking('http://127.0.0.1:5000/')
        self.recorder=DataRecorder()
        pass


    def send_audio(self, file_name):
        """ Calls networking module to send the audio file to the server. """
        print("sending audio", file_name)
        self.networking.send_order(file_name)



    def on_button_press(self, key):
        """ Define here what happens when the button is pressed (right now reacts to keyboard space) """
        if key==keyboard.Key.space:
            print("recording")
            file_name=self.recorder.start_recording()
            self.send_audio(file_name)

    def start(self):

        # create keyboard listener
        listener = keyboard.Listener(on_press=self.on_button_press)
        listener.start()
        while True:
            time.sleep(0.1) # delay
            # TODO: read speech-to-text results


if __name__=="__main__":

    ui=SpeechBoxUI()
    ui.start()
