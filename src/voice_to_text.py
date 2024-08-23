import sys
import whisper
import sounddevice as sd
import numpy as np
import wavio
import os
import webrtcvad

# Frame generation for VAD
def frame_generator(frame_duration_ms, audio, sample_rate):
    n = int(sample_rate * (frame_duration_ms / 1000.0) * 2)  # 2 bytes per sample for 16-bit audio
    offset = 0
    while offset + n < len(audio):
        yield audio[offset:offset + n]
        offset += n

# Voice Activity Detection function
def vad_decision(audio_data, sample_rate):
    vad = webrtcvad.Vad()
    vad.set_mode(1)  # 0 is the least aggressive, 3 is the most aggressive
    frames = frame_generator(20, audio_data, sample_rate)
    speech_frames = [vad.is_speech(frame, sample_rate) for frame in frames]
    return any(speech_frames)

# Transcribe audio from the microphone
def transcribe_from_microphone(model, duration=5.0, samplerate=16000):
    print("Recording...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")
    
    # Flatten the numpy array to bytes
    audio_bytes = recording.flatten().tobytes()

    # Apply VAD to check for speech presence
    if vad_decision(audio_bytes, samplerate):
        # Save the recording to a temporary file
        temp_filename = "temp_audio.wav"
        wavio.write(temp_filename, recording, samplerate, sampwidth=2)
        
        # Transcribe the temporary audio file
        result = model.transcribe(temp_filename, language="en")
        
        # Remove the temporary file after transcription
        os.remove(temp_filename)
        
        return result["text"]
    else:
        return "No speech detected."

# Transcribe audio from a file
def voice_to_text_from_file(model, audio_file):
    result = model.transcribe(audio_file, language="en")
    return result["text"]

if __name__ == "__main__":
    # Load the Whisper model once
    model = whisper.load_model("base.en")
    
    option = input("Select input method (1 for microphone, 2 for audio file): ")

    if option == "1":
        duration = float(input("Enter duration of recording in seconds: "))
        text = transcribe_from_microphone(model, duration=duration)
    elif option == "2":
        audio_file = input("Enter the path to the audio file: ")
        text = voice_to_text_from_file(model, audio_file)
    else:
        print("Invalid option selected.")
        text = None

    if text:
        print("Transcription: ", text)
