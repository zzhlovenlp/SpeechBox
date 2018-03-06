import wave, pyaudio, time

class DataRecorder:

	def __init__(self, save_folder, recording_length):
		self.save_folder = save_folder
		self.recording_length = recording_length
		## Default settings
		self.chunk_size = 1024
		self.channels = 2
		self.rate = 44100
		self.format = pyaudio.paInt16

	def start_recording(self):
		recorder = pyaudio.PyAudio()
		data_stream = recorder.open(format=self.format, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk_size)

		chunks = []
		for i in range(0, int(self.rate / self.chunk_size * self.recording_length)):
			data_chunk = stream.read(self.chunk_size)
			chunks.append(data_chunk)

		data_stream.stop_stream()
		data_strea.close()
		recorder.terminate()
		sample_size = recorder.get_sample_size(self.format)
		self.save_recording(chunks, sample_size)

	def save_recording(self, chunks, sample_size):
		filename = self.generate_filename
		with wave.open(self.save_folder + "/" + filename) as wave_file:
			wave_file.setnchannels(self.channels)
			wave_file.setsampwidth(sample_size)
			wave_file.setframerate(self.rate)
			wave_file.writeframes(b''.join(chunks))

	#	wave_file = wave.open(self.save_folder + "/" + filename)


	def generate_filename(self):
		curr_time = time.strftime("%Y:%m:%d::%H:%M:%S")
		return str(curr_time) + ".wav"


## Testing

if __name__ == "__main__":
	r = DataRecorder("test", 1)
	r.start_recording()
