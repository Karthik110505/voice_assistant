from voice_to_text import voice_to_text_from_file, transcribe_from_microphone  # Import necessary functions
from text_to_llm import generate_response  # Import LLM response generation function
from text_to_speech import text_to_speech  # Import text-to-speech function
import asyncio
import whisper

def main():
    # Initialize the Whisper model
    model = whisper.load_model("base.en")
    
    # Step 1: Ask the user to select input method
    option = input("Select input method (1 for microphone, 2 for audio file): ")

    if option == "1":
        # Record audio from the microphone
        duration = float(input("Enter duration of recording in seconds: "))
        print("Converting voice to text from microphone...")
        transcribed_text = transcribe_from_microphone(model, duration=duration)
    elif option == "2":
        # Use an audio file for transcription
        audio_file = input("Enter the path to the audio file: ")
        print("Converting voice to text from file...")
        transcribed_text = voice_to_text_from_file(model, audio_file)
    else:
        print("Invalid option selected.")
        return

    # Handle the case where no speech is detected
    if transcribed_text == "No speech detected.":
        print("No speech detected. Please try again.")
        return

    print(f"Transcribed Text: {transcribed_text}")

    # Step 2: Use LLM to generate a response based on the transcribed text
    print("Generating response from LLM...")
    response = generate_response(transcribed_text)    
    if response[1:5] == 'Mini':  # Specific response adjustment (if required)
        response = response[6:]
    else:
        response = response[1:]
    print(f"LLM Response: {response}")

    # Step 3: Convert the response to speech (Async call)
    print("Converting response text to speech...")
    asyncio.run(text_to_speech(response, output_file="response_audio.mp3"))
    print("Response has been saved to 'response_audio.mp3' in the data folder")

if __name__ == "__main__":
    main()
