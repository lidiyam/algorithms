class Solution(object):
    def wordMatch(self, word, wordList, queue):
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append(next_word)       


    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList: return 0
        wordList = set(wordList)
        queue = []
        length = 0
        queue.append(beginWord)

        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                if word == endWord: return length+1
                self.wordMatch(word, wordList, queue)
            length += 1

        return 0


if __name__ == '__main__':
    print Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])