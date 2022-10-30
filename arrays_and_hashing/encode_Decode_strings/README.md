The problem is to encode a string in the input then decode it at the output. 

constraint:
- dont add an extract array of integers in the implementation.

example
input = ['kenyatta', 'university']
output = ['kenyatta','university']

challenge
encoding 'kenyatta' 'university' into kenyattauniversity will present a challenge when decoding as we wont remember where the first string (kenyatta) ends nor where the second string begins (university). 

stategies:
1. use a special character at the middle of the strings. 
example:
kenyatta&university, so when decoding, we can identify '&' to recognise the string boundaries.
but the problem is that the string could have such special character, like kenya&tta, which could be missleading when decoding. 

2. use a combination of the length of the string and a special character. example
8&kenyatta10&university. this way while decoding, we can extract a string from using its length and strating from the special character. This is the strategy we will use to solve this problem. It is also the strategy employed by neetcode. 