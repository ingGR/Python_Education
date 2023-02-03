#Slicing String --> rebanar cadenas
s='Monty Python'
print(s[0:4]) 
print(s[6:7])

#String concatenation --> cocncatenación de cadenas 
a='hello'
b=a+'there'
print(b)
c=a+' '+'there'
print(c)
 
#Using in as a logical Operator
fruit='banana'
print('n' in fruit)
print('m' in fruit)

#String Library
greet = 'Hello Bob'

#.lower() --> minusculas
zap=greet.lower()
print(zap)

#.upper() --> minusculas
zap2=greet.upper()
print(zap2)


#type and dir

print(type(greet)) #--> implrime el tipo de dato 
#print(dir(greet)) #--> imprime los metodos de greet

#Searching A String with .find
print(fruit.find('na')) #--> return the position the first concidence
data='From Stephen.marquuard@utc.ac.za SAt JAn 5 09:14:16 2008'
low_position=data.find('@')
hight_poition=data.find(' ',low_position)
host=data[low_position+1:hight_poition]
print(host)

#Search and Replace with Replace
print(greet.replace('Bob', 'Jane')) #--> replace the first word for the second word

#Stripping Whitespace 
greet2='   Hello World  '
print(greet2.lstrip()) #-->remove the whitespace at the left
print(greet2.rstrip()) #-->remove the whitespace at the right
print(greet2.strip()) #-->remove both beginning and endding whitespace

#Prefixes
line='Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))


