import asyncio
from pyrogram import Client
import pyaudio
import wave
import numpy as np
from datetime import datetime
import os
import json

# Opening JSON file
f = open('secrets.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

print(data)

app = Client("RepRec", api_id=data["api_id"], api_hash=data["api_hash"])

def record_audio(threshold=10, silence_duration=1, sample_rate=48000, channels=1):
    """
    Records audio from the microphone when the volume exceeds a specified threshold,
    and stops recording after a specified duration of silence.
    """
    FORMAT = pyaudio.paInt16
    CHUNK = 1024
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=channels, rate=sample_rate, input=True, frames_per_buffer=CHUNK)
    print("Listening for audio...")
    frames = []
    silent_frames = 0
    recording = False

    while True:
        data = stream.read(CHUNK)
        volume_norm = np.linalg.norm(np.frombuffer(data, dtype=np.int16)) / CHUNK
        if volume_norm < threshold:
            if recording:
                silent_frames += 1
                if silent_frames > int(silence_duration * sample_rate / CHUNK):
                    print("Silence detected, stopping recording.")
                    break
        else:
            silent_frames = 0
            if not recording:
                print(f"Sound detected, starting recording... Volume: {volume_norm}")
                recording = True
        if recording:
            frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    timestamp = datetime.now()
    filename = f"{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.wav"
    wave_file = wave.open(filename, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(p.get_sample_size(FORMAT))
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()
    print(f"Audio saved as {filename}")

    return filename

async def send_audio(filename):
    chat_id = "-1002080755234"
    print("Sending audio...")
    await app.send_audio(chat_id, filename)
    os.remove(filename)
    print(f"File {filename} sent and removed.")

async def main():
    async with app:
        print("Bot connected. Starting audio monitoring and sending...")
        while True:
            filename = await asyncio.to_thread(record_audio)
            asyncio.create_task(send_audio(filename))

app.run(main())
