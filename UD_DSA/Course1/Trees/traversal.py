def pre_order(tree):
    def traverse(node):
        if node == None:
            return
        else:
            visit_order.append(node)
            traverse(node.left)
            traverse(node.right)
        return visit_order
    
    visit_order = list()
    root = tree.get_root()
    traverse(root)

def in_order(tree):
    def traverse(node):
        if node == None:
            return
        else:
            traverse(node.left)
            visit_order.append(node)
            traverse(node.right)
        return visit_order
    
    visit_order = list()
    root = tree.get_root()
    traverse(root)

def post_order(tree):
    def traverse(node):
        if node == None:
            return
        else:
            traverse(node.left)
            traverse(node.right)
            visit_order.append(node)
        return visit_order
    
    visit_order = list()
    root = tree.get_root()
    traverse(root)
