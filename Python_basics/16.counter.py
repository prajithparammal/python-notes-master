'''
Counter is basically a dic sub class.
'''
from collections import Counter
l = [1,1,1,1,2,3,3,3,3,4,5,5]
print(Counter(l)) ## can easily count the elements in a list

###########################
s='aaaabbbbccccddddeeefffggghhhiiiijjjjkkkkaaabbbcccddd'
print(Counter(s))

###########################
s='how many times does each word show up in this sentence word word shoe up up'
words = s.split()
print(Counter(words))
###########################
c = Counter(words)
print(c.most_common(2))  ##methods in Counter
###########################


