class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def _find_words_with_prefix(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)
        
        for char, child in node.children.items():
            self._find_words_with_prefix(child, prefix + char, result)

    def list_words_with_prefix(self, prefix):
        node = self.root
        result = []
        for char in prefix:
            if char not in node.children:
                return result  # No words start with this prefix
            node = node.children[char]
        self._find_words_with_prefix(node, prefix, result)
        return result

    def remove(self, word):
        def _remove(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False  # Word not found
                node.is_end_of_word = False  # Unmark the end of word
                return len(node.children) == 0  # If no children, remove node
            char = word[index]
            if char not in node.children:
                return False  # Word not found
            child_node = node.children[char]
            should_delete_child = _remove(child_node, word, index + 1)
            if should_delete_child:
                del node.children[char]  # Delete the child node if no other word depends on it
                return len(node.children) == 0 and not node.is_end_of_word
            return False
        _remove(self.root, word, 0)

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
trie.insert("banana")
trie.insert("batman")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("batman"))  # Output: True

trie.remove("app")
print(trie.search("app"))    # Output: False
print(trie.search("apple"))  # Output: True

print(trie.list_words_with_prefix("app"))  # Output: ['apple']
print(trie.list_words_with_prefix("ba"))   # Output: ['bat', 'banana', 'batman']
