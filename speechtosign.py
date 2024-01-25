from PIL import Image
import os
import speech_recognition as sr
import webbrowser
import time  # Import the time module

# Define the path to your image folder
images_folder = r'C:\Users\cnity\OneDrive\Desktop\imagessign'

# Dictionary with text values and corresponding image filenames
text_image_dict = {
    'hello': 'hello.png',
    'you': 'you.jpg',
    'how': 'how.gif',
    # Add more text-image mappings as needed
}

# Create a dictionary to store PIL Image objects
image_dict = {}

# Load images and store them in the dictionary
for text, image_filename in text_image_dict.items():
    image_path = os.path.join(images_folder, image_filename)
    print(f"Checking image for text: {text}, path: {image_path}")
    try:
        img = Image.open(image_path)
        image_dict[text] = img
    except FileNotFoundError:
        print(f"Image not found for text: {text}")

# Initialize recognizer
r = sr.Recognizer()

# Record Audio
with sr.Microphone() as source:
    print("Speak Anything : ")
    audio = r.listen(source)
    text = r.recognize_google(audio)

# Speech recognition using Google Speech Recognition
try:
    print("You said : " + text)

    # Display the images one by one based on the words in the recognized text
    for word in text.split():
        try:
            img = image_dict[word]
            img.show()  # Display the image using the default image viewer

            # Introduce a delay (adjust the time as needed)
            time.sleep(0)  # 2 seconds

            img.close()  # Close the image window

        except KeyError:
            print(f"Image not found for word: {word}")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
