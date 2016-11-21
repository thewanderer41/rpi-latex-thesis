if __name__ == "__main__":
	f = open("rpithes.bbl", 'r')
	text_list = []
	for line in f:
		if "BIBentrySTDinterwordspacing" in line:
			text_list.append("\n")
		text_list.append(line)
	f.close()
	f2 = open("rpithes.bbl", 'w')
	f2.writelines(text_list)
	f2.close()
