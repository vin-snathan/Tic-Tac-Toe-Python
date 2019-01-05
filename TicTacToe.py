# initialize data structure
gameBoard = {
    'top-L': '',
    'top-M': '',
    'top-R': '',
    'mid-L': '',
    'mid-M': '',
    'mid-R': '',
    'low-L': '',
    'low-M': '',
    'low-R': ''
}

winningCombinations = [
    ['top-L', 'top-M', 'top-R'],
    ['mid-L', 'mid-M', 'mid-R'],
    ['low-L', 'low-M', 'low-R'],

    ['top-L', 'mid-L', 'low-L'],
    ['top-M', 'mid-M', 'low-M'],
    ['top-R', 'mid-R', 'low-R'],

    ['top-L', 'mid-M', 'low-R'],
    ['low-L', 'mid-M', 'top-R']
]

playerX_positions = []
playerO_positions = []

# initialize player turn
turn = 'X'

# initialize game
def gameInit(board):
    print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
    print('--------')
    print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print('--------')
    print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}\n")

# function executes only after a minimum of a combined total of 5 moves have been made
def determineWinner(player, movesRemaining):
    if movesRemaining <= 5:
        if player == 'X':
            playerPositionList = playerX_positions
        else:
            playerPositionList = playerO_positions
        
        for winningCombo in winningCombinations:
            i = 0
            for player_position in playerPositionList:

                if player_position in winningCombo:
                    i += 1

                    if i == 3:
                        print(f"Player {player} wins the game!")
                        return True
    
    return False

gameInit(gameBoard)

# range is 9 as there are only a maximum of 9 possible moves in a game of tic-tac-toe
while True:

    # Assign an empty list to a variable to notify user of available moves
    availableMoves = []
    currentPlayer = turn

    # loop through gameBoard dictionary and utilize dict_key to determine which have empty values.
    # Append the key to the list
    for key in gameBoard:
        if not gameBoard[key]:
            availableMoves.append(key)
    
    if len(availableMoves) == 0:
        print('Draw!! \n')
        break

    # Notify player of available moves and request an input
    print(f"Here are the moves available to you, player {turn}: {availableMoves}\n")
    playerMove = input(f"Where would you like to move?\n")
    print('\n')

    # Determine whether player-entered input is a valid key in the dictionary and if 
    # the key does not have an existing valid value.
    if playerMove in gameBoard and not gameBoard[playerMove]:
        gameBoard[playerMove] = turn

        if turn == 'X':
            playerX_positions.append(playerMove)
            turn = 'O'
        else:
            playerO_positions.append(playerMove)
            turn = 'X'
        
        gameInit(gameBoard)

        gameState = determineWinner(currentPlayer, len(availableMoves))

        if gameState:
            break

    else:
        gameInit(gameBoard)
        if not playerMove in gameBoard:
            print('That is an invalid move!!\n')
        else:
            print('That space is already occupied, please select another move!!\n')
            




