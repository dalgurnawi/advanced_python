"""Build an index mapping word -> list of occurrences"""
import re
import sys
WORD_RD = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,1):
        for match in WORD_RD.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # Get the list of occurrences for word, or [] if not found
            occurrences = index.get(word, [])
            #Append new location to occurrences
            occurrences.append(location)
            # Put changed occurrences into index dict; this entails a second search through the index
            index[word] = occurrences
            # In the key=argument of sorted, I am not calling str.upper, just passing a reference to that method so the
            # sorted function can use it to normalize the words for sorting.

# display in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])