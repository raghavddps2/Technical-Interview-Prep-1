# add set_value and get_value functions
class Node:
    
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def get_value(self):
        return self.value
    
    def set_value(self,data):
        self.value  = data
        
    def set_left_child(self,left_node):
        self.left = left_node
    
    def set_right_child(self,right_node):
        self.right = right_node
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return (self.left != None)
    
    def has_right_child(self):
        return (self.right != None)

