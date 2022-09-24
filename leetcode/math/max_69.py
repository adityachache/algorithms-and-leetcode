# How does this program works?
# the replace() method in python replaces the first occurence of any character with the specified character if count is not mentioned it changes all occurences of that character
# we need to find the max element after changing ATMOST one digit from the given integer num




# THE KEY THING HERE WE NEED TO KNOW IS THAT THE FIRST occurence of 6 REPLACED WITH 9 WILL GIVE US THE MAXIMUM NUMBER
# AND REPLACE() BY DEFAULT IF COUNT IS 1 REPLACES THE FIRST OCCURENCE OF THE ELEMENT 
def max_69(num):
    maximum = str(num).replace('6','9',1)
    return int(maximum)


print(max_69(9669))





# 9996