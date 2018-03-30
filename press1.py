import random
import climb
import start
print('snakes and ladders')
ladders=[6,9,20,25,53,54,61]
ladders_score=[21,41,19,32,19,31,21]
#print (ladders)
snakes=[43,55,70,78,95,96]
snakes_score=[27,22,22,36,22,14]
#print(snakes)

#print(player1)
player1_score=0
player2_score=0
winner=100 
while 1 :
	print('player1 chance')
	print('player1 press enter')
	p=input()
	dice=random.randint(1,6)
	print('dice value of player1 is:',dice)
	player1_score=player1_score+dice
	if dice==6:
		player1score=start.started(dice)
		player1_score=player1score
	if player1_score in ladders:
		lindex=ladders.index(player1_score)
		print('ladder',lindex)
		print('player1 climbed')
		player1_score=player1_score+ladders_score[lindex]
		print('player1 press enter')
		p=input()
		dice=random.randint(1,6)
		if dice==6:
			player1_score=climb.climbed(dice,player1_score)
			print('player1 promoted')
			print(player1_score)
		else:
			player1_score=player1_score+dice
			print('player1 score after climbing is',player1_score)
	elif player1_score in snakes:
		print('snake zone')
		sindex=snakes.index(player1_score)
		print('!!!!',sindex)
		print('player1 is going down')
		player1_score=player1_score-snakes_score[sindex]
	else:
		print('player1 is in normal state')
	player1_score=player1_score+dice
	print('now player1 score is',player1_score)
	if player1_score==winner:
		print('player1 is winner')
		break
	print('player 2 chance')
	print('player2 press enter ')
	p=input()
	dice=random.randint(1,6)
	print('dice value of player2 is:',dice)
	player2_score=player2_score+dice
	if dice==6:
		player2score=start.started(dice)
		player2_score=player2score
	if player2_score in ladders:
		lindex=ladders.index(player2_score)
		print('ladder',lindex)
		print('player2 climbed')
		player2_score=player2_score+ladders_score[lindex]
		print('player2 press enter')
		p=input()
		dice=random.randint(1,6)
		if dice==6:
			player2_score=climb.climbed(dice,player2_score)
			print('player2 promoted')
			print(player2_score)
		else:
			player2_score=player2_score+dice
			print('score of player2 after climbing is ',player2_score)
	elif player2_score in snakes:
		sindex=snakes.index(player2_score)
		print('!!!!',sindex)
		print('player2 is going down')
		player2_score=player2_score-snakes_score[sindex]
	else:
		print('player2 is in normal state')
	player2_score=player2_score+dice
	print('now player2 score is',player2_score)
	if player2_score==winner:
	 	print('player2 is winner')
	 	break
