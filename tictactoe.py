#!/bin/python3

import random

win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

movecom={ 1:[1,1] , 2:[1,2] , 3:[1,3] , 4:[2,1] , 5:[2,2] , 6:[2,3] , 7:[3,1] , 8:[3,2] , 9:[3,3]}

def who_won(tt):
	l1=set()
	l2=set()
	for i in range(len(tt)):
		for j in range(len(tt[i])):
			if tt[i][j] == 'X':
				l1.add(i*3+j)
			elif tt[i][j] == 'O':
				l2.add(i*3+j)
	#print(l1)
	#print(l2)
	for i in win:
		if set(i)<=l1:
			return(1)
		elif set(i)<=l2:
			return(2)	
	else:
		return(0)


def print_board(a):
	for i in range(3):
		print(' '.join(a[i]))


def draw_board(a):
	print("--- "*3)
	for i in range(3):		
		print("| "+a[0][i], end=' ')
	print('|')
	print("--- "*3)
	for i in range(3):		
		print("| "+a[1][i], end=' ')
	print('|')
	print("--- "*3)
	for i in range(3):		
		print("| "+a[2][i], end=' ')
	print('|')
	print("--- "*3)


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return movecom[i]

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return movecom[i]

    
    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return movecom[5]
    
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return movecom[move]


    # Move on one of the sides.
    return movecom[chooseRandomMoveFromList(board, [2, 4, 6, 8])]



match={1:'X',2:'O'}



w1=0
w2=0

ch='y'

print("Welcome to tic-tac-toe")
print("Choose player mode (1/2)")
print("1. Single Player")
print("2. Two Player")
n=int(input("Enter choice: "))
if n==2:
	while ch.lower()=='y':
		a=[]
		for i in range(3):
			a.append([' ',' ',' '])
	
		draw_board(a)

		filled=set()
		pl=1
		while 1:
			print("Player %d, Enter move(x,y) (%s): " %(pl, match[pl]),end=' ')
			while 1:
				i,j=map(int,input().split(','))
				if ((i-1)*3+(j-1) not in filled):
					filled.add((i-1)*3+(j-1))
					a[i-1][j-1]=match[pl]
					break			
				else:
					print("Position already filled")
					print("Enter another move: ", end=' ')
	

			if pl==1:
				pl=2
			else:
				pl=1
			draw_board(a)
			#print(a)
			#print(who_won(a))
			if who_won(a)==1:
				print("Player 1 won")
				w1+=1
				print("Games won: Player 1: %d   Player 2: %d" %(w1,w2))
				ch=input("Wanna play again? (y/n): ")
				break
			elif who_won(a)==2:
				print("Player 2 won")
				w2+=1
				print("Games won: Player 1: %d   Player 2: %d" %(w1,w2))
				ch=input("Wanna play again? (y/n): ")
				break
			if len(filled)==9:
				print("No more moves possible")
				print("Games won: Player 1: %d   Player 2: %d" %(w1,w2))
				ch=input("Wanna play again? (y/n): ")
				break

elif n==1:
	while ch.lower()=='y':
		a=[]
		for i in range(3):
			a.append([' ',' ',' '])
	
		draw_board(a)

		filled=set()
		pl=1
		while 1:
			if pl==1:
				print("Enter your move(x,y) (%s): " %(match[pl]),end=' ')
				while 1:
					i,j=map(int,input().split(','))
					if ((i-1)*3+(j-1) not in filled):
						filled.add((i-1)*3+(j-1))
						a[i-1][j-1]=match[pl]
						#print(a)
						break			
					else:
						print("Position already filled")
						print("Enter another move: ", end=' ')
			elif pl==2:
				print("Computer's move")
				b=['a']
				for i in range(len(a)):
					for j in range(3):
						b.append(a[i][j])
						#print(b)
				x,y = getComputerMove(b, 'O')
				filled.add((x-1)*3+(y-1))
				a[x-1][y-1]='O'
	

			if pl==1:
				pl=2
			else:
				pl=1
			draw_board(a)
			#print(a)
			#print(who_won(a))
			if who_won(a)==1:
				print("Player 1 won")
				w1+=1
				print("Games won: Player 1: %d   Computer: %d" %(w1,w2))
				ch=input("Wanna play again? (y/n): ")
				break
			elif who_won(a)==2:
				print("Player 2 won")
				w2+=1
				print("Games won: Player 1: %d   Computer: %d" %(w1,w2))
				ch=input("Wanna play again? (y/n): ")
				break
			if len(filled)==9:
				print("No more moves possible")
				print("Games won: Player 1: %d   Computer: %d" %(w1,w2))
				ch=input("Wanna play again? (y/n): ")
				break
		
	
	
	
	


