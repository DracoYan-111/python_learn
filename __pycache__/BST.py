#创建一个构造函数
class BSTNode:
    def __init__(self, val=None):
        #将新节点的两个子节点初始化为None
        self.left = None     
        self.right = None
        self.val = val
#插入
    def insert(self, val):
        if not self.val:              #如果节点还没有值，我们可以只设置给定的值
            self.val = val
            return
        if self.val == val:   #如果我们尝试插入一个也存在的值，我们也可以简单地返回，因为这可以被视为“无操作”
            return 
        if val < self.val: #如果给定的值小于节点的值，并且我们已经有一个左子节点，那么我们递归调用我们的左子节点
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val) #如果我们还没有左子项，那么我们只需将给定值作为我们新的左项
            return
        if self.right:           #我们可以对右侧做同样的事情（但倒置）
            self.right.insert(val)
            return
        self.right = BSTNode(val)
        #获取最小值和最大值     遍历树的边缘以查找存储在其中的最小或最大值
        def get_min(self):
            current = self
            while current.left is not None:
                current = current.left
                return current.val
        def get_max(self):
            current = self
            while current.right is not None:
                current = current.right
                return current.val
        #删除
        def delete(self, val):

            if self == None:
               return self

            if val < self.val:

              self.left = self.left.delete(val)

              return self

            if val > self.val:

               self.right = self.right.delete(val)

               return self

            if self.right == None:

               return self.left

            if self.left == None:

               return self.right

            min_larger_node = self.right

            while min_larger_node.left:

             min_larger_node = min_larger_node.left

            self.val = min_larger_node.val

            self.right = self.right.delete(min_larger_node.val)

            return self
#存在
        def exists(self, val):
            if val == self.val:
                return True
            if val < self.val:
                if val.left == None:
                    return False
                return self.left.exists(val)
            if self.right == None:
                return False
            return self.left.exists(val)
    #按顺序排列
        def inorder(self, vals):
            if self.left is not None:
                self.left.inorder(vals)
            if self.val is not None:
                vals.append(self, val)
            if self.right is not None:
                self.right.inorder(vals)
                return vals
#预购
        def preorder(self, vals):
            if self.val is not None:
                vals.append(self, val) 
            if self.left is not None:
                self.left.preorder(vals)
            if self.right is not None:
                self.right.preorder(vals)
                return vals
#后交
        def postorder(self, vals):
            if self.left is not None:
                self.left.postorder(vals)
            if self.right is not None:
                self.right.postorder(vals)    
            if self.val is not None:
                vals.append(self, val)
                return vals
#使用BST
        def main():

           nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]

           bst = BSTNode()

           for num in nums:

            bst.insert(num)

            print("preorder:")

            print(bst.preorder([]))

            print("#")



            print("postorder:")

            print(bst.postorder([]))

            print("#")



            print("inorder:")

            print(bst.inorder([]))

            print("#")



            nums = [2, 6, 20]

            print("deleting " + str(nums))

           for num in nums:

            bst.delete(num)

            print("#")



            print("4 exists:")

            print(bst.exists(4))

            print("2 exists:")

            print(bst.exists(2))

            print("12 exists:")

            print(bst.exists(12))

            print("18 exists:")

            print(bst.exists(18))

#创建二叉树      
class binary_tree:
    def __init__(self, key):
        self.leftchild = None
        self.rightchild = None
        self.key = key
    class binary_tree:
        def __init__(self):    #生成一棵树来保存值
            self.root = None
#删除树
    def add(self, value):      #向树添加数据项的函数
        if self.key is None:  
            self.key = 2     #开始向二叉树添加元素
            return
        if self.key == value:
            return 
        if value < self.key:
            if self.leftchild:
                self.leftchild.add(value)
            else:
                self.leftchild = binary_tree(value)
        else:
            if self.rightchild:
                self.rightchild.add(value)
            else:
                self.rightchild = binary_tree(value)
#在树中添加数据
    root = binary_tree(50)
    elements = {20,56,3,4,7,10,17,20}
    for i in elements:
        root.add(i)
    root.search(50)
    #检查空节点
    def check(self, value):
        if self.key is None:
            self.key = value
    # 在树中搜索节点
    def search(self, value):
      if self.key == value:     #check if value is equal to the key val
        print("The node is present")
        return
      if value < self.key:    #Here left subtree can be empty or it can contain one or more nodes
        if self.leftchild:   #this condition is true if left subtree exists
            self.leftchild.search(value)
        else:
          print("The node is empty in the tree!")
      else:
        if self.rightchild:
            self.rightchild.search(value)   #search for all the values in the rightchild
            return True
        else:   
            print("The node is empty in the tree!")        


#创建二叉树
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    # 如果二叉搜索树为空，则创建一个新节点并将其声明为根
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # 如果newValue小于根中数据的值，则将其添加到左子树并递归进行
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
       # 如果newValue大于根中数据的值，则将其添加到右子树并递归进行
        root.rightChild = insert(root.rightChild, newValue)
    return root


root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)
node1 = root
node2 = node1.leftChild
node3 = node1.rightChild
node4 = node2.leftChild
node5 = node2.rightChild
node6 = node3.leftChild
node7 = node3.rightChild
print("Root Node is:")
print(node1.data)

print("left child of the node is:")
print(node1.leftChild.data)

print("right child of the node is:")
print(node1.rightChild.data)

print("Node is:")
print(node2.data)

print("left child of the node is:")
print(node2.leftChild.data)

print("right child of the node is:")
print(node2.rightChild.data)

print("Node is:")
print(node3.data)

print("left child of the node is:")
print(node3.leftChild.data)

print("right child of the node is:")
print(node3.rightChild.data)

print("Node is:")
print(node4.data)

print("left child of the node is:")
print(node4.leftChild)

print("right child of the node is:")
print(node4.rightChild)

print("Node is:")
print(node5.data)

print("left child of the node is:")
print(node5.leftChild)

print("right child of the node is:")
print(node5.rightChild)

print("Node is:")
print(node6.data)

print("left child of the node is:")
print(node6.leftChild)

print("right child of the node is:")
print(node6.rightChild)

print("Node is:")
print(node7.data)

print("left child of the node is:")
print(node7.leftChild)

print("right child of the node is:")
print(node7.rightChild)

def search(root, value):
    # node is empty
    if root is None:
        return False
    # 如果元素等于要查找的元素
    elif root.data == value:
        return True
    # 查找的元素小于当前节点
    elif root.data > value:
        return search(root.leftChild, value)
    # 要查找的元素大于当前节点
    else:
        return search(root.rightChild, value)
root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)
print("53 is present in the binary tree:", search(root, 53))
print("100 is present in the binary tree:", search(root, 100))






