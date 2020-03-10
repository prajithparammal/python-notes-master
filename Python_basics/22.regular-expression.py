import re
patterns = ["term1", 'term2']
text = 'This is a strong with term1, but not the other term'

for pattern in patterns:
    print('Searching for "%s" in:\n"%s"' %(pattern, text)),

    if re.search(pattern, text):
        print ("\n Match was found")
    else:
        print("\n No match was found")

print("#########################################################")

split_term = '@'
phrase = 'what is your email, is it hello@gmail.com?'
print(re.split(split_term,phrase))

print("#########################################################")
spliting = 'hello world'.split()
print (spliting)
print("#########################################################")
__findall = re.findall('match','Here is one match, here is another match')
print(__findall)

