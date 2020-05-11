import hashlib
import datetime 

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self,string):
        sha = hashlib.sha256()
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)


class BlockChain:
    def __init__(self):
        self.tail = None

    def add_block(self,data):
        timestamp = datetime.datetime.now()
        if self.tail == None:
            self.tail = Block(timestamp=timestamp,data=data,previous_hash=None)
        else:
            self.tail = Block(timestamp=timestamp,data=data,previous_hash=self.tail)

    def search(self,value):
        position_pointer = self.tail
        while position_pointer.previous_hash is not None:
            if position_pointer.hash == value:
                return position_pointer
            position_pointer=position_pointer.previous_hash

    def size(self):
        position_pointer = self.tail
        length = 0
        while position_pointer is not None:
            position_pointer = position_pointer.previous_hash
            length += 1
        return length

blockchain = BlockChain()
blockchain.add_block('my balance: 0 | cash flow: +10')
blockchain.add_block('my balance: 10 | cash flow: -15')
blockchain.add_block('my balance: 20 | cash flow: +15')
blockchain.add_block('my balance: 30 | cash flow: +5')
print(blockchain.size())