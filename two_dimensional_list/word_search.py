def search_helper(index,i,j,board,word):
    if index==len(word):
        return True
    if i<len(board) and j<len(board[0]) and word[index]==board[i][j]:
        curr=board[i][j]
        board[i][j]=None
        if search_helper(index+1,i+1,j,board,word)\
                or search_helper(index+1,i-1,j,board,word) \
                or search_helper(index+1,i,j+1,board,word) \
                or search_helper(index+1,i,j-1,board,word):
            return True
        board[i][j]=curr
    return False

def search(board,word):
    row=len(board)
    col=len(board[0])
    for i in range(row):
        for j in range(col):
            return search_helper(0,i,j,board,word)

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"
print(search(board,word))

