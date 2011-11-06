class BloomFilter(object):
    """Bloom filter spell checker"""

    def __init__(self, size=1000000, hashes=5, word_file='/usr/share/dict/words'):
        self.size = size
        self.hashes = hashes
        self.byte_array = [0] * self.size

        print "Loading up the word list, hasing %d times..." % self.hashes
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

print checker.includes('dadsadasdasdsadasdad')
print checker.includes('apple')
print checker.includes('cheese')
print checker.includes('ada422')
print checker.includes('cat')
print checker.includes('zookeeper')
print checker.includes('dasdsada298')