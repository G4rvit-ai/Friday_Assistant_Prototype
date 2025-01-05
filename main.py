import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://google.co.in")
        speak("Opening Google")
        

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
        

    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")
        

    elif "open chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
        speak("Opening ChatGpt")
        

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.in")
        speak("Opening Linkedin")

    elif "open github" in command:
        webbrowser.open("https://github.com")
        speak("Opening Github")
        print("Affirmative")

    elif "open amazon" in command:
        webbrowser.open("https://amazon.in")
        speak("Opening Amazon")

    elif "open apple" in command:
        webbrowser.open("https://apple.com/in/")
        speak("Opening Apple")

    elif "open samsung" in command:
        webbrowser.open("https://samsung.com/in/")
        speak("Opening Samsung")


    elif command.startswith("play songs"):
        try:
            song = command.split(" ", 1)[1] 
            link = musicLibrary.music.get(song)  
            if link:
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song {song}.")
        except IndexError:
            speak("Please specify a song to play.")

    elif "news" in command:
        webbrowser.open("https://newsapi.org")


if __name__ == "__main__":
    speak("Initializing Friday....")
    while True:
        print("Recognizing....")
        
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source, timeout=7, phrase_time_limit=7)

            word = recognizer.recognize_google(audio)  
            if word.lower() in ["hey friday", "friday"]:
                speak("Yes boss")
                print("Yes boss")
                
                with sr.Microphone() as source:
                    print("Friday Active....")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)  

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Error: Could not request results; check network connection.")
        except Exception as e:
            print(f"An error occurred: {e}")
