#! \Users\ratan\miniconda3\envs\practice\python3

import sys

def checkWin(board): 
    if board['1'] != ' ' and board['1'] == board['2'] and board['1'] == board['3']:
        return board['1']
    elif board['1'] != ' ' and board['1'] == board['4'] and board['1'] == board['7']:
        return board['1']
    elif board['1'] != ' ' and board['1'] == board['5'] and board['1'] == board['9']:
        return board['1']
    elif board['2'] != ' ' and board['2'] == board['5'] and board['2'] == board['8']:
        return board['2']
    elif board['3'] != ' ' and board['3'] == board['6'] and board['3'] == board['9']:
        return board['3']
    elif board['3'] != ' ' and board['3'] == board['5'] and board['3'] == board['7']:
        return board['3']
    elif board['4'] != ' ' and board['4'] == board['5'] and board['4'] == board['6']:
        return board['4']    
    elif board['7'] != ' ' and board['7'] == board['8'] and board['7'] == board['9']:
        return board['7']

def printBoard(board):
    print()
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['7']+'|'+board['8']+'|'+board['9'])

board = {
    '1' : ' ', '2' : ' ', '3' : ' ', '4' : ' ', '5' : ' ', '6' : ' ', '7' : ' ', '8' : ' ', '9' : ' ',
}
player = ['X','O']

print('1|2|3')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('7|8|9')

for i in range(9):
    print("-"*30)
    move = input('Player '+ player[i%2] +' turn. Move on which space?: ')

    while board[move] != ' ':
        move = input('Space INVALID ... Enter a Valid Space number: ')

    board[move] = player[i%2]
    winner = checkWin(board)
    printBoard(board)
    if winner:
        print("-"*30)
        print('Player',winner,'won the game!!!!!!!')
        print("-"*30)
        sys.exit()


print("-"*30)
print('Alas!! It\'s a Draw...!')
print("-"*30)

