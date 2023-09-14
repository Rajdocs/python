def fn(n):
  if n==0:
   return 0
  if n==1:
    return 1
  else:
    return fn(n-1)+fn(n-2) 

# if num > 0:
#     print("fn(", num, ") = ",fn(num) , sep ="")
# else:
#     print("Error in input")


num=int(input("enter a number :"))

if num > 0 :
    print("fn(", num, ") = ",fn(num) ,sep="")
else:
    print("error in input")
