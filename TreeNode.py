from random import random
from Traversal import preorder
#~ from Traversal import preorder

class TreeNode:
    
    __slots__= {"key","left","right"}
    
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None
        

class BinaryTree:
    """
    funcion recursiva: puede invocarse a si misma para obtener un resultado
    punto de retorno y sigue en un ciclo hasta el objetivo
     """

    def __init__(self):
        self.root = None
        

    def is_empty(self):
        return (self.root is None)

    def insert(self, new_key):
        self.root = self.__insert(self.root, new_key)

    def __insert(self, subtree, new_key):
        """
        Método oculto que reconstruye los Trees
        """

        if subtree is None:
            subtree = TreeNode(new_key)
        else:
            if random() <= 0.5:
                subtree.left  = self.__insert(subtree.left, new_key)
            else:
                subtree.right = self.__insert(subtree.right, new_key)

        return subtree
        
    def __len__(self):
        return self.__size(self.root)
        
    def __size(self, subtree):
        if subtree is None:
            return 0
        else:
            return (1 + self.__size(subtree.left) + 
                    self.__size(subtree.right))
                    
    def leaves (self):
        """ 
        retorna las hojas del árbol
        """
        return self.__leaves(self.root)
        
    
    
    def __leaves(self, subtree):
       
        if subtree is not None:
            if  self.__is_leave(subtree)is  True:
                return 1
            else:
                return (self.__leaves(subtree.right)+self.__leaves(subtree.left))  
           
        return 0
                
       
    def __is_leave(self , subtree):
        
        if subtree. right is None and subtree.left is None:
                 
            return True
        
        return False        
        
        
        
        
            
    def inodes (self):
        """  
        devuelve los nodos internos que no sean hojas
        """
        return self.__inodes()
    
    def __inodes (self):
        if self.__size (self.root) < 3:
            if self.root.left is not None and self.root.right is not None:
                return 0
        else:
            size=self.__size(self.root)
            num_leaves=self.leaves()
            
            return (size-num_leaves-1)    
       
    
        
    
    def depth (self):
        if self.root is not None:
            return (self.__depth(self.root))
        else :
            return 0    
    def __depth(self,subtree):
        
        if subtree is not None :
            left  = self.__depth(subtree.left)
            right = self.__depth(subtree.right)
            
            if left < right:
                return (right +1) 
            else :
                return (left +1) 
        else :
            return 0                      



if __name__ == '__main__':
    a = BinaryTree()
    a.insert(20)
    a.insert(10)
    a.insert(15)
    a.insert(17)
    a.insert(18)
    a.insert(5)
    a.insert(7)
    a.insert(8)
    a.insert(6)
    a.insert(40)
    print (a.depth())
    
    print("numero de inodes", a.inodes(), "tamaño ", len(a))
    
    preorder(a)

