"""二叉树遍历
# 参考连接：https://zhuanlan.zhihu.com/p/33977566
"""

class BitNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False
        
class BitTree:
    def __init__(self):
        self.root = None
        self.bitList = []

    def add_bit_item(self, item):
        if not isinstance(item, BitNode):
            item = BitBode(item)
        if self.root is None:
            self.root = item
            self.bitList.append(item)
        else:
            rootNode = self.bitList[0]
            while True:
                if item.data < rootNode.data:
                    # 往左移
                    if rootNode.left == None:
                        rootNode.left = item
                        self.bitList.append(item)
                        break
                    else:
                        rootNode = rootNode.left
                elif item.data > rootNode.data:
                    # 往右移
                    if rootNode.right == None:
                        rootNode.right = item
                        self.bitList.append(item)
                        break
                    else:
                        rootNode = rootNode.right

    def front_traverse(self,root):
        if root == None:
            return None
        print(root.data)
        self.front_traverse(root.left)
        self.front_traverse(root.right)

def display_bitTree(bitTree):
    if not isinstance(bitTree, BitTree):
        raise ValueError("类型错误")
    for bit in bitTree.bitList:
        print(bit.data)

def middle_traverse(root):
    if root == None:
        return None
    middle_traverse(root.left)
    print(root.data)
    middle_traverse(root.right)

def last_traverse(root):
    if root == None:
        return None
    last_traverse(root.left)
    last_traverse(root.right)
    print(root.data)

def floor_traverse(root):
    # 按层次遍历
    from collections import deque
    q = deque()
    if root == None:
        return None
    q.append(root)
    while q:
        node = q.pop()
        print(node.data)
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
    

if __name__ == "__main__":
    node1 = BitNode(15)
    node2 = BitNode(9)
    node3 = BitNode(16)
    node4 = BitNode(8)
    node5 = BitNode(10)
    node6 = BitNode(17)
    node7 = BitNode(20)
    bitTree = BitTree()
    for i in [node1,node2,node3,node4,node5,node6,node7,]:
        bitTree.add_bit_item(i)
    
    display_bitTree(bitTree)
    # 15 9 16 8 10 17 20
    print("先序遍历：")
    bitTree.front_traverse(bitTree.root)
    print("中序遍历：")
    middle_traverse(bitTree.root)
    print("后序遍历：")
    last_traverse(bitTree.root)
    print("按层次遍历：")
    floor_traverse(bitTree.root)