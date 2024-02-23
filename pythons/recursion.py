# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))
def fabo(n):
    if(n==0):
        return n
    elif(n==1):
        return n
    else:
        return fabo(n-1)+fabo(n-2)

terms =int(input("enter ho many numbers"))
for i in range(terms):
    print(fabo(i))