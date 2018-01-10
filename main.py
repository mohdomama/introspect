from utility import *
import sys

def run():
	if config.check_status():
		Productivity = list_handle.get_productivity()
		print('Percentage, Done, NotDone : ',Productivity)
	
	else:
		sys.exit()


def main():
	if len(sys.argv) == 1:
		run()
	
	else:
		if sys.argv[1] == 'clear':
			config.clear_all_lists()
			return
	
		elif sys.argv[1] == 'addlist':
			config.add_list(sys.argv[2], sys.argv[3])
			return

		else:
			print('Invalid Argument')
			sys.exit()



if __name__ == '__main__':
	main()
