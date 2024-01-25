# Speech-to-Sign-Language
This Python script uses the SpeechRecognition library to perform speech recognition using the Google Web Speech API. After recognizing the speech, it displays images based on the words in the recognized text using the PIL (Pillow) library.


--------------------------------------------------------Let's break down the code:-----------------------------------------------------------------------------------

Image Setup:

A folder path images_folder is defined, specifying the location of the image files.
A dictionary text_image_dict is created, associating text values with corresponding image filenames.
Load Images:

The script loads images from the specified folder and stores them in a dictionary (image_dict), where the text values are the keys, and the corresponding PIL Image objects are the values.
Speech Recognition:

The script initializes a SpeechRecognition recognizer (r) and captures audio using a microphone (with sr.Microphone() as source).
The recognized audio is obtained using r.listen(source) and converted to text using Google's Speech Recognition API (r.recognize_google(audio)).
Display Images:

The recognized text is split into words, and for each word, the corresponding image is displayed using the PIL show() method.
A delay of 0 seconds is introduced using time.sleep(0) (you can adjust this time if needed), and then the image window is closed using img.close().
Exception Handling:

The script includes exception handling for cases where speech recognition fails (sr.UnknownValueError) or there is an issue with the Google Speech Recognition service (sr.RequestError).
