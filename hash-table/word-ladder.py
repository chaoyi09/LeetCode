from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        front = {beginWord}
        back = {endWord}
        L = len(beginWord)
        step = 1

        while front and back:
            if len(front) > len(back):
                front, back = back, front

            next_front = set()
            for w in front:
                w_list = list(w)
                for i in range(L):
                    original = w_list[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original:
                            continue
                        w_list[i] = c
                        nw = "".join(w_list)
                        if nw in back:
                            return step + 1
                        if nw in word_set:
                            next_front.add(nw)
                            word_set.remove(nw)
                    w_list[i] = original
            front = next_front
            step += 1

        return 0
