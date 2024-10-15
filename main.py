import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as the audio source
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait")
    recognizer.adjust_for_ambient_noise(source)  # Adjust based on surrounding noise
    print("Say something!")
    
    # Capture the audio from the microphone
    audio = recognizer.listen(source)

    try:
        # Convert audio to text
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, I could not request results from the service.")
