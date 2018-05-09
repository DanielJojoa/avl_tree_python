#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from Traversal import preorder
from TreeNode import BinaryTree
from TreeNode import TreeNode
class BinarySearchTree(BinaryTree):

    def insert (self, new_key):
        """
         Agrega un dato al arbol , ordenadamente  de acuerdo a su valor
         a travez de  la fucion recursiva  __insert , retorna 
         :rtype: None 
        """
        if self.__valid_data(new_key):
            self.root = self.__insert(self.root,new_key)
        else :
            print ("Dato no valido ")    

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
    def __valid_data(self,data):

        if self.root is not None:
            fst_data=type(self.root.key)
            return (isinstance(data , fst_data))
            
        
        else :
            return True    

    def search(self, key_search):
        """
        Verifica  "si Key_search" dato  a buscar  hace parte  del  arbol
        a travez del metodo oculto "__search"
        :rtype: bool, Retornta True en caso de existir el dato en el arbol
        False en caso de no existir el dato en el arbol
        :objet: key_search, dato a buscar en el arbol
         
        """
        if self.__valid_data(key_search):
            return self.__search(self.root, key_search)
        else :
            print ("Dato no valido ")
            return False    

        

    def __search (self, subtree, key_search):
        """
        Verifica  "si Key_search" dato  a buscar  hace parte  del  arbol
        :rtype: bool, Retornta True en caso de existir el dato en el arbol
        False en caso de no existir el dato en el arbol
        :objet: key_search, dato a buscar en el arbol
         
        """
        if subtree is not None:
            if subtree.key == key_search:
                return True
            elif subtree.key > key_search:
                return self.__search(subtree.left, key_search)
            else:
                return self.__search(subtree.right, key_search)
        return False

    def find (self, key_find):
        """
        Verifica  "si Key_find" dato  a buscar  hace parte  del  arbol
        a travez de el metodo oculto "__find" y
        lo retorna en caso de encontrarlo 
        :rtype: objet, Retornta el objeto en caso de existir el dato en el arbol
        None en caso de no existir el dato en el arbol
        :objet: key_search, dato a buscar en el arbol
        :BynarySearchTree: self.root ,es el arbol en el que  se efectua 
        la busqueda 
        """
        if self.__valid_data(key_find):
            return self.__find(self.root,key_find)
        else :
            print ("Dato no valido ")
            return None    

        
        


    def __find (self, subtree, key_find):
        """
        Verifica  "si Key_search" dato  a buscar  hace parte  del  arbol
        :rtype: bool, Retornta True en caso de existir el dato en el arbol
        False en caso de no existir el dato en el arbol
        :objet: key_search, dato a buscar en el arbol
        :BynarySearchTree: subtree ,es el arbol en el que  se efectua 
        la busqueda 
        """
        if subtree is not None:
            if subtree.key == key_find:
                print (subtree.key)
                return subtree.key
            elif subtree.key > key_find:
                return self.__find(subtree.left, key_find)
            else:
                return self.__find(subtree.right, key_find)
        return None


    def find_min (self):
        """
        Busca  el dato  menor  dentro del arbol  y  lo retorna  ,  atravez
         del metodo oculto "__find_min"
        :rtype: objet, Retornta el objeto en caso de existir el dato
         en el arbol
        None en caso de no existir el dato en el arbol
        :BynarySearchTree: self.root ,es el arbol en el que  se efectua 
        la busqueda
         
        """
        
        return self.__find_min(self.root)


    def __find_min (self, subtree):
        """
        Busca  el dato  menor  dentro del arbol  y  lo retorna  
        :rtype: objet, Retornta el objeto en caso de existir el dato
         en el arbol
        None en caso de no existir el dato en el arbol
        :BynarySearchTree: self.root ,es el arbol en el que  se efectua 
        la busqueda
         
        """
        
        if subtree is not None:
                    
            if subtree.left is not None:
                if subtree.left.left is not None :  
                    
                    return self.__find_min(subtree.left)
                else:
                
                    return subtree.left.key
                
            else:
               
                return subtree.key 
        return None


    def find_max (self):
        """
        Busca  el dato  mayor  dentro del arbol  y  lo retorna  ,  atravez
         del metodo oculto "__find_min"
        :rtype: objet, Retornta el objeto en caso de existir el dato
         en el arbol
        None en caso de no existir el dato en el arbol
        :BynarySearchTree: self.root ,es el arbol en el que  se efectua 
        la busqueda
         
        """
        return self.__find_max(self.root)
    
    def __find_max(self,subtree):
        
        """
        Busca  el dato  mayor  dentro del arbol  y  lo retorna  ,  atravez
         del metodo oculto "__find_min"
        :rtype: objet, Retornta el objeto en caso de existir el dato
         en el arbol
        None en caso de no existir el dato en el arbol
        :BynarySearchTree: self.root ,es el arbol en el que  se efectua 
        la busqueda
         
        """
        if subtree is not None:
                    
            if subtree.right is not None:
                if subtree.right.right is not None:
                    return self.__find_max(subtree.right)    
                else:
                    return subtree.right.key
                    
            else:
                            
                return subtree.right.key 
        return None
    def remove_key(self,key):
        """
        Busca  el dato  "key"  dentro del arbol  y lo borra en caso de 
        existir a travez del metodo oculto:"_remove_key"
         
        :rtype: boolean, Retornta True  en caso de eliminar el dato
        False  en caso de no eliminarlo
        :BynarySearchTree: self.root ,es el arbol en el que  se efectua 
        la eliminacion
         
        """
        if self.__valid_data(key):
            return self.__remove_key(self.root,key)
        else :
            print ("Dato no valido ")
            return False    

        
            
    
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

if __name__ == '__main__':
    a = BinarySearchTree()
    a.insert(20)
    a.insert("10")
    a.insert(15)
    a.insert(17)
    a.insert(18)
    a.insert(5)
    a.insert(7)
    a.insert(8)
    #a.insert(6)
    a.insert(40)
    
    #a.insert(30)
    #a.insert(80)
    #a.insert(75)
    #a.insert(65)
    #a.insert(100)
    #a.insert(90)
    #a.insert(100)
    #preorder(a)
    #print ("//////////////////////////////////777")
    
    nada2 = a.remove_key("2")
    preorder(a)
    
    #nada = a.find(4)
    
    #nada2 = a.search(3)
    print ("existe 1 5 3?  ",nada2)


