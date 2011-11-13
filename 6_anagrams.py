import itertools

words = dict()

print "Loading in wordlist..."
for wordline in open('/usr/share/dict/words'):
  word = wordline.rstrip().lower()
  sorted_word = "".join(sorted(word))

  if sorted_word not in words:
    words[sorted_word] = [word]
  else:
    words[sorted_word].append(word)

print "Extracting out anagrams from loaded words..."
for k,v in words.items():
  if len(v) > 1:
    print ", ".join(v)