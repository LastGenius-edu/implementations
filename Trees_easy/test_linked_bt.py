from linked_binary_tree import LinkedBinaryTree

test_tr = LinkedBinaryTree(' a' )
#test_tr.is_empty()
print(test_tr)
print("root_val ", test_tr.get_root_val())
print("left_child ", test_tr.get_left_child())
test_tr.insert_left(' b' )
print("left_child ", test_tr.get_left_child())
print("left_child().get_root_val ", test_tr.get_left_child().get_root_val())

test_tr.insert_left(' bb' )
print("left_child ", test_tr.get_left_child())
print("left_child().get_root_val ", test_tr.get_left_child().get_root_val())

test_tr.insert_right(' c' )
print("right_child ", test_tr.get_right_child())
print("right_child().get_root_val ", test_tr.get_right_child().get_root_val())
test_tr.get_right_child().set_root_val(' hello' )
print("right_child().get_root_val", test_tr.get_right_child().get_root_val())

test_tr.inorder()

a_node = LinkedBinaryTree('A')
a_node.insert_left('B')
a_node.insert_right('C')

b_node = a_node.left_child
b_node.insert_right('D')

c_node = a_node.right_child
c_node.insert_left('E')
c_node.insert_right('F')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.key)
print(b_node.key)
print(c_node.key)
print(d_node.key)
print(e_node.key)
print(f_node.key)

print("inorder")
a_node.inorder()
print("preorder")
a_node.preorder()
print("postorder")
a_node.postorder()