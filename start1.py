import random
def started(dice1):
	if dice1==6:
		print('you are about to play')
		print('press enter') 
		p=input()
		print('i am in start block')
		dice2=random.randint(1,6)
		print('cmpltd dicing')
		dice1=dice1+dice2
		print('score is',dice1)
		if dice2==6:
			started(dice1)
		else:
			print('score is:',dice1)
			return(dice1)