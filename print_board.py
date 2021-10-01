tokens = ["X","O"]
length = 9
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

board = [i for i in range(1,length+1)]

rows = int(length ** 0.5)
mid = (length-1)//2
board[mid] = 'X'
size = len(board)
print("board has {0} cells".format(size))
print(build_banner(length))
for i in range(rows):
    print(build_border(length))
    for j in range(rows):
        print(format_value(length,board[i*rows+j]), end=" ")
    print("|")
    print(build_border(length))
    print(build_banner(length))

