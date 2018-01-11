import pyttsx3
import os


def make_message(Productivity):
	Salutaion = 'Hello '
	Name = os.environ['HOME'][6:]
	MessageBody = '! Todays productivity is '+ str(Productivity[0])  + '%. Well done! And keep going.'
	Message = Salutaion + Name + MessageBody
	return Message


def speak(Message, RelRate = -40, VoiceID = 'english'):
	engine = pyttsx3.init()
	engine.setProperty('voice', VoiceID)

	DefRate = engine.getProperty('rate')
	engine.setProperty('rate', DefRate + RelRate)

	engine.say(Message)
	engine.runAndWait()

def voice_notification(Productivity):
	Message = make_message(Productivity)
	speak (Message = Message)