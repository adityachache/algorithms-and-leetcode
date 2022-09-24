# fibonacci sequence using iterative approach
def fibo_iterative(num):
    firstnum = 0
    secondnum = 1
    count = 0
    while count <= num:
        thirdnum = firstnum + secondnum
        print(firstnum,end=' ')
        firstnum = secondnum
        secondnum = thirdnum
        count += 1
    
#print(fibo_iterative(10))

# fibonacci sequence using recursion
def fibo_recursive(num,count=0,firstnum=0,secondnum=1):
    thirdnum = firstnum + secondnum
    print(firstnum,end= ' ')
    if count == num:
        return None
    else:
        return fibo_recursive(num,count+1,firstnum=secondnum,secondnum=thirdnum)

#print(fibo_recursive(10))

# fibonacci number at the given index
def fibo_at_index_iterative(index):
    firstnum = 0
    secondnum = 1
    if index == 0:
        return firstnum
    elif index == 1:
        return secondnum
    else:
        for i in range(2,index+1):
            thirdnum = firstnum + secondnum
            firstnum = secondnum
            secondnum = thirdnum
        return thirdnum

# fibonacci number at given index using recursion
def fibo_at_index_recursive(index):
    if index == 0:
        return 0 
    elif index == 1:
        return 1
    else:
        return fibo_at_index_recursive(index-1) + fibo_at_index_recursive(index-2)
    
print(fibo_at_index_iterative(10))