str1=input("enter 1st string :\n ")
str2=input("enter the 2nd string :\n ")

if  len(str2)<len(str1):
    short=len(str2)
    large=len(str1)
else:
    short=len(str1)
    large=len(str2)

matchcnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchcnt+=1


print("similrities between two said strings : ")
print(matchcnt/large)
