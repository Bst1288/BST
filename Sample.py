class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                else:
                    if data > cur.data:
                        if cur.right == None:
                            cur.right = Node(data)
                            break
                        else:
                            cur = cur.right
        return self.root

    def printOut(self,node,level = 0):
        if node != None:
            self.printOut(node.right, level+1)
            print('     '*level, node)
            self.printOut(node.left, level+1)

    def checkPosition(self,node,data):
        if node == None:
            return 'Not exist'
        else:
            if data == node.data:
                if data == self.root.data:
                    return 'root'
                if node.left == None and node.right == None:
                    return 'leaf'
                else:
                    return 'inner'
            else:
                s = self.checkPosition(node.left,data)+self.checkPosition(node.right,data)
                s = s.replace('Not exist','')
                if s == '':
                    s = 'Not exist'

        return s

    def delete(self,root,data):
        r = self.root

        if root == None:
            return 'Error!'
        
        if r.left == None and r.right == None and r.data == data:
            r = None
        elif r.left != None and r.data == data:
            r = r.right
        elif r.right != None and r.data == data:
            r = r.left
        
        if data != root.data:
            if data < root.data:
                root.data = self.delete(root.left, data)
            else:
                root.data = self.delete(root.right, data)
        else:
            if root.left == None:
                root = root.right
                return root
            elif root.right == None:
                root = root.left
                return root
            else:
                c = root.right
                while c.left != None:
                    c = c.left
                root.data = c.data
                root.right = self.delete(root.right,c.data)

    def Ranking(self,node,data):
        if node == None:
            return 0
        
        rank = 0
        rank += self.Ranking(node.left,data)
        if data >= node.data:
            rank += 1
        rank += self.Ranking(node.right,data)

        return rank

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def height(h):
    if h == None:
        return -1
    else:
        return 1 + max(height(h.left),height(h.right))

def father(r,data):
    if r.data == data:
        return 'None because '+str(data)+' is root'
    if r.left == r.right == None:
        return 'Not found data'
    if (r.left != None and r.left.data == data)or(r.right != None and r.right.data == data):
        return r
    if data < r.data:
        return father(r.left,data)
    if data > r.data:
        return father(r.right,data)

#father
tree = BST()
inp,data = input('Enter :').split('/')

for i in inp.split():
    t = tree.insert(int(i))
tree.printOut(t)

f = father(t, int(data))
print(f)
'''
#height
tree = BST()
inp = [int(i) for i in input('Enter : ').split()]
for i in inp:
    t = tree.insert(i)
print('height is ',height(t))
'''

'''
#ranking
tree = BST()
inp,data = input('Enter : ').split('/')
for i in inp.split():
    t = tree.insert(int(i))
tree.printOut(t)
r = tree.Ranking(t,int(data))
print('Rank of ',data,' is ',str(r))
'''

'''
#delete
tree = BST()
data = input("Enter Input : ").split(",")
for i in data:
    sym = i.split(' ')

    if sym[0] == 'i':
        print('insert ' + sym[1]) #พิมพ์คำ insert ตามด้วยค่าที่ต้องการจะเพิ่มเข้า
        tree.insert(int(sym[1])) #เพิ่มค่านั้นลงไปใน tree
        printTree90(tree.root) #print tree ออกมาอีกรอบเมื่อแสดงหลังแก้ไขแล้ว
    elif sym[0] == 'd':
        print('delete '+ sym[1])
        tree.delete(tree.root, int(sym[1]))
        printTree90(tree.root)
'''

'''
#checkPosition
tree = BST()
inp = [int(i) for i in input('Enter : ').split()]
for i in range(1,len(inp)):
    t = tree.insert(inp[i])
tree.printOut(t)
print(inp[0], 'is',tree.checkPosition(tree.root,inp[0]))
'''

'''
#insert
tree = BST()
inp =
for i in inp:
    t = tree.insert(i)
tree.printOut(t)
'''