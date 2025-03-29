
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()

# Set rate and volume for speech
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take command from the user via microphone
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I am having trouble reaching the speech service.")
        return ""
    return command

# Function to respond to commands
def respond_to_command(command):
    if "hello" in command:
        speak("Hello, how can I assist you today?")
    
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
    
    elif "date" in command:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {date}")
    
    elif "open website" in command:
        speak("Opening the website for you.")
        webbrowser.open("https://www.google.com")
    
    elif "play music" in command:
        speak("Playing music.")
        os.system("start wmplayer")  # Plays music using Windows Media Player
    
    elif "goodbye" in command:
        speak("Goodbye, have a great day!")
        exit()
    
    else:
        speak("Sorry, I didn't understand that command. Please try again.")

# Main function to interact with Jarvis
def jarvis():
    speak("Hi, I am Jarvis. How can I assist you?")
    
    while True:
        command = listen()  # Listen for a command
        if command:
            respond_to_command(command)  # Respond to the command

# Start the assistant
if __name__ == "__main__":
    jarvis()
