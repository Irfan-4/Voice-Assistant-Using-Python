import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import os
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

x = input("Your name: ")
y = "Hey " + x + ", what can I do for you?"
engine.say(y)
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command=""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()

            if x.lower() in command:
                command = command.replace(x.lower(), '').strip()    
                print(command)
    except:
        pass
    return command


def run_assistant():
    command = take_command()
    print("You said:", command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'open file' in command:
        file_name = command.replace('open file', '').strip()
        try:
            os.startfile(file_name)
        except FileNotFoundError:
            talk('File not found.')
    elif 'open notepad' in command:
        os.system('notepad')
    elif 'open file explorer' in command:
        os.system('explorer')
    elif 'open website' in command:
        website = command.replace('open website', '')
        talk('Opening ' + website)
        webbrowser.open('https://www.' + website)
    elif 'search' in command:
        search_query = command.replace('search', '')
        talk('Searching for ' + search_query)
        pywhatkit.search(search_query)
    elif 'power off' in command:
        talk('System will shutdown in 1 minute')
        pywhatkit.shutdown(time=60)
    elif 'cancel' in command:
        talk('Shutdown canceled')
        pywhatkit.cancel_shutdown()
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with Wi-Fi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'exit' in command:
        talk('Goodbye! Have a good day!')
        sys.exit()
    else:
        talk('Please repeat the command.')


try:
    while True:
        run_assistant()
except KeyboardInterrupt:
    talk('Goodbye!')


#More functionalities of pywhatkit

#import pywhatkit

# Text to Handwriting
#pywhatkit.text_to_handwriting("irfan from hyderabad", rgb=[0, 0, 0])

# Send WhatsApp Message
#pywhatkit.sendwhatmsg('+917989137800', 'Aur kya chalra!', 00, 10)
# Make sure to replace the phone number and message with the actual ones you want to use.

# Image to ASCII Art
#pywhatkit.image_to_ascii_art("image.png", "ascii_art.txt")

# Convert Image to ASCII Art and Save to File

#def convert_image_to_ascii_art(input_image_path, output_text_file):
#    pywhatkit.image_to_ascii_art(input_image_path, output_text_file)

#input_image_path = r"C:\Users\irfan\Downloads\Ananthagiri Hills-06.08.2023\Snapchat-52531953.jpg"
#output_text_file = "ascii_art.txt"
#convert_image_to_ascii_art(input_image_path, output_text_file)

# Shutdown System
#pywhatkit.shutdown(time=60)  # System will shut down in 60 seconds

# Cancel Shutdown
#pywhatkit.cancel_shutdown()

# Playing YouTube Video
#pywhatkit.playonyt("Python programming tutorial")

# Search and Browse
#pywhatkit.search("How to make a paper airplane")
#pywhatkit.search("Python programming")

# Convert Text to Speech and Save as Audio File
#pywhatkit.text_to_speech("Hello, how can I help you?", "output_audio.mp3")

# Convert Text to PDF
#pywhatkit.text_to_pdf("Hello, this is a PDF example.", "output_pdf.pdf")


