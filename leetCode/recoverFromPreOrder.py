import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    
if __name__ == "__main__":
    traversal = "1-2--3--4-5--6--7"
    i = 0
    n = len(traversal)
    tree = []

    while i < n:
        depth = 0
        while i < n and traversal[i] == '-':
            depth += 1
            i += 1

        numStr = ''
        while i < n and traversal[i].isdigit():
            numStr += traversal[i]
            i += 1

        if numStr:
            tree.append((int(numStr), depth))
    
    

    




