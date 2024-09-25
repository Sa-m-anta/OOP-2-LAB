
#Multiplication-table of 5
num=5
for i in range(1,11):
    if i == 6:
        continue
    elif i==9:
        break
    print(num ,"*",i,"=", num*i)



#use of function
def oddOrEven(num):
    if num % 2 == 0:
        return 0
    else:
        return 1


num = int(input("Enter a number: "))
result =oddOrEven(num)
print(result)



# Array
num=[1,2,3,4]

for i in num:
    if i % 2 == 0:
        print("the even number is",i)


