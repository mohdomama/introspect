from . import config


def get_count(ListPath, Checked = '[x]', Unchecked = '[ ]'):
	with open(ListPath, 'r') as File:
		String = File.read()
		CheckNum = String.count(Checked)
		UncheckNum = String.count(Unchecked)

	Percentage = (CheckNum *100) // (CheckNum + UncheckNum)
	return Percentage, CheckNum, UncheckNum


def save_date():
	pass


def reset_checklist(ListPath, Checked = '[x]', Unchecked = '[ ]'):
	with open(ListPath, 'r') as File:
		String = File.read()
		String = String.replace(Checked, Unchecked)

	with open(ListPath, 'w') as File:
		File.write(String)
		


def get_productivity():
	Lists = config.get_lists()
	Percentage, CheckNum, UncheckNum = get_count(ListPath = Lists[0][1])
	save_date()
	reset_checklist(ListPath = Lists[0][1])
	return Percentage, CheckNum, UncheckNum