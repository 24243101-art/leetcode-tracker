# Last updated: 7/9/2026, 10:07:56 AM
class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_sentences = dfs(end)
                    for rest in rest_sentences:
                        if rest:
                            sentences.append(word + " " + rest)
                        else:
                            sentences.append(word)
            memo[start] = sentences
            return sentences

        return dfs(0)
