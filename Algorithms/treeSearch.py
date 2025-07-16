import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def insertTree(self, root, data):
        newNode = Node(data)
        if root is None:
            return newNode
        
        if data <= root.data:
            root.left = self.insertTree(root.left, data)
        else:
            root.right = self.insertTree(root.right, data)
        
        return root
    
    def insert(self, data):
        self.root = self.insertTree(self.root, data)

    def pre_order(self):
        self._pre_order_traversal(self.root)
        print()  

    def _pre_order_traversal(self, root):
        if root:
            print(root.data, end=' ')
            self._pre_order_traversal(root.left)
            self._pre_order_traversal(root.right)
    
    def BFT(self):
        if self.root is None:
            print("The tree is empty")
        else:
            q = queue.Queue()
            q.put(self.root)
            while not q.empty():
                temp = q.get()
                print(temp.data, end=' ')
                
                if temp.left is not None:
                    q.put(temp.left)
                if temp.right is not None:
                    q.put(temp.right)
            print()
    
    def DST(self):
        if self.root is None:
            print("the tree is empty")
            return

        stack = [(self.root, 0)]

        while stack:
            node, depth = stack.pop()
            print(f"{'-'*depth}{node.data}", end='')

            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))
            

        print()  

if __name__ == "__main__":
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(3)
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)

    tree.pre_order()  

