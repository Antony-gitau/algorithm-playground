# a word/phrase, A is an anagram of another word/phrase,B if all letters 
# in A are rearranged and used only once to form word/phrase B. 

#this is the class returns true if the words are anagrams and false otherwise.


class anagram:
    def checkAnagram(s:str, t:str) -> bool:
        #approach one 
        #sort the two strings
        if sorted(s) == sorted(t): #if the two strings are the same, then they are anagrams
            print('its an anagram')
        
            return  True
        
        #else not
        print('not an anagram')
        return False

        #could also be a single line of code
        return sorted(s) == sorted(t)

#example
check = anagram.checkAnagram('wood','doow')

#could also be a single line of code