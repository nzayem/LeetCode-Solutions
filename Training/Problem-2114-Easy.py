# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/


class Solution:

    def mostWordsFound(self, sentences: List[str]) -> int:

        return (max([len(sentence.split(' ')) for sentence in sentences]))
