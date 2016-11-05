# Method to reverse integer
def myreverse(n):
    rev = 0  
    while n > 0:
        rev = (10*rev) + n%10
        n //= 10
    return rev

n = int(input("Give the integer number to be reversed: "))
print("")
print("Given integer: ")
print(n)

# Chck if the given number is negative, if so make it positive
neg = False
if n < 0:
    neg = True
    n = abs(n)
print("Reversed integer number: ")
a = myreverse(n)

# To account for negative value (original and reversed shd have negative values)
if neg :
    a = -a
    n = -n
# Spit out the reversed number
print(a)

# To check if the number is palindrome
print("")
if (a == n):
    print("Given number is Palindrome")
else:
    print("Given number is NOT palindrome")
