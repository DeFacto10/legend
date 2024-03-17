import json, pyaudio
#from multiprocessing import Process
from vosk import Model, KaldiRecognizer
from threading import Thread
from gpt import gpt
wait_answer = True

def speech_to_text():
    # voice_sheairng
    model = Model("voice_models/vosk-model-small-ru-0.4")
    rec = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)



    def listen():
        answer = json.loads(rec.Result())
        if answer['text']:
            print(answer['text'])
            if "наташа" in answer['text']:
                wait_answer = False
                gpt(answer['text'])
                gpt(answer['text'])





    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0) and wait_answer == True:
            voice = Thread(target=listen, args=())
            voice.start()
            voice.join()

if __name__ == "__main__":
    speech_to_text()