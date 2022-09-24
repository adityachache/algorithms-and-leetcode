class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        # encode in this format
        string = ""
        for s in strs:
            string += str(len(s)) + ',' + s
        
        return string

       # 4,lint4,code4,love,4,you

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != ',':
                j += 1
            length = int(str[i:j])
            actual_string = str[j+1: j+1+length]
            res.append(actual_string)
            i = j + 1 + length
        return res

       