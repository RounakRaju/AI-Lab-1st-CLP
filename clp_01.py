#Problem-01:

a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
c=int(input("Enter the number3:"))

if(a>=b and a>=c):
   print("The maximum number is",a)
elif(b>=a and b>=c):
   print("The maximum number is",b)
else:
   print("The maximum number is",c)

#Problem-02:

def digit_count_sum(a):
    a = abs(a)          
    b = 0               
    c = 0               
    if a == 0:          
        return 1, 0                 
    
    while a > 0:        
        d = a % 10                       
        c = c + d       
        b = b + 1                       
        a = a // 10                        
    return b, c        

a = int(input("Enter an integer: "))  
b, c = digit_count_sum(a)                                               
print("Digit count:", b)               
print("Digit sum:", c)                 

#problem-03
def bubble_binary_search(a, b):
    c = len(a)                 

    for i in range(c - 1):      
        for j in range(c - 1):  
            if a[j] > a[j + 1]: 
                d = a[j]        
                a[j] = a[j + 1]
                a[j + 1] = d
    c = 0                       
    d = len(a) - 1              
    while c <= d:               
        b_mid = (c + d) // 2   

        if a[b_mid] == b:       
            return b_mid        

        elif a[b_mid] < b:     
            c = b_mid + 1       

        else:                  
            d = b_mid - 1       
    return -1 
                  
a = list(map(int, input("Enter list elements: ").split()))
b = int(input("Enter target value: "))
c = bubble_binary_search(a, b)  
if c != -1:
    print("Target found at index:", c)
else:
    print("Target not found in the list")
