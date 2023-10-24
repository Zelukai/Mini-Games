'''
**first value is suit, second is card value

Player Cards:
Each player will have a hand (list)
Each hand is initialized by appending to it 7 randomized unique indices from the main deck
Each value added to a hand must be popped from the deck (so that the card actually moves to the player)
**if the append and pop happen within the same spot in the loop, the indices do not need to be unique as repeats will be impossible
There can be up to 7 players
**gameloop(): for i in range(playerCount): #create hands **gameloop recursively calls itself when a new game starts
**there is a while i < playerCount loop where i represents the turn that resets itself to the first player each time i reaches playerCount (checks at the end of the loop if i==playerCount then i = 0)
 - i.e. while i < playerCount:
 			blabla
 			if gameEnd() == true: #gameEnd is true when a player's cardcount == 0
				print(f"{winner} wins!")
				print("Would you like to play again? y/n")
				playAgain = input()
				if playAgain == 'y' or playAgain == 'Y':
					gameloop()
				elif playAgain == 'n' or playAgain == 'N':
					break
 				else: 
 					print('um you didn't follow instructions bye')
 					break
 			i += 1
 			if i == playerCount and gameEnd == false:
 				i = 0
 - cardCount checker: def gameEnd(playerCount, playerHand)
 						for i in range(playerCount):
 							if len(playerHand[i]) == 0:
 								return true
 							else: return false
**action() function repeats within gameloop and recusively calls itself each new turn. This function lets you select actions, which call action functions

Each action of moving a card will have a function: 
 - drawing from the deck (append player/botHand from deck index and pop from deck at index)
 - getting a card from another player (append playerHand from opponent and pop from player/botHand at index)
 	- two possibilites: if playerhascard(i, j) == True: # add to hand and remove from this hand  OR if playerhascard(i, j) == False #print('Go Fish!') draw()
 	**I can simplify these statements to if playerhascard: and if not playerhascard because they're true false statements 
 	  - **The second if statement need not exist either--after debugging, it will just be in an else statement
 - draw function: draw(), where a random index of the deck is added to the current player's hand
 - take function: attempt([i, j]) where i is the suit and j is the card value of the card the player is asking for

 **it looks like the index at the time of a true if statement must be stored in a variable to be used for appending and popping

Rules of Go Fish:
 - 2 or 3 players: 7 cards each, 4 or 5 players: 5 cards each

Actions in Go Fish:
 - Blabla

FUTURE:
**Can scale game further by allowing for playercounts greater than 7 in go fish. 
 - For every chunk of seven players a deck is generated, and you can just append the deck onto itself again with minimal restructuring


 Go fish only cares about numbers, so I can ignore suits (create a command to strip the deck of the suit value)
  **do this by generating a new list with just the card numbers as values because it's frivolous to have one-value lists
    - note that the other lists will be deleted and only the relevant list will remain as it passes the other functions as parameters, they do not run on their own


'''

# Imports

import random
import sys

print(sys.version)


# Function List

def generateNumberDeck():
	deck = []
	for j in range(4):
		for k in range(13):
			deck.append([j+1, k+1])
	return deck

def convertWordDeck(numberDeck):
	for i in range(52):
		if numberDeck[i][0] == 1:
			numberDeck[i][0] = "Hearts"
		elif numberDeck[i][0] == 2:
			numberDeck[i][0] = "Diamonds"
		elif numberDeck[i][0] == 3:
			numberDeck[i][0] = "Clubs"
		elif numberDeck[i][0] == 4:
			numberDeck[i][0] = "Spades"

		for j in range(13):
			if numberDeck[i][1] == 1:
				numberDeck[i][1] = "Ace"
			elif numberDeck[i][1] == 11:
				numberDeck[i][1] = "Jack"
			elif numberDeck[i][1] == 12:
				numberDeck[i][1] = "Queen"
			elif numberDeck[i][1] == 13:
				numberDeck[i][1] = "King"

	return numberDeck

def playerCounter(min, max):
	playerCount = int(input(f"How many total players would you like in this game? ({min}-{max}): ")) #collect playerCount
	print(f"playerCount input: {playerCount}") #debugging
	if playerCount >= min and playerCount <= max:
		print(f"playerCount check: {playerCount}") #debugging
		return playerCount
	else:
		print("The requested number of players is not available for this game. \nPlease try again, remember that this number includes you.")
		playerCounter(min, max)
	

def convertGoFishDeck(wordDeck):
	goFishDeck = []
	for i in range(52):
		goFishDeck.append(wordDeck[i][1])

	return goFishDeck

def go_fish_gameEnd(playerCount, playerHands): #implies that there is a list stories lists of playerhands, which each store lists of cards...
	#NON-FUNCTIONAL -- NEEDS FIX (can't detext the true condition)
 	for i in range(playerCount):
 		if len(playerHands[i]) == 0:
 			return True
 		else: return False



def go_fish_gameLoop():
	print("Welcome to Go Fish!")
	deck = convertGoFishDeck(convertWordDeck(generateNumberDeck())) #generate go fish deck
	playerCount = playerCounter(2, 5) #ask for the number of players (including user)
	print(playerCount) #debugging **Doesn't give value when the command loops from misinput FAILS EDGE-CASE
	if playerCount == 2 or playerCount == 3: #incredibly clunky and brute force checks before i figure out what i want to do for scaling player count above 5
		startingCards = 7
	elif playerCount == 4 or playerCount == 5:
		startingCards = 5
	playerHands = []
	for i in range(playerCount):
		for j in range(startingCards): #adds cards to current hand index consistent with number of players
			tempCardIndex = random.randint(0, len(deck)-1) #selects a random card from the deck
			playerHands[i].append(deck[tempCardIndex]) #adds card to the list of current playerHands index (hopefully this creates a list??)
			deck.pop(tempCardIndex) #removes card from deck since it was moved to playerHands index
	print(playerHands)
	#create playerhands based on playercount
	#run turn loop until game is over

	'''
	while i < playerCount:
 			blabla
 			if go_fish_gameEnd() == true: #gameEnd is true when a player's cardcount == 0
				print(f"{winner} wins!")
				print("Would you like to play again? y/n")
				playAgain = input()
				if playAgain == 'y' or playAgain == 'Y':
					gameloop()
				elif playAgain == 'n' or playAgain == 'N':
					break
 				else: 
 					print("um you didn't follow instructions bye")
 					break
 			i += 1
 			if i == playerCount and go_fish_gameEnd == False:
 				i = 0
 	'''



#Game Setup and Initialization

#deck = convertGoFishDeck(convertWordDeck(generateNumberDeck())) #remove this line when gameLoop is run
#print(deck) #debugging
#print(len(deck)) #debugging
#print(f"{deck[0][1]} of {deck[0][0]}") #debugging **can be generalized to i and j of a current card **NOT applicaple to Go Fish deck

#Game Running

go_fish_gameLoop()

#print(go_fish_gameEnd(5, [[[1], [1]], [[1], [1], [1]], [[1], [1]], [[1]], []])) #debugging gameEnd **fails, non-functional
#print(go_fish_gameEnd(5, [[[1], [1]], [[1], [1], [1]], [[1], [1]], [[1]], [[]]])) #debugging gameEnd **fails, non-functional

#Game Ending



