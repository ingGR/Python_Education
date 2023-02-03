#Problem

""" Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

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
    digitos = [int(i) for i in str(n)]
    digitos.sort(reverse=True)    
    num_bigger=(int("".join(map(str,digitos))))
    if num_bigger==n:
        return -1
    else:
        return num_bigger


print(next_bigger(414))    