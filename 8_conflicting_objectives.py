import itertools

def partitions_of(word):
  return [ (word[0:i+1], word[i+1:]) for i in range(len(word)) ]

# READABLE as possible

# wordfile = open('/usr/share/dict/words')
# wordlist = [line.rstrip().lower() for line in wordfile]

# for word in wordlist:
#   if len(word) is not 6:
#     continue
  
#   for front, back in partitions_of(word):
#     if (front in wordlist) and (back in wordlist):
#       print "'%s' is made up of '%s' and '%s'" % (word, front, back)


# FAST as possible

# dictionary = open('/usr/share/dict/words')

# words = set(line.rstrip().lower() for line in dictionary)

# for word in words:
#   for front, back in partitions_of(word) if:
#     if (front in words) and (back in words):
#       print "'%s' is made up of '%s' and '%s'" % (word, front, back)
#       break

# EXTENSIBLE as possible

class ConcatinationChecker():
  """
  Finds words in the provided wordlist file that are made up of two smaller
  words in the same wordfile
  """

  def __init__(self, wordfile='/usr/share/dict/words'):
    self.wordfile = open(wordfile)
    self.words = set(line.rstrip().lower() for line in self.wordfile)

  def check(self, word):
    return any(self._in_dictionary(partition)
               for partition in self._partitions(word))

  def checkDictionary(self, length=6):
    return filter(self.check, self._words_of_length(length))

  def _in_dictionary(self, obj):
    return all(part in self.words for part in obj)

  def _partitions(self, word):
    return [ (word[0:i+1], word[i+1:]) for i in range(len(word)) ]

  def _words_of_length(self, required_length):
    select(word in self.words if len(words) is required_length)

checker = ConcatinationChecker()
print checker.checkDictionary()