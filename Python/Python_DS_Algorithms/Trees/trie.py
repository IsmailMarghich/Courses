class TrieNode:
    def __init__(self):
        self.children = {} #we will be strong the children in dictionaries
        self.endOfString = False #wether we are at the end of a string or not

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word): #function to insert into a trie
        currrent = self.root
        for i in word: #we iterate over each character in the string
            char = i
            node = currrent.children.get(char) #we look if the letter already exists
            if node == None: #otherwise we add each character as a node to the tree
                node = TrieNode()
                currrent.children.update({char:node})
            currrent = node
        currrent.endOfString = True #after the word has been inserted, we mark it as the end of a string
        print('Successfully inserted')

    def searchString(self, word): #function to search through a trie
        currentNode = self.root #set a starting node
        for i in word: #iterate over each letter in the word
            node = currentNode.children.get(i) #look it up in the dictionary
            if node == None: #if we cant find a letter, it doesnt exist
                return False
            currentNode = node #continue to the next node in dictionary
        
        if currentNode.endOfString == True: #if we reach end of string, that means the word exists
            return True
        else:
            return False #otherwise we return false because the word is partially there

def deleteString(root, word, index): #when deleting a string from a Trie, there are three scenarios
        char = word[index]
        currentNode = root.children.get(char)
        Deletable = False
        if len(currentNode.children) > 1: #Some other prefix of string is the same as the one we want to delete
            deleteString(currentNode, word, index)
            return False
        if index == len(word) - 1: #the string is a prefix of another string
            if len(currentNode.children) >= 1:
                currentNode.endOfString = False
                return False
            else:
                root.children.pop(char)
                return True
        if currentNode.endOfString == True: #other string is a prefix of this string
            deleteString(currentNode, word, index + 1)
            return False

        Deletable = deleteString(currentNode, word, index+1) #not any node depends on this string
        if Deletable == True:
            root.children.pop(char)
            return True
myTrie = Trie()
myTrie.insertString('App')
myTrie.insertString('Appl')
print(myTrie.searchString('Ap')) #returns False
print(myTrie.searchString('App')) #return True
deleteString(myTrie.root, 'App', 0) #delete the word App
print(myTrie.searchString('App')) #returns false because we deleted App
#Because of the way a Trie makes use of the same node to store letters used by multiple words
#It means searching through a string is O(M) time complexity, where M is the maximum size of a string in the Trie, making it very efficient
#The down side is the storage requirment, since you will be needing to store all the letters and wether a node is at the end of a string or not