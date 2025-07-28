class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def preorder(node): #전위 순회
    if node is None:
        return
    print(node.val, end=' ')    # 루트
    preorder(node.left)         # 왼쪽
    preorder(node.right)        # 오른쪽
def inorder(node): #중위 순회
    if node is None:
        return
    inorder(node.left)          # 왼쪽
    print(node.val, end=' ')    # 루트
    inorder(node.right)         # 오른쪽
def postorder(node): #후위순회
    if node is None:
        return
    postorder(node.left)        # 왼쪽
    postorder(node.right)       # 오른쪽
    print(node.val, end=' ')    # 루트
