# Voice-Assistant-Using-Python

The "Voice Assistant using Python" project is a simple yet powerful implementation of a voice-controlled assistant that interacts with users through voice commands. The assistant can perform a variety of tasks, such as playing music on YouTube, searching the web, retrieving information from Wikipedia, telling jokes, providing the current time, and more. The assistant uses various Python libraries, including speech_recognition, pyttsx3, pywhatkit, datetime, wikipedia, pyjokes, and sys to achieve its functionality.

>>Features:

-Voice Interaction: Users can interact with the voice assistant by speaking voice commands.
-Task Execution: The assistant can execute various tasks, such as playing YouTube videos, searching the web, and retrieving information.
-Shutdown Control: Users can command the assistant to initiate a system shutdown, with the ability to cancel the shutdown as well.
-Time Information: The assistant provides the current time when requested by the user.
-Wikipedia Search: Users can ask the assistant to provide a summary of a person using Wikipedia.
-Jokes: The assistant can tell jokes to provide a touch of humor.
-Exiting: Users can exit the assistant by giving an appropriate command.

>>How It Works:

-The user's name is collected at the start to personalize the assistant's greetings.
-The assistant waits for the user's voice command using the speech_recognition library.
-The user's voice command is processed and matched with predefined actions.
-Based on the command, the assistant performs the relevant task using various Python libraries:
-Playing YouTube videos with pywhatkit.playonyt().
-Searching the web with pywhatkit.search().
-Retrieving information from Wikipedia with wikipedia.summary().
-Providing current time using datetime.datetime.now().
-Telling jokes using pyjokes.get_joke().
-Initiating system shutdown with pywhatkit.shutdown() and canceling it with pywhatkit.cancel_shutdown().
-The assistant responds with spoken messages using the pyttsx3 text-to-speech library.

>>Usage:

-Users can run the script and provide their name.
-Users can start giving voice commands prefixed with their name.
-The assistant interprets and executes the commands, responding with appropriate actions.
==This project showcases the power of combining different Python libraries to create a functional voice assistant that performs tasks in response to voice commands, making it a useful and interactive tool for various everyday activities.
