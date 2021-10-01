from random import randint

tokens = ["X","O"]

# a list model data structure length
length = 9
board = [i for i in range(1,length+1)]
rows = int(length ** 0.5)
mid = (length-1)//2
board[mid] = 'X'
size = len(board)
print("board has {0} cells".format(size))

def build_border (n):
    spaces = int(n ** 0.5)
    border = ""
    for i in range(spaces):
        border = border + "|       "
    border = border + "|"
    return border

def build_banner(n):
    spaces = int(n ** 0.5)
    banner = ""
    for i in range(spaces):
        banner = banner + "+-------"
    banner = banner + "+"
    return banner

def format_value(length, val):
    is_token = val in tokens
    num = -1
    if not is_token:
        num = int(val)
    if num < 10 | is_token:
        return "|   {0}  ".format(val)
    return "|   {0} ".format(val)


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(build_banner(length))
    for i in range(rows):
        print(build_border(length))
        for j in range(rows):
            print(format_value(length, board[i*rows+j]), end=" ")
        print("|")
        print(build_border(length))
        print(build_banner(length))


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    move = int(input("Enter your move: "))
    
    # validate
    while move > length or move < 1:
        print("Invalid move")
        move = int(input("Enter your move:"))
    val = board[move - 1]
    while val in tokens:
        print("Invalid move")
        move = int(input("Enter your move:"))
        val = board[move - 1]
    board[move - 1] = "O"

def make_list_of_free_fields(board):
    free_flds = []
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    for i in range(len(board)):
        if board[i] not in tokens:
            row = i//rows
            col = i%rows
            free_flds.append((row,col))
    return free_flds
    
def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    count = 0
    winners = [[0,4,8],[0,3,6],[0,1,2],[2,4,6],[3,4,5],[1,4,7],[2,5,8],[6,7,8]]
    for win in winners:
        for index in win:
            if board[index] == sign:
                count+=1
        if count == 3:
            return True
        count = 0
    return False
    

def draw_move(board):
    # The function draws the computer's move and updates the board.
    move = randint(0,length-1)
    val = board[move]
    while val in tokens:
        move = randint(0,length-1)
        val = board[move]
    board[move] = "X"
    display_board(board)

victory = False
display_board(board)
while not victory or len(make_list_of_free_fields(board)) != 0:
    enter_move(board)
    display_board(board)
    victory = victory_for(board, "O")
    if victory:
        break
    draw_move(board)
    victory = victory_for(board, "X")
    if victory:
        break
if victory: 
    print("Winner")
display_board(board)
    
