import itertools

words = dict()
anagrams = dict()

print "Loading in wordlist..."
for wordline in open('/usr/share/dict/words'):
  word = wordline.rstrip().lower()
  sorted_word = "".join(sorted(word))

  if sorted_word not in words:
    words[sorted_word] = word
  elif not sorted_word in anagrams:
    anagrams[sorted_word] = [words[sorted_word], word]
  else:
    anagrams[sorted_word].append(word)

for word,alist in anagrams.items():
  print ", ".join(alist)