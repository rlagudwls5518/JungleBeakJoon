class Node:
    def __init__(self):
        self.children = {} # 자식 노드 저장 할 dict
        self.is_end = False # 단어의 끝 표시

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
trie = Trie()
trie.insert("cat")
trie.insert("cap")
trie.insert("can")

assert trie.search("cat") == True
assert trie.search("car") == False
assert trie.starts_with("ca") == True
assert trie.starts_with("dog") == False