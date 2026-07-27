# Last updated: 7/27/2026, 10:19:03 AM
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.isEnd = False
5
6
7class WordDictionary:
8
9    def __init__(self):
10        self.root = TrieNode()
11
12    def addWord(self, word):
13        node = self.root
14
15        for ch in word:
16            if ch not in node.children:
17                node.children[ch] = TrieNode()
18
19            node = node.children[ch]
20
21        node.isEnd = True
22
23    def search(self, word):
24
25        def dfs(node, index):
26
27            if index == len(word):
28                return node.isEnd
29
30            ch = word[index]
31
32            if ch == '.':
33                for child in node.children.values():
34                    if dfs(child, index + 1):
35                        return True
36                return False
37
38            if ch not in node.children:
39                return False
40
41            return dfs(node.children[ch], index + 1)
42
43        return dfs(self.root, 0)