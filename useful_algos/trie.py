class TrieNode(object):
    def __init__(self, char):
        # whether this can be the end of a word
        self.is_end = False
        # char stored at this node of the trie
        self.char = char
        # a counter to indicate how many times this word has been inserted
        # (if is_end = True)
        self.counter = 0
        # a dictionary of child nodes, keys are chars, values are nodes
        self.children = {}
class Trie(object):
    def __init__(self):
        # The trie has at least the root node.
        # The root node does not store any character
        self.root = TrieNode("")
    def insert(self, word):
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child 
        # for the current node
        node = self.root
        for i in range(len(word)):
            if word[i] in node.children:
                # we found the next char in the children, advance node
                node = node.children[word[i]]
            else:
                # we have not found the char, need to add new nodes
                node.children[word[i]] = TrieNode(word[i])
                node = node.children[word[i]]
        # mark end node as containing word
        node.is_end = True
        # increment counter of seeing end of word
        node.counter += 1
        
    def query(self, x):
        # Given an input (a prefix), retrieve all words stored in
        # the trie with that prefix, sort the words by the number of 
        # times they have been inserted
        
        self.output = []
        node = self.root
        # check if prefix is the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot find x in trie, return empty list
                return []
        # traverse the trie to get all candidates
        self.DFS(node, x)
        # sort the results in reverse order and return 
        return sorted(self.output, key=lambda x: x[1], reverse=True)
    
    def DFS(self, node, prefix):
        # DFS traversal of the trie
        # node: the node to start with
        # prefix: the current prefix, for tracing a word while traversing the trie
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        for child in node.children.values():
            self.DFS(child, prefix + node.char)
                    