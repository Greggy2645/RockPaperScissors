import random
import time

winreeks = 0
verliezen = 0
list = ["Steen", "Papier", "Schaar"]
random = random.randint(1,3)
sps = "blank"
if random == 1:
    sps = list[0]
elif random == 2:
	sps = list[1]
elif random == 3:
	sps = list[2]
#print(sps)
sps_user = str(input('Steen, Papier of Schaar?\n'))
if sps_user == "Schaar" and sps == "Papier":
	print('You Won!')
	winreeks += 1
elif sps_user == "Schaar" and sps== "Steen":
	print('awhh, you lost')
	verliezen += 1
elif sps_user == "Steen" and sps == "Schaar":
	print('You won!')
	winreeks += 1
elif sps_user == "Steen" and sps == "Papier":
	print('You lost')
	verliezen += 1
elif sps_user == "Schaar" and sps == "Papier":
	print('You won!')
	winreeks += 1
elif sps_user == "Schaar" and sps == "Steen":
	print('You lost!')
	verliezen += 1

if verliezen > 2:
	print('you lost whahhah')
	exit()

if winreeks > 2:
	print('you won!')
	exit()
#dit moet nog gefixt worden
#@tereboooooo helupp
