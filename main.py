import pyaudio
import wave

def record_audio(output_file, record_seconds):
    chunk = 1024  # Record in chunks of 1024 samples
    format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    rate = 44100  # Record at 44100 samples per second

    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

record_audio("output.wav", 5)
