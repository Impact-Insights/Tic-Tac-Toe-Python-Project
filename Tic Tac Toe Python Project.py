# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 13:43:02 2024

@author: Mahlogonolo Mathekga
"""

import random

board = ["-", "-","-",
         "-", "-","-",
         "-", "-","-"]

currentPlayer = "X"
winner = None
gameRunning = True



#printing the game board
def printBoard(board):
    print(board[0],  " | " ,  board[1] , " | ", board[2])
    print("-------------")
    print(board[3], " | " ,  board[4] , " | ", board[5])
    print("-------------")
    print(board[6] , " | " ,  board[7] , " | ", board[8])
 
    
#take player input
def playerInput(board):
    inp = int(input("Enter a number from 1 -9: "))
    if inp >= 1 and  inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Spot is already played or Occupied")
            

#check for a win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner =  board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner - board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0] 
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("This is a Tie!")
        gameRunning = False
        
def checkForWin():
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        print(f"Game Over!, the winner is {winner}")
        gameRunning = False
    

#switch a player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"


#check for a win or tie again

def computerPlayer(baord):
    while currentPlayer == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkForWin()
    checkTie(board)
    switchPlayer()
    computerPlayer(board)
    checkForWin()
    checkTie(board)


