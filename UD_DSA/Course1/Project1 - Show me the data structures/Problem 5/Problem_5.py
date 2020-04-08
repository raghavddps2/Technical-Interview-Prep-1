#%% Imports and functions declaration
import time
import hashlib


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash(data)

    def __repr__(self):
        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)

    @staticmethod
    def _calc_hash(string: str) -> str:
        """
        Given a string, calculates the SHA-256 hash of it
        :param string: text we want to calculate th hash of
        :return: hash of the imputed text
        """
        sha = hashlib.sha256()
        sha.update(string.encode('utf-8'))
        return sha.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.tail = None

    def addBlock(self, data):
        """ Append a value to the end of the BlockChain. """

        if self.tail is None:
            self.tail = Block(data=data, previous_hash=None)

        else:
            #Most crucial, here we are specifying the previouss hash as the previous node itself.
            self.tail = Block(data=data, previous_hash=self.tail)



    def show_blocks(self):
        out1 = []
        block = self.tail
        while block:
            out1.append([block.data, block.timestamp, block.hash])
            block = block.previous_hash
        return out1



print("TEST CASE 1")
my_blockchain = BlockChain()
my_blockchain.addBlock("Credit - Rs 1000")
my_blockchain.addBlock("Debit - Rs 1000")
my_blockchain.addBlock("Credit - Rs 1000")
my_blockchain.addBlock("Debit - Rs 1000")
my_blockchain.addBlock("Credit - Rs 10000")
my_blockchain.addBlock("Debit - Rs 1000")
my_blockchain.addBlock("Debit - Rs 1000")
print(my_blockchain.show_blocks())


print("TEST CASE 2- No blocks(edge)")
my_blockchain1 = BlockChain()
print(my_blockchain1.show_blocks())

print("TEST CASE 3 - Only two blocks")
my_blockchain2 = BlockChain()
my_blockchain2.addBlock("Patient 1 - SSN no")
my_blockchain2.addBlock("Patient 2 - SSN no")
my_blockchain2.addBlock("Patient 3 - SSN no")
print(my_blockchain2.show_blocks())


"""
Output:
TEST CASE 1
[['Debit - Rs 1000', 1586376023.8111377, '6c46204e67dda9491837020be28f0174e55f911a73c8ad9dbc54ab195106f1cd'], ['Debit - Rs 1000', 1586376023.8111353, '6c46204e67dda9491837020be28f0174e55f911a73c8ad9dbc54ab195106f1cd'], ['Credit - Rs 10000', 1586376023.811133, '9a19219d6e03614f0be0ef730f4026d117f6ec93e999ad6b57b99e7b6423b375'], ['Debit - Rs 1000', 1586376023.8111303, '6c46204e67dda9491837020be28f0174e55f911a73c8ad9dbc54ab195106f1cd'], ['Credit - Rs 1000', 1586376023.8111277, 'b564bc4358b170efb09f7d70842494d25ab243b99a051bcf50d2ea0fd2b1534b'], ['Debit - Rs 1000', 1586376023.8111236, '6c46204e67dda9491837020be28f0174e55f911a73c8ad9dbc54ab195106f1cd'], ['Credit - Rs 1000', 1586376023.8111095, 'b564bc4358b170efb09f7d70842494d25ab243b99a051bcf50d2ea0fd2b1534b']]
TEST CASE 2- No blocks(edge)
[]
TEST CASE 3 - Only two blocks
[['Patient 3 - SSN no', 1586376023.8112304, '498cf617e2849684d3093e67eaa9535c08e3d72ccc40a3c4fb266a3864948f8f'], ['Patient 2 - SSN no', 1586376023.8112268, '4cd2826316b747c5dff0ee25e649bdd4c92f44e46df4c66d9a8d84af879d8d8e'], ['Patient 1 - SSN no', 1586376023.8112197, 'c6bdcddb1586a377867b89a8b01060a33cc22243e10355cb6a845d0a9901dbc5']]
(base) 
"""

