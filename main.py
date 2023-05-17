import speech_recognition as sr

#obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("say something: ")
    audio = r.listen(source)
    
#recognize speech using sphinx
try:
    print("sphinx thinks you said: "+r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Cantt understand")
except sr.RequestError as e:
    print("Sphinx:",format(e))