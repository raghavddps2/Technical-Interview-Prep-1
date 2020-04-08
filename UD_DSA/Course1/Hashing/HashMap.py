import math

class LinkedListNode:

    def __init__(self,key,value):
        self.key = key
        self.value  = value
        self.next = None


class HashMap:

    def __init__(self,initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.num_entries = 0
        self.p = 37
        self.load_factor = 0.7
    
    def size(self):
        return self.num_entries

    def get_hash_code(self,data):
        string = str(data)
        hash_code = 0
        for i in range(0,len(string)):
            hash_code = hash_code + ord(string[i])*math.pow(self.p,i)
        return hash_code%len(self.bucket_array)
    
    def get_bucket_index(self,key):
        return int(self.get_hash_code(key))

    def put(self,key,value):
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key,value)

        head = self.bucket_array[bucket_index]

        #Executed if the same key exists!!
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        #Executed if not found in the chain, put it at first
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries = self.num_entries + 1

        curr_load_factor = self.num_entries/len(self.bucket_array)
        if curr_load_factor > self.load_factor:
            self.num_entries = 0
            self.rehash()

    def rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2*old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        #For each value in the array, we iterate oover the index'ex linked list!
        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key,value)
                head = head.next

    def delete(self,key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        if head is None:
            return "-1"
        else:
            if head.key == key:
                head = head.next
                self.bucket_array[bucket_index] = head
            else:
                pre = None
                curr = head
                while curr.key != key:
                    pre = curr
                    curr = curr.next
                
                pre.next = curr.next
            self.num_entries = self.num_entries -1 
            return "1"

    
    def get(self,key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

hash_map = HashMap(7)

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))

hash_map.delete("one")

print(hash_map.get("one"))
print(hash_map.size())