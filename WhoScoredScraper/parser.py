import re
files = ["bundesliga.csv", "liga.csv", "premier.csv", "serie_a.csv"]
output = ["bundesliga_out.csv", "liga_out.csv", "premier_out.csv", "serie_a_out.csv"]
for init,out in zip(files,output):
	f = open("Data/" + init, "r")
	a = open("Data/" + out, "w+")
	start = 1
	scores = 0
	passers = 0
	keepers = 0
	defenders = 0
	for line in f:
		if start:
			line = line.strip('\n')
			line = line.strip('\r')
			splitted = line.split(",")
			splitted.append("Skills\r")
			line = ",".join(splitted)
			a.write(line)
			start = 0
		else:
			line = line.strip('\n')
			line = line.strip('\r')
			splitted = line.split(",")
			splitted[3] += " (" + splitted[0] + ")"
			position = re.findall(r"[\w']+", splitted[5])
			for pos in position:
				if pos == "GK":
					splitted[5] = "Keeper"
					break
				elif pos == "FW":
					splitted[5] = "Forward"
					break
				elif pos == "D":
					splitted[5] = "Defender"
					break
				elif pos == "AM" or pos == "DM" or pos == "M":
					splitted[5] = "Midfielder"
			if(splitted[13] == '-'):
				splitted[13] = str(0)
			goals = float(splitted[13])
			if goals > 15:
				splitted.append("Scoring")
				#print splitted[3]
				scores += 1
			if(splitted[18] == '-'):
				splitted[18] = str(0)
			pass_percentage = float(splitted[18])
			if pass_percentage > 95:
				splitted.append("Passing")
				#print splitted[3]
				passers += 1
			if(splitted[21] == '-'):
				splitted[21] = str(0)
			rating = float(splitted[21])
			if rating >= 7 and splitted[5] == "Keeper":
				splitted.append("Goalkeeping")
				#print splitted[3]
				keepers += 1
			if rating >= 7.4 and splitted[5] == "Defender":
				splitted.append("Defending")
				#print splitted[3]
				defenders += 1
			line = ",".join(splitted)
			a.write(line + "\r")
	print "Top scorers added to " + out + ": " + str(scores)
	print "Top passers added to " + out + ": " + str(passers)
	print "Top keepers added to " + out + ": " + str(keepers)
	print "Top defenders added to " + out + ": " + str(defenders)