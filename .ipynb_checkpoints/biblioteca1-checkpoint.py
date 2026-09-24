# from fractions import Fraction

# a = Fraction(3, 5)
# b = Fraction(1)
# c = a + b
# d = Fraction(4, 6)
# d 
# e = a + d
# print(a,b,c,d,e)



def fibonacci(n):
    '''Esta regresa los numeros de fibonacci menores a n'''
    
    output = []
    
    f1,f2 = 1,1

    while f2 < n:
        output.append(f2)        
        f1,f2 = f2,f1+f2
    
    return output
