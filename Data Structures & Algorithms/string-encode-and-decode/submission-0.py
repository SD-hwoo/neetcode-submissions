class Solution:

    def encode(self, strs: List[str]) -> str:
        word = []
        for s in strs:
            word.append(chr(len(s)))
            for ch in s:
                new = chr(ord(ch) + 3)
                word.append(new)
        print(''.join(word))
        return ''.join(word)
    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            word_length = ord(s[i])
            i += 1
            word = []
            for j in range(i, word_length + i):
                new = chr(ord(s[j]) - 3)
                word.append(new)
            words.append(''.join(word))
            i += word_length

        return words
