# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        #We simply create the root node here and assign 
        self.root = RouteTrieNode()
        self.handler = root_handler
    def insert(self,path,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        #Insert
        node = self.root
        for path in path:
            node.insert(path)
            node = node.children[path]
        node.handler = handler

    def find(self,paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path in paths:
            if path not in node.children:
                return None
            node = node.children[path]

        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
#This is the base RouteTrieNode
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self,path_block):
        # Insert the node as before
        if path_block not in self.children:
            self.children[path_block] = RouteTrieNode()
        else:
            pass

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self,root_handler,empty_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler=root_handler)
        self.non_found_handler = empty_handler

    def add_handler(self,paths,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(paths)
        self.router.insert(path=path, handler=handler)

    def lookup(self,path):
        path = self.split_path(path)
        if len(path) == 0:
            return self.router.handler

        searching = self.router.find(paths=path)

        if searching is None:
            return self.non_found_handler
        else:
            return searching


    def split_path(self,path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        result_temp = path.split(sep='/')
        return [element for element in result_temp if element != '']

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


#Outputs
# root handler
# not found handler
# about handler
# about handler
# not found handler