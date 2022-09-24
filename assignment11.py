# 1. Write a python script to calculate sum of first N natural numbers
# 2. Write a python script to calculate sum of squares of first N natural numbers
# 3. Write a python script to calculate sum of cubes of first N natural numbers
# 4. Write a python script to calculate sum of first N odd natural numbers
# 5. Write a python script to calculate sum of first N even natural numbers
# 6. Write a python script to calculate factorial of a given number
# 7. Write a python script to count digits in a given number
# 8. Write a python script to calculate sum of digits of a given number
# 9. Write a python script to print binary equivalent of a given decimal number. (do not
# use bin() method)
# 10. Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)

# 1) .................................................................
# n=int(input("Enter n : "))
# s=(n*n-n)/2
# print(s)


# 2) ................................................................
# n=int(input("Enter n : "))
# sum=0
# for i in range(1,n+1):
#     sum+=pow(i,2)
# print(sum)


# 3) .....................................................................
# n=int(input("Enter n : "))
# sum=0
# for i in range(1,n+1):
#     sum+=pow(i,3)
# print(sum)


# 4) .......................................................................
# n=int(input("Enter n : "))
# sum=0
# for i in range(1,n+1,2):
#     sum+=pow(i,2)
# print(sum)


# 5) ......................................................................
# n=int(input("Enter n : "))
# sum=0
# for i in range(2,n+1,2):
#     sum+=pow(i,2)
# print(sum)


# 6) ...............................................................
# n=int(input("Enter n : "))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)


# 7) .................................................................
# n=int(input("Enter n : "))
# c=0
# while n>0:   #1234
#     c+=1
#     n=n//10
# print('count =',c)


# 8) ....................................................................
# n=int(input("Enter n : "))
# r=0
# s=0
# while n>0:   #1234
#     r=n%10
#     s+=r
#     n=n//10
# print('count =',s)


# 10) .....................................................................
