''' linked (node based) implementation binary tree ADT '''
from collections import deque

class BinaryTree:
    '''Lineked nodes in binary tree'''
    class _Node:
        __slots__='_element','_parent','_left','_right'

        def __init__(self,element,parent=None,left=None,right=None):
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right

    def __init__(self):
        self._root=None
        self._size=0

    def __len__(self):
        return self._size
    # no node
    def is_empty(self):
        return len(self)==0

    def root(self):
        return self._root

    def parent(self,node):
        return node._parent

    def left(self,node):
        return node._left

    def right(self,node):
        return node._right

    def sibling(self,node):
        parent=self.parent(node)
        if parent is None:
            return None
        if node is self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self,node):
        result=[]
        if self.left(node) is not None:
            result.append(self.left(node))
        if self.right(node) is not None:
            result.append(self.right(node))
        return result

    def count_children(self,node):
        count=0
        if self.right(node) is not None:
            count+=1
        if self.left(node) is not None:
            count+=1
        return count
    
    def count_nodes(self,node):
        if node is None:
            return 0
        return 1+ self.count_nodes(self.left(node))+ self.count_nodes(self.right(node))

    def count_leaves(self,node):
        if node is None:
            return 0
        if self.count_children(node)==0:
            return 1
        return self.count_leaves(self.left(node))+self.count_leaves(self.right(node))
    
    def is_root(self,node):
        return self._root is node
    
    def is_leaf(self,node):
        return self.count_children(node)==0

    def depth(self,node):
        if self.is_root(node):
            return 0
        return 1 +self.depth(self.parent(node))

    def height(self,node):
        if node is None:
            return 0

        if self.is_leaf(node):
            return 0
        return 1+ max(self.height(i) for i in self.children(node))

    #----TRAVERSAL----
    # ROOT--LEFT--RIGHT
    def preorder(self,node=None,result=None):
        if result is None:
            result=[]
        if node is None:
            if self.is_empty():
                return
            node=self.root()
        result.append(node)
        for i in self.children(node):
            self.preorder(i,result)
        return result
    # LEFT-RIGHT-ROOT
    def postorder(self,node=None,result=None):
        if result is None:
            result=[]
        if node is None:
            if self.is_empty():
                return
            node=self.root()

        for i in self.children(node):
            self.postorder(i,result)
        result.append(node)
        return result   
    #LEFT-ROOT-RIGHT
    def inorder(self,node=None,result=None):
        if result is None:
            result=[]
        if node is None:
            if self.is_empty():
                return
            node=self.root()

        if self.left(node) is not None:
            self.inorder(self.left(node),result)
        result.append(node)
        if self.right(node) is not None:
            self.inorder(self.right(node),result)
        return result
    # TREE LEVEL ORDER
    def levelorder(self,node=None,result=None):
        result=[]

        if not self.is_empty() :
            fringe=deque()
            fringe.append(self.root())
            while fringe:
                node=fringe.popleft()
                result.append(node)
                for i in self.children(node):
                    fringe.append(i)
        return result

    #def count_nodes(self):
    #return len(self.preorder())

    #def count_leaves(self):
    #count = 0
    # for node in self.preorder():
    #if self.num_children(node) == 0:
    #count += 1
    #return count

    def addroot(self,e):
        if self._root is not None:
            raise ValueError("root exist")
        self._size=1
        self._root=self._Node(e)
        return self._root

    def addleft(self,node,e):
        if node._left is not None:
            raise ValueError("left child exist")
        self._size+=1
        node._left=self._Node(e,parent=node)
        return node._left

    def addright(self,node,e):
        if node._right is not None:
            raise ValueError("right child exist")
        self._size+=1
        node._right=self._Node(e,parent=node)
        return node._right

    def replace(self,node,e):
        old=node._element
        node._element=e
        return old

    def delete(self,node):
        if self.count_children(node)>=2:
            raise ValueError("node has 2 children")
        child=node._left if node._left else node._right
        if child is not None:
            child._parent=node._parent
        if node is self._root:
            self._root=child
        else:
            parent=node._parent
            if node is parent._left:
                parent._left=child
            else:
                parent._right=child
        self._size-=1
        node._parent=node
        return node._element
    



    


            

