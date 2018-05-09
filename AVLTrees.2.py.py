from BinarySearchTree import BinarySearchTree
from TreeNode import TreeNode
from Traversal import preorder
from TreeNode import BinaryTree
class AVLTree(BinarySearchTree):
    def insert (self, new_key):
        """
        Agrega un dato al arbol , ordenadamente  de acuerdo a su valor
        a travez de  la fucion recursiva  __insert , retorna 
        :rtype: None 
        """
        
        self.root = self.__insert(self.root,new_key)
        self.root = self.__balance (self.root)
        self.root = self.__balance (self.root)
        
        
          

    def __insert (self, subtree, new_key):
        """
        Agrega el  dato "key" de manera  ordenada segun su valor.
        :BynariSearchTree: subtree, arbol en el que se inserta el dato
        :objet: key.Dato  a infresar 
        :rtype: BinarySearchTree
        """
        if subtree is None:
            subtree = TreeNode(new_key)
        elif subtree.key > new_key:
            subtree.left = self.__insert(subtree.left,new_key)
        elif subtree.key < new_key:
            subtree.right = self.__insert(subtree.right,new_key)
        else:
            print ("Duplicate Key!!")

        return subtree
    
    
    def max (self, number1, number2):
        if number1>number2:
            return number1
        else:number2    
     
       
                            
    def __factorBalance(self, subtree):
        right = BinaryTree()
        left  = BinaryTree()
        right.root = subtree.right
        left.root  = subtree.left

        return ( right.depth() - left.depth() )
        
    
    def balance(self, subtree):
        pass
    def __has_children(self,subtree,key):
        """
            Permite saber  cuantos hijso tiene  un nodo  , ubicandolo con el key 
            que tiene el nodo
            :rtype:int , regresa el numero de hijos que tiene el nodo en arbol
            :objet: key dato  a buscar en el arbol
            :BinarySearchTree: subtree, es el arbol en el que se  busca  el nodo 
            
        """
        if subtree is not None:
                    if subtree.key == key:
                        if subtree.left is not None and subtree.right is not None:
                            return 2    
                        elif subtree.left is not None or subtree.right is not None:
                            return 1
                        else: 
                            return 0
                    elif subtree.key > key:
                        return self.__has_children(subtree.left, key)
                    else:
                        return self.__has_children(subtree.right, key)
        return False         
           
    def __new_subtree(self, subtree,subtree2):
        if subtree is not None:
                if subtree.right is not None:
                    
                    subtree.right=self.__new_subtree(subtree.right,subtree2)
                    return subtree
                else:
                    
                    subtree.right=subtree2
                    return subtree     
    def __balance(self, subtree):
        
        if subtree is not  None:
            if self.__factorBalance(subtree)== 2 and self.__factorBalance(subtree.right) !=-2 and self.__factorBalance(subtree.right) !=2:
                subtree = self.__turn_left(subtree)
                
            elif self.__factorBalance(subtree) ==-2 and self.__factorBalance(subtree.left) !=2 and self.__factorBalance(subtree.right) !=-2:
                subtree = self.__turn_right(subtree)
            
            
            elif subtree.right is not None:
                #subtree.left = self.__balance(subtree.left)
                subtree.right = self.__balance(subtree.right)
            elif subtree.left is  not None:
                subtree.left = self.__balance(subtree.left)
                #subtree.right = self.__balance(subtree.right)    
        else:
            print("entra  a los  demas  lados")
            subtree.left = self.__balance(subtree.left)

            subtree.right = self.__balance(subtree.right)
        

        return subtree          
        
             
        
    def __turn_right(self,subtree):
        
        if self.__factorBalance(subtree.left) == -1 and subtree. left.right is  None:
            #rotacion  simple  a la derecha 
            print ("rotacion  simple  a la derecha")
            aux  = TreeNode(0)
            aux = subtree.left
            aux.left = subtree.left.left
            subtree.left = None
            subtree.left=None
            aux.right = subtree
            subtree= aux
        
            return subtree 
        else :     
            # rotacion  a la doble a la  derecha 
            print ("rotacion doble  a la derecha")
            root = subtree.left.right
            subtree.left.right = None
            left = subtree.left
            subtree.left = None
            right = subtree
            subtree = None
            if root.left is not None :
                aux = root.left
                subtree = root
                subtree.left = left
                subtree.right= right
                subtree.left.right = aux
                return subtree
            elif root.right is not None:
                aux = root.right
                subtree = root
                subtree.left = left
                subtree.right= right
                subtree.left.right = aux
                return subtree
            else:    
                subtree = root
                subtree.left = left
                subtree.right= right
                return subtree
        
            
    def __turn_left(self,subtree):
        aux  = TreeNode(0)
        root  = TreeNode(0)
        left  = TreeNode(0)
        right = TreeNode(0)
        
        
        if self.__factorBalance(subtree.right) ==  1 and subtree.right.left is None :
            # rotacion simple a la derecha 
            
            aux           = subtree.right
            aux.right     = subtree.right.right
            subtree.right = None
            subtree.left  = None
            aux.left      = subtree
            return aux
            
        else:     
            
            aux = TreeNode(0)
            root = subtree.right.left
            subtree.right.left = None
            right = subtree.right
            subtree.right = None
            left = subtree
            subtree = None
            if root.left is not None :
                aux = root.left
                subtree = root
                subtree.left = left
                subtree.right= right
                subtree.right.left = aux
                return subtree
            elif root.right is not None:
                aux = root.right
                subtree = root
                subtree.left = left
                subtree.right= right
                subtree.right.left = aux
                return subtree
            else:    
                subtree = root
                subtree.left = left
                subtree.right= right
                return subtree
            
        

    def remove_key (self, key):
        
        self.__remove_key(self.root,key)
        subtree = AVLTree()
        self.__reorder(self.root,subtree)
        self.root =subtree.root
        
        print ("este  es el tamaño del arbol" , len(subtree))
    
        print ("----------------------")
        #preorder(subtree)
        
        print ("++++++++++++++++++++++++++++++++")
        
            
    def __remove_key(self,subtree,key):
        """
        Busca  el dato  "key"  dentro del arbol  y lo borra en caso de 
        existir a travez de los metodos ocultos:
         "__delete_node_without_children"
         "__delete_node_with_one_children"
         "__delete_node_with_two_children"
        :rtype: boolean, Retornta True  en caso de eliminar el dato
        False  en caso de no eliminarlo
        :BynarySearchTree: self.root ,es el arbol en el que  se efectua 
        la eliminacion
         
        """
        
        if self.search(key):
            
            if self.__has_children(subtree,key) == 0:
                
                if self.root.key == key:
                    self.root=None
                else:
                    
                    self.__delete_node_without_children(subtree,key)
                    return True    
            elif self.__has_children(subtree,key) == 1:
                
                if self.root.key == key:
                    
                    if self.root.left is not None:
                        self.root = self.root.left
                        return True
                    else:
                        self.root = self.root.right
                        return True   
                else:
                    subtree=self.__delete_node_with_one_children(subtree,key)        
                    return True 
            elif self.__has_children(subtree,key) == 2:
                
                self.root = self.__delete_node_with_two_children(subtree,key)
                return True
                
                
                
                            
        else :
            print ("EL ELEMTO QUE DESEA BORRAR NO HACE PARTE DEL ARBOL BINARIO DE BUSQUEDA")
            return False 
    
    
    
    
    def __delete_node_with_one_children(self, subtree,key_search):
        """
        Elimina  el  nodo   en caso  que  este  solo tenga  un  hijo
        :rtype: Boolean Retorna True , esta previamente validado en el 
        metodo __remove_key  que  el subtree que  ingrees  a esta funcion
        unicamente tenga un hijo 
        :objet:key, deto que  contiene el nodo a borrar
        :BinarySearchTree: subtree, sub arbol en el que se  efectuará la 
         eliminacion
        
        """
 
        
        if subtree is not None:
            
            if subtree.left is not None and subtree.left.key == key_search:
                
                if subtree.left.left is not None :
                    
                    subtree.left=subtree.left.left
                    return subtree
                   
                else:
                    subtree.left=subtree.left.right
                    return subtree
                
                           
            elif subtree.right is not None and subtree.right.key == key_search:
                
                if subtree.right.left is not None :
                    
                    subtree.right=subtree.right.left
                    return subtree
                   
                else:
                    subtree.right=subtree.right.right
                    return subtree
                
                           
            
            elif subtree.key > key_search:
                
                return self.__delete_node_with_one_children(subtree.left, key_search)
            else:
                
                return self.__delete_node_with_one_children(subtree.right, key_search)   
    def __delete_node_without_children(self,subtree,key_search):
        """
        Elimina  el  nodo   en caso  que  este  no tenga    hijos
        :rtype: Boolean Retorna True , esta previamente validado en el 
        metodo __remove_key  que  el subtree que  ingrese  a esta funcion
        no tenga hijos
        :objet:key, deto que  contiene el nodo a borrar
        :BinarySearchTree: subtree, sub arbol en el que se  efectuará la 
         eliminacion
        
        """
         
        if subtree is not None:
            
            if subtree.right.key == key_search:
                
                subtree.right=None
                
                return subtree    
            elif subtree.left.key == key_search:
                
                subtree.left=None
                
                return subtree
            elif subtree.key > key_search:
                
                return self.__delete_node_without_children(subtree.left, key_search)
            else:
                
                return self.__delete_node_without_children(subtree.right, key_search)
        return False    
    
    
    def __delete_node_with_two_children(self,subtree,key):
        """
        Elimina  el  nodo   en caso  que  este  solo tenga  dos  hijos
        :rtype: Boolean Retorna True , esta previamente validado en el 
        metodo __remove_key  que  el subtree que  ingrees  a esta funcion
        unicamente tenga dos hijos 
        :objet:key, deto que  contiene el nodo a borrar
        :BinarySearchTree: subtree, sub arbol en el que se  efectuará la 
         eliminacion
        
        """

        if subtree is not None :
            
            if subtree.key == key:
                
                subtree=self.__new_subtree(subtree.left,subtree.right)
                return subtree
            elif subtree.key > key:
                subtree.left = self.__delete_node_with_two_children(subtree.left,key)
                return subtree
            else:
                subtree.right=self.__delete_node_with_two_children(subtree.right,key)
                return subtree        
    def __new_subtree(self, subtree,subtree2):
        if subtree is not None:
            if subtree.right is not None:
                
                subtree.right=self.__new_subtree(subtree.right,subtree2)
                return subtree
            else:
                
                subtree.right=subtree2
                return subtree    
      
    
    
    
    
    
    def __reorder (self,subtree, new_tree) :
    
        if subtree is not None:
            
            new_tree.insert(subtree.key)
            self.__reorder(subtree.left,new_tree)
        
            self.__reorder (subtree.right, new_tree)
  
        
if __name__ == '__main__':
    a = AVLTree()
    a.insert(20)
    a.insert(5)
    a.insert(57)
    a.insert(98)
    a.insert(100)
    a.insert(95)
    a.insert(101)
    a.insert(190)
    
    print ("____preorder inicial___")
    preorder(a)
    print ("====================")
    """
    
    
    a.insert(57)
    a.insert(5)
    a.insert(98)
    a.insert(95)
    a.insert(101)
    a.insert(100)
    a.insert(190)
    preorder(a)
    """
    print ("---------------------")
    a.remove_key(20)
    preorder(a)
