# # variable

# print(10+12)

# #INPUT 
# x=input()
# print(x)

# array
# x=[1,2,3,4,5,6,7,8,9]

# print(len(x))
# print(x[0])
# print(x[2:])
# print(x[::-1])
# print(x[:])

# x[3]=55
# print(x)

# for i in x:
#     print(i)
# for i in range(1,10,2):
#     print(i)

# # number gassing
# l=40
# for i in range(3):
#     a=int(input())
#     if(a==l):
#         print("winnner")
#         break
#     print("loser")
    
# if len(x)<=9:
#     x.append(12)
# print(x)

# string
# name="homaira apu"
# stri="allalalal"
# age=12
# for i in name:
#     print(i)

# print(name[::-1])
# print(name[:4])
# print(len(name))
# print(name.upper())
# print(name.replace('h','p'))
# print(name.strip())
# print(name.split(","))

# for i in range(len(name) - 1, -1, -1):
#     print(name[i])
    
# print(name+stri)
# print("the book is "+name+"is mine")
# print("homaira age is"+str(age))
# print(f"homaira is {age}")

# condition
x=int(input())
if(x%2==0):
    print("even")
else:
    print("odd")

if(x<=100 and x>=80):
    print("a+")
elif(x<=79 and x>=75):
    print("a")
elif(x<=74 and x>=70):
    print("a-")
else:
    print("fail")
