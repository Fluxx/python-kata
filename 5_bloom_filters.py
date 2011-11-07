class BloomFilter(object):
    """Bloom filter spell checker"""

    def __init__(self, size=100000000, hashes=2, word_file='/usr/share/dict/words'):
        self.size = size
        self.hashes = hashes

        print "Creating a %s element byte array..." % self.size
        self.byte_array = [0] * self.size

        print "Loading up the word list, hashing %d times..." % self.hashes
        for word in open(word_file):
            self.add(word.strip())

    def add(self, word):
        for i in self.indexes(word):
            self.byte_array[i] = 1

    def hash_at(self, i, word):
        return hash(word + str(i)) % self.size

    def indexes(self, word):
        return [ self.hash_at(i, word) for i in range(self.hashes) ]

    def values(self, word):
        return [ self.byte_array[i] for i in self.indexes(word) ]

    def includes(self, word):
        return all(self.values(word))

checker = BloomFilter()

words = [
    'kitchen',
    'apple',
    'cheese',
    'ada422',
    'cat',
    'zookeeper',
    'data',
    'i;2h[22',
    'chef',
    'mammal',
    'lamp'
]

for word in words:
    print "%s: %s" % (word.rjust(15), checker.includes(word))