#Problem

""" In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list 
with the strings filtered out. """

#My solution

def filter_list(list):
    filtered_out=[]
    for i in list:
        if type(i)==int:
            filtered_out.append(i)
    return filtered_out  

# test 

list_1=[1, 2, 'a', 'b']
list_2=[1, 'a', 'b', 0, 15]
list_3=[1, 2, 'aasf', '1', '123', 123]

print (filter_list(list_1))
print (filter_list(list_2))
print (filter_list(list_3))