import re
files = ["bundesliga.txt", "liga.txt", "premier.txt", "serie_a.txt"]
output = ["bundesliga_out.txt", "liga_out.txt", "premier_out.txt", "serie_a_out.txt"]
for init,out in zip(files,output):
	f = open("Data/" + init, "r")
	a = open("Data/" + out, "w+")
	start = 1
	scores = 0
	passers = 0
	keepers = 0
	defenders = 0
	for line in f:
		skill_added = 0
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
			splitted[4] += " (" + splitted[0] + ")"
			position = re.findall(r"[\w']+", splitted[6])
			for pos in position:
				if pos == "GK":
					splitted[6] = "Keeper"
					break
				elif pos == "FW":
					splitted[6] = "Forward"
					break
				elif pos == "D":
					splitted[6] = "Defender"
					break
				elif pos == "AM" or pos == "DM" or pos == "M":
					splitted[6] = "Midfielder"
			if(splitted[14] == '-'):
				splitted[14] = str(0)
			goals = float(splitted[14])
			if goals > 15 and not skill_added:
				splitted.append("Scoring")
				#print splitted[4]
				skill_added = 1
				scores += 1
			if(splitted[19] == '-'):
				splitted[19] = str(0)
			pass_percentage = float(splitted[19])
			if pass_percentage > 95 and not skill_added:
				splitted.append("Passing")
				#print splitted[4]
				skill_added = 1
				passers += 1
			if(splitted[22] == '-'):
				splitted[22] = str(0)
			rating = float(splitted[22])
			if rating >= 7 and splitted[6] == "Keeper" and not skill_added:
				splitted.append("Goalkeeping")
				#print splitted[4]
				skill_added = 1
				keepers += 1
			if rating >= 7.4 and splitted[6] == "Defender" and not skill_added:
				splitted.append("Defending")
				#print splitted[4]
				skill_added = 1
				defenders += 1
			if not skill_added:
				splitted.append("null")
			line = ",".join(splitted)
			a.write(line + "\r")
	print "Top scorers added to " + out + ": " + str(scores)
	print "Top passers added to " + out + ": " + str(passers)
	print "Top keepers added to " + out + ": " + str(keepers)
	print "Top defenders added to " + out + ": " + str(defenders)