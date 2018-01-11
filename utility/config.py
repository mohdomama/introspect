import csv
import os

# This is the path to data folder with respect to main folder. Make it more generic.
DataPath = 'data/'
DataFiles = ['lists.csv'] 


def create_data_folder():
	os.mkdir(DataPath)
	for File in DataFiles:
		open(DataPath + File, 'w').close()


def clear_all_lists():
	for File in DataFiles:
		open(DataPath + File, 'w').close()


def add_list(ListName, ListPath):
	Writer = csv.writer(open(DataPath + DataFiles[0], 'a'))
	Writer.writerow([ListName, ListPath])


def add_time():
	pass


def get_lists():
	Reader = csv.reader(open(DataPath + DataFiles[0], 'r'))
	return list(Reader)

def get_time():
	pass


def check_status():
	try:
		if  not os.path.isdir(DataPath):
			create_data_folder()

		if len(get_lists()) == 0:
			print ('No lists added. Add <listname> and <listpath> (space seperated):')
			ListName, ListPath = input().split()
			add_list(ListName, ListPath)

		return True

	except Exception as e:
		print(e)
		return False