class BloomFilter(object):
    """Bloom filter spell checker"""

    def __init__(self, size=100000000, hashes=2, word_file='/usr/share/dict/words'):
        self.size = size
        self.hashes = hashes
        self.word_file = word_file

        print "Creating a %s element byte array..." % self.size
        self.byte_array = [0] * self.size

        print "Loading up the word list, hashing %d times..." % self.hashes
        for word in open(self.word_file):
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

################################################################################
# Test run #####################################################################
################################################################################

checker = BloomFilter()

import string
import random
import subprocess

def random_string(size=5):
    characters = (random.choice(string.ascii_lowercase) for x in range(size))
    return''.join(characters)

number_strings_to_check = 10000

print 'Tryng %s random generated words...' % number_strings_to_check

false_positves = 0

for i in range(number_strings_to_check):
    word = random_string(5)

    if checker.includes(word):
        command = ('grep', '-w', word, checker.word_file)
        try:
            subprocess.check_output(command)
        except subprocess.CalledProcessError:
            false_positves += 1

format = (false_positves, number_strings_to_check, (float(false_positves) / number_strings_to_check)*100)
print "%s false positives out of %s total checks (%s%%)" % format
