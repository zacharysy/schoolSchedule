import json

"""
schedList = 
{dayNumber:
	{periodNumber[
		name,
		room,
		timeStart,
		timeEnd
		]}
	}
"""	
	
schedList = {}

#day 1
periodList = {}
periodList[0] = ["Assembly","HS Gym","07:10","08:15"]
periodList[1] = ["Physics","Rm S302","08:20","09:20"]
periodList[2] = ["Economics","Rm S404","09:25","10:25"]
periodList[3] = ["Recess","Canteen","10:26","10:44"]
periodList[4] = ["Physics","Rm S303","10:45","11:45"]
periodList[5] = ["Computer Science","Rm S505","11:50","12:50"]
periodList[6] = ["Lunch","Canteen","12:51","13:39"]
periodList[7] = ["Math","Rm S504","13:40","14:40"]

schedList[1] = periodList

#day 2
periodList = {}
periodList[0] = ["Homeroom","Rm S306","07:15","07:35"]
periodList[1] = ["English Literature","Rm S507","07:40","08:40"]
periodList[2] = ["Physics","Rm S302","08:45","09:45"]
periodList[3] = ["Recess","Canteen","09:46","10:04"]
periodList[4] = ["Study Hall","Rm S404","10:05","11:05"]
periodList[5] = ["TOK","Rm S206","11:10","12:10"]
periodList[6] = ["Lunch","Canteen","12:09","12:54"]
periodList[7] = ["Economics","Rm S404","12:55","13:55"]
periodList[8] = ["Computer Science","Rm S505","14:00","15:00"]

schedList[2] = periodList

#day 3
periodList = {}
periodList[0] = ["Homeroom","Rm S306","07:15","07:40"]
periodList[1] = ["Chinese","Rm S308","07:45","08:45"]
periodList[2] = ["Filipino","Rm S204","08:50","09:50"]
periodList[3] = ["Recess","Canteen","09:51","10:19"]
periodList[4] = ["Computer Science","Rm S505","10:20","11:20"]
periodList[5] = ["English Literature","Rm S507","11:25","12:25"]
periodList[6] = ["Lunch","Canteen","12:26","13:49"]
periodList[7] = ["Math","Rm S504","13:50","14:50"]

schedList[3] = periodList

#day 4
periodList = {}
periodList[0] = ["Homeroom","Rm S306","07:15","07:35"]
periodList[1] = ["English Literature","Rm S507","07:40","08:40"]
periodList[2] = ["Economics","Rm S404","08:45","09:45"]
periodList[3] = ["Recess","Canteen","09:46","10:04"]
periodList[4] = ["Physics","Rm S302","10:05","11:05"]
periodList[5] = ["Chinese","Rm S206","11:10","12:10"]
periodList[6] = ["Lunch","Canteen","12:09","12:54"]
periodList[7] = ["Computer Science","Rm S302","12:55","13:55"]
periodList[8] = ["Math","Rm S504","14:00","15:00"]

schedList[4] = periodList

#day 5
periodList = {}
periodList[0] = ["Homeroom","Rm S306","07:15","07:35"]
periodList[1] = ["Filipino","Rm S402","07:40","08:40"]
periodList[2] = ["Chinese","Rm S206","08:45","09:45"]
periodList[3] = ["Recess","Canteen","09:46","10:04"]
periodList[4] = ["Economics","Rm S404","10:05","11:05"]
periodList[5] = ["Math","Rm S504","11:10","12:10"]
periodList[6] = ["Lunch","Canteen","12:09","12:54"]
periodList[7] = ["English Literature","Rm S507","12:55","13:55"]
periodList[8] = ["Computer Science","Rm S506","14:00","15:00"]

schedList[5] = periodList

#day 6
periodList = {}
periodList[0] = ["Homeroom","Rm S306","07:15","07:40"]
periodList[1] = ["Physics","Rm S302","07:45","08:45"]
periodList[2] = ["Filipino","Rm S402","08:50","09:50"]
periodList[3] = ["Recess","Canteen","09:51","10:19"]
periodList[4] = ["Chinese","Rm S206","10:20","11:20"]
periodList[5] = ["English Literature","Rm S507","11:25","12:25"]
periodList[6] = ["Lunch","Canteen","12:26","13:49"]
periodList[7] = ["Math","Rm S504","13:50","14:50"]

schedList[6] = periodList

#day 7
periodList = {}
periodList[0] = ["Homeroom","Rm S306","07:15","07:35"]
periodList[1] = ["Filipino","Rm S402","07:40","08:40"]
periodList[2] = ["Math","Rm S504","08:45","09:45"]
periodList[3] = ["Recess","Canteen","09:46","10:04"]
periodList[4] = ["Physics","Rm S302","10:05","11:05"]
periodList[5] = ["Economics","Rm S404","11:10","12:10"]
periodList[6] = ["Lunch","Canteen","12:09","12:54"]
periodList[7] = ["Chinese","Rm S206","12:55","13:55"]
periodList[8] = ["Computer Science","Rm S505","14:00","15:00"]

schedList[7] = periodList

file = open("SchedList.json","w")
file.write(json.dumps(schedList))
file.close()

for n in range(1,8):
	for i in range(len(schedList[n])):
		print(schedList[n][i])
	print("\n")
	
