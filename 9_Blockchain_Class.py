import hashlib as hasher
import datetime as date


# This is the basis of every block in the blockchain. It is important to understand what is going on here to
# understand the rest of how it works. To begin, a block consists of an index (what NUMBER block is it in the chain? For example,
# the first block would be 1), a timestamp, a piece of data that you want to store in the block (for example, if you were a
# business you might want to store a transaction amount), and a previous hash (I'll get more into this later).
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
# You also need to store the block's hash. This is a random sequence of letters and numbers that identify the block.
# It works like this: You take all of the information you put in the block, and puts it in a code that identifies the block.
        self.hash = self.hash_block()

# This is a block. A block is just an object
# that becomes encrypted based
# on the last block, hence why it is "un-hackable"
    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp)+
                    str(self.data)+
                    str(self.previous_hash)).encode())
# For every block after the first block, you need to "hash", or encrypt, every block's hash along WITH the previous block's hash.
# Example: Block 1's hash is "g5Tf" and you input Block 2's information. In order to make it unhackable,
# you concatenate the two strings of information together and it will give you a new hash, let's say "8vwj". This basically happens by hashing
# "g5Tf" and whatever Block 2's information together and turning back into a 4 character string. Therefore, Block 2's finalized hash is "8vwj".
# This way, the previous Block is necessary for ANY future blocks.
        return sha.hexdigest()
# sha.hexdigest() is the method you call on the block to hash it.


# Manually construct a block with
# index zero and arbitrary previous hash
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    # Each block has a number
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Create Blockchain itself
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
# Every time you make a new block, the previous block updates to the current block.
num_of_blocks_to_add = 1

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} has been added to the blockchain.".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))

# Run this and you should get a blockchain!
