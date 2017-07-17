# 井字棋
import random


def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    """选择使用的符号O或者X"""
    letter = ''
    while not (letter == 'O' or letter == 'X'):
        print('Do you want to be O or X?')
        letter = input().upper()

    if letter == 'X':
        # 前面的是用户,后面是电脑的图案
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # 谁先走
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    # 使用列表传入移动，列表是引用的，所以都会改变
    board[move] = letter


def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter))


def getBoardCopy(board):
    # 拷贝一个board
    dupeBorad = []

    for i in board:
        dupeBorad.append(i)

    return dupeBorad


def isSpacceFree(board, move):
    # 判断移动的步格是不是空，可移动的
    return board[move] == ' '


def getPlayerMove(board):
    # 用户输入

    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpacceFree(board, int(move)):
        print('What is your next move?(1-9)')
        move = input()

    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # 返回一个有效的移动步数，电脑计算
    # 若没有返回None
    possibleMoves = []

    for i in movesList:
        if isSpacceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # 获取到棋盘和电脑的图形，之后电脑决定如何移动
    if computerLetter == 'X':
        playerLetter == 'O'

    else:
        playerLetter == 'X'

    # 电脑逻辑
    # 首先检查下一步是否能赢，返回下一步
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpacceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # 如果用户下一步要赢，要阻止
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpacceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # 角落有空的，占一个角
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # 中间没填时，填掉中间
    if isSpacceFree(board, 5):
        return 5

    # 占据旁边
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # 判断棋盘是否满了
    for i in range(1, 10):
        if isSpacceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # 重置棋盘
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # 玩家回合
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:

            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
