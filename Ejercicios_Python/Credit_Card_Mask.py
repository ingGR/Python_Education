#Problem

""" Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However,
since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'. """

#My solition 

def maskify(cc):
    out=""
    for l in range (len(cc)):
        if l==(len(cc)-1) or l==(len(cc)-2) or l==(len(cc)-3) or l==(len(cc)-4):
            out +=cc[l]
        else:    
            out +="#"
                        
    return out

#test
 
c="Hola mundo"    
print (maskify(c))    

#solution with fewer lines

""" # return masked string
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:] """