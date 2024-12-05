class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.count =0
    def insert(self, data):
        n = Node(data)
        if self.root == None:
            self.root = n
            self.count +=1
        else:
            temp = self.root
            while True:
                if temp.item>data and temp.left ==None:
                    print(temp.item)
                    temp.left =n
                    self.count +=1
                    break

                elif temp.item>data and temp.left !=None:
                    temp = temp.left

                elif temp.item<data and temp.right == None:
                    print(temp.item)
                    temp.right = n
                    self.count +=1
                    break
                
                elif temp.item<data and temp.right != None:
                    temp = temp.right
    
    def search(self, data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if root is None or data == root.item:
            return root
        elif data <root.item:
            return self.rsearch(root.left,data)
        elif data >root.item:
            return self.rsearch(root.right,data)

    def inorder(self):
        self.rinorder(self.root)

    def rinorder(self,root):
        # 1st try
        # if root.left==None and root.right==None:
        #     print(root.item)
        # if root.left is not None:
        #     self.rinorder(root.left)
        # if root.left and root.right==None:
        #     print(root.item)
        # if root.left==None and root.right:
        #     print(root.item)
        # if root.left and root.right:
        #     print(root.item)
        # if root.right is not None:
        #     self.rinorder(root.right)

        #2nd Try
        # if root.left:
        #     self.rinorder(root.left)
        # if root:
        #     print(root.item)
        # if root.right:
        #     self.rinorder(root.right)

        #3Try
        if root:
            self.rinorder(root.left)
            print(root.item)
            self.rinorder(root.right)

    def preorder(self):
        self.Rpreorder(self.root)

    def Rpreorder(self,root):
        if root:
            print(root.item)
            self.Rpreorder(root.left)
            self.Rpreorder(root.right)
            
    def postorder(self):
        self.Rpostorder(self.root)

    def Rpostorder(self,root):
        if root:
            self.Rpostorder(root.left)
            self.Rpostorder(root.right)
            print(root.item)
    
    def min_value(self, tempp):
        temp = tempp
        while temp.left is not None:
            temp = temp.left
        print(temp.item)
        return temp.item

    def max_value(self, tempp):
        temp = tempp
        while temp.right is not None:
            temp = temp.right
        print(temp.item)
        return temp.item
    
    def delete(self, data):
        self.Rdelete(self.root, data)

    def Rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left= self.Rdelete(root.left, data)
        elif data > root.item:
            root.right =  self.Rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item == self.min_value(root.right)
            self.Rdelete(root.right, root.item)
        return root
    
    def size(self):
        print(self.count)
tree = BST()
tree.insert(60)
tree.insert(30)
tree.insert(20)
tree.insert(45)
tree.insert(70)
tree.insert(10)
tree.insert(90)
print(tree.search(10))
tree.inorder()
print("..............................")
tree.preorder()
print("..............................")
tree.postorder()
print("..............................")
tree.size()