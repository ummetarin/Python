# # variable

# print(10+12)

# #INPUT 
# x=input()
# print(x)

# array
x=[1,2,3,4,5,6,7,8,9]

print(len(x))
print(x[0])
print(x[2:])
print(x[::-1])
print(x[:])

x[3]=55
print(x)

for i in x:
    print(i)
for i in range(1,10,2):
    print(i)

# number gassing
l=40
for i in range(3):
    a=int(input())
    if(a==l):
        print("winnner")
        break
    print("loser")
    
if len(x)<=9:
    x.append(12)
print(x)


