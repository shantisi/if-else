# year=int(input("enter year"))
# if year%4==0 and year%400==0:
#     print("leapyear")
# else:
#     print("not leapyear")

# i=1
# k=1
# while i<=5:
#     j=1
#     while j<=k:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i+1
#     k=k+2  


# list=[34,56,96,0,11,1,2,5,100]
# i=0
# max=0
# max1=0
# min=1
# while i<len(list):
#     if list[i]<min:
#         min=list[i] 
#     if list[i]>max:
#         max=list[i] 
#     i=i+1

# i=0
# while i<len(list):
#     if list[i]>max1 and list[i]!=max:
#         max1=list[i]
#     i=i+1  
# print(max)
# print(max1)             
# print(min)  


list=[[2,5,8,1,7,9]]
r=[]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if type(list[i])==list:
          r.append(list[i][j])
        j=j+1
    i=i+1
print(r)    