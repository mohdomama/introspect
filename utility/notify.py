import subprocess as s

DataPath = 'data/lists.csv'

def send_notification(name, notification):
	s.call(['notify-send', name, notification])

def parse_name(file_name, file_path):
	with open(file_path.split('\n')[0]) as File:
		line_count = 0
		for line in File:
			line_count+=1
			if(line_count==5):
				heading_line = line
	name = ""
	for i in heading_line:
		if(i.isalnum()):
			name+=i
	if(name not in file_name):
		file_name.append(name)

def get_file_name():
	file_name = []
	with open(DataPath) as File:
		for line in File:
			file_path = line.split(',')[1]
			parse_name(file_name, file_path)
	return file_name

def create_notification(Productivity):
	MessageBody = " Total task done "+str(Productivity[1])+" out of"+ str(Productivity[2])
	file_name = get_file_name()
	for name in file_name:
		send_notification(name, MessageBody)
