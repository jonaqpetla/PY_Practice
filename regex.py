import re
# use raw strings - don't want python to interpret our regex specifications
stringVariable = 'String with the Pattern we\'re searching for embedded within it.'
pattern = re.compile(r'\bPattern we\'re searching for\b')
matches = pattern.finditer(stringVariable)
for match in matches:   # match objects with span and match itself
           print(match)
           print(match.span())
           print(match.string)

# group extraction example
stringVariable = '''
https://www.google.com
http://wikipedia.org
https://www.cnn.org '''
pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
matches = pattern.finditer(stringVariable)
for match in matches:
    print(match.group(2), match.group(3))
subbedString = pattern.sub(r'\2\3', stringVariable)
print(subbedString)

# pattern.findall() method returns only the matched strings or the groups. limited use case
# pattern.search(stringVariable) returns the first match
# re.compile(r'pattern', re.IGNORECASE)