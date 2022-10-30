class Solution:
    "this class will have an encoding and decoding function"
    def encoding(self, strings):
        """we will loop through all the strings in the list as 
            we get length of each string and also append a special character 
            after the length of the string.
        """
        #the output of this function will  be a single string lexample 4#neet4#code
        result = ""
        for string in strings:
            string = str(len(string)) + "#" + string 
        return result.append(string)

    def decoding(self, string):
        #the result will be a list of strings
        #the indx mark the beginning of a string
        result, indx = [], 0

        #while we are string within the length of the enconded string,
        while indx < len(string):
            current_indx = indx #current index marks the location we are begining from
            #while we are have not yet reached the special character (#) that we encoded 
            while string[current_indx] != '#' :
                #keep moving along the characters of the string till you reach the "#"
                current_indx += 1

            #when you find the "#", slice the string
            length = int(string[indx:current_indx])
            result.append(string[current_indx+1: current_indx+1+length])
            indx = current_indx +1+ length
        return result



