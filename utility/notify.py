import subprocess as s

DataPath = 'data/lists.csv'

def send_notification(Name, Notification):
	s.call(['notify-send', Name, Notification])

def parse_name(FileName, FilePath):
	with open(FilePath.split('\n')[0]) as File:
		LineCount = 0
		for Line in File:
			LineCount+=1
			if(LineCount==5):
				HeadingLine = Line
	Name = ""
	for i in HeadingLine:
		if(i.isalnum()):
			Name+=i
	if(Name not in FileName):
		FileName.append(Name)

def get_file_name():
	FileName = []
	with open(DataPath) as File:
		for Line in File:
			FilePath = Line.split(',')[1]
			parse_name(FileName, FilePath)
	return FileName

def create_notification(Productivity):
	MessageBody = " Total task done "+str(Productivity[1])+" out of "+ str(Productivity[2])
	FileName = get_file_name()
	for Name in FileName:
		send_notification(Name, MessageBody)
