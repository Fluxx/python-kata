import itertools

wordfile = open('/usr/share/dict/words')
wordlist = [line.rstrip().lower() for line in wordfile]

def partitions_of(word):
  return [ (word[0:i+1], word[i+1:]) for i in range(len(word)) ]

for word in wordlist:
  if len(word) is not 6:
    continue
  
  for front, back in partitions_of(word):
    if (front in wordlist) and (back in wordlist):
      print "'%s' is made up of '%s' and '%s'" % (word, front, back)