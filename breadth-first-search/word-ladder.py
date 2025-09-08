from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        if not wordList:
            return 0
        
        word_set = set(wordList)
        
        return self.bidirectionalBFS(beginWord, endWord, word_set)
    
    def bidirectionalBFS(self, beginWord: str, endWord: str, word_set: set) -> int:

        if beginWord == endWord:
            return 1
        
        begin_set = {beginWord}
        end_set = {endWord}
        
        visited = {beginWord, endWord}
        
        steps = 1
        
        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            next_set = set()
            
            for word in begin_set:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word in end_set:
                            return steps + 1
                        
                        if new_word in word_set and new_word not in visited:
                            next_set.add(new_word)
                            visited.add(new_word)
            
            begin_set = next_set
            steps += 1
        
        return 0