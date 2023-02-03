#problem

""" Create a function that takes a positive integer and returns the  bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil """

#Mysolution

def next_bigger(n):
    digits = [int(i) for i in str(n)]
    size=len(digits)
    for i in range(1,(size)):
        """ if digits[-i]>digits[-(i+1)]:
            aux=digits[-(i+1)]
            digits[-(i+1)]=digits[-i]
            digits[-i]=aux          
            break
        else:
            continue """
        #print(size-i)    
        print(digits[size-i])
        #print(size-(i+1))     
        print(digits[size-(i+1)])
        print(digits[size-i]>digits[size-(i+1)])    
        if digits[size-i]>digits[size-(i+1)]:
            aux=digits[size-(i+1)]
            digits[size-(i+1)]=digits[size-i]
            digits[size-i]=aux          
            break
        
    
    num_bigger=(int("".join(map(str,digits))))
    if num_bigger==n:
        return -1
    else:
        return num_bigger
    
#test

print(next_bigger(1234567890))

#best solution    