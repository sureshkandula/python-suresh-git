#trying to write a program to do all expressions
"""
import re

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print ('Looking for "%s" in "%s" ->' % (pattern, text),)

    if re.search(pattern, text):
        print ('found a match!')
    else:
        print ('no match'    )

"""
"""
import re
pattern = 'cat'
text = 'Does text match the pattern? this was a apple this much'

if (re.search(pattern, text)):
    print ('match found')
else:
    print('no match found')

"""
"""
import re
pattern = 'cat'
text = 'Does text cat match the pattern? this was a apple this much'
match = re.search(pattern, text)

s = match.start()
e = match.end()

print ('Found "%s" in "%s" from %d to %d ("%s")' % \
       (match.re.pattern, match.string, s, e, text[s:e]))
"""
"""
import re
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24 August9 Dec 12",re.M|re.I)

for match in matches:
    # This will print:
    #   June 24
    #   August 9
    #   Dec 12
    print ("Full match: %s" % (match))


regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    # This will now print:
    #   0 7
    #   9 17
    #   19 25
    # which corresponds with the start and end of each match in the input string
    print ("Match at index: %s, %s" % (match.start(), match.end()))

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this',
                                     'that',
                                     ]
            ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print ('Looking for "%s" in "%s" ->' % (regex.pattern, text),)

    if regex.search(text):
        print ('found a match!')
    else:
        print ('no match')


"""
"""
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))

"""
"""
import re

text = 'This is some text -- with punctuation.'

print(text)
print()

for pattern in [ r'^(?P<first_word>\w+)',
                 r'(?P<last_word>\w+)\S*$',
                 r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
                 r'(?P<ends_with_t>\w+t)\b',
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print('Matching "%s"' % pattern)
    print('  ', match.groups())
    print('  ', match.groupdict())
    print()
"""
import re

text = 'This is some text -- with punctuation.'

print ('Input text            :', text)

# word starting with 't' then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print ('Pattern               :', regex.pattern)

match = regex.search(text)
print ('Entire match          :', match.group(0))
print ('Word starting with "t":', match.group(1))
print ('Word after "t" word   :', match.group(2))

"""
import re
text = 'This is some text -- with punctuation.'
print (text)
print()
for pattern in [ r'^(\w+)',           # word at start of string
                 r'(\w+)\S*$',        # word at end of string, with optional punctuation
                 r'(\bt\w+)\W+(\w+)', # word starting with 't' then another word
                 r'(\w+t)\b',         # word ending with 't'
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print('Matching "%s"' % pattern)
    print('  ', match.groups())
    print()