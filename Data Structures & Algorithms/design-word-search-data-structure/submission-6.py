from collections import deque
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch in current.children:
                current = current.children[ch]
            else:
                current.children[ch] = TrieNode()
                current = current.children[ch]
        current.end = True

    def search(self, word: str) -> bool:
        q = deque([(self.root, 0)])
        while q:
            current, i = q.popleft()
            if i == len(word):
                if current.end:
                    return True
                continue

            ch = word[i]

            if ch in current.children:
                q.append((current.children[ch], i + 1))
            elif ch == ".":
                for ch in current.children:
                    q.append((current.children[ch], i + 1))
                

        return False