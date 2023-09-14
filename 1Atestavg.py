m1=int(input("enter the marks for test : "))
m2=int(input("enter the marks for test :"))
m3=int(input("enter the marks for test :"))

if m1<=m2 and m1<=m3:
    avgmarks = (m2+m3)/2
elif m2<=m1 and m1<=m3:
    avgmarks = (m2+m3)/2
elif m3<=m1 and m3<=m2:
    avgmarks = (m2+m1)/2

print("Average of two test marks out of three test is",avgmarks)
