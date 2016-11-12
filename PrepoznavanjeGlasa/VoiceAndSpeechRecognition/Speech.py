import speech_recognition as sr


def recognition():
    while more:
        rec = sr.Recognizer()
        key = 'close program'
        with sr.Microphone() as source:
            audio = rec.listen(source)
        try:
            output = rec.recognize_google(audio)

            print(output)

            if output == key:
                return output

        except sr.UnknownValueError:
            print("error")
            exit()


if __name__ == '__main__':
    more = True
    recognition()
