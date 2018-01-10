import csv

# This is the path to data folder with respect to main folder. Make it more generic.
DataPath = 'data/lists.csv' 


def clear_all_lists():
	open(DataPath, 'w').close()


def add_list(ListName, ListPath):
	Writer = csv.writer(open(DataPath, 'a'))
	Writer.writerow([ListName, ListPath])


def add_time():
	pass


def get_lists():
	Reader = csv.reader(open(DataPath, 'r'))
	return list(Reader)

def get_time():
	pass


def check_status():
	try:
		if len(get_lists()) == 0:
			print ('No lists added. Add <listname> and <listpath> (space seperated):')
			ListName, ListPath = input().split()
			add_list(ListName, ListPath)

		return True

	except Exception as e:
		print(e)
		return False