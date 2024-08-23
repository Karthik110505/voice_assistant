import edge_tts
import asyncio
import os

# Function to convert text to speech
async def text_to_speech(text, output_file):
    # Let user choose between male or female voice
    voice_choice = input("Choose a voice (1 for female, 2 for male): ")
    if voice_choice == "1":
        voice = 'en-US-JennyNeural'
    elif voice_choice == "2":
        voice = 'en-US-GuyNeural'
    else:
        print("Invalid choice, defaulting to female voice.")
        voice = 'en-US-JennyNeural'

    # Take numerical input for rate and pitch, automatically add + and %
    rate_value = input("Enter the speech rate as a number (e.g., 10 for +10%): ")
    rate = f"+{rate_value}%"
    
    pitch_value = input("Enter the pitch as a number (e.g., 5 for +5Hz): ")
    pitch = f"+{pitch_value}Hz"
    
    # Ensure the 'output files' directory exists outside the 'src' folder
    data_dir = "../output files"  # Go up one level and into 'output files' folder
    os.makedirs(data_dir, exist_ok=True)

    # Create and save the TTS output to the specified folder
    output_path = os.path.join(data_dir, output_file)
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(output_path)

# Example usage
if __name__ == "__main__":
    asyncio.run(text_to_speech("Hello, how are you?", "response_audio.mp3"))
