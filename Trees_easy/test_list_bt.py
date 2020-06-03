from list_binary_tree import *

test_tr = ListBinaryTree(3)
insertLeft(test_tr,4)
print(test_tr)
insertLeft(test_tr,5)
print(test_tr)
insertRight(test_tr,6)
print(test_tr)
insertRight(test_tr,7)
print(test_tr)
left_child = getLeftChild(test_tr)
print(left_child)

setRootVal(left_child,9)
print(test_tr)
insertLeft(left_child,11)
print(test_tr)
print(getRightChild(getRightChild(test_tr)))

x = ListBinaryTree('a')
insertLeft(x,'b')
insertRight(x,'c')
insertRight(getRightChild(x),'d')
insertLeft(getRightChild(getRightChild(x)),'e')

print(x)