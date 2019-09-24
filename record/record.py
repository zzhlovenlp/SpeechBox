import pyaudio
import wave

CHUNK = 1024
#define the chunk
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100	
#define the bit rate	
RECORD_SECONDS = 5	
#set the recording time
WAVE_OUTPUT_FILENAME = "output.wav"


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
#open the data stream
				
print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
#start recording
print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()
#close the data stream

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
#close pyaudio