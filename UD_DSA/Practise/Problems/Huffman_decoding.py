#This shows how we built up the Huffman tree. 
#Our major task here is to decode the huffman tree.
#This is the beautiful Huffman decoding program!

import queue as Queue
from queue import PriorityQueue
#Importance of using PriorityQueue for HuffMan decoding is must!!
import copy
cntr = 0

class Node:

    #This takes the freq and the data.
    def __init__(self,freq,data):

        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self,other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

#This builds the tree and returns root.
def huffman_hidden():

    q = Queue.PriorityQueue()

    #We enter all the elements according too the frequency in the priority queue.
    for key in freq:
        q.put((freq[key],key,Node(freq[key],key)))
    
    #Sabse, pehle least wale niklenge, this is building the tree bottom up.!
    while q.qsize() != 1:

        a = q.get()
        b = q.get()
        obj = Node(a[0]+b[0],'\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq,obj.data,obj))
    
    root = q.get()
    root = root[2]
    return root

def dfs_hidden(obj,already):

    if (obj == None):
        return
    elif obj.data != '\0':
        code_hidden[obj.data] = already
    
    dfs_hidden(obj.right,already+"1")
    dfs_hidden(obj.left,already+"0")

def decodeHuff(root,s):

    tempo = copy.deepcopy(root)
    decodedString = ""
    for char in s:
        
        if char == '0':
            tempo = tempo.left
        else:
            tempo = tempo.right

        if tempo.left == None and tempo.right == None:
            decodedString = decodedString + tempo.data
            tempo = root
    return decodedString

#Step1, we take the input for the data to be decoded from the user.
data = input()

#Step2, we will map each character to its frequency.
freq = {}
for char in data:
    if char in freq:
        freq[char] = freq[char]+1
    else:
        freq[char] = 1
print(freq)
#Strp3, we create the huffman tree of the data we receive and we store the root.
root = huffman_hidden()

code_hidden = {}
#We will make the dict for mapping.
dfs_hidden(root,"")
print(code_hidden)
#if we have only 1 input.
if len(code_hidden) == 1:
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""
for char in data:
    toBeDecoded += code_hidden[char]
print(toBeDecoded)
#ALl we have to do is decode this now!
print(decodeHuff(root,toBeDecoded))
