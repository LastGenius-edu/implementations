from linked_binary_tree import LinkedBinaryTree

a = LinkedBinaryTree()
print ('!!!')
a._add_root('!!')
a._add_left(a.root(),'????')
print ('!')
print(a.left(a.root()).element())
a._delete(a.left(a.root()))

