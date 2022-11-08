class Node :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) :
        return str(self.data)

class BST :
    def __init__(self) :
        self.root = None

    def insert(self,data) :
        if self.root == None :
            self.root = Node(data)
        else :
            now = self.root
            while True :
                if data < now.data :
                    if now.left == None :
                        now.left = Node(data)
                        break
                    else :
                        now = now.left
                else :
                    if now.right == None :
                        now.right = Node(data)
                        break
                    else :
                        now = now.right
        return self.root

    def delete(self,node,data) :
        if self.root == None :
            return
        elif self.root.data == data :
            if self.root.left == None and self.root.right == None :
                self.root == None 
            elif self.root.left == None :
                self.root = self.root.right
            elif self.root.right == None :
                self.root = self.root.left

        if node.data != data :
            if data < node.data :
                node.left = self.delete(node.left,data)
            else :
                node.right = self.delete(node.right,data)
        else :
            if node.left == None :
                node = node.right
                return node
            elif node.right == None :
                node = node.left
                return node
            else :
                now = node.right
                while now.left != None :
                    now = now.left
                node.data = now.data
                node.right = self.delete(node.right,now.data)
        return node

def isBinsrySearchTree(root) :
    def isBST(node,min=-1,max=101) : # กรณีนี้ในโจทย์ให้ถ้าข้อมูล < 0 หรือ > 100 จะ return false
        if node.data <= min or node.data >= max :
            return False

        left = True
        right = True

        if node.left != None :
            left = isBST(node.left,min,node.data)

        if node.right != None :
            right = isBST(node.right,node.data,max)

        return left and right

    if root == None :
        return True

    return isBST(root)

def printTree(node,level = 0) :
    if node != None :
        printTree(node.right,level+1)
        print("     " * level ,node)
        printTree(node.left,level+1)

inp = [ int(i) for i in [ 0,1,2,3,4,5,6 ] ]
bst = BST()

for i in inp :
    root = bst.insert(i)

printTree(bst.root)
bst.delete(bst.root,0)
printTree(bst.root)
print(isBinsrySearchTree(root))