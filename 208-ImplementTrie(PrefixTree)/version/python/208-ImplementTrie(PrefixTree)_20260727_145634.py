# Last updated: 7/27/2026, 2:56:34 PM
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.isEnd = False
5
6
7class Trie:
8
9    def __init__(self):
10        self.root = TrieNode()
11
12    def insert(self, word):
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
24        node = self.root
25
26        for ch in word:
27            if ch not in node.children:
28                return False
29
30            node = node.children[ch]
31
32        return node.isEnd
33
34    def startsWith(self, prefix):
35        node = self.root
36
37        for ch in prefix:
38            if ch not in node.children:
39                return False
40
41            node = node.children[ch]
42
43        return True