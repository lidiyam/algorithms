class Solution(object):
    
    def dfs(self, i, j, curr, board, word):
        if  i >= len(board) or \
            j >= len(board[0]) or \
            i < 0 or j < 0: 
            return False
        if curr == len(word): return True
        if board[i][j] == word[curr] and (curr+1) == len(word): return True
        if board[i][j] == word[curr]:
            temp = board[i][j]
            board[i][j] = '#'
            ret =       self.dfs(i+1,j, curr+1,board, word) or \
                        self.dfs(i,j+1, curr+1,board, word) or \
                        self.dfs(i-1,j, curr+1,board, word) or \
                        self.dfs(i,j-1, curr+1,board, word)
            board[i][j] = temp
            return ret
        return False
        
    def exist(self, board, word):
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(i, j, 0, board, word):
                    return True
        return False


if __name__ == '__main__':
    inputD = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"

    print Solution().exist(inputD, word)
